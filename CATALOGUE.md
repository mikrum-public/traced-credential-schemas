# TRACED pilot credential catalogue (draft v0.1)

> Generated from `schemas/` by `tools/build_catalogue.py`. Pre-project draft; subject to change in T4.1.

## Overview

| # | Credential | Consolidates | Issuer | Holder | Legal basis |
|---|---|---|---|---|---|
| 1 | **A01 Transporter Authorisation (intra-EU)** | A01 Transporter Authorisation (Intra-EU) | Competent authority of the Member State where the transporter is established (Art. 10(1)(a), Art. 12). | Transporter — the legal person's (EU Business) wallet. | Reg (EC) No 1/2005 Art. 6(1)–(2), 10, 11, 12, 13; Reg (EC) No 1/2005 Annex III, Chapters I and II (specimen authorisations) |
| 2 | **B01 Driver Certificate of Competence (Animal Welfare)** | B01 Driver Certificate of Competence (Animal Welfare) | Competent authority or designated body of the Member State (Art. 17(2)); training and independent examination per Annex IV. | In the pilot: held in the transporter's legal-entity wallet with the driver as subject, linked to the transporter by the mandate credential defined in T2.4 / D1.1. | Reg (EC) No 1/2005 Art. 6(5), 17(2); Reg (EC) No 1/2005 Annex IV (training); Reg (EC) No 1/2005 Annex III, Chapter III (specimen certificate) |
| 3 | **C01 Vehicle Type Approval (Livestock) incl. C05 Loading Density & Capacity** | C01 Vehicle Type Approval (Livestock); C05 Loading Density & Capacity | Competent authority or body designated by the Member State (Art. 18(1)). | Transporter (legal-entity wallet); bound to the vehicle by VIN. | Reg (EC) No 1/2005 Art. 6(8), 7(1), 18; Reg (EC) No 1/2005 Annex I, Chapters II, VI and VII; Reg (EC) No 1/2005 Annex III, Chapter IV (specimen certificate) |
| 4 | **G01 Consignment Animal Identification** | G01 Consignment Animal Identification | Competent authority, as operator of the national identification and registration database (authentic source) — e.g. the Italian national database (BDN) run by IZS Teramo for the Ministry of Health. | Transporter for the journey (legal-entity wallet); presentable by the keeper at departure and destination. | Reg (EC) No 1/2005 Art. 4(1)(a); Reg (EU) 2016/429 (Animal Health Law) Art. 109, 112–115; Delegated Reg (EU) 2019/2035 (identification and traceability of kept terrestrial animals) |
| 5 | **H03 Official Veterinarian Mandate** | H03 Official Veterinarian Mandate | Competent authority that appoints the official veterinarian. | The official veterinarian (natural person); holder model fixed in T2.4. | Reg (EC) No 1/2005 Art. 2(p); Reg (EU) 2017/625 (Official Controls Regulation) Art. 3(26), 3(32) |
| 6 | **H01 Animal Health Certificate (Pre-Movement)** | H01 Animal Health Certificate (Pre-Movement) | Official veterinarian (certifying officer) of the competent authority at the place of departure. | Operator dispatching the consignment; carried by the transporter (legal-entity wallet). | Reg (EU) 2016/429 (Animal Health Law) Art. 143, 145, 149, 150; Delegated Reg (EU) 2020/688; Implementing Reg (EU) 2021/403 (model certificates); Reg (EU) 2017/625 (Official Controls Regulation) Art. 3(26)–(27) |
| 7 | **H02 Fitness-to-Travel Assessment** | H02 Fitness-to-Travel Assessment | Official veterinarian at the place of departure for long journeys between Member States (Art. 15(2)); otherwise the keeper at the place of departure (Art. 8(1)). | Transporter (legal-entity wallet), for the journey. | Reg (EC) No 1/2005 Art. 3(b), 8(1), 15(2); Reg (EC) No 1/2005 Annex I, Chapter I |
| 8 | **I01 Journey Pre-Approval (anchor)** | I01 Journey Pre-Approval (anchor); I02 En-Route Welfare Log Entry; I07 Post-Arrival Journey Completion Report | Competent authority of the place of departure (Art. 14(1)); bound events are signed by their own signers (see events/). | Organiser / transporter (legal-entity wallet). | Reg (EC) No 1/2005 Art. 4, 5(4), 14(1); Reg (EC) No 1/2005 Annex II, points 1–3 and Section 1 (Planning) |
| 9 | **I05 Journey Time Compliance Attestation** | I05 Journey Time Compliance Attestation | TRACED rules-as-code determination engine (machine issuer, electronic seal of the service operator); runs at the edge and on the platform. | Transporter (legal-entity wallet). | Reg (EC) No 1/2005 Art. 15(1), 15(4); Reg (EC) No 1/2005 Annex I, Chapter V, point 1 |
| 10 | **I09 Destination Farm Reception & Welfare Assessment** | I09 Destination Farm Reception & Welfare Assessment | Keeper at the place of destination (Art. 8(2); Annex II, point 4 and Section 3). At a slaughterhouse, the official veterinarian's controls remain a separate official control and are referenced, not replaced. | Keeper at destination; shared with the transporter and the authorities. | Reg (EC) No 1/2005 Art. 8(2), 15(3), 26(3); Reg (EC) No 1/2005 Annex II, point 4, Sections 3 and 5; Reg (EC) No 1/2005 Annex I, Chapter I |
| 11 | **J01 Farm/Holding Registration** | J01 Farm/Holding Registration | Competent authority keeping the register of establishments. | Operator of the establishment (keeper). | Reg (EU) 2016/429 (Animal Health Law) Art. 84, 93, 94, 101; Reg (EC) No 1/2005 Art. 4(1)(a) |
| 12 | **K05 TRACES NT Journey Registration Record** | K05 TRACES NT Journey Registration Record | Competent authority of the place of departure, from its TRACES NT record, through the authority verify-and-issue channel (T4.4). | Transporter (legal-entity wallet). | Reg (EC) No 1/2005 Art. 14(1)(d); Reg (EU) 2016/429 (Animal Health Law) Art. 152; Reg (EU) 2019/1715 (IMSOC / TRACES) |

