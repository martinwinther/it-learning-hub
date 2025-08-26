# Computer Networking Fundamentals

## Overview

Computer networking enables devices to communicate and share resources across
various network types. Understanding networking fundamentals is essential for
cybersecurity professionals to secure network communications and protect against
network-based threats.

## Network Types

### Local Area Network (LAN)

- **Definition**: Connects devices in the same building or campus
- **Characteristics**: High-speed, limited geographic scope
- **Use Cases**: Office networks, home networks, campus networks
- **Security**: Controlled environment, easier to secure

### Wide Area Network (WAN)

- **Definition**: Connect offices in different locations and the internet
- **Characteristics**: Large geographic scope, slower speeds
- **Use Cases**: Corporate networks, internet connectivity
- **Security**: More complex security requirements

### Wireless Networks

- **Wi-Fi**: Creates wireless LAN connections
- **PAN (Personal Area Network)**: Bluetooth networks for personal devices
- **NFC**: Short-range wireless connections for contactless communication

## TCP/IP Protocol Suite

### TCP/IP Overview

Modern networking uses a suite of protocols called TCP/IP. This suite uses the
Internet Protocol (IP) for routing information over networks at the Network
layer. Each communication also uses a Transport layer protocol, which is commonly
the Transmission Control Protocol (TCP) or the User Datagram Protocol (UDP).

### Internet Protocol (IP)

- **Purpose**: Assigns each computer on the network its own IP address
- **Function**: Breaks down data into packets of a few kilobytes
- **Benefits**: Makes the network more reliable (like small cars moving freely vs.
  huge trucks blocking the road)
- **Layer**: Network layer of the OSI model

### Transmission Control Protocol (TCP)

- **Purpose**: Sets up and tears down connections between source and destination
- **Functions**:
  - Tracks packets and controls transmission rate
  - Requests new packets if they get lost
  - Confirms delivery
- **Characteristics**: Reliable, connection-oriented
- **Use Cases**: Web browsing, email, file transfers

### User Datagram Protocol (UDP)

- **Purpose**: Alternative to TCP, less reliable but faster
- **Characteristics**: Used when speed is more important than ensuring every
  packet reaches destination
- **Use Cases**: Streaming video, online gaming, voice over IP
- **Trade-offs**: Speed vs. reliability

### Internet Control Message Protocol (ICMP)

- **Purpose**: Allows devices to communicate about network operation
- **Functions**:
  - Detects if systems are alive
  - Finds path between two systems
  - Identifies network issues
- **Part of**: TCP/IP suite

## OSI Model (Open Systems Interconnection)

### OSI Model Overview

The Open Systems Interconnection (OSI) model describes network communications
using seven layers. They are, in order, the Physical layer, Data-Link layer,
Network layer, Transport layer, Session layer, Presentation layer, and
Application layer.

### The Seven Layers

#### 1. Physical Layer

- **Function**: Sends bits using wires, radio waves, fiber optics
- **Components**: Cables, connectors, network interface cards
- **Protocols**: Ethernet, Wi-Fi, Bluetooth
- **Security**: Physical access control, cable security

#### 2. Data-Link Layer

- **Function**: Transfers data between two nodes on the same physical network
- **Components**: Switches, network interface cards
- **Protocols**: Ethernet, Wi-Fi, PPP
- **Security**: MAC address filtering, VLANs

#### 3. Network Layer

- **Function**: Expands network to different nodes
- **Components**: Routers, layer 3 switches
- **Protocols**: Internet Protocol (IP), ICMP, ARP
- **Security**: Firewalls, IP filtering, routing security

#### 4. Transport Layer

- **Function**: Connects between systems and transfers data
- **Protocols**: TCP and UDP are transport layer protocols
- **Components**: Transport layer protocols
- **Security**: Port filtering, connection monitoring

#### 5. Session Layer

- **Function**: Manages the exchange of communications between systems
- **Protocols**: NetBIOS, RPC, SQL
- **Components**: Session management software
- **Security**: Session hijacking protection, timeout controls

#### 6. Presentation Layer

- **Function**: Translates data so it can be transmitted
- **Responsibilities**:
  - Determines how to represent a character in terms of bits
  - Encrypts/decrypts data
- **Protocols**: SSL/TLS, JPEG, MPEG
- **Security**: Encryption, data format validation

#### 7. Application Layer

- **Function**: Determines how the user interacts with the data
- **Protocols**: HTTP, SMTP, SSH, FTP
- **Components**: Applications, web browsers, email clients
- **Security**: Application-level security, input validation

### OSI Model Summary Table

