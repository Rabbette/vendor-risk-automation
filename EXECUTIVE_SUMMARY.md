# Executive Summary: PeopleFlow HR Vendor Risk Assessment

**Prepared for:** Meridian Health Leadership
**Prepared by:** GRC Team
**Date:** June 27, 2026
**Subject:** Security risk assessment of proposed SaaS HR vendor, PeopleFlow HR

## Summary

As part of standard vendor onboarding procedure, PeopleFlow HR was evaluated against Meridian Health's baseline third-party security requirements before contract signature. The assessment identified **two High Risk Exceptions** that should be resolved or formally accepted before this vendor is granted access to employee data.

## Findings

PeopleFlow HR does not currently support multi-factor authentication for user accounts, and does not maintain a documented incident response plan. Both are treated as baseline, non-negotiable requirements for any vendor handling employee or health-adjacent data, independent of how strong the vendor's other controls are. By contrast, the vendor met or exceeded expectations on encryption (both at rest and in transit), data retention policy, SOC 2 certification, HIPAA compliance, and backup/recovery practices.

## Business Impact

The absence of multi-factor authentication materially increases the likelihood that a single compromised credential could expose employee records, including any health-related data processed through the HR platform. The absence of a documented incident response plan means that, in the event of a breach, the vendor's response time and containment effectiveness cannot be reliably predicted, which directly affects Meridian Health's own regulatory notification obligations under HIPAA.

## Recommendation

Onboarding should not proceed until PeopleFlow HR either implements multi-factor authentication and a documented incident response plan, or these gaps are formally accepted as a documented residual risk by a designated risk owner with appropriate sign-off authority. Re-assessment is recommended within 90 days if either exception is accepted rather than remediated.

## Time and Effort Saved

This assessment, including questionnaire design and review, took under 30 minutes using an automated triage script, compared to an estimated 2 to 3 hours for a fully manual review of the same questionnaire. At an organization processing multiple vendor assessments per quarter, this approach scales linearly without added review time per vendor.