Bound events (not separate credentials; they carry items consolidated in I01): I02 En-Route Welfare Log Entry (bound event), I07 Post-Arrival Journey Completion Report (bound event).

## A01 Transporter Authorisation (intra-EU)

Authorisation of the transporter by the competent authority of the Member State where it is established (Type 1: Art. 10; Type 2, long journeys: Art. 11).

- **Schema:** [`schemas/a01-transporter-authorisation.schema.json`](schemas/a01-transporter-authorisation.schema.json) · **vct:** `urn:traced:credential:a01-transporter-authorisation:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** A01 Transporter Authorisation (Intra-EU)
- **Issuer:** Competent authority of the Member State where the transporter is established (Art. 10(1)(a), Art. 12).
- **Holder:** Transporter — the legal person's (EU Business) wallet.
- **Verifiers:** Competent authority of the place of departure (Art. 14(1)(a)(i)); Official veterinarians at control posts and exit points (Art. 21(1)(a)); Competent authority of the place of destination; Organisers contracting transport (Art. 5(1))
- **Legal basis:** Reg (EC) No 1/2005 Art. 6(1)–(2), 10, 11, 12, 13; Reg (EC) No 1/2005 Annex III, Chapters I and II (specimen authorisations)
- **Forward compatibility:** COM(2023) 770 (proposal) — forward-compatibility only: transporter authorisation provisions; mapping in T2.1.
- **Validity:** ≤ 5 years; changes to be notified within 15 working days (Art. 6(2)). · **Revocation:** Suspension or withdrawal (Art. 26(4)(c)) → status list update.
- **Integrity:** Issuer electronic seal (qualified where available).
- **Use cases:** UC-1 pre-departure, UC-3 official verification at control points

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `authorisationNumber` | string | yes | no — always disclosed | Number unique in the issuing Member State (Art. 13(2)). |
| `authorisationType` | string (type1 \\| type2) | yes | no — always disclosed | type1 = Art. 10(1), not valid for long journeys; type2 = Art. 11(1), valid for all journeys incl. long journeys. |
| `transporter` | legalEntity | yes | no — always disclosed | The authorised transporter (legal person). Name and number of Type 2 authorisations are public (Art. 13(4)). |
| `scopeLimitations` | object | no | yes | Limitations set by the authority (Art. 13(1)), e.g. species or means of transport. |
| `navigationSystemDemonstrated` | boolean | no | yes | Type 2 only: use of the navigation system demonstrated (Art. 11(2)). |
| `issuingAuthority` | competentAuthority | yes | no — always disclosed | Competent authority that granted the authorisation (one authority per transporter, Art. 12). |
| `dateOfIssue` | date | yes | no — always disclosed | Date of issue. |
| `validUntil` | date | yes | no — always disclosed | End of validity; not more than five years from issue (Art. 10(2), 11(3)). |

**Open questions for T4.1:** (1) Reuse LPID/EUCC for the transporter identity once available in the EU Business Wallet; keep only the authorisation-specific claims here.

## B01 Driver Certificate of Competence (Animal Welfare)

Certificate of competence for drivers and attendants of road vehicles transporting domestic Equidae, bovine, ovine, caprine, porcine animals or poultry (Art. 6(5), 17(2)).

- **Schema:** [`schemas/b01-driver-certificate-of-competence.schema.json`](schemas/b01-driver-certificate-of-competence.schema.json) · **vct:** `urn:traced:credential:b01-driver-certificate-of-competence:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** B01 Driver Certificate of Competence (Animal Welfare)
- **Issuer:** Competent authority or designated body of the Member State (Art. 17(2)); training and independent examination per Annex IV.
- **Holder:** In the pilot: held in the transporter's legal-entity wallet with the driver as subject, linked to the transporter by the mandate credential defined in T2.4 / D1.1.
- **Verifiers:** Competent authority of the place of departure (Art. 14(1)(a)(i)); Official veterinarians at control posts and exit points (Art. 21(1)(b)); Competent authority granting a Type 2 authorisation (Art. 11(1)(b)(i))
- **Legal basis:** Reg (EC) No 1/2005 Art. 6(5), 17(2); Reg (EC) No 1/2005 Annex IV (training); Reg (EC) No 1/2005 Annex III, Chapter III (specimen certificate)
- **Forward compatibility:** COM(2023) 770 (proposal) — forward-compatibility only: certificate of competence provisions; mapping in T2.1.
- **Validity:** As set nationally. · **Revocation:** Suspension or withdrawal (Art. 26(5)).
- **Integrity:** Issuer electronic seal.
- **Use cases:** UC-1 pre-departure, UC-3 official verification at control points

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `certificateNumber` | string | yes | no — always disclosed | Certificate number. |
| `person` | naturalPerson | yes | yes | The driver or attendant. Personal data: disclosed only for identity matching at a check. |
| `speciesScope` | array of species | yes | no — always disclosed | Species or group of species the certificate covers (Art. 17(2) allows limitation). |
| `issuingAuthorityOrBody` | object | yes | no — always disclosed | Competent authority or body designated by the Member State (Art. 17(2)). |
| `dateOfIssue` | date | yes | no — always disclosed | Date of issue. |
| `validUntil` | date | no | no — always disclosed | End of validity where national rules set one (Reg (EC) No 1/2005 sets none). |