| LAYER | PROTOCOLS | FUNCTION |
|-------|-----------|----------|
| APPLICATION LAYER | HTTP, SMTP, SSH, ETC. | User interaction with data |
| PRESENTATION LAYER | DATA TRANSLATION AND ENCRYPTION | Data format and encryption |
| SESSION LAYER | EXCHANGES BETWEEN SYSTEMS | Session management |
| TRANSPORT LAYER | TCP AND UDP | End-to-end communication |
| NETWORK LAYER | INTERNET PROTOCOL (IP) | Routing and addressing |
| DATA LINK LAYER | DATA TRANSFER BETWEEN TWO NODES | Local network communication |
| PHYSICAL LAYER | WIRES, RADIOS, AND OPTICS | Physical transmission |

## IP Addressing

### IPv4 Addressing

A system's IP address uniquely identifies it on a network. IPv4 addresses use the
dotted quad notation of four integers ranging from 0 to 255 separated by periods.

#### IPv4 Format

- **Example**: 10.15.100.240
- **Format**: Four octets separated by periods
- **Range**: Each octet ranges from 0 to 255
- **Total Addresses**: Approximately 4.3 billion addresses

#### IPv4 Address Assignment

- **Static Assignment**: You assign an IP address manually and are responsible
  for ensuring uniqueness
- **Dynamic Assignment**: Using DHCP (Dynamic Host Configuration Protocol) which
  assigns IP addresses automatically from a pool
- **APIPA**: If DHCP fails, systems assign themselves an address using Automatic
  Private IP Addressing (APIPA), always starting with 169.254

#### Identifying Valid IPv4 Addresses

To identify a valid IP address, use the process of elimination:

**Invalid Conditions**:

- **Octet Size**: No octet should be larger than 255
- **Loopback**: IP addresses starting with 127 are reserved for loopback
  (except 127.0.0.1)
- **First Octet**: Should not be higher than 223
  - 224-239: Multicast addresses
  - 240-255: Experimental addresses

### IPv6 Addressing

IPv6 addresses use eight groups of four hexadecimal digits separated by colons.

#### IPv6 Format

- **Example**: fae0:2660:a0a1:2efe:c84b:4c44:3467:a1ed
- **Format**: Eight groups of four hexadecimal digits
- **Separator**: Colons between groups
- **Total Addresses**: 340 undecillion addresses

#### IPv6 Benefits

- **Larger Address Space**: Vastly more addresses available
- **Better Security**: Built-in security features
- **Improved Performance**: More efficient routing
- **Auto-configuration**: Automatic address assignment

### Address Uniqueness

- **Global Uniqueness**: IP addresses cannot be used on any other system in the
  world if they are connected to the internet
- **Communication Requirements**: Source and destination addresses are involved
  in every network communication

## Domain Name System (DNS)

### DNS Purpose

DNS server translates a URL to an IP address.

### DNS Resolution Process

1. **Local Cache**: Check local DNS cache first
2. **DNS Server**: Query configured DNS server
3. **Recursive Resolution**: If the DNS server doesn't know the address, it asks
   other DNS servers
4. **Response**: Return IP address to requesting system

### DNS Security

- **DNS Spoofing**: Attackers redirect DNS queries to malicious servers
- **DNSSEC**: DNS Security Extensions provide authentication
- **DNS Filtering**: Block access to malicious domains

## Network Ports and Applications

### Port Overview

Network ports are particular logical locations on a system associated with
specific applications. Port numbers range from 0 to 65,535.

### Port Ranges

#### Well-Known Ports (0-1023)

- **Definition**: Reserved for common applications, assigned by Internet
  authorities
- **Examples**:
  - Port 80: Web servers (HTTP)
  - Port 443: Secure web servers (HTTPS)
  - Port 22: SSH
  - Port 25: SMTP (unencrypted)
  - Port 587: SMTP (encrypted)

#### Registered Ports (1024-49151)

- **Definition**: Vendors can register these ports
- **Examples**:
  - Port 1433: Microsoft SQL Server
  - Port 1521: Oracle Database
  - Port 3389: Remote Desktop Protocol (RDP)

#### Dynamic Ports (49152-65535)

- **Definition**: Applications can use these temporarily
- **Use**: Ephemeral ports for client connections

### Important Ports to Memorize

- **53**: DNS
- **20/21**: FTP
- **80**: HTTP
- **443**: HTTPS
- **1433**: Microsoft SQL
- **1521**: Oracle Database
- **3389**: RDP
- **25**: SMTP (unencrypted)
- **587**: SMTP (encrypted)
- **22**: SSH

## Securing Wi-Fi Networks

### Wi-Fi Security Overview

Wi-Fi networks use a variety of authentication technologies, including preshared
keys, enterprise authentication, and captive portals. In addition, Wi-Fi networks
should use either WPA2 or WPA3 encryption to provide secure communications.

### Basic Security Measures

#### Disable SSID Broadcasting

