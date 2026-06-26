# Vendor Security Questionnaire

**Used for:** Evaluating third-party SaaS vendors before onboarding
**Scenario:** A fictional healthcare startup ("Meridian Health") is evaluating a new SaaS HR platform vendor ("PeopleFlow HR") before signing a contract.
**Framework basis:** Questions are modeled on NIST Cybersecurity Framework (CSF) 2.0 categories and the Standardized Information Gathering (SIG) Lite questionnaire used industry-wide for vendor risk assessments.

This questionnaire is sent to the vendor. Their answers get fed into `vendor_responses.json`, which the triage script (`triage_vendor.py`) reads and scores.

---

## Section 1: Identity & Access Management
*(Maps to NIST CSF 2.0: PR.AA — Identity Management, Authentication, and Access Control)*

1. Does your platform support multi-factor authentication (MFA) for all user accounts?
2. Do you enforce role-based access control (RBAC) so users only see data relevant to their role?
3. How quickly can an administrator deactivate a former employee's access after termination?

## Section 2: Data Protection
*(Maps to NIST CSF 2.0: PR.DS — Data Security)*

4. Is data encrypted at rest (while stored)?
5. Is data encrypted in transit (while being transmitted, e.g. HTTPS/TLS)?
6. Where is customer data physically stored (which country/region)?
7. Do you have a documented data retention and deletion policy?

## Section 3: Incident Response & Monitoring
*(Maps to NIST CSF 2.0: DE — Detect, RS — Respond)*

8. Do you have a documented incident response plan?
9. What is your commitment for notifying customers after a confirmed data breach (in hours)?
10. Do you conduct regular security monitoring/logging of access to customer data?

## Section 4: Compliance & Governance
*(Maps to NIST CSF 2.0: GV — Govern)*

11. Are you SOC 2 Type II certified, or do you hold an equivalent independent security audit?
12. Are you compliant with HIPAA if handling protected health information (PHI)?
13. Do you have a named individual or team responsible for security/compliance?

## Section 5: Business Continuity
*(Maps to NIST CSF 2.0: RC — Recover)*

14. Do you maintain regular backups of customer data?
15. What is your documented Recovery Time Objective (RTO) in the event of an outage?

---

## Scoring Logic Summary

The triage script treats the following answers as **automatic High Risk Exceptions**, regardless of how the vendor scores elsewhere:

- No to Multi-Factor Authentication (Q1)
- No to Encryption at Rest (Q4)
- No to Encryption in Transit (Q5)
- No to Incident Response Plan (Q8)
- No to HIPAA Compliance, if the vendor will handle PHI (Q12)

These five controls are treated as non-negotiable baseline requirements for any vendor touching healthcare data. A vendor can be excellent everywhere else and still fail vendor risk review if any of these come back "No."