**Open questions for T4.1:** (1) Holder model for a natural-person credential used in a legal-entity context (T2.4): transporter wallet + mandate credential vs. the driver's own EUDI Wallet.

## C01 Vehicle Type Approval (Livestock) incl. C05 Loading Density & Capacity

Certificate of approval of a means of transport by road for long journeys (Art. 18), consolidated with the vehicle capacity data needed to check space allowances (Annex I, Chapter VII) at loading.

- **Schema:** [`schemas/c01-vehicle-approval-and-capacity.schema.json`](schemas/c01-vehicle-approval-and-capacity.schema.json) · **vct:** `urn:traced:credential:c01-vehicle-approval-and-capacity:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** C01 Vehicle Type Approval (Livestock); C05 Loading Density & Capacity
- **Issuer:** Competent authority or body designated by the Member State (Art. 18(1)).
- **Holder:** Transporter (legal-entity wallet); bound to the vehicle by VIN.
- **Verifiers:** Competent authority of the place of departure (Art. 14(1)(a)(i)); Competent authority of the country of destination (Art. 6(8)); Official veterinarians at control posts and exit points (Art. 21(1)(d))
- **Legal basis:** Reg (EC) No 1/2005 Art. 6(8), 7(1), 18; Reg (EC) No 1/2005 Annex I, Chapters II, VI and VII; Reg (EC) No 1/2005 Annex III, Chapter IV (specimen certificate)
- **Forward compatibility:** COM(2023) 770 (proposal) — forward-compatibility only: model certificate of approval of means of transport by road (owner, vehicle identification, max decks, max surface, species/categories).
- **Validity:** ≤ 5 years; void on welfare-relevant modification. · **Revocation:** Suspension or withdrawal (Art. 26(4)(c)).
- **Integrity:** Issuer electronic seal.
- **Use cases:** UC-1 pre-departure, UC-3 official verification at control points

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `approvalCertificateNumber` | string | yes | no — always disclosed | Number unique in the issuing Member State (Art. 18(2)). |
| `vehicle` | object | yes | no — always disclosed | Vehicle identification. Claim names kept aligned with vehicle-registration attestations (mVRC) so the two can be linked by VIN. |
| `owner` | legalEntity | yes | no — always disclosed | Owner identification as in the specimen certificate. |
| `speciesCategories` | array of species | yes | no — always disclosed | Species/categories the vehicle is approved to transport. |
| `maxDecks` | integer | yes | no — always disclosed | Maximum number of decks. |
| `usableFloorAreaPerDeckM2` | array of number | yes | no — always disclosed | Usable floor area per deck, in m² (C05). Input to the space-allowance check. |
| `equipment` | object | no | yes | Long-journey equipment found compliant at inspection (Annex I, Chapter VI). |
| `capacityProfile` | array of object | no | yes | C05: informative maximum loading per species/category and weight class, derived from floor area and Annex I, Chapter VII. The binding check is the rules-as-code determination at loading, per journey. |
| `inspection` | object | no | yes | Inspection on which the approval rests (Art. 18(1)(b)). |
| `issuingAuthority` | competentAuthority | yes | no — always disclosed | Competent authority or designated body that granted the approval. |
| `dateOfIssue` | date | yes | no — always disclosed | Date of issue. |
| `validUntil` | date | yes | no — always disclosed | Not more than five years; invalid as soon as the vehicle is modified or refitted in a way that affects animal welfare (Art. 18(2)). |

**Open questions for T4.1:** (1) Whether the capacity profile is issued by the authority or computed by the operator from floor area (then C05 claims move to the I01 anchor).

## G01 Consignment Animal Identification

Official identification linkage, issued once per consignment. Content follows the identification regime of the species: official identifiers (or a commitment to them) for individually identified species; holding mark, batch reference, headcount and weight for batch-identified species.

- **Schema:** [`schemas/g01-consignment-animal-identification.schema.json`](schemas/g01-consignment-animal-identification.schema.json) · **vct:** `urn:traced:credential:g01-consignment-animal-identification:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** G01 Consignment Animal Identification
- **Issuer:** Competent authority, as operator of the national identification and registration database (authentic source) — e.g. the Italian national database (BDN) run by IZS Teramo for the Ministry of Health.
- **Holder:** Transporter for the journey (legal-entity wallet); presentable by the keeper at departure and destination.
- **Verifiers:** Competent authority of the place of departure; Official veterinarians at control posts; Keeper and competent authority at destination
- **Legal basis:** Reg (EC) No 1/2005 Art. 4(1)(a); Reg (EU) 2016/429 (Animal Health Law) Art. 109, 112–115; Delegated Reg (EU) 2019/2035 (identification and traceability of kept terrestrial animals)
- **Forward compatibility:** Unchanged by COM(2023) 770; identification rules sit in the Animal Health Law.
- **Validity:** Single journey. · **Revocation:** Superseded if the consignment changes before departure.
- **Integrity:** Issuer electronic seal; source records remain in the national database.
- **Use cases:** UC-1 pre-departure, UC-3 official verification at control points, UC-4 destination & anomaly

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `consignmentId` | string | yes | no — always disclosed | Consignment identifier, bound to the I01 journey anchor. |
| `journeyId` | string | yes | no — always disclosed | I01 journey identifier. |
| `species` | species | yes | no — always disclosed | Species carried. |
| `identificationRegime` | string (individual \\| batch) | yes | no — always disclosed | individual or batch identification, per species rules. |
| `headcount` | integer | yes | no — always disclosed | Number of animals in the consignment. |
| `individualIdentifiers` | array of string | no | yes | Official identifiers of each animal (individual regime). |
| `identifiersCommitment` | digest | no | no — always disclosed | Cryptographic commitment (e.g. Merkle root) to the individual identifiers, with disclosure on demand — alternative to listing them. |
| `batch` | object | no | yes | Batch identification (batch regime). |
| `originEstablishment` | place | yes | no — always disclosed | Establishment of origin (registration number required). |
| `sourceDatabase` | object | yes | no — always disclosed | Authentic source: the national identification and registration database. |
| `extractedAt` | dateTime | yes | no — always disclosed | Time the consignment data was drawn from the source database. |