- **Purpose**: Service Set Identifier is the name you see when choosing a network
- **Security Benefit**: Hiding it can increase security as users can't see the
  network
- **Limitation**: Not a strong security measure alone

#### Change Default Passwords

- **Issue**: Most wireless access points come with default passwords
- **Solution**: Change default passwords immediately
- **Best Practice**: Use strong, unique passwords

### Wi-Fi Authentication Methods

#### Preshared Keys (PSK)

- **Process**: Whenever the user wants to connect, they use the key
- **Big Limitations**:
  - Changing the key is a big burden
  - Keys are shared, making user identification difficult
- **Use Cases**: Home networks, small offices

#### Enterprise Authentication

- **Process**: The organization runs an authentication server that verifies
  credentials
- **Method**: Using username and passwords
- **Benefits**: Individual user accounts, centralized management
- **Use Cases**: Corporate networks, educational institutions

#### Captive Portals

- **Process**: Provides authentication on an unencrypted network using a portal
- **Examples**: Hotel or airport Wi-Fi
- **Security**: Limited security, primarily for access control

### Wireless Encryption Standards

#### Wired Equivalent Privacy (WEP)

- **Status**: Known to suffer from security vulnerabilities
- **Current Use**: No longer used in modern networks
- **Security Level**: INSECURE

#### Wi-Fi Protected Access (WPA)

- **Technology**: Used Temporal Key Integrity Protocol (TKIP)
- **Process**: Changes the encryption key for each packet
- **Status**: New vulnerabilities have been found, no longer secure
- **Security Level**: INSECURE

#### WPA2

- **Technology**: Uses CCMP based on AES
- **Status**: Considered secure but has potential issues
- **Security Level**: SECURE

#### WPA3

- **Requirement**: Required on new devices
- **Technology**: Uses CCMP but adds Simultaneous Authentication of Equals (SAE)
- **Benefit**: More secure initial setup of encrypted wireless communications
- **Security Level**: SECURE

### Wi-Fi Security Status Table

| STANDARD | SECURITY STATUS |
|----------|----------------|
| OPEN NETWORK | INSECURE |
| WEP | INSECURE |
| WPA | INSECURE |
| WPA2 | SECURE |
| WPA3 | SECURE |

## Network Security Considerations

### Network Segmentation

- **VLANs**: Virtual Local Area Networks for logical separation
- **Subnetting**: Divide networks into smaller, manageable segments
- **Firewalls**: Control traffic between network segments

### Network Monitoring

- **Intrusion Detection**: Monitor for suspicious network activity
- **Traffic Analysis**: Analyze network traffic patterns
- **Log Management**: Collect and analyze network logs

### Network Access Control

- **NAC**: Network Access Control systems
- **802.1X**: Port-based network access control
- **Guest Networks**: Separate networks for visitors

## Real-World Applications

### Enterprise Networks

- **Corporate Security**: Comprehensive network security measures
- **Remote Access**: Secure VPN connections for remote workers
- **Guest Access**: Controlled guest network access
- **Monitoring**: Continuous network monitoring and alerting

### Home Networks

- **Basic Security**: WPA2/WPA3 encryption, strong passwords
- **Guest Networks**: Separate network for visitors
- **Device Management**: Control which devices can connect
- **Parental Controls**: Content filtering and access controls

### Public Wi-Fi

- **Security Risks**: Open networks are inherently insecure
- **VPN Usage**: Use VPNs on public networks
- **Sensitive Data**: Avoid transmitting sensitive data on public networks
- **Awareness**: Be aware of network security status

## Best Practices

### For Network Administrators

- **Regular Updates**: Keep network equipment and firmware updated
- **Security Audits**: Regular security assessments
- **Access Control**: Implement strong access controls
- **Monitoring**: Continuous network monitoring
- **Documentation**: Maintain network documentation

### For End Users

- **Strong Passwords**: Use strong, unique passwords
- **VPN Usage**: Use VPNs on untrusted networks
- **Software Updates**: Keep devices and software updated
- **Awareness**: Be aware of network security risks
- **Sensitive Data**: Protect sensitive data transmission

## Summary

Effective computer networking requires:

- **Understanding Protocols**: Knowledge of TCP/IP and OSI model
- **Proper Addressing**: Correct IP address configuration and management
- **Port Management**: Understanding network ports and applications
- **Wi-Fi Security**: Implementing appropriate Wi-Fi security measures
- **Network Monitoring**: Continuous monitoring and security assessment

Key success factors:

- **Security First**: Implement security measures from the start
- **Regular Updates**: Keep systems and protocols current
- **Monitoring**: Continuous network monitoring and alerting
- **Training**: Educate users on network security
- **Documentation**: Maintain comprehensive network documentation

Understanding computer networking fundamentals is essential for cybersecurity
professionals and helps organizations build secure, reliable network
infrastructure.
