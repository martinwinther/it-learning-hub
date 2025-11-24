# Wireless LAN Architectures

## Overview

Wireless LANs use 802.11 to send frames over a shared RF medium. Access points (APs) provide the bridge between wireless clients and the wired LAN. This chapter focuses on 802.11 frame basics, client association, and how APs are deployed and managed in different architectures.

## 802.11 frame format

### Frame structure

- 802.11 encapsulates Layer 3 packets into frames for transmission over the air.
- Wireless operation differs from Ethernet over cable, so 802.11 defines its own frame format.
- Depending on standard and message type, some fields may be absent.
- Up to four address fields can appear in a single 802.11 frame.

### Address fields

802.11 frames can contain any combination of these addresses:

- Basic service set identifier (BSSID)  
  MAC address of the AP that represents the BSS.

- Destination address (DA)  
  Final recipient of the frame.

- Source address (SA)  
  Original sender of the frame.

- Receiver address (RA)  
  Immediate recipient of the frame on this hop.

- Transmitter address (TA)  
  Immediate sender of the frame on this hop.

Ethernet usually needs only a source and destination MAC because it forwards over a single cabled segment at a time. Wireless often needs to distinguish between immediate sender or receiver and the original endpoints, so 802.11 can use more address fields.

### Address field example

Example: PC1 sends traffic to PC2 through AP1.

- PC1 uses AP1 as the immediate receiver.
- RA equals the BSSID (AP1 MAC), placed in Address 1.
- DA is the MAC address of PC2.
- SA is the MAC address of PC1.
- TA is the MAC address of the device transmitting the frame on the air.

Different frame types use different patterns, and not all four address fields appear in every frame. Full combinations are beyond CCNA scope, but the key idea is that 802.11 can separate original endpoints from the immediate wireless hop.

### Frame header fields

Main header fields:

- Frame Control  
  Indicates frame type and subtype and various control flags.

- Duration or ID  
  Either the time the channel is reserved for this frame or an association identifier, depending on frame type.

- Sequence Control  
  Used for fragmentation and retransmission identification.

- QoS Control  
  Used to prioritize traffic classes when QoS is enabled.

- HT (High Throughput) Control  
  Supports high throughput features in 802.11n, 802.11ac, and later standards.

- Frame Body  
  Encapsulated payload, often an IP packet.

- Frame Check Sequence (FCS)  
  Allows the receiver to detect corruption in the frame.

## Client association process

### Association overview

Client connectivity to an AP is called association. A client must discover an AP, authenticate, and associate before sending or receiving data over the wireless LAN.

High level steps:

1. Discover APs and SSIDs.
2. Authenticate with a chosen AP.
3. Associate with the AP.
4. Begin data transfer.

### Discovery methods

Clients use either active or passive scanning.

- Active scanning  
  - Client sends probe requests on one or more channels.  
  - APs reply with probe responses that list supported SSIDs.  
  - Faster AP discovery at the cost of more client transmissions and power use.

- Passive scanning  
  - Client listens for beacon frames sent periodically by APs.  
  - Beacons advertise SSIDs and capabilities.  
  - Conserves client power but discovery can take longer.

In both cases the result is a list of visible SSIDs and APs that the client can choose from.

### Authentication and association

After discovering a suitable AP, the client:

1. Sends an authentication request frame to the AP.  
2. Receives an authentication response.  
3. Sends an association request.  
4. Receives an association response indicating success or failure.

Only after successful authentication and association can the client send and receive data frames through the AP.

## 802.11 message types

802.11 defines three broad frame categories.

### Management frames

- Used to establish and maintain communications in the WLAN.
- Examples:
  - Beacon
  - Probe request and probe response
  - Authentication and deauthentication
  - Association and disassociation

Management frames allow APs to advertise BSSs and control which clients can participate.

### Control frames

- Used to support reliable delivery over the RF medium.
- Key examples:
  - Request to send (RTS)
  - Clear to send (CTS)
  - Acknowledgment (Ack)

