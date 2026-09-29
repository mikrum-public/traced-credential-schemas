#!/usr/bin/env python3
"""Validate the TRACED credential schemas.

Checks:
  1. every schema is valid JSON Schema 2020-12;
  2. every example validates against its schema (common definitions resolved locally);
  3. every schema carries the required x-traced annotations;
  4. the pilot set is complete: 12 credentials consolidating 15 compliance documents and evidence items.

Usage:  pip install jsonschema referencing  &&  python tools/validate.py
"""
import json
import pathlib
import sys

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED_ANNOTATIONS = ["id", "kind", "status", "version", "category", "consolidates", "issuer", "holder",
                        "verifiers", "legalBasis", "validity", "revocation", "format", "vct"]
EXPECTED_CREDENTIALS = 12
EXPECTED_ITEMS = 15

errors = []
schemas = {}
for path in sorted((ROOT / "schemas").rglob("*.schema.json")):
    doc = json.loads(path.read_text(encoding="utf-8"))
    try:
        Draft202012Validator.check_schema(doc)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path.name}: not a valid 2020-12 schema: {exc}")
    schemas[path] = doc

registry = Registry().with_resources((doc["$id"], Resource.from_contents(doc)) for doc in schemas.values())

credentials, items = 0, []
for path, doc in schemas.items():
    if path.name == "common.schema.json":
        continue
    xt = doc.get("x-traced", {})
    missing = [k for k in REQUIRED_ANNOTATIONS if k not in xt]
    if missing:
        errors.append(f"{path.name}: missing x-traced annotations {missing}")
    for name, prop in doc.get("properties", {}).items():
        if "x-disclosable" not in prop:
            errors.append(f"{path.name}: property '{name}' has no x-disclosable flag")
    if xt.get("kind") == "credential":
        credentials += 1
        items += xt.get("consolidates", [])
    rel = path.relative_to(ROOT / "schemas")
    example = ROOT / "examples" / str(rel).replace(".schema.json", ".example.json")
    if not example.exists():
        errors.append(f"{path.name}: no example at {example.relative_to(ROOT)}")
        continue
    validator = Draft202012Validator(doc, registry=registry, format_checker=FormatChecker())
    for err in validator.iter_errors(json.loads(example.read_text(encoding="utf-8"))):
        errors.append(f"{example.name}: {'/'.join(map(str, err.path))}: {err.message}")

if credentials != EXPECTED_CREDENTIALS:
    errors.append(f"expected {EXPECTED_CREDENTIALS} credentials, found {credentials}")
if len(items) != EXPECTED_ITEMS or len(set(items)) != EXPECTED_ITEMS:
    errors.append(f"expected {EXPECTED_ITEMS} distinct consolidated items, found {len(items)} ({len(set(items))} distinct)")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK — {len(schemas)} schema files, {credentials} credentials consolidating {len(items)} items; all examples valid.")
