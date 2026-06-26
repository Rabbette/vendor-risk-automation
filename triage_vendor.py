"""
Vendor Risk Automation - Third-Party Security Questionnaire Triage
---------------------------------------------------------------------
Reads a vendor's questionnaire responses (JSON) and automatically flags
"High Risk Exceptions" based on a baseline security rubric.

The scenario: a fictional healthcare startup (Meridian Health) is
evaluating a new SaaS HR vendor (PeopleFlow HR) before signing a
contract. Certain controls are non-negotiable when a vendor will
handle Protected Health Information (PHI), regardless of how well
they score elsewhere.
"""

import json
from datetime import datetime

# ---------------------------------------------------------------------
# STEP 1: Define the baseline rubric.
# Each entry says: which question key to check, what answer counts as
# a failure, and why that control matters (used in the report output).
# ---------------------------------------------------------------------

BASELINE_CONTROLS = [
    {
        "key": "q1_mfa_supported",
        "fail_value": "No",
        "label": "Multi-Factor Authentication (MFA)",
        "why_it_matters": "Without MFA, a single stolen password can fully compromise an account with access to employee data.",
    },
    {
        "key": "q4_encryption_at_rest",
        "fail_value": "No",
        "label": "Encryption at Rest",
        "why_it_matters": "Unencrypted stored data is fully readable if the underlying storage is ever breached or misconfigured.",
    },
    {
        "key": "q5_encryption_in_transit",
        "fail_value": "No",
        "label": "Encryption in Transit",
        "why_it_matters": "Data sent without encryption can be intercepted in transit between systems.",
    },
    {
        "key": "q8_incident_response_plan",
        "fail_value": "No",
        "label": "Incident Response Plan",
        "why_it_matters": "Without a documented plan, a breach response will be improvised and slower, increasing damage and notification delays.",
    },
]

# This control only applies if the vendor will handle PHI (Protected Health Information)
PHI_CONDITIONAL_CONTROL = {
    "key": "q12_hipaa_compliant",
    "fail_value": "No",
    "label": "HIPAA Compliance",
    "why_it_matters": "Any vendor handling PHI without HIPAA compliance exposes the client to direct regulatory liability.",
}


def load_vendor_responses(json_path: str):
    """Reads the vendor's questionnaire response file."""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def evaluate_vendor(vendor_data: dict):
    """
    Checks the vendor's responses against the baseline rubric.
    Returns a list of exceptions found (empty list means the vendor
    passed every baseline control).
    """
    responses = vendor_data["responses"]
    exceptions = []

    # Check the always-required controls
    for control in BASELINE_CONTROLS:
        answer = responses.get(control["key"])
        if answer == control["fail_value"]:
            exceptions.append({
                "control": control["label"],
                "answer_given": answer,
                "why_it_matters": control["why_it_matters"],
            })

    # Check the PHI-conditional control, only if this vendor will handle PHI
    if vendor_data.get("will_handle_phi"):
        answer = responses.get(PHI_CONDITIONAL_CONTROL["key"])
        if answer == PHI_CONDITIONAL_CONTROL["fail_value"]:
            exceptions.append({
                "control": PHI_CONDITIONAL_CONTROL["label"],
                "answer_given": answer,
                "why_it_matters": PHI_CONDITIONAL_CONTROL["why_it_matters"],
            })

    return exceptions


def print_report(vendor_data: dict, exceptions: list):
    """Prints a clean, readable vendor risk report to the terminal."""
    print("=" * 70)
    print("VENDOR RISK ASSESSMENT REPORT")
    print(f"Vendor: {vendor_data['vendor_name']}")
    print(f"Assessment date: {vendor_data['assessment_date']}")
    print(f"Evaluated by: {vendor_data['evaluated_by']}")
    print(f"Will handle PHI: {vendor_data['will_handle_phi']}")
    print("=" * 70)
    print()

    if not exceptions:
        print("RESULT: PASS")
        print("No high-risk exceptions found against baseline controls.")
    else:
        print(f"RESULT: {len(exceptions)} HIGH RISK EXCEPTION(S) FOUND")
        print()
        for i, exc in enumerate(exceptions, start=1):
            print(f"  {i}. {exc['control']} - Answer given: {exc['answer_given']}")
            print(f"     Why it matters: {exc['why_it_matters']}")
            print()
        print("RECOMMENDATION: Do not proceed with onboarding until the above")
        print("exceptions are remediated or formally accepted as a documented risk")
        print("by a designated risk owner.")


def save_report_json(vendor_data: dict, exceptions: list, output_path: str):
    """Saves the assessment result as a JSON file for record-keeping."""
    report = {
        "vendor_name": vendor_data["vendor_name"],
        "assessment_date": vendor_data["assessment_date"],
        "evaluated_by": vendor_data["evaluated_by"],
        "generated_at": datetime.now().isoformat(),
        "exception_count": len(exceptions),
        "exceptions": exceptions,
        "overall_result": "PASS" if not exceptions else "HIGH RISK EXCEPTIONS FOUND",
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)


if __name__ == "__main__":
    vendor_data = load_vendor_responses("vendor_responses.json")
    exceptions = evaluate_vendor(vendor_data)
    print_report(vendor_data, exceptions)
    save_report_json(vendor_data, exceptions, "risk_assessment_report.json")
    print()
    print("Full report saved to risk_assessment_report.json")
