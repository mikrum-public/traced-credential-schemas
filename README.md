# TRACED — pilot credential schemas (draft v0.1)

> **Pre-project draft; subject to change in T4.1.**
> This repository publishes the draft schemas for the twelve pilot credentials of the TRACED proposal, before the project starts. They have not yet been validated by the competent authorities. They are not an official format of any Member State, of the European Commission or of TRACES NT. All example data are fictitious.

TRACED (*Trusted, Real-time Automated Compliance for animal transport, Enabled by verifiable Data*) is a proposal to the Digital Europe Programme (DIGITAL-2026-AI-DATA-10-COMPLIANCE). It pilots compliance simplification for live-animal transport:

- compliance data that EU law already requires is captured once;
- the data is transmitted automatically to the competent authorities;
- it is checked in real time;
- it is carried as verifiable credentials that are compatible with the emerging EU Business Wallet specifications.

These schemas are the credential layer of that design.

## What is in the set

The set applies the **credential-boundary principle**: documents are not mapped one-to-one to credentials. Instead, items are grouped when they share three things:

- a common issuer;
- a similar lifecycle and validity;
- a shared verification context.

Applied to the pilot scope, this gives **twelve credentials that consolidate fifteen compliance documents and evidence items**. Two credentials carry more than one item:

- **C01** carries C01 and C05.
- **I01** carries I01, I02 and I07. I02 and I07 are signed events bound to the I01 journey anchor, not separate credentials.

| # | Credential | Consolidates | Issuer |
|---|---|---|---|
| 1 | A01 Transporter Authorisation (intra-EU) | A01 | Competent authority of establishment |
| 2 | B01 Driver Certificate of Competence | B01 | Competent authority / designated body |
| 3 | C01 Vehicle Approval & Capacity | C01, C05 | Competent authority / designated body |
| 4 | G01 Consignment Animal Identification | G01 | Authority's identification & registration database |
| 5 | H03 Official Veterinarian Mandate | H03 | Appointing competent authority |
| 6 | H01 Animal Health Certificate (pre-movement) | H01 | Official veterinarian (via TRACES NT) |
| 7 | H02 Fitness-to-Travel Assessment | H02 | Official veterinarian at departure |
| 8 | I01 Journey Pre-Approval — *anchor* | I01, I02, I07 | Competent authority of departure |
| 9 | I05 Journey Time Compliance Attestation | I05 | Rules-as-code determination engine |
| 10 | I09 Destination Reception & Welfare Assessment | I09 | Keeper at destination |
| 11 | J01 Farm/Holding Registration | J01 | Competent authority (register of establishments) |
| 12 | K05 TRACES NT Journey Registration Record | K05 | Competent authority of departure |

[`CATALOGUE.md`](CATALOGUE.md) gives the full detail for each credential, generated from the schemas:

- the claims, with data type and whether each is mandatory;
- issuer, holder and verifiers;
- the legal basis;
- which claims support selective disclosure;
- validity and revocation;
- open questions.

**Out of scope:**

- **Sensor and telematics streams** (position, temperature, space) are not credentials. They are source-authenticated evidence (integrity Tier 2), held in tamper-protected storage and referenced by digest.
- **Third-country export credentials** fall outside the pilot, which runs on intra-EU corridors only.
- **The mandate credential** that links a driver to the transporter's legal entity is part of the trust framework. It is defined in the project's legal and data-governance work, not in this set.

## Repository layout

```
schemas/                  JSON Schema (2020-12) of the disclosed claims of each credential
  common.schema.json      shared definitions (legal entity, authority, place, digest, pinned versions …)
  events/                 I02 and I07: signed events bound to the I01 anchor
examples/                 one fictitious example per schema (validated in CI)
tools/validate.py         schema, example and completeness checks (12 credentials / 15 items)
tools/build_catalogue.py  regenerates CATALOGUE.md from the schemas
CATALOGUE.md              human-readable catalogue (generated)
```

Each schema carries three kinds of annotation:

- **`x-traced` block:** credential metadata — id, what it consolidates, issuer, holder, verifiers, legal basis, validity, revocation, integrity tier, `vct`, open questions.
- **`x-disclosable` flag on every claim:** `true` means the claim is issued as a selectively disclosable claim; `false` means it is always disclosed, because the check cannot be made without it.
- **Validation annotations:** unknown-keyword annotations are ignored by standard JSON Schema validators.

## Format profile

The draft targets **SD-JWT VC** (IETF OAuth WG, *SD-JWT-based Verifiable Credentials*), the selective-disclosure format used by the EUDI Wallet Architecture and Reference Framework (ARF). Issuance and presentation use OpenID4VCI and OpenID4VP. Each schema describes the claims of one credential type. The SD-JWT VC envelope carries the registered claims:

