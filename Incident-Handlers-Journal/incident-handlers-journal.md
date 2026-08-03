# Incident Handler's Journal

---

# Journal Entry #1

**Date:** July 30, 2026

---

# Project Description (Executive Summary)

This journal entry documents a simulated ransomware incident affecting a small U.S. healthcare clinic. The purpose of this activity was to practice structured incident documentation using the 5 W's framework (Who, What, When, Where, and Why) to capture the essential details of a cybersecurity incident. Effective documentation is a critical component of the incident response lifecycle because it supports investigations, facilitates communication among stakeholders, preserves key findings, and provides a historical record for future security incidents.

**This entry represents the first record in an ongoing incident handler's journal that will document security incidents, observations, and lessons learned throughout the incident response course.**

---

# Tools Used

No specialized cybersecurity software was required for this activity. The incident was analyzed using the provided scenario details, incident documentation, and the 5 W's (Who, What, When, Where, and Why) incident analysis framework.

## Methodologies

- Incident Handler's Journal
- 5 W's Incident Documentation Framework
- Incident Response Documentation
- Scenario-Based Incident Analysis

---

# Incident Summary (5 W's)

## Who

An organized group of unethical hackers known to target healthcare and transportation organizations conducted the attack. The attackers gained unauthorized access to the organization's network through a targeted phishing campaign.

---

## What

The organization experienced a ransomware attack that encrypted critical business and patient files. Employees were unable to access medical records, business applications, and other essential systems, resulting in a complete disruption of normal business operations.

---

## When

The incident occurred on **Tuesday at approximately 9:00 a.m.**, when employees began reporting that they could no longer access files on their computers and ransom notes appeared across multiple workstations.

---

## Where

The attack impacted a small U.S. healthcare clinic specializing in primary-care services. The ransomware affected the organization's internal computer systems, preventing employees from accessing patient records and other mission-critical resources.

---

## Why

The attackers successfully compromised the organization's network through phishing emails containing malicious attachments. Once an employee downloaded the attachment, malware was installed, allowing the attackers to deploy ransomware that encrypted the organization's files. The ransom demand indicates the attackers were financially motivated.

---

# Additional Notes

## Observations

- Phishing remains one of the most common initial access vectors used to deploy ransomware.
- Employee security awareness training could significantly reduce the likelihood of successful phishing attacks.
- Maintaining secure offline backups and regularly testing disaster recovery procedures can minimize operational downtime and reduce reliance on ransom payments.

## Questions for Further Investigation

1. How could stronger email filtering and phishing awareness training have prevented this incident?
2. Should organizations ever pay a ransomware demand, or should recovery rely exclusively on secure backups and incident response procedures?
3. What endpoint detection and monitoring controls could have detected or prevented the ransomware before file encryption occurred?

---

# Key Skills Demonstrated

- Security Incident Documentation
- Incident Response Fundamentals
- Ransomware Analysis
- Phishing Attack Analysis
- Root Cause Analysis
- Threat Assessment
- Technical Documentation
- Security Reporting
- Critical Thinking
- Structured Incident Analysis

---

# Key Takeaways

- Thorough documentation is an essential component of every stage of the incident response lifecycle.
- The 5 W's framework provides a structured and repeatable method for recording and communicating incident details.
- Ransomware attacks frequently originate from phishing campaigns and can rapidly disrupt critical business operations.
- Maintaining detailed incident journals supports future investigations, strengthens organizational knowledge, and improves incident response readiness.


---

# Journal Entry #2

**Date:** July 31, 2026

---

# Project Description (Executive Summary)

This journal entry documents the analysis of a packet capture (PCAP) file using Wireshark, a graphical network protocol analyzer widely used during security investigations. The objective of this activity was to develop foundational network traffic analysis skills by examining packet headers, protocol layers, and communication patterns. This exercise aligns with the Detection and Analysis phase of the NIST Incident Response Lifecycle, where network traffic is examined to validate alerts, identify suspicious activity, and better understand communications between systems.

---

# Tools Used

**Wireshark**

