
# Security Concepts

## Overview

Security in networking focuses on protecting data and systems while still allowing necessary access. For CCNA, the key ideas are the CIA triad, basic terminology, common attack types, and the main building blocks of a security program and network defenses.

## CIA triad

### Elements

- Confidentiality  
  Only authorized entities can access data.

- Integrity  
  Data remains accurate and unaltered except by authorized entities.

- Availability  
  Systems and data remain accessible and usable when required.

### Using the CIA triad

- Every attack harms one or more CIA properties.  
- Every control is intended to protect one or more CIA properties.  
- Data includes stored, processed, and transmitted information.  
- Systems include devices, networks, and infrastructure that handle this data.

## Security terminology

### Vulnerability

- Any weakness that can reduce confidentiality, integrity, or availability.  
- Exists in software, hardware, configuration, or procedures.  
- No system is free of vulnerabilities.

### Exploit

- Specific method, tool, or technique that takes advantage of a vulnerability.  
- Can be a script, malware, or manual procedure.

### Threat

- Potential for a vulnerability to be exploited.  
- Includes threat actors, such as attackers or insiders, with intent and capability.

### Mitigation

- Control or measure that reduces the likelihood or impact of a threat.  
- Examples: patches, ACLs, Port Security, firewalls, training, physical locks.

## Network threats

### Denial of Service (DoS) and DDoS

- DoS  
  - Attempt to make a system or service unavailable.  
  - Often targets bandwidth, CPU, or connection tables.  
  - Example: TCP SYN flood filling a server connection table with half open sessions.

- Distributed DoS (DDoS)  
  - DoS performed from many compromised devices (botnet).  
  - Harder to block due to many sources.

CIA impact: mainly availability.

### Spoofing

- Falsifying identity information, such as source IP or MAC address.  
- Used in many attacks, including SYN floods and some DoS variants.  
- Makes tracing the real attacker more difficult.

### DHCP exhaustion

- Also called DHCP starvation.  
- Large number of DHCP DISCOVER messages with spoofed MAC addresses.  
- Goal is to consume the DHCP pool and prevent legitimate clients from obtaining addresses.  
- Classified as both spoofing and DoS.

### Reflection and amplification

- Reflection  
  - Attacker sends requests that appear to originate from the victim.  
  - Third party servers (reflectors) send responses to the victim.

- Amplification  
  - Small requests trigger large responses.  
  - Common reflectors: NTP, DNS, other UDP based services.

Combined reflection and amplification attacks are powerful DDoS techniques.

### Man in the middle (MITM)

- Attacker intercepts and possibly alters traffic between two systems.  
- Example: ARP poisoning (ARP spoofing).  
  - Attacker sends fake ARP replies that map victim IP addresses to attacker MAC.  
  - Traffic flows through the attacker instead of directly between hosts.

CIA impact: confidentiality and potentially integrity.

### Reconnaissance

- Information gathering phase used to prepare future attacks.  
- Includes scanning, fingerprinting, and open source intelligence (OSINT).  
- OSINT uses public data such as DNS, WHOIS, social media, and company websites.

### Malware

- Malicious software that performs unwanted actions on a system.  
- Often relies on user actions such as opening attachments or running files.

Common types:

- Virus  
  - Attaches to legitimate files or programs and spreads when they execute.

- Worm  
  - Spreads automatically over networks by exploiting vulnerabilities.

- Trojan horse  
  - Appears legitimate but performs hidden malicious functions.

- Backdoor  
  - Provides unauthorized remote access to the system.

- Ransomware  
  - Encrypts files and demands payment for decryption.

### Password related attacks

- Usernames are often easy to determine.  
- Security usually depends on password strength and handling.

- Dictionary attack  
  - Tries common passwords from a list.

- Brute force attack  
  - Tries all possible character combinations.  
  - Becomes less practical as length and complexity increase.

## Social engineering

### Social engineering overview

