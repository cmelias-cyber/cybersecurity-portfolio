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

**Date:** August 2, 2026

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