Wireshark is a graphical network protocol analyzer that enables security analysts to capture, inspect, and analyze network traffic. During this activity, Wireshark was used to open and examine a packet capture (PCAP) file, inspect packet structures across multiple protocol layers, and apply display filters to isolate relevant traffic for analysis.

## Methodologies

- Network Traffic Analysis
- Packet Inspection
- Protocol Analysis
- Display Filtering
- Detection and Analysis (NIST Incident Response Lifecycle)

---

# Activity Summary

During this activity, a packet capture file containing web browsing traffic was analyzed using Wireshark. Display filters were applied to isolate specific IP addresses, MAC addresses, DNS traffic, TCP communications, and application-layer data. Individual packets were examined to better understand protocol behavior across the Ethernet, IPv4, TCP, and DNS layers, demonstrating how packet inspection can support incident investigations and network troubleshooting.

---

# Additional Notes

## Observations

- Display filters significantly improve the efficiency of packet analysis by narrowing large packet captures to relevant network traffic.
- Examining protocol layers individually provides valuable insight into how data is encapsulated and transmitted across a network.
- DNS queries, TCP sessions, and HTTP communications each reveal different aspects of network behavior that can assist during incident investigations.
- Packet analysis is a fundamental skill for validating alerts and identifying suspicious network activity.

## Questions for Further Investigation

1. How can packet analysis be combined with SIEM data to accelerate incident investigations?
2. What indicators within packet captures commonly suggest malicious network activity?
3. How does encrypted traffic affect the visibility available during packet analysis?

---

# Key Skills Demonstrated

- Wireshark Navigation
- Network Traffic Analysis
- Packet Inspection
- Protocol Analysis
- Display Filtering
- TCP/IP Fundamentals
- DNS Analysis
- Technical Investigation
- Critical Thinking

---

# Key Takeaways

- Wireshark provides detailed visibility into network communications at multiple protocol layers.
- Packet inspection enables analysts to identify communication patterns and validate network activity.
- Display filters allow analysts to efficiently isolate relevant packets within large network captures.
- Understanding packet structure is an essential skill for incident detection, forensic investigations, and network security analysis.


---

# Journal Entry #3

**Date:** August 1, 2026

---

# Project Description (Executive Summary)

This journal entry documents the investigation of a suspicious file hash using VirusTotal, a threat intelligence platform widely used by security analysts to identify malicious files and associated indicators of compromise (IoCs). The objective of this activity was to validate a security alert, evaluate the file's maliciousness, and identify additional indicators that could support future detection and response efforts. This investigation aligns with the **Detection and Analysis** phase of the NIST Incident Response Lifecycle, where analysts validate alerts, assess potential threats, and gather evidence to determine the scope and impact of an incident. :contentReference[oaicite:0]{index=0}

---

# Tools Used

**VirusTotal**

VirusTotal is a cloud-based threat intelligence platform that analyzes suspicious files, URLs, domains, IP addresses, and file hashes using results from numerous security vendors and community intelligence. During this activity, VirusTotal was used to investigate a SHA-256 file hash, review vendor detection results, examine malware behavior, and identify additional indicators of compromise associated with the malicious file. :contentReference[oaicite:1]{index=1}

## Methodologies

- Threat Intelligence Analysis
- Indicator of Compromise (IoC) Identification
- Malware Investigation
- Detection and Analysis (NIST Incident Response Lifecycle)
- Pyramid of Pain Framework

---

# Incident Summary (5 W's)

## Who

An unknown malicious actor distributed a password-protected malicious spreadsheet attachment through a phishing email targeting an employee at a financial services company.

---

## What

An employee downloaded and opened the malicious attachment, resulting in the execution of a malicious payload. An intrusion detection system later detected unauthorized executable files and generated an alert for the Security Operations Center (SOC). :contentReference[oaicite:2]{index=2}

---

## When

The employee received the email at **1:11 p.m.**, opened the attachment at **1:13 p.m.**, unauthorized executable files appeared at **1:15 p.m.**, and the SOC received an alert at **1:20 p.m.** :contentReference[oaicite:3]{index=3}

---

## Where

The incident occurred on an employee's workstation within a financial services organization after a malicious email attachment was executed. :contentReference[oaicite:4]{index=4}