**Open questions for T4.1:** (1) Commitment scheme for individual identifiers (salted Merkle tree vs. per-identifier SD-JWT disclosures).

## H03 Official Veterinarian Mandate

Attests that a veterinarian is appointed by the competent authority to act for it, and for which official activities — so that vet-signed credentials can be verified across Member States, offline.

- **Schema:** [`schemas/h03-official-veterinarian-mandate.schema.json`](schemas/h03-official-veterinarian-mandate.schema.json) · **vct:** `urn:traced:credential:h03-official-veterinarian-mandate:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** H03 Official Veterinarian Mandate
- **Issuer:** Competent authority that appoints the official veterinarian.
- **Holder:** The official veterinarian (natural person); holder model fixed in T2.4.
- **Verifiers:** Any relying party checking a vet-signed credential (H01, H02, I02 check events, I09); Authorities of other Member States; Transporters and keepers
- **Legal basis:** Reg (EC) No 1/2005 Art. 2(p); Reg (EU) 2017/625 (Official Controls Regulation) Art. 3(26), 3(32)
- **Forward compatibility:** Unaffected; definition sits in the Official Controls Regulation.
- **Validity:** Duration of the appointment. · **Revocation:** On end or suspension of the appointment → status list.
- **Integrity:** Issuer electronic seal.
- **Use cases:** UC-1 pre-departure, UC-3 official verification at control points, UC-4 destination & anomaly

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `officialVeterinarian` | naturalPerson | yes | yes | The appointed veterinarian. |
| `professionalId` | string | yes | no — always disclosed | Registration or staff identifier of the veterinarian. |
| `appointingAuthority` | competentAuthority | yes | no — always disclosed | Competent authority that appointed the veterinarian. |
| `mandateScope` | array of string | yes | no — always disclosed | Official activities covered. |
| `territorialScope` | string | yes | no — always disclosed | Region or Member State where the mandate applies. |
| `validFrom` | date | yes | no — always disclosed | Start of the mandate. |
| `validUntil` | date | no | no — always disclosed | End of the mandate. |

**Open questions for T4.1:** (1) Relationship to certifying-officer registration in TRACES NT (avoid duplicating what TRACES already asserts).

## H01 Animal Health Certificate (Pre-Movement)

Wallet representation of the official animal health certificate for movements between Member States. It references and preserves the TRACES NT certificate — it does not replace it.

- **Schema:** [`schemas/h01-animal-health-certificate.schema.json`](schemas/h01-animal-health-certificate.schema.json) · **vct:** `urn:traced:credential:h01-animal-health-certificate:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** H01 Animal Health Certificate (Pre-Movement)
- **Issuer:** Official veterinarian (certifying officer) of the competent authority at the place of departure.
- **Holder:** Operator dispatching the consignment; carried by the transporter (legal-entity wallet).
- **Verifiers:** Competent authority of the place of destination; Official veterinarians at control posts; TRACES NT cross-check by any authority
- **Legal basis:** Reg (EU) 2016/429 (Animal Health Law) Art. 143, 145, 149, 150; Delegated Reg (EU) 2020/688; Implementing Reg (EU) 2021/403 (model certificates); Reg (EU) 2017/625 (Official Controls Regulation) Art. 3(26)–(27)
- **Forward compatibility:** Unaffected by COM(2023) 770.
- **Validity:** As set for the certificate model; single movement. · **Revocation:** Replacement or cancellation in TRACES NT → status list.
- **Integrity:** Tier 3 — pre-authenticated: TRACES NT signature validated and preserved; wallet copy sealed by the issuer.
- **Use cases:** UC-1 pre-departure, UC-3 official verification at control points

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `certificateReference` | string | yes | no — always disclosed | TRACES NT certificate reference. |
| `certificateModel` | string | no | no — always disclosed | Model certificate applied (Implementing Reg (EU) 2021/403). |
| `consignmentId` | string | yes | no — always disclosed | Consignment identifier (G01). |
| `species` | species | yes | no — always disclosed | Species. |
| `headcount` | integer | yes | no — always disclosed | Number of animals certified. |
| `attestations` | array of object | no | yes | Animal health attestations certified, as requirement–outcome pairs. |
| `testsPerformed` | array of object | no | yes | Laboratory tests referred to in the certificate. |
| `certifyingOfficer` | object | yes | yes | Official veterinarian who signed; resolvable to an H03 mandate. |
| `placeOfIssue` | place | yes | no — always disclosed | Place of issue. |
| `signedAt` | dateTime | yes | no — always disclosed | Time of signature in TRACES NT. |
| `originalSignatureDigest` | digest | yes | no — always disclosed | Digest of the signed TRACES NT certificate (Tier 3: original signature validated and preserved). |

