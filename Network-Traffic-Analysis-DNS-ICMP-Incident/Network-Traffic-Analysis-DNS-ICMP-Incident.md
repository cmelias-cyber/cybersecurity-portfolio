# Network Traffic Analysis: DNS and ICMP Incident

## Objective

The purpose of this project is to analyze network traffic logs using tcpdump to identify the cause of a service disruption. The focus is on examining DNS queries and ICMP error responses to determine which protocol and service were affected.

---

## Incident Summary

Users reported being unable to access the website **[www.yummyrecipesforme.com](http://www.yummyrecipesforme.com)**, receiving the error message:

“destination port unreachable.”

Initial investigation revealed that DNS requests sent over UDP were not successfully reaching the DNS server.

---

## Network Traffic Analysis

The tcpdump logs show that:

* The client system sent **UDP packets** to the DNS server on **port 53**
* The DNS request was attempting to resolve the domain name to an IP address
* The server responded with **ICMP error messages**
* The error message received was: **“udp port 53 unreachable”**

This indicates that the DNS service on the destination server was not accessible.

---

## Protocols Involved

### UDP (User Datagram Protocol)

UDP was used to send DNS queries to the server. Since UDP is connectionless, it does not guarantee delivery, making it dependent on service availability at the destination port.

### DNS (Domain Name System)

DNS is responsible for translating domain names into IP addresses. The failure of DNS requests prevented the browser from obtaining the IP address needed to load the website.

### ICMP (Internet Control Message Protocol)

ICMP was used by the server to return error messages. The “port unreachable” message indicates that no service was listening on the specified port.

---

## Key Findings

* **Port affected:** 53 (DNS service)
* **Error type:** ICMP “destination port unreachable”
* **Affected protocol:** DNS over UDP
* **Impact:** Users unable to resolve domain name and access website

---

## Root Cause Analysis

The most likely cause of the incident is that **port 53 on the DNS server was unavailable**.

Possible reasons include:

* DNS service was down or not running
* Firewall blocking UDP port 53
* Misconfigured DNS server settings

---

## Response and Next Steps

The issue was identified after users reported being unable to access the website. The IT team used tcpdump to capture and analyze network traffic, revealing repeated ICMP error responses.

Recommended next steps include:

* Verify DNS server status and ensure the service is running
* Check firewall rules for UDP port 53
* Confirm correct DNS configuration
* Monitor network traffic for continued anomalies

---

## Security Implications

This type of issue could indicate:

* A **Denial of Service (DoS) attack** targeting DNS services
* Misconfiguration of critical network services
* Network-level filtering or blocking

Failure of DNS services can disrupt access to web resources and impact business operations.

---

## Skills Developed

* Analyzing packet-level network data
* Interpreting ICMP error messages
* Understanding DNS and UDP interactions
* Identifying service-level failures
* Writing structured cybersecurity incident reports