---

## Why

The phishing email successfully convinced the employee to download and execute a password-protected malicious attachment. The investigation used VirusTotal to validate the malicious file hash, identify related indicators of compromise, and support further incident detection and response activities. :contentReference[oaicite:5]{index=5}

---

# Additional Notes

## Observations

- Threat intelligence platforms significantly improve the efficiency of malware investigations by aggregating analysis from multiple security vendors.
- File hashes provide reliable indicators for identifying known malicious files across different security tools.
- Investigating related indicators of compromise strengthens an organization's ability to detect similar threats in the future.
- The Pyramid of Pain demonstrates that higher-level indicators, such as attacker tactics and techniques, are generally more difficult for adversaries to modify than simple file hashes.

## Questions for Further Investigation

1. Which additional indicators of compromise should be incorporated into security monitoring and detection rules?
2. Could enhanced email filtering or security awareness training have prevented the malicious attachment from being executed?
3. How can threat intelligence gathered from VirusTotal improve future incident response investigations?

---

# Key Skills Demonstrated

- Threat Intelligence Analysis
- Malware Investigation
- VirusTotal Analysis
- Indicator of Compromise (IoC) Identification
- SHA-256 Hash Analysis
- Incident Investigation
- Threat Assessment
- Security Documentation
- Critical Thinking

---

# Key Takeaways

- Threat intelligence platforms accelerate incident investigations by providing community-driven malware analysis.
- File hashes serve as valuable indicators of compromise for identifying known malicious artifacts.
- Combining multiple sources of threat intelligence improves confidence when validating security alerts.
- Understanding indicators of compromise and the Pyramid of Pain strengthens an analyst's ability to detect and respond to future attacks.

---

# Journal Entry #4

**Date:** August 3, 2026

---

# Project Description (Executive Summary)

This journal entry documents the review and finalization of an incident handler's journal developed throughout the Google Cybersecurity Professional Certificate. The objective of this activity was to review previous incident investigations, improve documentation quality, ensure completeness, and consolidate technical findings into a single professional reference. This activity aligns with the **Post-Incident Activity** phase of the NIST Incident Response Lifecycle, where documentation is reviewed, lessons learned are captured, and opportunities for continuous improvement are identified.

---

# Tools Used

No specialized cybersecurity software was required for this activity.

The journal was reviewed using previously completed incident investigations, technical analyses, and documentation produced throughout the course. The focus of this activity was on improving documentation quality, maintaining consistency across journal entries, and organizing findings into a professional incident response reference.

## Methodologies

- Incident Documentation Review
- Lessons Learned
- Continuous Improvement
- Post-Incident Activity (NIST Incident Response Lifecycle)
- Technical Documentation

---

# Activity Summary

The incident handler's journal was reviewed to verify the accuracy, completeness, and consistency of all previous entries. Existing documentation was refined by correcting formatting, expanding technical explanations, identifying the applicable NIST Incident Response Lifecycle phases, and organizing the journal into a professional portfolio artifact that demonstrates incident response knowledge and technical growth.

---

# Additional Notes

## Observations

- Consistent documentation improves communication during incident response and supports future investigations.
- Reviewing previous work helped identify opportunities to improve technical writing and strengthen incident documentation.
- Organizing multiple investigations into a single journal creates a valuable professional reference that demonstrates continuous learning.

## Questions for Future Development

1. How can future incident journals be expanded to include more complex investigations and enterprise security tools?
2. Which documentation practices are most valuable during real-world incident response engagements?
3. How can standardized documentation improve collaboration between SOC analysts and incident responders?

---

# Key Skills Demonstrated

- Incident Documentation
- Technical Writing
- Documentation Review
- Lessons Learned
- Post-Incident Analysis
- Continuous Improvement
- Incident Response Lifecycle
- Professional Portfolio Development

---

# Key Takeaways

- Well-maintained documentation is a critical component of effective incident response.
- Reviewing previous investigations strengthens both technical understanding and reporting quality.
- Lessons learned support continuous improvement of future incident response efforts.
- Maintaining an incident handler's journal creates a lasting professional record of technical growth and practical cybersecurity experience.



