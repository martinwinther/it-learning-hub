# Security Concepts

## Overview

The most secure network would be a closed system, like a house with no doors or windows. But just like a house with no doors or windows would be uninhabitable, a completely isolated network would be counterproductive. The entire purpose of a network is connectivity—the ability to share, communicate, and access resources both within and outside of its confines. In the real world, networks need to interact with other networks, applications, and users. But this interconnectivity introduces vulnerabilities from a variety of angles, so security concerns must always be at the forefront of any network design. The CCNA isn't a cybersecurity certification per se. However, just as networking is an essential skill for nearly any IT professional, the same can be said of security. A system is only as secure as its weakest link, and security is everyone's responsibility—including those in non-IT roles.

## CIA Triad

### Three Elements

The CIA triad describes the goals of information security:

- **Confidentiality**: Systems and data should only be accessible by authorized entities
- **Integrity**: Systems and data should be trustworthy. For example, data should not be altered during storage or transmission except by authorized entities
- **Availability**: Systems and data should be accessible and usable by authorized entities when required

### CIA Triad Purpose

- Basically, security program should ensure that systems and data can only be accessed by authorized users
- Can only be controlled or modified by authorized users
- Are available to authorized users when needed
- If all three of these elements are ensured, we can say that systems and data are "secure"
- As we cover various security concepts, always keep CIA triad in mind
- Consider how particular attack harms confidentiality, integrity, or availability of data
- Consider how particular security solution protects them
- Note that data refers to information that is stored, processed, or transmitted
- Systems refers to devices, networks, and infrastructure that facilitate storage, processing, and transmission of this data

## Security Terminology

### Vulnerability

- Vulnerability is any potential weakness that can compromise security (CIA) of system or data
- Using house as analogy, window is vulnerability that can potentially be used by intruder to enter house
- No system is perfectly secure
- Even closed system with no network connection to outside world has vulnerabilities that can be exploited
- Example: malicious user with physical access to devices is one potential threat

### Exploit

- Exploit is something that can potentially be used to take advantage of vulnerability
- Continuing with house analogy, rock that can be used to break window is exploit

### Threat

- Threat is real possibility of vulnerability to be exploited
- Intruder who intends to use rock to break window and enter your house is threat
- Depending on where you live and likelihood of threats, may choose to implement measure like installing metal bars over house's windows
- This is example of mitigation technique—measure implemented to protect against threats

### Mitigation Technique

- Mitigation technique is measure implemented to protect against threats
- Example: installing metal bars over windows to protect against intruders
- In computer networks, standard network protocols like DHCP contain vulnerabilities that can be exploited using various tools (computer programs)
- Malicious user who intends to use such tools to harm CIA of your network is threat
- Fortunately, there are mitigation techniques like DHCP Snooping that can be implemented to protect against such threats

## Network Threats

### Denial-of-Service (DoS) Attacks

- Denial-of-service (DoS) attack is malicious attempt to disrupt targeted system, service, or network and render it unusable
- Referring to CIA triad, DoS attacks affect target's availability
- Example: TCP SYN flood attack exploits TCP three-way handshake by flooding target with SYN messages
- After being flooded with SYN messages, target responds to each SYN message with SYN-ACK message
- Adds each connection to its TCP connection table
- However, final ACK message required to complete each TCP connection never comes
- Resulting in target's TCP connection table being full of "half-open" connections
- As result, legitimate users are unable to access target server
- Server has reached its maximum capacity and cannot accept any more connections

### Distributed Denial-of-Service (DDoS) Attacks

- Attack using single device is example of DoS attack
- Attack using group of devices infected with malware (called botnet) is distributed denial-of-service (DDoS) attack
- Botnet is group of devices infected with malware
- Used to attack target in distributed manner (instead of attacking from single device)

### Spoofing Attacks

- Spoofing attack is any attack that involves falsifying device's identity
- For example, by using fake source IP or MAC address
- Spoofing is used in variety of attacks
- Example: SYN flood attacks often involve spoofing
- Attacker can spoof their source IP address so that target's SYN-ACK replies are not sent back to attacker