| Envelope claim | Use in TRACED |
|---|---|
| `iss` | issuer identifier, resolvable to a trust anchor (e.g. a trusted list for public-sector issuers) |
| `vct` | credential type, e.g. `urn:traced:credential:i01-journey-pre-approval:0.1` (provisional identifiers; final hosting fixed in T4.1) |
| `iat`, `nbf`, `exp` | issuance and validity window |
| `cnf` | holder key binding: the key of the holder's wallet (for operators, the legal person's wallet) |
| `status` | revocation / suspension through a status list (IETF *Token Status List*). For offline verification the list is cached, and the result shows how fresh the status used was |

A W3C Verifiable Credentials Data Model 2.0 encoding and an ISO/IEC 18013-5 (mdoc) encoding are possible later. They are not part of this draft.

**Offline verification.** A proof is verified from four things, without a real-time call to the issuer:

- its signature;
- its issuer;
- its validity;
- its binding to the journey (`journeyId`, and for events `previousEventDigest`).

The verifier also uses the latest synchronised status.

**Versioning.** Schemas follow semantic versioning. The semantic-model, schema-set and rule-set versions in force at journey start are pinned in the I01 anchor (`pinnedVersions`) and govern the journey to completion, so a new version never invalidates a journey that is under way.

## Alignment with the EU wallet ecosystem

This draft reuses published structures from the EU digital-identity large-scale pilots. It does not redefine them.

- **WE BUILD** (large-scale pilot for business and legal-person use cases of the EUDI and EU Business Wallets) publishes an attestation rulebook and schema catalogue: <https://github.com/webuild-consortium/webuild-attestation-rulebooks-catalog>. It pairs human-readable rulebooks with machine-readable JSON Schemas for SD-JWT claims and sample data. Its rulebook template marks each attribute as disclosable or not. TRACED follows the same pattern:
  - schemas for SD-JWT VC claims, sample data and a per-claim disclosable flag;
  - each credential is intended to become a rulebook in T4.1.
  - **Operator identity** is not redefined here. Legal persons are identified by the EUID, as in the Legal Person Identification Data (LPID) attestation, whose rulebook keeps only two mandatory attributes: the EUID and the legal name ([EWC LPID rulebook](https://github.com/EWC-consortium/eudi-wallet-rulebooks-and-schemas/blob/main/rulebooks/rb001-legal-person-identification-data.md)). The TRACED credentials carry only the authorisations, approvals and events that animal-transport law adds on top of that identity.
- **APTITUDE** (large-scale pilot for travel and mobility use cases, including the mobile Vehicle Registration Certificate, mVRC): <https://aptitude.digital-identity-wallet.eu/>. The vehicle identification claims of C01 (VIN, registration plate, registration country) are kept aligned with vehicle-registration attestations, so a vehicle's registration attestation and its animal-transport approval can be linked by VIN. There is no dependency on APTITUDE.
- **EUDI attestation rulebook template:** <https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog>. The T4.1 rulebooks will follow its structure (attributes, encoding, usage, trust anchors, revocation, compliance).
- **European Business Wallets:** the Commission proposal COM(2025) 838. TRACED is forward-compatible with it. The pilot does not depend on its timeline, and it runs on conformant credentials issued within the consortium if the wallet ecosystem is not yet available.

No formal cooperation with these pilots is implied by this alignment.

## Legal anchors

- Council Regulation (EC) No 1/2005 on the protection of animals during transport. This is the primary basis for A01, B01, C01, H02, I01/I02/I07, I05 and I09.
- Regulation (EU) 2016/429 (Animal Health Law) and its delegated and implementing acts: G01, H01, J01, K05.
- Regulation (EU) 2017/625 (Official Controls Regulation): H01, H03.
- Commission Implementing Regulation (EU) 2019/1715 (IMSOC / TRACES): K05. TRACED reads TRACES NT and does not modify it.
- COM(2023) 770, the proposal revising the animal-transport rules, is used for forward-compatibility notes only.

Every legal reference is a draft mapping. It is confirmed with the participating Member State bodies in the project's obligation inventory (T2.1).

## Validate locally

```bash
pip install jsonschema referencing
python tools/validate.py          # schema validity, examples, 12 credentials / 15 items
python tools/build_catalogue.py   # regenerate CATALOGUE.md after editing a schema
```

## Status and roadmap

| Version | When | What |
|---|---|---|
| 0.1.0 | pre-project | This draft, prepared from the proposal's credential design and published by the coordinator |
| 0.x | project, T4.1 | Validation with the Member State bodies; one rulebook per credential; issuer and holder models settled (T2.4) |
| 1.0 | project, D4.1 (M14) | Credential set used in the integrated pilot; released on the Interoperable Europe Portal with the TRACED open-source components (D7.2) |

## Licence

- **Schemas, tools and examples:** European Union Public Licence v1.2 ([`LICENSE`](LICENSE), SPDX `EUPL-1.2`).
- **Documentation** (README.md, CATALOGUE.md): dual-licensed EUPL-1.2 and Creative Commons Attribution 4.0 International ([`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt)), as planned for the TRACED open-source release.

## Contact

Mikrum Informatikai Szolgáltató Zrt. (MIKRUM), coordinator of the TRACED proposal. Issues and comments are welcome through the repository's issue tracker.