- Targets human behavior rather than software or hardware.  
- Aims to trick individuals into revealing information or performing actions.  
- Frequently used to deliver malware or obtain credentials.

### Phishing and variants

- Phishing  
  - Deceptive messages that imitate trusted sources.  
  - Often contain malicious links or attachments.

- Spear phishing  
  - Targeted phishing aimed at specific organizations or individuals.

- Whaling  
  - Phishing aimed at high value targets such as executives.

- Smishing  
  - Phishing via SMS.

- Vishing  
  - Phishing via voice calls.

### Pretexting

- Social engineer creates a scenario (pretext) to justify a request.  
- Example: impersonating IT staff to obtain login details or direct a user to a fake site.

### Tailgating

- Also called piggybacking.  
- Attacker follows an authorized person into a secure area.  
- Exploits politeness or distraction.

### Human factors

- Social engineering exploits:  
  - Trust in authority.  
  - Desire to help others.  
  - Reciprocity (returning favors).  
  - Commitment and consistency.  
  - Sense of urgency.

Security programs treat social engineering as a major risk and rely on awareness and training to reduce it.

## Security program elements

### User awareness

- Keeps security concepts visible in day to day work.  
- May include simulated phishing campaigns and regular reminders.  
- Goal is to build habit of caution with links, attachments, and requests.

### User training

- More formal education on policies and procedures.  
- Covers topics such as acceptable use, incident reporting, and handling sensitive data.

### Physical access control

- Protects equipment and cabling.  
- Examples:
  - Locked rooms and racks.  
  - Badge readers with access lists.  
  - Cameras in sensitive areas.  
  - Stronger controls such as multi factor locks for data centers.

## Password security

### Password best practices

- Use sufficient length (for example, 15 or more characters).  
- Use a mix of upper and lower case letters, numbers, and symbols.  
- Use different passwords for different accounts.  
- Avoid common words and easily discovered personal details.

### Password change policy

- Frequent forced changes tend to produce weaker passwords and reuse.  
- Modern guidance favors strong unique passwords changed when:  
  - Breach is suspected.  
  - Malware or compromise is detected.  
  - Policy requires a change for specific events.

### Password managers

- Store and manage passwords securely.  
- Benefits:
  - Generate long, complex, unique passwords.  
  - Auto fill reduces exposure to keyloggers.  
  - Encrypted storage protects passwords at rest.

### Password storage and hashing

- Cleartext password storage is unacceptable.  
- Passwords should be stored as nonreversible hashes.  
- Hash functions produce fixed length outputs and are one way.

### Cisco IOS password storage

- `enable password` creates a type 0 (cleartext) password.  
- `service password-encryption` converts many passwords to weak type 7 encrypted form.  
- Stronger option:

  ```cisco
  enable secret <password>
  ```

- `enable secret` stores a hashed password:  
  - Type 5: MD5  
  - Type 8: SHA256  
  - Type 9: scrypt

- Command to choose a specific algorithm:

  ```cisco
  enable algorithm-type {md5 | sha256 | scrypt} secret <password>
  ```

- Equivalent options exist for `username` commands.

## Multifactor authentication

### Factors

- Knowledge (something known)  
  Passwords, PINs, security answers.

- Possession (something held)  
  Badges, hardware tokens, phones, authenticator apps.

- Inherence (something inherent)  
  Biometrics such as fingerprints or facial recognition.

### MFA definition

- True MFA uses factors from at least two different categories.  
- Example combinations:
  - Password plus code from an authenticator app.  
  - Badge plus fingerprint scan.

## Digital certificates

### Purpose

- Digital certificates provide identity verification for systems such as websites.  
- Used heavily with TLS and HTTPS.

### Certificate authorities

- Certificate Authority (CA) issues and signs certificates.  
- Browsers and devices trust a set of root CAs.  
- When visiting a site, the browser:
  - Checks the certificate.  
  - Verifies the CA that signed it.  
  - Confirms hostname and validity period.