### DHCP Exhaustion Attack

- Another example of attack that involves spoofing is DHCP exhaustion attack (also known as DHCP starvation)
- Attacker sends countless DHCP DISCOVER messages using spoofed MAC addresses
- To exhaust DHCP server's address pool
- Preventing legitimate clients from receiving IP addresses
- This is example of both spoofing attack and DoS attack

### Reflection Attacks

- In reflection attack, attacker sends spoofed requests (using IP address of target) to third-party servers
- Called reflectors in this context
- This triggers servers to send responses to target, overwhelming it
- Reflection attacks can be particularly effective when small request triggers large amounts of data to be sent in response
- This is called amplification attack
- Reflection/amplification attack is example of both DoS attack and spoofing attack
- NTP and DNS are two common protocols used for reflection/amplification attacks
- Because small requests can result in large responses

### Man-in-the-Middle (MITM) Attacks

- Man-in-the-middle (MITM) attack is attack in which attacker secretly intercepts communications between two parties
- Relaying messages between them
- Attacker gains access to contents of communications and can even alter them without communicating parties noticing
- One example is ARP poisoning (or ARP spoofing)
- In which attacker sends spoofed ARP replies to make communicating hosts send their frames to attacker instead of directly to each other
- Through legitimate ARP exchange, hosts learn each other's MAC addresses
- However, attacker sends malicious ARP replies to hosts
- Overwriting their legitimate ARP table entries with "poisoned" entries
- That map hosts' IP addresses to attacker's MAC address
- As result, attacker is able to intercept frames sent between hosts
- Instead of sending frames to each other's correct MAC address, hosts will send frames to attacker's MAC address
- Regarding CIA triad, this affects confidentiality of communications

### Reconnaissance Attacks

- Reconnaissance attack isn't attack in and of itself but is rather used to gather information about target
- That can be used for future attack
- Reconnaissance attacks don't necessarily use illicit techniques to gather information
- Common part of reconnaissance attacks is open-source intelligence (OSINT)
- Which involves collecting and analyzing information that is publicly available
- Example: WHOIS lookup can be used to learn email addresses, phone numbers, physical addresses, etc. of domain's owners

### Malware

- Malware stands for malicious software
- Refers to harmful programs that can "infect" target computer and then perform malicious actions
- Like encrypting files, enabling unauthorized access, stealing personal data, etc.
- Common element of most types of malware is that they rely on human intervention to spread
- Should always be careful about what email attachments you open and what websites you visit
- If you are unsure, it is always best to err on side of caution and not open it or visit it

### Types of Malware

- **Virus**: Type of malware that attaches itself to legitimate program or file. When program or file is executed, virus is also executed. Viruses can spread to other computers by infecting files that are shared between computers.
- **Worm**: Type of malware that can spread without human intervention. Worms often spread across networks by exploiting vulnerabilities in software.
- **Trojan horse**: Type of malware that disguises itself as legitimate software. Trojan horses are often spread through email attachments or malicious websites.
- **Backdoor**: Type of malware that allows unauthorized users to access infected computer. Backdoors are often installed by Trojan horses or other types of malware.
- **Ransomware**: Type of malware that encrypts files on infected computer and demands payment (often in cryptocurrency) to decrypt files. Ransomware is often spread through email attachments or malicious websites.

### Password-Related Attacks

- Most common form of user authentication is username/password combination
- Determining user's username is usually simple task for attacker
- It's often publicly displayed username or user's email address
- Therefore, we rely on strength of password to provide necessary security
- Attackers have few options to learn user's password

### Dictionary Attacks

- Dictionary attack uses program that runs through "dictionary"—list of common passwords
- To find target's password

### Brute-Force Attacks

- Brute-force attack uses program that tries every possible combination of letters, numbers, and special characters
- To find target's password
- To protect against these methods, it's essential to use sufficiently strong passwords
- Feasibility of brute-force attacks decreases with length and complexity of password

## Social Engineering

### Social Engineering Overview

