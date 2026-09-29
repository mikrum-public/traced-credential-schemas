#!/usr/bin/env python3
"""Build CATALOGUE.md from the x-traced annotations and properties of the schemas.
The schemas are the source of truth; do not edit CATALOGUE.md by hand.

Usage:  python tools/build_catalogue.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ORDER = ["A01", "B01", "C01", "G01", "H03", "H01", "H02", "I01", "I02", "I07", "I05", "I09", "J01", "K05"]


def type_of(prop):
    if "$ref" in prop:
        return prop["$ref"].split("/")[-1]
    t = prop.get("type", "")
    if t == "array":
        inner = prop.get("items", {})
        return "array of " + (inner.get("$ref", "").split("/")[-1] or inner.get("type", "object"))
    if "enum" in prop:
        return t + " (" + " \\| ".join(prop["enum"]) + ")"
    return t


def esc(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


docs = {}
for path in (ROOT / "schemas").rglob("*.schema.json"):
    doc = json.loads(path.read_text(encoding="utf-8"))
    if "x-traced" in doc:
        docs[doc["x-traced"]["id"]] = (path, doc)

out = ["# TRACED pilot credential catalogue (draft v0.1)", "",
       "> Generated from `schemas/` by `tools/build_catalogue.py`. Pre-project draft; subject to change in T4.1.", "",
       "## Overview", "",
       "| # | Credential | Consolidates | Issuer | Holder | Legal basis |", "|---|---|---|---|---|---|"]
n = 0
for cid in ORDER:
    path, doc = docs[cid]
    xt = doc["x-traced"]
    if xt["kind"] != "credential":
        continue
    n += 1
    out.append(f"| {n} | **{esc(doc['title'])}** | {esc('; '.join(xt['consolidates']))} | {esc(xt['issuer'])} | {esc(xt['holder'])} | {esc('; '.join(xt['legalBasis']))} |")
out += ["", "Bound events (not separate credentials; they carry items consolidated in I01): "
        + ", ".join(docs[c][1]["title"] for c in ["I02", "I07"]) + ".", ""]

for cid in ORDER:
    path, doc = docs[cid]
    xt = doc["x-traced"]
    rel = path.relative_to(ROOT)
    out += [f"## {doc['title']}", "", doc["description"], "",
            f"- **Schema:** [`{rel}`]({rel}) · **vct:** `{xt['vct']}` · **format:** {xt['format']}",
            f"- **Kind:** {xt['kind']}" + (f" (bound to {xt['parent']})" if xt.get("parent") else ""),
            f"- **Consolidates:** {'; '.join(xt['consolidates']) or '— (carried under I01)'}",
            f"- **Issuer:** {xt['issuer']}", f"- **Holder:** {xt['holder']}",
            f"- **Verifiers:** {'; '.join(xt['verifiers'])}",
            f"- **Legal basis:** {'; '.join(xt['legalBasis'])}",
            f"- **Forward compatibility:** {xt.get('forwardCompatibility', '—')}",
            f"- **Validity:** {xt['validity']} · **Revocation:** {xt['revocation']}",
            f"- **Integrity:** {xt.get('integrity', '—')}",
            f"- **Use cases:** {', '.join(xt.get('useCases', []))}", "",
            "| Claim | Type | Mandatory | Selectively disclosable | Description |", "|---|---|---|---|---|"]
    req = set(doc.get("required", []))
    for name, prop in doc["properties"].items():
        out.append(f"| `{name}` | {esc(type_of(prop))} | {'yes' if name in req else 'no'} | "
                   f"{'yes' if prop.get('x-disclosable') else 'no — always disclosed'} | {esc(prop.get('description', ''))} |")
    if xt.get("openQuestions"):
        out += ["", "**Open questions for T4.1:** " + " ".join(f"({i}) {q}" for i, q in enumerate(xt["openQuestions"], 1))]
    out.append("")

(ROOT / "CATALOGUE.md").write_text("\n".join(out), encoding="utf-8")
print(f"CATALOGUE.md written: {n} credentials, {len(docs)} schema documents")
