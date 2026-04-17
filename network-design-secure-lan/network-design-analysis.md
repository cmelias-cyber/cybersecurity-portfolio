# Network Design Analysis: Secure Local Area Network (LAN)

## Objective

The purpose of this project was to design a secure Local Area Network (LAN) by correctly placing networking devices and security controls. The design focuses on maintaining connectivity while protecting internal systems from unauthorized access.

---

## Network Structure

The network consists of the following components:

Internet
→ Firewall
→ Router
→ Server
→ Firewall
→ Switch
→ Devices
→ Wireless Access Point (WAP)

Each component plays a specific role in maintaining both connectivity and security.

---

## Device Placement and Security Rationale

### Router

The router connects the internal network to the internet and directs network traffic between systems. It acts as the central point for communication between internal devices and external networks.

### Firewall

Firewalls are placed between network segments to filter traffic and enforce security policies. In this design, multiple firewalls provide layered protection and help prevent unauthorized access to sensitive systems.

This approach follows the principle of **defense in depth**, where multiple security controls reduce the risk of a single point of failure.

### Switch

The switch connects internal devices such as workstations, laptops, and desktops. It allows devices to communicate efficiently within the local network while maintaining organized traffic flow.

### Server

The server provides centralized services and resources to network users. Separating the server from direct internet exposure reduces the risk of external attacks targeting sensitive data.

### Wireless Access Point (WAP)

The wireless access point allows devices to connect to the network wirelessly. Placing the WAP behind a firewall ensures that wireless traffic is monitored and controlled before reaching internal systems.

This reduces the risk associated with unsecured or unauthorized wireless connections.

---

## Security Principles Applied

The network design applies several foundational cybersecurity principles:

* Defense in depth
* Network segmentation
* Access control
* Traffic filtering
* Protection of internal resources

These principles are commonly used in enterprise environments to maintain secure and reliable network operations.

---

## Skills Developed

Through this project, the following skills were strengthened:

* Understanding network infrastructure components
* Designing secure network layouts
* Applying cybersecurity best practices
* Interpreting network diagrams
* Documenting technical systems