- Social engineering is act of manipulating individuals into divulging confidential information or performing specific actions
- Typically bypassing traditional security measures
- Instead of exploiting software vulnerabilities, social engineering targets human element of security
- Which is often weakest link

### Phishing

- Phishing is perhaps most widespread form of social engineering
- Attackers send deceptive emails, pretending to be from trustworthy entity
- To trick recipients into clicking malicious links, downloading malware, or providing sensitive information
- Email's spam folder is likely full of such emails

### Types of Phishing

- **Spear phishing**: More targeted form of phishing, often aimed at employees of certain company
- **Whaling**: Phishing targeted at high-profile individuals, such as company CEO
- **Smishing** (SMS phishing): Phishing via SMS text messages
- **Vishing** (voice phishing): Phishing performed over phone

### Pretexting

- Pretexting is another type of social engineering attack
- In which attacker creates fabricated scenario in attempt to manipulate target
- Example: attacker might call employee and say "Hi, this is Jeremy from IT department. Due to company policy, we need to reset your password. Can you go to this URL, log in, and change your password?"
- This is also example of vishing

### Tailgating

- Tailgating (or piggybacking) is physical method
- In which attacker seeks entry into restricted area by following someone authorized to enter
- Attacker exploits target's courtesy or distraction
- People are likely to hold door for attacker, even if entering restricted area

### Social Engineering Psychology

- All of these attacks exploit various aspects of human social behavior
- People tend to comply with requests from figures of authority
- We also tend to comply with requests from people we like
- If someone does something for us, we naturally want to return favor
- Once committed to certain choice or action, people are more likely to follow through
- It's hard to back out
- Furthermore, many social engineering attacks also play on creating sense of urgency
- To make targets act without thinking
- Social engineering is often precursor or facilitator to technical threats
- Acting as "human exploit"
- Example: attacker might use phishing to deceive user into downloading malware
- User is vulnerability that attacker exploits with social engineering to enable malware threat

## Security Program Elements

### User Awareness

- To defend against social engineering, it's essential to raise awareness and provide training
- So individuals can recognize and respond appropriately to deceptive tactics
- CCNA exam topics list three essential elements of security program: user awareness, user training, and physical access control
- User awareness programs are not formal training
- But are designed to make employees aware of potential security threats and risks
- Example: company might send out false phishing emails to trick employees into clicking link and signing in with their login credentials
- Although emails themselves are harmless, employees who fall for false emails will be informed that it is part of user awareness program
- That they should be more cautious about phishing emails and other deceptive tactics
- Regular reminders like this keep security at forefront of employees' minds
- Which is crucial; security is everyone's responsibility

### User Training

- User training programs are more formal educational programs
- Usually mandatory for some or all employees (depending on topic)
- Examples are dedicated training sessions educating users on corporate security policies
- Or how to avoid potential threats (such as social engineering attacks)

### Physical Access Control

- Physical access control protects systems and data from potential threats
- By only allowing authorized users into areas such as network closets or data center floors
- Example: badge readers can be installed to only allow authorized users to open door
- Unlike traditional key, badges are flexible
- User permissions can easily be changed
- Example: permissions can be removed when employee leaves company
- However, for particularly sensitive areas, locks requiring multifactor authentication (such as badge scan and fingerprint scan) are preferred
- Security cameras—monitoring actions of employees and guests on premises—are another example of physical access control

## Password Security

### Password Best Practices