**Open questions for T4.1:** (1) Who seals the wallet copy: the certifying officer via the authority, or the verify-and-issue channel (T4.4) on reading the TRACES NT record.

## H02 Fitness-to-Travel Assessment

Assessment that the animals are fit for the intended journey (Art. 3(b), Annex I Chapter I), performed before loading; short-lived.

- **Schema:** [`schemas/h02-fitness-to-travel-assessment.schema.json`](schemas/h02-fitness-to-travel-assessment.schema.json) · **vct:** `urn:traced:credential:h02-fitness-to-travel-assessment:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** H02 Fitness-to-Travel Assessment
- **Issuer:** Official veterinarian at the place of departure for long journeys between Member States (Art. 15(2)); otherwise the keeper at the place of departure (Art. 8(1)).
- **Holder:** Transporter (legal-entity wallet), for the journey.
- **Verifiers:** Official veterinarians at control posts and exit points (Art. 21(1)(c)); Competent authority en route (Art. 15(1)); Keeper and competent authority at destination
- **Legal basis:** Reg (EC) No 1/2005 Art. 3(b), 8(1), 15(2); Reg (EC) No 1/2005 Annex I, Chapter I
- **Forward compatibility:** COM(2023) 770 (proposal) — forward-compatibility only: Art. 17 (obligations for keepers prior to the journey, incl. fitness for transport).
- **Validity:** Until departure plus tolerance. · **Revocation:** Not revoked; expires.
- **Integrity:** Issuer electronic seal; Tier 1 sealed photo evidence may be attached by reference.
- **Use cases:** UC-1 pre-departure, UC-3 official verification at control points

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `consignmentId` | string | yes | no — always disclosed | Consignment identifier (G01). |
| `journeyId` | string | yes | no — always disclosed | I01 journey identifier. |
| `assessedAt` | dateTime | yes | no — always disclosed | Time of the assessment (before loading). |
| `placeOfAssessment` | place | yes | no — always disclosed | Place of departure. |
| `outcome` | string (fit \\| fit-with-conditions) | yes | no — always disclosed | Overall outcome for the consignment as loaded. |
| `animalsAssessed` | integer | yes | no — always disclosed | Number of animals assessed. |
| `animalsExcluded` | integer | no | yes | Animals found unfit and not loaded. |
| `conditions` | array of string | no | yes | Conditions under Annex I, Chapter I, point 3 (e.g. slightly injured, transport under veterinary supervision). |
| `assessor` | object | yes | yes | Assessor; for long journeys between Member States the check is part of the official animal health checks (Art. 15(2)). |
| `validUntil` | dateTime | yes | no — always disclosed | Planned departure plus a tolerance fixed in T4.1. |

**Open questions for T4.1:** (1) Tolerance window and whether a keeper-issued variant is needed for short journeys in the pilot.

## I01 Journey Pre-Approval (anchor)

The journey anchor: the approved journey plan (journey log, Section 1 — Planning). Every later signed event — I02 en-route entries, K05 border registration, I07 completion, I09 reception — binds to its journeyId.

- **Schema:** [`schemas/i01-journey-pre-approval.schema.json`](schemas/i01-journey-pre-approval.schema.json) · **vct:** `urn:traced:credential:i01-journey-pre-approval:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** I01 Journey Pre-Approval (anchor); I02 En-Route Welfare Log Entry; I07 Post-Arrival Journey Completion Report
- **Issuer:** Competent authority of the place of departure (Art. 14(1)); bound events are signed by their own signers (see events/).
- **Holder:** Organiser / transporter (legal-entity wallet).
- **Verifiers:** Every competent authority and official veterinarian on the route; Control posts; Keeper and competent authority at destination
- **Legal basis:** Reg (EC) No 1/2005 Art. 4, 5(4), 14(1); Reg (EC) No 1/2005 Annex II, points 1–3 and Section 1 (Planning)
- **Forward compatibility:** COM(2023) 770 (proposal) — forward-compatibility only: Art. 15 (journey log submitted in TRACES and approved by the competent authority of departure before the journey starts).
- **Validity:** Until journey completion (I07). · **Revocation:** Cancellation before departure → status list.
- **Integrity:** Issuer electronic seal; the anchor of the hash-linked event trail.
- **Use cases:** UC-1 pre-departure, UC-2 in-transit welfare, UC-3 official verification at control points, UC-4 destination & anomaly

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `journeyId` | string | yes | no — always disclosed | Distinguishing number of the journey log (Annex II, point 3(a)). |
| `journeyType` | string (long-journey \\| short-journey) | yes | no — always disclosed | long-journey (> 8 h, Art. 2(m)) or short-journey. |
| `organiser` | legalEntity | yes | no — always disclosed | Organiser (Art. 2(q)). |
| `transporters` | array of object | yes | no — always disclosed | Transporters in the journey log, by authorisation number (A01). |
| `responsiblePerson` | naturalPerson | no | yes | Natural person responsible for information on planning, execution and completion (Art. 5(2)–(3)). |
| `animals` | object | yes | no — always disclosed | Animals planned. |
| `placeOfDeparture` | place | yes | no — always disclosed | Place of departure (Art. 2(r)). |
| `plannedDeparture` | dateTime | yes | no — always disclosed | Date and time of departure (Art. 4(1)(c)). |
| `placeOfDestination` | place | yes | no — always disclosed | Intended place of destination (Art. 2(s)). |
| `expectedDurationHours` | number | yes | no — always disclosed | Expected duration of the journey (Art. 4(1)(e)). |
| `plannedRestAndTransferPoints` | array of object | no | yes | Planned places of rest or transfer, incl. control posts. |
| `vehicleApprovalNumbers` | array of string | yes | no — always disclosed | C01 approval numbers of the vehicles used. |
| `driverCertificateNumbers` | array of string | no | yes | B01 certificate numbers of drivers and attendants. |
| `healthCertificateReferences` | array of string | no | yes | H01 references (may be added after approval; Annex II, point 3(b)). |
| `approval` | object | yes | no — always disclosed | Approval by the competent authority of the place of departure after its checks (Art. 14(1)(a)–(c)). |
| `pinnedVersions` | versionSet | yes | no — always disclosed | Semantic-model, credential-schema and rule-set versions pinned at journey start. |