RTS and CTS coordinate access to the shared medium and help reduce collisions by reserving airtime. This improves reliability but adds overhead, so many modern networks rarely use RTS and CTS. Ack frames remain essential, because wireless links are less reliable and frames need positive confirmation. If an Ack is not received, the sender retransmits the frame.

### Data frames

- Carry user data between clients and APs.
- Payload is typically an IPv4 or IPv6 packet.
- Make up the majority of traffic once clients are associated.

## AP architectures

### Architecture types

Three main AP architectures appear in CCNA scope:

- Autonomous APs  
  Self contained units configured and managed individually.

- Lightweight APs  
  Centrally managed by a wireless LAN controller (WLC) using split MAC and CAPWAP tunnels.

- Cloud based APs  
  Managed by a SaaS cloud platform, such as Cisco Meraki.

These are different AP types, not just modes that any AP can adopt. Some models support only autonomous operation, some only lightweight, and some are designed as cloud managed devices.

## Autonomous APs

### Autonomous AP overview

- Self contained AP with full local intelligence.
- Handles client authentication, encryption, and management functions.
- Does not rely on an external controller.
- Useful in small networks with only a few APs.

### VLAN mapping and trunking

- Common to map each SSID to a VLAN on the wired side.
- AP acts as a bridge between SSIDs and VLANs.
- Typical uplink is an 802.1Q trunk to a switch.

Example layout:

- SSID EMPLOYEES mapped to VLAN 10.
- SSID GUEST mapped to VLAN 20.
- Management VLAN 99 used for AP management access.

A dedicated management VLAN improves security by separating management traffic from user data.

### Management of autonomous APs

- Each AP is configured directly via:
  - Console port
  - Telnet or SSH
  - Web GUI (HTTP or HTTPS)

- Individual management is practical only in very small deployments.
- Once a network reaches more than a handful of APs, centralized control becomes preferable.

## Lightweight APs and wireless LAN controllers

### WLC and LWAP overview

- Large WLANs use a wireless LAN controller (WLC) to centralize control.
- APs managed by a WLC are called lightweight APs (LWAPs).
- LWAPs rely on the WLC for many control plane functions.

This is called split MAC architecture:

- LWAPs handle real time RF tasks.
- WLC handles management and policy tasks.

### MAC functions split

LWAP responsibilities:

- Transmitting and receiving RF signals.
- Encrypting and decrypting 802.11 frames.
- Sending beacons and responding to probe requests.

WLC responsibilities:

- RF management (channel and power selection).
- Client authentication and association logic.
- Security and QoS policy enforcement.
- Central configuration and monitoring.

### Connection differences

- Autonomous APs usually connect to the LAN using trunk ports and perform SSID to VLAN mapping themselves.
- LWAPs typically connect with access ports in a single management VLAN.
- The WLC performs SSID to VLAN mapping and handles client data forwarding.

### CAPWAP tunnels

WLCs and LWAPs use CAPWAP to build tunnels across the wired network.

- CAPWAP creates two tunnels per LWAP:
  - Control tunnel (UDP port 5246) for management traffic between LWAP and WLC.
  - Data tunnel (UDP port 5247) for client data frames.

- CAPWAP control tunnel is encrypted by default.
- Data tunnel encryption is optional and uses Datagram Transport Layer Security (DTLS).

Central control allows features such as:

- Automatic channel selection.
- Dynamic transmit power adjustment.
- Self healing coverage if an AP fails.

## WLC deployment options

Different deployments use different WLC form factors.

### Unified WLC

- Dedicated hardware appliance.
- Models scale from a few hundred LWAPs up to thousands.
- High capacity models support up to about 6,000 LWAPs and 64,000 clients.

### Cloud WLC

- Virtual machine running in a private or public cloud.
- Capacity depends on allocated resources.
- Can reach similar scale as large unified WLCs.

### Embedded WLC

- WLC integrated into a switch.
- Suitable for smaller deployments.
- Typical capacity up to around 200 APs and 4,000 clients.

### Mobility Express and embedded AP controllers

- WLC functionality integrated into an AP.
- Historically known as Mobility Express.
- Scales to around 100 LWAPs and 2,000 clients.
- Newer Cisco platforms often use the term embedded WLC for both switch based and AP based controllers.