- Passwords—secret strings of characters—are essential tool for user authentication
- Only legitimate user(s) of account should know password
- When using password as means of user authentication, it's important that password is strong
- Meaning that it's resilient to password-related attacks
- Here are few best practices regarding passwords:
  - **Length**: Use at least 15 characters (although length recommendations vary)
  - **Complexity**: Include upper- and lowercase letters, numbers, and special symbols (#, @, !, ?, etc.)
  - **Unique**: Don't use same password for multiple accounts
  - **Hard to guess**: Don't use common words or personal information about you that is publicly available (that OSINT reconnaissance attack could reveal)

### Password Change Policy

- It is often recommended that users be required to change their passwords regularly
- However, there is growing trend against this for few reasons
- First, there is no particular benefit to changing password that hasn't been compromised (if current password is already strong)
- Second, requiring users to regularly change passwords tends to lead to weaker passwords
- Users will often reuse passwords from other accounts
- Instead, it's recommended to change passwords only in certain circumstances
- Such as after data breach (in which case password may have been compromised)
- Or if you discover malware on your device

### Password Managers

- Password manager is software tool that users can use to store and manage passwords
- One popular example is Bitwarden, but most modern web browsers have their own built-in password managers too
- These days, using password manager is generally considered best practice for variety of reasons:
  - **Length and complexity**: Users can generate and store long, complex, and unique passwords for each account, without having to remember each password
  - **Auto-fill**: Password manager can automatically fill in usernames/passwords without requiring any keystrokes from user. This can prevent passwords from being learned by keylogger malware that reads and logs keystrokes
  - **Encrypted storage**: Password managers encrypt stored passwords, so even if device is compromised, passwords in manager are protected

### Password Storage

- It's crucial that password remains secret
- If it loses its secrecy, it no longer serves as valid means of authenticating user's identity
- To that end, it's crucial to protect passwords "at rest"
- Do not store passwords as cleartext (unencrypted text)
- Instead, passwords should be stored as hashes
- Hash function converts input (password, in this case) into fixed-length string—hash—that cannot be reverted to original input
- Hash functions are one-way (irreversible)

### Cisco IOS Password Storage

- For review, can use `enable password password` to configure enable password that is stored in cleartext
- Cisco calls this type 0 password—not acceptable from security standpoint
- Can use `service password-encryption` command to make device encrypt enable password (and other passwords) with weak form of reversible encryption
- Cisco calls this type 7 password
- Type 7 passwords are also unacceptable, as they can easily be decrypted with free online tools
- Instead of `enable password`, should always use `enable secret` command
- Which stores configured password as secure hash using one of multiple supported hashing algorithms
- Algorithms supported depend on device model and IOS version
- If simply configure `enable secret password`, without specifying hash algorithm, device will use its default hash algorithm
- Which for many years was MD5 (type 5) but is now scrypt (type 9) in modern devices

### Cisco IOS Password Hashing Algorithms

- To configure enable secret and hash it with particular algorithm, use `enable algorithm-type algorithm secret password` command
- Options that can be used for algorithm argument:
  - `md5` (type 5)
  - `sha256` (type 8)
  - `scrypt` (type 9)
- US National Security Agency (NSA) has released set of recommendations regarding Cisco IOS passwords and how to configure them
- NSA recommends type 8, but type 9 (Cisco's recommendation) is also considered very strong
- Enable secret will be saved in running-config file as `enable secret type hash`
- With algorithm type being indicated by its number
- If you want to configure same enable secret on another device, can simply copy and paste command as it appears in running-config
- `enable secret type hash` command allows you to configure already-hashed enable secret without having to retype cleartext password
- Equivalent commands for configuring user account are `username username algorithm-type algorithm secret password` to create user account and hash its password with specified algorithm
- And `username username secret type hash` to create user account with already-hashed password

## Multifactor Authentication

### MFA Overview

- No matter how strong password is, it remains potential vulnerability
- If malicious actor learns account's password, they can access account
- Instead of simple username/password authentication, multifactor authentication is becoming increasingly prevalent as more secure option
- Multifactor authentication (MFA) is process of verifying user's identity by requiring multiple forms of authentication before granting access
- Usually two, in which case it can also be called two-factor authentication (2FA)
- Goal is to enhance security by ensuring that even if one authentication factor is compromised (i.e., attacker learns your password), unauthorized access is still prevented by need for additional factors

### Authentication Factors

The "factors" of MFA are usually categorized into three main types:

- **Knowledge** (Something you know):
  - Passwords or PINs
  - Security questions and answers
- **Possession** (Something you have):
  - ID badge
  - Smartphone receiving SMS codes or push notifications
  - App like Google Authenticator that generates one-time codes. To obtain code, you need access to specific device where app is installed
- **Inherence** (Something you are):
  - Biometrics such as facial, palm, fingerprint, or retinal scan

### True MFA

- To truly be considered MFA, factors from different categories must be used
- Requiring password and PIN is not considered true MFA because both are something you know
- Example of true MFA is requiring user to touch their badge to badge reader (something you have) and scan their fingerprint (something you are) to enter restricted area
- Another example is logging in with username/password and receiving SMS code on your phone
- Username/password combination is something you know
- SMS code, although password-like code, is dependent on something you have—your smartphone

## Digital Certificates

### Digital Certificate Overview

- Digital certificates are key form of authentication
- Predominantly used by websites
- Most modern websites use digital certificates to prove their identity
- To prove that website you are visiting is who it says it is and not fake website designed to imitate legitimate website

### Certificate Authority

- When you connect to website, your browser will check site's digital certificate
- Verifying its authenticity with trusted Certificate Authority (CA)
- Organization that issues and verifies digital certificates
- Can think of CAs as "passport offices" for digital certificates
- If everything checks out, your connection proceeds securely using HyperText Transfer Protocol Secure (HTTPS)
- Encrypted and secure version of HTTP
- If not, you'll typically receive warning alerting you to potential risks
- In Google Chrome, website with valid digital certificate will display padlock next to URL
- Digital certificates are essential part of modern internet
- They help to ensure that users are able to connect to websites securely
- That they are not being redirected to fake websites
- Also play essential role in enabling secure, encrypted communications via HTTPS

## Authentication, Authorization, and Accounting (AAA)

### AAA Overview

- Authentication, authorization, and accounting (AAA, pronounced "triple-A") is framework for controlling user access in network
- AAA divides user access control into three components:
  - Verifying users' identities (authentication)
  - Granting appropriate access (authorization)
  - Recording user activities (accounting)

### Authentication

- Authentication is process of verifying identity of user or system
- Answers question "Who are you?"
- Ideally, this is performed using MFA

### Authorization

- Once authenticated, next step is to grant user or device appropriate access
- Authorization answers question "What are you allowed to do?"
- This could include which files user is allowed to read or modify
- Which services user can access
- Which Cisco IOS commands they can use, etc.

### Accounting

- Accounting is process of keeping track of user activities
- Accounting answers question "What did you do?"
- Every action user takes can be logged
- From opening or editing file to making configuration changes to device
- This is crucial for audits, troubleshooting, and understanding user behavior

### AAA Server

- Implementing AAA in network involves centralized AAA server
- That controls user authentication, authorization, and accounting
- From this server, can control user accounts and credentials
- What each user is authorized to do
- Keep account of each user's activities
- Cisco's AAA server solution is called Identity Services Engine (ISE)

## RADIUS and TACACS+

### AAA Protocols

- AAA is typically implemented using one of two protocols:
  - Remote Authentication Dial-In User Service (RADIUS)
  - Terminal Access Controller Access-Control System Plus (TACACS+)
- Cisco network devices (and ISE) support both protocols
- RADIUS and TACACS+ both serve purpose of providing AAA functionality to control user access
- But there are differences between them
- Both protocols are open standards that have been implemented by various vendors
- Although TACACS+ was originally developed by Cisco

### RADIUS vs TACACS+ Differences

- One major difference is that whereas TACACS+ keeps all three AAA components separate, RADIUS combines authentication and authorization into single operation (called Access Request)
- Because TACACS+ keeps all three components as separate operations, it often provides more granular control
- RADIUS and TACACS+ also differ in Layer 4 protocols they use
- RADIUS uses UDP, and RADIUS server listens on ports 1812 (for authentication/authorization) and 1813 (for accounting)
- TACACS+, on other hand, uses TCP as its Layer 4 protocol
- TACACS+ server listens on TCP port 49 for all messages
- Whereas TACACS+ encrypts contents of all messages between client and server, RADIUS only encrypts password in Access Request message
- Rest of Access Request message's content, and contents of other RADIUS messages, are sent in cleartext

### RADIUS vs TACACS+ Use Cases

- Although more robust features of TACACS+ may make it seem superior choice for AAA protocol, both are used in different scenarios
- TACACS+ is typically used to control device administration
- Such as admin configuring router or switch
- TACACS+ provides granular control over which commands user can use
- This can be configured on per-user or per-group basis (with users assigned to different groups)
- RADIUS, on other hand, is typically used to control network access
- This is largely due to simplicity and efficiency of RADIUS compared to TACACS+
- Especially when such granular control is not necessary

## 802.1X

### 802.1X Overview

- 802.1X (usually pronounced "dot one X") is standard created by IEEE for port-based network access control (PNAC)
- Basically, it's way to secure each port on switch
- Allowing only authorized devices to connect to network
- Without 802.1X, device connected to switch port can immediately send DHCP request, lease IP address, and begin communicating over network
- 802.1X changes that

### 802.1X Operation

- When device first connects to port secured by 802.1X, port remains locked until user successfully authenticates
- Only traffic that is allowed is 802.1X authentication traffic
- 802.1X defines three components:
  - **Supplicant**: Client device that wants to connect to network
  - **Authenticator**: Network device that supplicant connects to
  - **Authentication server**: Server that verifies supplicant's credentials (usually RADIUS server)

### Extensible Authentication Protocol (EAP)

- 802.1X uses framework called Extensible Authentication Protocol (EAP) for authentication process
- Which defines various authentication methods and message formats
- However, RADIUS is usually employed as protocol for checking credentials provided by supplicant
- 802.1X, paired with RADIUS, is used for both wired and wireless access control

## Firewalls

### Firewall Overview

- CCNA exam focuses primarily on configuring Cisco routers and switches
- However, type of network device most synonymous with network security is firewall
- Although firewall configuration is beyond scope of CCNA exam, you are expected to have basic understanding of how firewalls work
- Routers and switches both have various security features
- Example: routers can use ACLs to control which types of traffic are permitted and denied
- In fact, ACLs applied to router's interfaces are form of stateless firewall
- They examine each packet on per-packet basis and decide to permit or deny it
- Without considering other context, such as packet's relation to other packets (i.e., whether this packet is reply to previously permitted packet)

### Stateful Firewalls

- Most modern firewalls are stateful firewalls
- They don't just consider individual packets with no other context
- But also each packet's relationship to other packets
- Example: stateful firewall might block all internet traffic from entering internal network
- Generally good idea, given public nature of internet
- However, if host in internal network initiates communication with host on internet (i.e., google.com's web server), firewall will allow reply traffic from internet host
- Stateless firewalls (like ACLs on router) are not able to consider context of packets like this
- Each packet is considered independently

### Firewall Zones

- Firewalls consider how packets move between zones when determining whether to permit or deny them
- If host in Inside zone initiates communication with host in Outside zone, firewall will permit reply traffic
- However, if host in Outside zone attempts to initiate communication with host in Inside zone, firewall will block it
- Figure shows two zones, but firewalls can have many different zones
- With different policies controlling communication between hosts in each zone
- Example: it's common to have zone called demilitarized zone (DMZ)
- Servers that need to be reachable from public internet are placed here
- So that they can be accessed without compromising security of hosts in Inside zone
- Most firewalls have their own routing capabilities
- Depending on size and requirements of network, firewall's routing capabilities may be sufficient
- Or you may need separate router

## Next-Generation Firewalls

### NGFW Overview

- Next-generation firewall (NGFW) is bit of marketing lingo that has become standard terminology for type of firewall
- That goes beyond functionalities of traditional firewalls
- While core remains stateful packet filtering, NGFW incorporates several advanced security features

### Application Visibility and Control (AVC)

- One of those advanced features is Application Visibility and Control (AVC)
- AVC means that firewall can not only identify traffic based on information like source and destination addresses and ports
- But can also examine actual contents of packets to identify application
- Similar to NBAR, as we covered in chapter 10

### Advanced Malware Protection (AMP)

- Cisco NGFWs can also integrate with their anti-malware offering, Advanced Malware Protection (AMP)
- This allows firewall to inspect files to identify and protect against all types of malware
- Such as those we covered in section on malware

### Intrusion Prevention System (IPS)

- Another common feature of NGFW is Intrusion Prevention System (IPS) functionality
- Historically, IPS was separate hardware device
- However, in modern networks, IPS feature is typically integrated within NGFW
- This integration simplifies and streamlines implementation and management of IPS

### IPS Functionality

- IPS inspects network traffic for malicious or suspicious activities
- Once detected, IPS takes predefined actions, such as blocking traffic
- Instead of operating based on user-configured rules, IPS downloads attack "signatures"
- Identifiable patterns of data that can be used to detect malicious activity
- From vendor (i.e., Cisco)
- IPS is also capable of building picture of typical network activity
- Looking for anomalies that don't match up with that baseline
- Following are some threats that IPS can protect against:
  - DoS and DDoS
  - Malware such as viruses, worms, Trojan horses, and ransomware
  - Reconnaissance attacks
  - SQL injections

### Next-Generation IPS (NGIPS)

- Next-Generation IPS (NGIPS) includes additional features:
  - **Contextual awareness**: NGIPS gathers contextual information about applications, device types, operating systems, users, etc. NGIPS uses these details to better understand actual activity on network
  - **Talos integration**: Talos is security research company that's part of Cisco. Threat intelligence gathered by Talos includes attack signatures and known bad actors (known malicious IP addresses, websites, etc.)
  - **Application Visibility and Control (AVC)**: Like Cisco's NGFW, NGIPS can also examine contents of packets to identify application

### NGFW Summary

- Listing various features of Cisco's security products can sound like marketing pitch
- You don't have to be able to list all of these features for CCNA exam
- Just understand that NGFW includes additional features like IPS and anti-malware functionality on top of stateful packet filtering

## Real-World Applications

- **Network security**: Implementing security measures to protect network infrastructure
- **Access control**: Controlling who can access network resources
- **Threat mitigation**: Protecting against various types of attacks
- **Compliance**: Meeting security requirements and regulations
- **Incident response**: Detecting and responding to security incidents
- **Security awareness**: Educating users about security threats

## Troubleshooting

### Common Issues

- **Unauthorized access**: Verify authentication and authorization are configured correctly
- **Password issues**: Check password complexity and storage methods
- **AAA failures**: Verify RADIUS/TACACS+ server connectivity and configuration
- **Firewall blocking legitimate traffic**: Check firewall rules and zones

### Troubleshooting Steps

1. Verify authentication: Check user credentials and MFA configuration
2. Check authorization: Verify user has appropriate permissions
3. Review accounting logs: Check for unauthorized access attempts
4. Test firewall rules: Verify traffic is being permitted/denied correctly
5. Check security policies: Ensure policies are properly configured

## Best Practices

- Implement defense in depth with multiple layers of security
- Use strong passwords and password managers
- Enable MFA wherever possible
- Regularly update and patch systems
- Monitor and log security events
- Provide security awareness training to users
- Implement physical access controls
- Use firewalls to segment network
- Keep security policies up to date
- Regularly review and audit security configurations

## Summary

- CIA triad describes goals of information security: confidentiality (prevent unauthorized access), integrity (prevent unauthorized alteration), and availability (ensure resources are accessible by authorized entities when required)
- Attacks target one or more components of CIA triad
- Vulnerability is any potential weakness that can compromise CIA of system or data
- Exploit is something that can potentially be used to take advantage of vulnerability
- Threat is real possibility of vulnerability to be exploited, such as attacker who wants to exploit vulnerability
- Mitigation technique is measure implemented to protect against threats
- Denial-of-service (DoS) attack is malicious attempt to disrupt targeted system, service, or network and render it unusable
- Distributed denial-of-service (DDoS) attack is DoS attack performed from group of devices infected with malware, called botnet
- Spoofing attack is any attack that involves falsifying device's identity, such as by using fake source IP or MAC address
- DHCP exhaustion (or DHCP starvation) attack involves attacker sending countless DHCP DISCOVER messages to exhaust DHCP server's address pool
- In reflection attack, attacker sends spoofed requests (using IP address of target) to third-party servers (called reflectors), triggering servers to send responses to target
- Reflection attacks can be particularly effective when small requests trigger asymmetrically large responses (amplification attack)
- Man-in-the-middle (MITM) attack is attack in which attacker secretly intercepts communications between two parties
- ARP poisoning (or ARP spoofing), in which attacker sends spoofed ARP replies, is example of MITM attack
- Reconnaissance attack is used to gather information about target that can be used for future attack
- Reconnaissance attacks often employ open-source intelligence (OSINT), which involves gathering publicly available information
- Malware (malicious software) refers to harmful programs that can infect target computer and perform malicious actions
- Common types of malware include viruses, worms, Trojan horses, backdoors, and ransomware
- Dictionary attack uses program that runs through list of common passwords
- Brute-force attack tries every possible combination of letters, numbers, and special characters
- Social engineering is act of manipulating individuals into divulging confidential information or performing specific actions
- Common social engineering attacks include phishing, spear phishing, whaling, smishing, vishing, pretexting, and tailgating/piggybacking
- To defend against social engineering attacks, it's essential to raise awareness and provide training
- User awareness programs are not formal training but are designed to make employees aware of potential security threats
- User training programs are more formal educational programs that educate users on corporate security policies
- Physical access control protects systems and data by only allowing authorized users into restricted areas
- Passwords should be of sufficient length (15+ characters) and complexity (upper- and lowercase letters, numbers, and symbols), and be unique and hard to guess
- Password manager is software that stores and manages passwords, allowing users to store strong passwords without having to remember each one
- Cisco IOS passwords should be stored as secure hashes using `enable algorithm-type algorithm secret password` command
- Type 5 (md5) was default hash algorithm for many years, but modern Cisco devices use type 9 (scrypt). NSA recommends type 8 (sha256)
- Multifactor authentication (MFA), or two-factor authentication (2FA), is process of authenticating user with multiple forms (factors) of authentication
- There are three main categories of factors: knowledge (something you know), possession (something you have), and inherence (something you are)
- MFA must use factors from different categories
- Digital certificate is form of authentication predominantly used by websites, issued and verified by Certificate Authority (CA)
- AAA is framework for controlling user access in network, dividing access control into authentication (verifying users' identities), authorization (granting appropriate access), and accounting (recording user activities)
- Cisco's AAA server solution is Identity Services Engine (ISE)
- RADIUS and TACACS+ are main AAA protocols
- RADIUS combines authentication and authorization into single operation (Access Request), but TACACS+ keeps all three separate
- RADIUS uses UDP ports 1812 and 1813, and TACACS+ uses TCP port 49
- RADIUS encrypts only passwords, but TACACS+ encrypts entire contents of all messages
- RADIUS is typically used for network access, and TACACS+ is typically used for device administration
- 802.1X is standard for port-based network access control (PNAC), requiring devices to authenticate before accessing network
- 802.1X defines three components: supplicant (client device), authenticator (network device), and authentication server (RADIUS server)
- 802.1X uses Extensible Authentication Protocol (EAP) framework, with RADIUS usually employed for checking credentials
- ACLs applied to router's interfaces are form of stateless firewall, examining each packet independently
- Modern firewalls are stateful firewalls, considering packet's relationship to other packets
- Firewalls use concept of zones to differentiate between areas of network, such as Inside, Outside, and DMZ
- Next-generation firewall (NGFW) incorporates several advanced security features beyond stateful packet filtering
- Features include Application Visibility and Control (AVC), Advanced Malware Protection (AMP), and Intrusion Prevention System (IPS)
- IPS inspects network traffic for malicious activities using attack signatures downloaded from vendor
- IPS can protect against DoS/DDoS attacks, malware, reconnaissance attacks, SQL injections, and more