**Open questions for T4.1:** (1) Short journeys: whether the pilot issues an anchor for journeys without an approval step today.

## I02 En-Route Welfare Log Entry (bound event)

A signed journey event bound to the I01 anchor and hash-linked to the previous event. Sensor streams are not credentials: temperature is summarised here, the raw Tier-2 data stay in tamper-protected storage and are referenced by digest.

- **Schema:** [`schemas/events/i02-en-route-welfare-log-entry.schema.json`](schemas/events/i02-en-route-welfare-log-entry.schema.json) · **vct:** `urn:traced:event:i02-en-route-welfare-log-entry:0.1` · **format:** SD-JWT VC (event type)
- **Kind:** bound-event (bound to I01)
- **Consolidates:** — (carried under I01)
- **Issuer:** Transporter (driver device, on behalf of the transporter — Annex II, Section 4); official-check events are signed by the checking official veterinarian or authority.
- **Holder:** Transporter; synchronised progressively to the platform.
- **Verifiers:** Competent authority en route (Art. 15(1)); Control posts; Competent authority of destination and departure
- **Legal basis:** Reg (EC) No 1/2005 Annex II, Section 4; Reg (EC) No 1/2005 Annex I, Chapter V (intervals, journey times, rest); Reg (EC) No 1/2005 Art. 6(9) and Annex I, Chapter VI, point 4 (navigation system); Reg (EC) No 1255/97 Art. 6 (fitness to continue confirmed on the journey log at control posts)
- **Forward compatibility:** COM(2023) 770 (proposal) — forward-compatibility only: journey records in TRACES; mapping in T2.1.
- **Validity:** Permanent record ("valid at the time"). · **Revocation:** Not revoked; corrections are new events.
- **Integrity:** Signed event; hash-linked; Tier-2 sensor data by digest.
- **Use cases:** UC-2 in-transit welfare, UC-3 official verification at control points

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `journeyId` | string | yes | no — always disclosed | I01 anchor. |
| `sequenceNumber` | integer | yes | no — always disclosed | Position in the event trail. |
| `previousEventDigest` | digest | yes | no — always disclosed | Digest of the previous event (or of the anchor for the first event). |
| `eventType` | string (departure \\| rest-start \\| rest-end \\| watering-feeding \\| transfer \\| control-post-arrival \\| control-post-departure \\| official-check \\| anomaly) | yes | no — always disclosed | Event type. |
| `occurredAt` | dateTime | yes | no — always disclosed | Event time. |
| `location` | object | yes | yes | Where the event occurred. Driver geolocation is personal data: country is always disclosed, coordinates only when the check requires them. |
| `welfare` | object | no | yes | Welfare observations for the event. |
| `fitToContinue` | boolean | no | no — always disclosed | Official-check and control-post events: animals confirmed fit to continue. |
| `sensorEvidenceDigest` | digest | no | yes | Digest of the Tier-2 sensor/telematics records covering the event. |
| `signer` | object | yes | no — always disclosed | Who signed this event. |

**Open questions for T4.1:** (1) Granularity: one event per stop vs. periodic welfare summaries.

## I07 Post-Arrival Journey Completion Report (bound event)

Closes the journey trail: the transporter's completion declaration (journey log Section 4) and the record-keeping facts that replace the paper return of the journey log.