- Valid certificates allow encrypted HTTPS sessions and protect against some impersonation attacks.

## AAA framework

### Components

- Authentication  
  Verifies identity.

- Authorization  
  Determines allowed actions.

- Accounting  
  Records activity.

### AAA servers

- Centralize control of user accounts and permissions.  
- Provide consistent policies across many devices.  
- Cisco solution: Identity Services Engine (ISE).

## RADIUS and TACACS+

### AAA protocols

- Both protocols carry AAA information between network devices and AAA servers.  
- Cisco devices support both.

### Main differences

- Operation:
  - RADIUS combines authentication and authorization.  
  - TACACS+ keeps authentication, authorization, and accounting separate.

- Transport:
  - RADIUS uses UDP (ports 1812 and 1813).  
  - TACACS+ uses TCP (port 49).

- Encryption:
  - RADIUS encrypts only the password field.  
  - TACACS+ encrypts the entire payload.

### Common use cases

- TACACS+  
  - Often used for device administration.  
  - Provides granular control of which commands are permitted.

- RADIUS  
  - Often used for network access control (VPN, Wi-Fi, 802.1X).  
  - Simpler and efficient where detailed command control is not required.

## 802.1X

### 802.1X overview

- IEEE 802.1X provides port based network access control.  
- Controls access to a LAN or WLAN before full network connectivity is granted.

### Roles

- Supplicant  
    Client device that requests access.

- Authenticator  
    Switch or wireless controller that controls the port.

- Authentication server  
    Typically a RADIUS server that verifies credentials.

### Operation

- When a device connects, the port allows only 802.1X traffic.  
- Supplicant provides credentials using Extensible Authentication Protocol (EAP).  
- Authenticator relays EAP information to the RADIUS server.  
- On success, the port transitions to a normal data state.  
- Used for both wired and wireless access control.

## Firewalls and next generation features

### Stateless and stateful filtering

- ACLs on routers act as stateless firewalls.  
- Each packet is evaluated independently with no awareness of previous packets.

- Stateful firewalls:
  - Track sessions and connection states.  
  - Allow return traffic for sessions initiated from trusted zones.  
  - Provide more context aware control.

### Firewall zones

- Firewalls define security zones (for example, inside, outside, DMZ).  
- Policies control traffic between zones.  
- DMZ commonly holds public facing servers that should not have full access to the internal network.

### Next generation firewalls (NGFW)

- Extend stateful inspection with additional features such as:
  - Application Visibility and Control (AVC)  
    Identifies traffic by application, not just port and protocol.

  - Advanced Malware Protection (AMP)  
    Integrates anti malware scanning.

  - Intrusion Prevention System (IPS)  
    Uses signatures and behavior analysis to detect and block attacks.

### Next generation IPS (NGIPS)

- Adds contextual awareness, threat intelligence feeds such as Talos, and application awareness.  
- Protects against threats such as DoS/DDoS, malware, reconnaissance, and injection attacks.

## Quick review

- CIA triad defines confidentiality, integrity, and availability as core security goals.  
- Vulnerabilities, exploits, threats, and mitigations describe how weaknesses are attacked and controlled.  
- Common network threats include DoS/DDoS, spoofing, DHCP exhaustion, reflection and amplification, MITM, reconnaissance, malware, and password attacks.  
- Social engineering uses psychological manipulation with techniques such as phishing, pretexting, and tailgating.  
- Security programs rely on user awareness, training, and physical access controls.  
- Strong password practices, secure hashing on Cisco IOS, and multifactor authentication significantly improve authentication security.  
- Digital certificates and CAs enable authenticated, encrypted connections with HTTPS.  
- AAA with RADIUS and TACACS+ centralizes authentication, authorization, and accounting.  
- 802.1X integrates with RADIUS to enforce port based network access control.  
- Firewalls, NGFW features, and IPS/NGIPS provide layered network protection beyond basic ACLs.
