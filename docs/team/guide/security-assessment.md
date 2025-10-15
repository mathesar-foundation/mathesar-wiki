# Security Assessment guide

This page serves as a guide for Mathesar team members to use when trying to decide the risk or severity of a (potential) vulnerability.

## CVSS

For now, we'll use the typical standard CVSS when trying to figure out whether a vulnerability is a big problem. For convenience, here's a calculator with nice tooltips to explain how to fill it out:

https://nvd.nist.gov/vuln-metrics/cvss/v4-calculator

## Assessment of issues and proposed features

If a team member notices a proposed feature or issue that we plan to implement, and that feature has some perceived security risk, that team member should do an assessment based on their understanding of the proposed feature using the calculator above. Only fill out the "Base Metrics" section. For example, consider [File Upload support in forms](https://github.com/mathesar-foundation/mathesar/issues/4829). Here's my attempt at an assessment:

![sec_assess_ex_before.png](/assets/images/sec_assess_ex_before.png)

This assessment is based _only_ on the issue description. If the score is "Medium" or "High", or if the team is otherwise uncomfortable with the security implications, we then discuss mitigation options, and then reassess.

### Review of PR related to or fixing issue with security implications

This is basically the same, except that if we can't convince ourselves that the score for the CVSS system (Base Metrics only) is "Low" or "None", we should not merge.

In general, any mitigation documentation or work should be included in the PR. It's too easy to skip the follow-up PR and leave the vulnerability in.