- **Schema:** [`schemas/events/i07-post-arrival-journey-completion.schema.json`](schemas/events/i07-post-arrival-journey-completion.schema.json) · **vct:** `urn:traced:event:i07-post-arrival-journey-completion:0.1` · **format:** SD-JWT VC (event type)
- **Kind:** bound-event (bound to I01)
- **Consolidates:** — (carried under I01)
- **Issuer:** Transporter (Annex II, point 6).
- **Holder:** Transporter; made available to the authority that granted the authorisation and the authority of departure.
- **Verifiers:** Competent authority of the place of departure (Annex II, point 8); Competent authority that granted the transporter authorisation
- **Legal basis:** Reg (EC) No 1/2005 Annex II, points 6 and 8; Section 4; Reg (EC) No 1/2005 Art. 6(9)
- **Forward compatibility:** COM(2023) 770 (proposal) — forward-compatibility only: journey records retained in TRACES.
- **Validity:** Permanent record. · **Revocation:** Not revoked.
- **Integrity:** Signed event; closes the hash-linked trail.
- **Use cases:** UC-4 destination & anomaly

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `journeyId` | string | yes | no — always disclosed | I01 anchor. |
| `previousEventDigest` | digest | yes | no — always disclosed | Digest of the last event in the trail. |
| `arrivalAt` | dateTime | yes | no — always disclosed | Arrival at the place of destination. |
| `actualDurationHours` | number | yes | no — always disclosed | Actual journey duration. |
| `restPeriods` | integer | no | yes | Number of rest periods taken. |
| `deviationsFromPlan` | array of string | no | yes | Deviations from the approved plan, with reasons. |
| `anomalyReportReferences` | array of string | no | yes | References to anomaly reports (Annex II, Section 5). |
| `navigationRecordsRetained` | boolean | yes | no — always disclosed | Navigation-system records retained (≥ 3 years, Art. 6(9)). |
| `declarationCompletedAt` | dateTime | yes | no — always disclosed | Time the transporter completed and signed the declaration (Annex II, point 6). |
| `signer` | object | yes | no — always disclosed | Transporter signing the declaration. |

## I05 Journey Time Compliance Attestation

Result of the deterministic rules-as-code check of journey times and rest periods (Annex I, Chapter V) over the event trail. It is evidence for the verifier, not an authority decision, and it is not machine learning. Driving hours of the driver are a separate rule and not part of this credential.

- **Schema:** [`schemas/i05-journey-time-compliance-attestation.schema.json`](schemas/i05-journey-time-compliance-attestation.schema.json) · **vct:** `urn:traced:credential:i05-journey-time-compliance-attestation:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** I05 Journey Time Compliance Attestation
- **Issuer:** TRACED rules-as-code determination engine (machine issuer, electronic seal of the service operator); runs at the edge and on the platform.
- **Holder:** Transporter (legal-entity wallet).
- **Verifiers:** Competent authority en route — checks of travel times and rest periods (Art. 15(1)); Competent authority of destination and of departure (ex post)
- **Legal basis:** Reg (EC) No 1/2005 Art. 15(1), 15(4); Reg (EC) No 1/2005 Annex I, Chapter V, point 1
- **Forward compatibility:** COM(2023) 770 (proposal) — forward-compatibility only: revised journey-time limits would be a new rule-set version, not a new schema.
- **Validity:** Point in time; re-issued as the trail grows. · **Revocation:** Superseded by a later attestation for the same journey.
- **Integrity:** Service electronic seal; references the evaluated evidence by digest.
- **Use cases:** UC-2 in-transit welfare, UC-3 official verification at control points

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `journeyId` | string | yes | no — always disclosed | I01 anchor. |
| `evaluatedAt` | dateTime | yes | no — always disclosed | Time of evaluation. |
| `coversEventsUpTo` | integer | yes | no — always disclosed | Last I02 sequence number included. |
| `result` | string (compliant \\| non-compliant \\| indeterminate) | yes | no — always disclosed | Overall result. |
| `rulesApplied` | array of string | yes | no — always disclosed | Legal provisions evaluated, e.g. "Annex I, Chapter V, 1.4(d)". |
| `segments` | array of object | no | yes | Per-segment result. |
| `extensionApplied` | boolean | no | yes | Two-hour extension used (Annex I, Chapter V, point 1.8). |
| `evidenceDigest` | digest | no | yes | Digest of the event trail and Tier-2 data evaluated. |
| `engine` | object | yes | no — always disclosed | Determination engine and rule set. |

**Open questions for T4.1:** (1) Legal standing of a machine-issued attestation: to be settled in T2.4 / T3.3 (evidence only; the authority decides).

## I09 Destination Farm Reception & Welfare Assessment

Arrival event and condition on arrival, each animal categorised fit, unfit or dead in line with Reg (EC) No 1/2005; injuries are assessed within "unfit". Carries the UC-4 anomaly reporting — there is no separate mortality or injury credential.

- **Schema:** [`schemas/i09-destination-reception-and-welfare-assessment.schema.json`](schemas/i09-destination-reception-and-welfare-assessment.schema.json) · **vct:** `urn:traced:credential:i09-destination-reception-and-welfare-assessment:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** I09 Destination Farm Reception & Welfare Assessment
- **Issuer:** Keeper at the place of destination (Art. 8(2); Annex II, point 4 and Section 3). At a slaughterhouse, the official veterinarian's controls remain a separate official control and are referenced, not replaced.
- **Holder:** Keeper at destination; shared with the transporter and the authorities.
- **Verifiers:** Competent authority of the place of destination; Competent authority of the place of departure (notification of breaches, Art. 26(3)); Transporter
- **Legal basis:** Reg (EC) No 1/2005 Art. 8(2), 15(3), 26(3); Reg (EC) No 1/2005 Annex II, point 4, Sections 3 and 5; Reg (EC) No 1/2005 Annex I, Chapter I
- **Forward compatibility:** COM(2023) 770 (proposal) — forward-compatibility only: destination checks and recording in TRACES; mapping in T2.1.
- **Validity:** Permanent record. · **Revocation:** Not revoked; corrections are new versions.
- **Integrity:** Issuer signature; Tier-1 sealed evidence by digest.
- **Use cases:** UC-4 destination & anomaly

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `journeyId` | string | yes | no — always disclosed | I01 anchor. |
| `placeOfDestination` | place | yes | no — always disclosed | Place of destination (establishment id required). |
| `destinationType` | string (holding \\| slaughterhouse \\| assembly-centre \\| other) | yes | no — always disclosed | Type of destination. |
| `arrivalAt` | dateTime | yes | no — always disclosed | Arrival time. |
| `unloadingCompletedAt` | dateTime | no | no — always disclosed | End of unloading. |
| `animalsReceived` | integer | yes | no — always disclosed | Animals received. |
| `conditionOnArrival` | object | yes | no — always disclosed | Counts by category. |
| `animals` | array of object | no | yes | Per-animal findings where the law requires individual traceability; otherwise omitted. |
| `anomalyReportReference` | string | no | yes | Anomaly report (Annex II, Section 5), if any. |
| `evidenceDigests` | array of digest | no | yes | Tier-1 sealed photo/video evidence, by digest. |
| `receivedBy` | object | yes | no — always disclosed | Keeper at the place of destination. |

