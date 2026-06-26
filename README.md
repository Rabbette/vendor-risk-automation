# Vendor Risk Automation

An automated Third-Party Vendor Risk Assessment workflow. Reads a vendor's completed security questionnaire and automatically flags non-negotiable baseline security gaps as High Risk Exceptions, the same triage judgment a GRC analyst applies when reviewing new vendors before contract signature.

## Scenario

A fictional healthcare startup, **Meridian Health**, is evaluating a new SaaS HR platform, **PeopleFlow HR**, before onboarding. Because the vendor will handle employee data that may include Protected Health Information (PHI), certain controls are treated as mandatory regardless of how the vendor scores elsewhere.

## Architecture

```
VENDOR_QUESTIONNAIRE.md   ->  the questions sent to the vendor (NIST CSF 2.0 / SIG Lite based)
vendor_responses.json     ->  the vendor's completed answers
triage_vendor.py          ->  reads responses, checks against baseline rubric, flags exceptions
risk_assessment_report.json -> generated output: machine-readable assessment result
```

## Baseline controls (non-negotiable)

These four controls trigger an automatic High Risk Exception if answered "No," regardless of the vendor's overall score:

1. Multi-Factor Authentication (MFA)
2. Encryption at Rest
3. Encryption in Transit
4. Incident Response Plan

A fifth control, **HIPAA Compliance**, is conditionally checked only when the vendor will handle PHI.

Full question text and the reasoning behind each control lives in `VENDOR_QUESTIONNAIRE.md`.

## Running it

```
python triage_vendor.py
```

Reads `vendor_responses.json`, prints a readable risk report to the terminal, and saves a structured `risk_assessment_report.json` for record-keeping.

## Note on data

The vendor, company, and all responses in this repository are fictional, built to demonstrate the assessment logic. No real vendor or company data is used.

## What I'd build next

- A scoring tier system (Low/Medium/High/Critical) instead of pass/fail, weighted by data sensitivity
- A simple web form so a non-technical analyst could submit vendor answers without editing JSON directly
- Integration with a ticketing system to auto-open a remediation ticket when an exception is found
