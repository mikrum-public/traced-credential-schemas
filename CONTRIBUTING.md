# Contributing

This is a pre-project draft. Comments are most useful on:

1. **Legal mapping** — is the legal basis of a credential or claim right for your Member State?
2. **Issuer and holder** — who signs what, to whom, and who may verify.
3. **Selective disclosure** — which claims a check can do without.
4. **Alignment** — overlaps with attestations defined in the EUDI / EU Business Wallet ecosystem (e.g. WE BUILD rulebooks).

Open an issue, or a pull request that edits the schema in `schemas/`, then run:

```bash
pip install jsonschema referencing
python tools/validate.py
python tools/build_catalogue.py
```

`CATALOGUE.md` is generated; do not edit it by hand. Never add real personal data or real identifiers to `examples/`.

Contributions are accepted under the EUPL-1.2 (schemas, tools, examples) and EUPL-1.2 / CC BY 4.0 (documentation).