**Open questions for T4.1:** (1) Signature means for keepers without a legal-entity wallet (farms run by natural persons).

## J01 Farm/Holding Registration

Registration (and, where required, approval) of the establishment of origin, with the status information needed for the pre-departure check.

- **Schema:** [`schemas/j01-holding-registration.schema.json`](schemas/j01-holding-registration.schema.json) · **vct:** `urn:traced:credential:j01-holding-registration:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** J01 Farm/Holding Registration
- **Issuer:** Competent authority keeping the register of establishments.
- **Holder:** Operator of the establishment (keeper).
- **Verifiers:** Competent authority of the place of departure; Organiser and transporter (origin check); Competent authority of destination
- **Legal basis:** Reg (EU) 2016/429 (Animal Health Law) Art. 84, 93, 94, 101; Reg (EC) No 1/2005 Art. 4(1)(a)
- **Forward compatibility:** Unaffected by COM(2023) 770.
- **Validity:** Short: status statements carry their own validity; re-issued on change. · **Revocation:** On deregistration, suspension or new restriction → status list.
- **Integrity:** Issuer electronic seal.
- **Use cases:** UC-1 pre-departure

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `registrationNumber` | string | yes | no — always disclosed | Registration number of the establishment. |
| `approvalNumber` | string | no | no — always disclosed | Approval number, where the establishment is approved (e.g. assembly centre). |
| `establishmentType` | string (holding \\| assembly-centre \\| control-post \\| slaughterhouse \\| other) | yes | no — always disclosed | Type of establishment. |
| `operator` | object | no | yes | Operator of the establishment; a natural person's name is personal data. |
| `location` | place | yes | no — always disclosed | Address of the establishment. |
| `speciesKept` | array of species | yes | no — always disclosed | Species kept. |
| `movementRestriction` | boolean | yes | no — always disclosed | Whether a movement restriction applies at the time of issue. |
| `healthStatus` | array of object | no | yes | Disease-status statements relevant to movement. |
| `competentAuthority` | competentAuthority | yes | no — always disclosed | Authority keeping the register. |
| `statusAsOf` | dateTime | yes | no — always disclosed | Time the status was taken from the register. |

**Open questions for T4.1:** (1) Keepers who are natural persons: EUDI Wallet vs. an authority-held record presented by reference.

## K05 TRACES NT Journey Registration Record

Wallet-verifiable reference to the journey's registration in TRACES NT and the notifications sent to the authorities concerned, with the border-crossing events of the journey. TRACED reads TRACES NT; it does not modify it.

- **Schema:** [`schemas/k05-traces-nt-journey-registration-record.schema.json`](schemas/k05-traces-nt-journey-registration-record.schema.json) · **vct:** `urn:traced:credential:k05-traces-nt-journey-registration-record:0.1` · **format:** SD-JWT VC
- **Kind:** credential
- **Consolidates:** K05 TRACES NT Journey Registration Record
- **Issuer:** Competent authority of the place of departure, from its TRACES NT record, through the authority verify-and-issue channel (T4.4).
- **Holder:** Transporter (legal-entity wallet).
- **Verifiers:** Competent authorities en route and at destination; Official veterinarians at control posts
- **Legal basis:** Reg (EC) No 1/2005 Art. 14(1)(d); Reg (EU) 2016/429 (Animal Health Law) Art. 152; Reg (EU) 2019/1715 (IMSOC / TRACES)
- **Forward compatibility:** COM(2023) 770 (proposal) — forward-compatibility only: Art. 15 (journey log in TRACES). TRACES modernisation is not coupled to the wallet timeline.
- **Validity:** Until journey completion. · **Revocation:** Cancellation in TRACES NT → status list.
- **Integrity:** Issuer electronic seal; mirrors TRACES NT references only.
- **Use cases:** UC-3 official verification at control points

| Claim | Type | Mandatory | Selectively disclosable | Description |
|---|---|---|---|---|
| `journeyId` | string | yes | no — always disclosed | I01 anchor. |
| `tracesReferences` | object | yes | no — always disclosed | TRACES NT references. |
| `notifiedAuthorities` | array of object | no | yes | Authorities notified via TRACES (Art. 14(1)(d); AHL Art. 152). |
| `borderCrossings` | array of object | no | yes | Planned and actual internal-border crossings. |
| `registeredAt` | dateTime | yes | no — always disclosed | Time of registration in TRACES NT. |
| `recordedBy` | competentAuthority | yes | no — always disclosed | Authority whose TRACES NT record this reflects. |

**Open questions for T4.1:** (1) Availability of a TRACES NT test or acceptance environment for the pilot.