## LWAP operational modes

LWAPs can operate in several modes, some serving clients and others focused on monitoring and analysis.

### Client serving modes

- Local mode  
  - Default mode.  
  - LWAP provides BSSs and tunnels all client traffic to the WLC using CAPWAP.

- FlexConnect mode  
  - LWAP can locally switch client traffic between wireless and wired LANs.  
  - Reduces latency and WAN bandwidth to the WLC.  
  - Can be enabled per SSID.  
  - FlexConnect enabled SSIDs can continue to pass traffic locally even if the LWAP temporarily loses connectivity to the WLC.

- Bridge and Flex plus Bridge modes  
  - Used in mesh deployments.  
  - LWAPs form wireless links between each other and can also bridge between wired LANs.  
  - Flex plus Bridge adds FlexConnect local switching to mesh operation.

### Monitoring and analysis modes

- Monitor  
  - Radios listen only.  
  - Used for RF analysis and rogue device detection.

- Rogue Detector  
  - Radios disabled.  
  - Listens on the wired LAN to help identify rogue devices.

- Sniffer  
  - Captures all wireless frames on a specific channel.  
  - Sends captured traffic to the WLC or analysis tools such as Wireshark.

- SE Connect  
  - Dedicated to RF spectrum analysis across channels.  
  - Feeds spectrum data to tools such as Cisco Spectrum Expert.

Rogue devices are unauthorized APs or clients connected without permission and can be a security risk, so detection is an important operational goal.

## Cloud based APs

### Architecture overview

- Cloud based APs use a SaaS cloud platform for configuration and monitoring.
- Cisco Meraki is the main Cisco example.
- APs build encrypted management tunnels to the cloud platform.

Key points:

- RF data, client statistics, and events are sent to the cloud.
- Administrators use a web based dashboard for configuration and monitoring.
- User data traffic remains on the local LAN and is not tunneled to the cloud.

This provides centralized management without deploying an on premises WLC.

### Cloud based vs cloud WLC

- Cloud based AP architecture  
  - APs are managed by a SaaS platform.  
  - No WLC is deployed in the customer network.  

- Cloud WLC deployment  
  - Split MAC architecture using CAPWAP.  
  - WLC runs as a VM in a data center or public cloud.  

These are different concepts and both appear in CCNA topics.

## Cloud managed network devices

### Meraki platform

- Meraki manages more than APs.  
- Switches, firewalls, cameras, and sensors can also be managed from the same dashboard.

### Cloud management characteristics

- Centralized configuration and monitoring through a web interface.
- Devices connect to the cloud platform and download their configuration.
- Zero touch provisioning allows new devices to be deployed with minimal local setup.

### Cloud management benefits

- Rapid deployment using templates and automated provisioning.
- Simplified management from a single dashboard instead of per device CLI.
- Enhanced visibility and analytics for traffic and client behavior.
- Automated firmware and security updates.
- Improved operational efficiency in many environments.

### Considerations

- Centralized cloud management may not fit every organization.
- Some networks require on premises management data, specialized features, or deeper customization.

## Quick review

- 802.11 frames have their own header format and can include up to four address fields to distinguish original endpoints from immediate wireless hops.  
- Client association requires discovery, authentication, and association before data frames can flow.  
- Management frames handle beacons, probes, and join and leave events, control frames support reliable delivery, and data frames carry user payloads.  
- Autonomous APs map SSIDs to VLANs locally and are manageable in small deployments; larger networks typically rely on WLCs and LWAPs.  
- Split MAC architecture uses LWAPs for real time RF tasks and a WLC for centralized control, with CAPWAP control and data tunnels between them.  
- WLCs can be deployed as dedicated appliances, VMs in the cloud, embedded controllers in switches, or embedded controllers inside APs.  
- LWAP modes include Local, FlexConnect, Bridge, and several monitoring modes that help with RF analysis and rogue detection.  
- Cloud based APs and broader cloud managed platforms such as Meraki provide centralized management from a SaaS dashboard while keeping user data local.  
