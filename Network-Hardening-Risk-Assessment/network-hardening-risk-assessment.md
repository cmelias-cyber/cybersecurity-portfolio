# Network Hardening Risk Assessment

## Objective
The objective of this assessment is to analyze security weaknesses identified after a data breach at a social media organization and recommend network hardening measures to reduce the risk of future attacks.

The investigation identified several vulnerabilities, including shared employee passwords, use of a default administrator password, lack of firewall filtering rules, and absence of multifactor authentication (MFA). These weaknesses increased the risk of unauthorized access and exposure of sensitive customer information. This assessment evaluates the organization’s security risks and proposes hardening controls designed to strengthen network security, improve access control, and reduce the organization’s overall attack surface.posture and reduce the risk of future breaches.

---

## Identified Vulnerabilities
- Shared employee passwords
- Default database administrator password
- Missing firewall filtering rules
- Lack of multifactor authentication (MFA)

## Recommended Hardening Measures

### 1. Password Policies
Explain:
- prohibit password sharing
- require unique passwords
- prevent default passwords
- reduce brute-force risk

### 2. Multifactor Authentication (MFA)
Explain:
- secondary verification
- protects accounts even if passwords are compromised
- effective against credential attacks

### 3. Firewall Maintenance and Port Filtering
Explain:
- restrict unauthorized inbound/outbound traffic
- reduce attack surface
- monitor abnormal traffic patterns

## Why These Controls Are Effective
Short section tying recommendations back to the breach scenario.

Example:
- Password controls reduce credential compromise risk
- MFA limits unauthorized account access
- Firewall filtering improves network traffic control and visibility

## Security Recommendations
Short operational recommendations such as:
- perform regular configuration reviews
- enforce least privilege access
- conduct periodic security audits
- review firewall rules regularly

## Conclusion
The analysis identified multiple security weaknesses that directly contributed to the data breach, including shared user credentials, a default administrative password, lack of firewall filtering rules, and absence of multifactor authentication.

These vulnerabilities created an environment where unauthorized access was possible with minimal resistance, allowing attackers to compromise customer data and gain control over sensitive systems.

Implementing layered network hardening controls such as MFA, strong password policies, and properly configured firewall rules reduces the attack surface and makes unauthorized access significantly more difficult. When combined, these measures improve overall network resilience and help prevent similar breaches in the future.
