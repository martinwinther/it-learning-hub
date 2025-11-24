# Wireless LAN Architectures

## Overview

In the previous chapter, we covered the basic building blocks of wireless LANs, starting with the fundamentals of radio frequency (RF) and connecting devices wirelessly in different types of service sets. In this chapter, we will continue on that theme by examining 802.11 frames and message types. We will then zoom out and look at the bigger picture—the different ways wireless access points (APs) can be deployed and managed to provide wireless access to clients in networks of all sizes.

## 802.11 Frame Format

### Frame Structure

- Like Ethernet, 802.11 encapsulates Layer 3 packets in frames before sending them over physical medium—air, in 802.11's case
- As we covered in previous chapter, sending frames over air is quite bit different from sending them along cable
- For that reason, 802.11 defines its own frame format and variety of message types necessary to facilitate wireless communications
- 802.11 frame format
- Field sizes in bytes are indicated above each field
- Depending on 802.11 standard being used and message type, some of fields might not be present in frame
- There are up to four address fields instead of typical two

### Address Fields

- Let's focus on second point
- Ethernet connects devices over bounded medium—cables
- Because of this, each frame needs only source address and destination address to identify sender and receiver
- Communicating via AP over air, unbounded medium, adds some complexity that requires additional address fields
- 802.11 frames contain up to four
- These can identify some combination of following addresses:
  - Basic service set identifier (BSSID): AP's BSSID
  - Destination address (DA): Final recipient of frame
  - Source address (SA): Original sender of frame
  - Receiver address (RA): Immediate recipient of frame
  - Transmitter address (TA): Immediate sender of frame

### Address Field Example

- PC1 sends frame to PC2
- By specifying different immediate and final recipient, PC1 sends its frame via AP1 instead of directly to PC2
- RA = BSSID in figure means RA and BSSID are identical: they are AP1's MAC address
- And it is specified in Address 1 field when PC1 sends frame
- Same applies to TA = SA, RA = DA, and TA = BSSID
- Figure shows just one example demonstrating that PC1 can specify different immediate and final recipient
- There are various possible patterns, and depending on message type, there might be one, two, three, or four address fields in 802.11 frame
- Such details are well beyond scope of CCNA exam

### Frame Header Fields

- Frame Control: Provides information such as message type and subtype
- Duration/ID: Depending on message type, this field can indicate time (in milliseconds) channel will be dedicated to transmission of frame, or identifier for association (connection between client and AP)
- Sequence Control: Used to reassemble fragmented message and identify retransmitted frames
- QoS Control: Used in QoS to prioritize certain traffic types
- HT (High Throughput) Control: Used to support higher data transfer rates of 802.11n, 802.11ac, and later standards
- Frame Body: Message encapsulated inside of frame
- FCS (Frame Check Sequence): Like Ethernet FCS, this allows receiving device to check if frame was corrupted in transit

## Client Association Process

### Association Overview

- In section on message types, we'll take look at some 802.11 message types
- But before that, let's see some of them in action in client association process
- Client's connection to AP is called association
- For client to send and receive wireless traffic via AP, client must be associated with AP
- And before AP will allow client to associate with it, it must authenticate client; it must ensure that it is valid client
- Client association process
- Probe request/response exchange allows PC1 to discover AP1
- PC1 then authenticates and associates with AP1

### Discovery Methods

- Process begins with PC1 sending probe request to discover any APs (and SSIDs they offer) within range
- There are two ways to accomplish this:
  - Active scanning: Client sends probe requests and listens for probe responses from APs (as shown in figure). This helps clients discover APs more quickly, although constant active scanning can shorten client's battery life
  - Passive scanning: Client listens for beacon messages from APs; APs send beacon messages periodically to advertise each BSS. This can conserve client's battery life, but it may take longer for client to discover available APs

### Authentication and Association

- After client discovers AP, whether through active or passive scanning, it can then request to authenticate and associate with AP
- Client can only send data over wireless LAN after successfully authenticating and associating with AP
- Although 802.11 active scanning and passive scanning are probably new terms to you, you've surely experienced them before
- When you connect your phone or laptop to Wi-Fi at new cafe or someone's house and see list of available SSIDs
- Those SSIDs are advertised by APs your device discovered through either active or passive scanning
- Your device likely discovers unfamiliar APs/SSIDs even within your own home
- If that happens, it means that your device either received beacons from those APs or exchanged probe requests/responses with them

## 802.11 Message Types

### Three Main Types

- Management: Used to establish communications in wireless LAN
- Control: Used to facilitate delivery of frames over medium
- Data: Used to carry data payloads (typically, IP packets)

### Management Frames

- Let's take look at some examples of each message type, starting with management
- Message types shown in previous section—probe, beacon, authentication, and association—are all 802.11 management messages
- Another example is disassociation, which client sends to end its association with AP
- Management messages are used to establish communications in wireless LAN and allow AP to manage BSS by controlling which clients can participate

### Control Frames

- Second type is control, which is used to facilitate delivery of frames over medium
- Three examples are request-to-send (RTS), clear-to-send (CTS), and acknowledgment (Ack)
- RTS, CTS, and Ack messages facilitate smooth communication over medium
- RTS asks for permission to transmit frame, and CTS grants permission
- Ack acknowledges receipt of frame
- RTS/CTS mechanism of asking for and granting permission to transmit frame helps to reduce collisions in wireless LAN
- However, it adds additional overhead: for each data frame to be sent, two extra frames (RTS and CTS) must be transmitted
- Which can reduce overall network efficiency
- Modern networks usually do not use RTS/CTS
- Ack messages, on other hand, are necessity
- Nature of wireless networks makes frame delivery less reliable than on wired networks
- So Ack mechanism is used to verify that frames have been properly delivered
- After device successfully receives frame, it must send Ack back to sender
- If Ack isn't received, frame is retransmitted

### Data Frames

- Data frames are final 802.11 frame type
- These are frames that carry actual data to and from wireless clients that are communicating over network
- In most cases, payload of these frames is IP packet—IPv4 or IPv6

## AP Architectures

### Three Main Architectures

- APs can be integrated into network in multiple ways
- For example, as standalone units that you configure and manage individually
- Or centrally managed from wireless LAN controller (WLC) or SaaS cloud platform
- In this section, we will cover three main AP architectures:
  - Autonomous APs: Self-contained units that operate independently of other APs, with each requiring individual configuration and management
  - Lightweight APs: APs that are centrally managed by WLC. Complex tasks such as client authentication, security policy enforcement, and RF management are offloaded to WLC, simplifying AP deployment and management
  - Cloud-based APs: APs that are managed remotely over internet via cloud service

### Architecture Types

- Autonomous, lightweight, and cloud based are not simply operational modes that any AP is capable of
- They are different types of APs
- Example: for AP to function as autonomous AP, it requires additional hardware and software capabilities that aren't present in lightweight APs
- Some APs can only be autonomous, some can only be lightweight, and some can be either
- Same goes for cloud-based APs
- Standard Cisco AP cannot operate as cloud-based AP—only those sold by Cisco Meraki (company Cisco acquired in 2012)

## Autonomous APs

### Autonomous AP Overview

- Autonomous AP is self-contained unit
- It has necessary built-in intelligence to handle all aspects of wireless network operations
- From client authentication to data encryption—autonomous AP doesn't rely on external controller
- Each autonomous AP functions as standalone entity, requiring individual configuration and management
- Autonomous APs are useful in small networks or in areas where only few APs are needed
- Offering simple setup without need for additional centralized control systems
- Two autonomous APs providing two ESSs for clients
- Autonomous APs connect to wired LAN via trunk links to support multiple SSIDs/VLANs

### Autonomous AP Configuration

- Autonomous APs connect to wired LAN via trunk links
- This is because they typically support multiple SSIDs, each mapped to Ethernet VLAN on wired LAN
- Example: one SSID may be for employee access while another is for guest access
- In figure, one SSID is mapped to VLAN 10, and other SSID is mapped to VLAN 20
- AP translates between each SSID and VLAN, serving as bridge between wireless and wired LANs
- Trunk ports are necessary to support multiple VLANs on wired network
- Figure also lists management VLAN (VLAN 99)—VLAN dedicated to managing APs themselves (and other network devices, like switches in LAN)
- As mentioned in chapter on Telnet and SSH, creating separate VLAN to isolate management traffic is considered best practice
- This isolation streamlines device management and enhances network security by segregating management traffic from user data

### Autonomous AP Management

- Autonomous APs require individual configuration
- Which is done directly through CLI using console port, Telnet, or SSH
- Or through GUI via web browser using HTTP/HTTPS
- Individually managing APs is feasible in small network with only few APs
- But when network grows beyond 5 to 10 APs, it becomes inefficient
- And in larger networks, which can have thousands of APs spread across many LANs
- Individually managing autonomous APs is just not practical; centralized management becomes essential

## Lightweight APs and Wireless LAN Controllers

### WLC Overview

- To support larger wireless LANs, wireless LAN controller (WLC) is used to centralize control and simplify operations
- AP that is controlled by WLC is called lightweight AP (LWAP)
- LWAPs offload many of their functions to WLC
- This is called split-MAC architecture, where real-time media access control (MAC) operations are performed by LWAPs
- And more complex, non-real-time functions are handled by WLC

### Media Access Control

- Media access control (MAC) is one of main functions of Layer 2 of TCP/IP model
- That manages how devices uniquely identify themselves (MAC addresses) and communicate over shared network medium, like Ethernet or Wi-Fi

### Split-MAC Architecture

- WLC is responsible for management functions, such as RF management (setting each LWAP's channel and transmit power)
- Client authentication and association
- And QoS and security policy enforcement
- LWAPs handle real-time functions like transmitting and receiving RF signals
- Encryption of 802.11 frames
- Sending beacon messages
- Responding to clients' probe requests, etc.
- Two LWAPs managed by WLC
- WLC handles management functions, and LWAPs handle real-time functions
- Note that precise location of WLC in network can vary
- It could be in remote data center, connected to core or distribution switch in LAN
- Or even incorporated into switch or AP
- Later in this section, we'll examine these different options

### Connection Differences

- Key difference between autonomous APs and LWAPs is how they connect to wired network
- Autonomous APs use trunk ports to handle multiple VLANs for different SSIDs (plus management VLAN)
- In contrast, LWAPs typically connect to wired LAN using access ports, which only support single VLAN—management VLAN, in this case
- Job of translating between SSIDs and VLANs is offloaded to WLC
- To achieve this, protocol called Control and Provisioning of Wireless Access Points (CAPWAP) is used to establish tunnels between LWAPs and WLC
- LWAPs tunnel client data frames to WLC, which translates them into Ethernet frames

### CAPWAP Tunnels

- Remember what tunnel is: virtual communication pathway
- Tunnels don't make new physical pathway; bits still pass over wired LAN
- However, tunneled messages are encapsulated with additional headers, as we covered in chapter on VPNs
- CAPWAP doesn't just create one tunnel between each LWAP and WLC
- It creates two: data tunnel and control tunnel
- CAPWAP data tunnel is used to tunnel traffic sent to and from wireless clients associated with LWAP: laptops, smartphones, etc.
- CAPWAP control tunnel is used to tunnel communications between LWAP and WLC
- WLC uses this tunnel to configure LWAPs and manage their operations
- CAPWAP creates two tunnels between each LWAP and WLC: control tunnel and data tunnel
- Control tunnel uses UDP port 5246, and data tunnel uses UDP port 5247

### CAPWAP Encryption

- CAPWAP control tunnel is encrypted by default, but data tunnel isn't
- Can enable data tunnel encryption for additional security
- CAPWAP encryption uses Datagram Transport Layer Security (DTLS)—type of TLS that uses UDP instead of TCP

### Split-MAC Benefits

- Centralizing control of LWAPs with split-MAC architecture provides several advantages
- Not just in terms of scalability
- Example: WLC gathers information about RF environment from LWAPs it manages
- And can intelligently make decisions such as which channels each LWAP should use
- Optimal transmit power of each AP, etc.
- This also allows for self-healing coverage: if one LWAP stops working, WLC can make nearby LWAPs increase their transmit power to maintain coverage area

### CAPWAP History

- CAPWAP is industry-standard protocol but is based on protocol called Lightweight Access Point Protocol (LWAPP)
- LWAPP was developed by Airespace, company that was purchased by Cisco in 2005

## WLC Deployment Options

### Deployment Overview

- In network with more than 5 to 10 APs, should consider using WLC to centrally control your wireless LANs
- However, there's big difference between network with, for example, 20 to 30 APs and network with thousands of them
- For that reason, there is no one-size-fits-all WLC solution
- There are variety of WLC deployment options that meet different needs
- WLC deployment options
- Unified WLC is dedicated hardware appliance
- Cloud WLC is VM deployed in private or public cloud
- Embedded WLC is integrated into switch
- Mobility Express WLC is integrated into AP
- To avoid showing same network four times with WLC in different locations, included all four deployment options in figure
- In practice, network would typically employ one option suited to its specific needs

### Unified WLC

- Unified WLC is dedicated hardware appliance
- Cisco offers various hardware models that can support anywhere from few hundred LWAPs to as many as 6,000 LWAPs and 64,000 clients with single WLC
- If your network has to support more WLCs and clients than that, you'll have to deploy second WLC

### Cloud WLC

- Cloud WLC is virtual machine (VM) deployed on server in cloud
- It could be, for example, private cloud in company's data center or public cloud platform
- Depending on hardware resources available to VM, cloud WLC can support 1,000, 3,000, or even 6,000 LWAPs
- And up to 64,000 clients—as much as unified WLC

### Embedded WLC

- Embedded WLC is WLC integrated into switch
- Embedded WLCs are more suitable for smaller deployments, supporting up to 200 APs and 4,000 clients

### Mobility Express WLC

- For even smaller deployments, Cisco Mobility Express integrates WLC within AP
- Supporting up to 100 LWAPs and 2,000 clients
- WLC deployment options summary:
  - Name: Unified, Description: Dedicated hardware appliance, Max LWAPs: 6,000, Max Clients: 64,000
  - Name: Cloud, Description: VM deployed in cloud, Max LWAPs: 6,000, Max Clients: 64,000
  - Name: Embedded, Description: Integrated into switch, Max LWAPs: 200, Max Clients: 4,000
  - Name: Mobility Express, Description: Integrated into AP, Max LWAPs: 100, Max Clients: 2,000
- In Cisco's newer line of WLCs and APs, they have dropped Mobility Express terminology
- Using term embedded both for WLC integrated into switch and WLC integrated into AP
- Be aware of both terms for CCNA exam

## LWAP Operational Modes

### Client-Serving Modes

- In previous chapter, we looked at few additional AP operational modes: repeater, workgroup bridge, and outdoor bridge
- LWAPs controlled by WLC can also be configured to operate in various modes
- In some modes, LWAP provides network service to clients
- And in others, it is dedicated to more specialized network management role
- First, let's examine client-serving modes:
  - Local: Standard operational mode, providing BSSs for clients. LWAP tunnels all client traffic to WLC via CAPWAP
  - FlexConnect: Similar to Local, but client traffic doesn't have to be tunneled to WLC; LWAP can locally switch client traffic between wired and wireless LANs
  - Bridge and Flex + Bridge: Used in mesh deployments

### Local Mode

- Local is default LWAP operational mode that we have covered so far
- LWAP in local mode offers BSSs for clients and tunnels all client traffic to WLC via CAPWAP data tunnel
- However, this is not always desirable
- Tunneling all client traffic to WLC can be inefficient, especially if WLC and clients aren't located in same LAN

### FlexConnect Mode

- FlexConnect offers more flexible approach (hence name) in which LWAP can locally switch client traffic between wired and wireless LANs
- No need to tunnel it to WLC
- This reduces latency for client traffic because it doesn't have to travel all way to WLC and back
- And also conserves bandwidth on WAN connections leading to WLC
- FlexConnect can be configured on per-SSID basis
- With FlexConnect enabled, LWAP can locally switch traffic between SSIDs and VLANs
- FlexConnect can be enabled per SSID
- Another benefit of FlexConnect is that LWAP can locally switch traffic between FlexConnect-enabled SSIDs and wired LAN even if it loses its connection to WLC
- This allows clients using those SSIDs to maintain connectivity even if such problem occurs

### Bridge Mode

- LWAP operating in Bridge mode can form wireless mesh with other LWAPs without directly connecting each LWAP to wired network infrastructure
- MBSS, as we covered in previous chapter
- LWAPs in Bridge mode can also function as bridges connecting wired LANs (like "outdoor bridge" mode, as covered in chapter 18)
- Flex + Bridge mode adds FlexConnect on top of Bridge mode
- Allowing LWAPs to locally switch client traffic without tunneling it to WLC

### Network Management Modes

- Monitor: LWAP doesn't transmit from its radios; it is dedicated to analyzing RF environment and detecting unauthorized ("rogue") devices
- Rogue Detector: LWAP's radios are entirely disabled; it is dedicated to analyzing traffic on wired LAN to detect rogue devices
- Sniffer: LWAP captures all wireless traffic on specific channel. Captured messages are then sent to WLC and can be redirected to analysis software such as Wireshark for detailed inspection and troubleshooting
- SE-Connect: LWAP is dedicated to RF spectrum analysis on all channels. It feeds data to spectrum analysis software like Cisco Spectrum Expert for in-depth evaluation of RF landscape

### Rogue Devices

- Rogue is unauthorized AP or client that has been connected to network without network administrator's permission
- Rogue devices can pose security risk, so identifying and dealing with them is important

### Management Mode Benefits

- Although these operational modes don't directly serve clients
- Dedicating LWAPs to specific tasks such as RF spectrum analysis, rogue device detection, and traffic analysis can give important insights into status of network
- This can help proactively identify and address problems in wireless LANs

## Cloud-Based APs

### Cloud-Based Overview

- In addition to autonomous and lightweight APs, there is third option that can be considered middle ground between two: cloud-based
- Cloud-based AP architecture uses cloud platform to streamline management of APs
- Essentially, it's public SaaS cloud service
- Cisco's offering is Cisco Meraki
- Cisco Meraki offers cloud-based APs
- Meraki APs are managed using Meraki's cloud platform, which connects to each AP using encrypted tunnel
- User data traffic from clients is not tunneled to cloud—only management traffic

### Meraki Operation

- Meraki APs communicate with Meraki cloud platform over internet in encrypted tunnel
- Each AP sends RF spectrum information, client statistics, and various other kinds of information to Meraki cloud over this tunnel
- Admin can log in to Meraki dashboard—web browser-based tool—to centrally manage APs
- User data, however, is not tunneled to cloud; it goes straight to wired LAN

### Cloud-Based Benefits

- Cloud-based APs use cloud computing to offer scalable, easy-to-manage wireless network solution
- Unlike autonomous APs that are managed individually or lightweight APs that require WLC
- Cloud-based APs connect to SaaS cloud service for configuration and management
- This architecture simplifies complex tasks such as deploying new APs, adjusting configurations, monitoring network health, and troubleshooting problems
- Although centralized management is common to lightweight and cloud-based APs
- Main advantages of cloud-based approach are simplicity and ease of use

### Cloud-Based vs Cloud WLC

- Don't mix up concepts of cloud-based AP architecture and cloud WLC deployment
- Cloud-based AP architecture manages APs using SaaS cloud platform
- Cloud WLC deployment is split-MAC architecture with WLC deployed as VM in cloud

## Cloud-Managed Network Devices

### Meraki Platform

- Although best known for their cloud-based APs, Cisco Meraki offers variety of network devices that can be managed from their cloud platform
- Switches, firewalls, Internet of Things (IoT) devices like cameras and sensors, etc.
- In this section, let's move our focus away from wireless LANs to consider characteristics and benefits of cloud-based network management platforms like Meraki

### Cloud Management Characteristics

- Cloud-managed network devices offer centralized approach to network management
- Where configuration, monitoring, and troubleshooting are all handled through cloud-based platform
- This centralized approach is key characteristic of cloud-managed devices
- Instead of managing devices one by one via CLI, can manage all devices from single web-based dashboard
- This offers variety of benefits for many enterprises

### Cloud Management Benefits

1. **Rapid and simplified deployment**: Cloud management platforms like Meraki use zero-touch provisioning (ZTP) to facilitate deployment of new network devices without requiring manual configuration of each device. Newly connected devices automatically connect to Meraki cloud and download their configurations. This is much simpler than traditional process, which involves manually configuring new devices one by one via console port before deploying them to network
2. **Simplified management**: With unified interface for managing all devices in network, administrators can spend less time on routine management tasks. Configuration changes can be applied to all devices at once through cloud, eliminating need for manual configuration of each device
3. **Enhanced visibility and analytics**: Cloud platforms provide detailed analytics and reporting tools that can help administrators understand network usage patterns, identify bottlenecks in network, and optimize network performance
4. **Automated updates**: Network device firmware updates and security patches can be automatically deployed to all devices, ensuring they are up-to-date. Out-of-date software can be serious vulnerability, so this is critical part of maintaining secure network
5. **Operational efficiency**: By simplifying overall process of deploying and managing network through centralized management and automation, operating expenses (OpEx)—ongoing costs associated with maintaining network—are reduced

### Cloud Management Considerations

- Two key takeaways are centralized management and simplicity
- Cloud management solutions like Meraki offer modern, efficient, and scalable approach to network management for many enterprises
- However, it might not be ideal for organizations with highly specialized or complex networking requirements
- Stringent data privacy concerns that mandate keeping all management data on-premises
- Or those that require deep customization and control beyond what cloud platforms typically offer

## Real-World Applications

- **Enterprise wireless networks**: Centralized management of large-scale wireless deployments
- **Small business networks**: Simplified management for networks with limited IT resources
- **Remote site management**: Managing APs across multiple locations from central location
- **Cloud-managed infrastructure**: Complete network infrastructure managed from cloud platform
- **Network monitoring**: Dedicated APs for RF analysis and rogue device detection

## Troubleshooting

### Common Issues

- **AP not joining WLC**: Verify CAPWAP connectivity and discovery methods
- **Client connectivity problems**: Check WLAN configuration and security settings
- **Performance issues**: Monitor RF environment and channel utilization
- **Management access**: Verify management interface and authentication settings

### Troubleshooting Steps

1. Verify WLC connectivity: Check management interface and network connectivity
2. Check AP discovery: Verify DHCP option 43 and discovery methods
3. Review WLAN configuration: Check SSID, security, and interface mapping
4. Monitor RF environment: Check channel utilization and interference
5. Test client connectivity: Verify client can associate and authenticate

## Best Practices

- Use WLC for networks with more than 5-10 APs
- Choose appropriate WLC deployment option based on network size
- Configure proper management VLAN for APs
- Use CAPWAP encryption for additional security
- Enable self-healing coverage features
- Monitor RF environment regularly
- Use dedicated APs for monitoring and analysis
- Document wireless network architecture

## Summary

- 802.11 defines frame format that differs from Ethernet in couple of key ways
- Depending on 802.11 standard and message type, some fields might not be present
- And there are up to four address fields instead of two
- 802.11 address fields identify some combination of following, depending on message type:
  - Basic service set identifier (BSSID): AP's BSSID
  - Destination address (DA): Final recipient of frame
  - Source address (SA): Original sender of frame
  - Receiver address (RA): Immediate recipient of frame
  - Transmitter address (TA): Immediate sender of frame
- Client's connection to AP is called association
- For client to send and receive wireless traffic via AP, client must be associated with AP
- To discover nearby APs, client can send probe request
- APs will respond with probe response
- This is called active scanning
- In passive scanning, client listens for beacon messages that APs send periodically to advertise each BSS
- After discovering AP, client must send authentication request and then, if successful, association request
- 802.11 defines three main types of messages: management, control, and data
- Management frames are used to establish and maintain communications in wireless LAN
- Examples include probe, beacon, authentication, and association messages
- Control frames are used to facilitate delivery of frames over medium
- And include request-to-send (RTS) and clear-to-send (CTS), which are used to request and grant permission to transmit frame
- And acknowledgment (Ack), which is used to acknowledge receipt of frame
- Data frames carry actual data to and from wireless clients communicating over network
- APs can be deployed in three main architectures: autonomous, lightweight, and cloud-based
- Autonomous AP is self-contained unit with built-in intelligence to handle all aspects of wireless network operations
- Autonomous APs connect to wired LAN via trunk links; autonomous APs need to be able to translate each SSID to VLAN on wired LAN
- Furthermore, separate management VLAN should be used to connect to and manage AP itself
- Autonomous APs require individual configuration, which is done through CLI (console, Telnet, or SSH) or GUI via web browser using HTTP/HTTPS
- Individually managing autonomous APs is not feasible in larger networks
- To support larger wireless LANs, wireless LAN controller (WLC) is used to centralize control and simplify operations
- AP that is controlled by WLC is called lightweight AP (LWAP)
- LWAPs offload many of their functions to WLC; this is called split-MAC architecture
- Real-time operations (sending and receiving RF signals, encrypting frames) are handled by each LWAP
- And non-real-time functions (RF management, client authentication and association, QoS and security policy) are handled by WLC
- Whereas autonomous APs connect to wired LAN via trunk ports, LWAPs connect via access ports in management VLAN
- Job of translating between SSIDs and VLANs is offloaded to WLC
- Control and Provisioning of Wireless Access points (CAPWAP) protocol is used to establish tunnels between LWAPs and WLC
- LWAPs tunnel frames from clients to WLC, which translates them into Ethernet frames in appropriate VLAN
- CAPWAP establishes two tunnels from each LWAP to WLC
- Data tunnel is used to tunnel traffic sent to and from wireless clients
- Control tunnel is used to tunnel communications between LWAP and WLC
- CAPWAP control tunnel is encrypted by default, but data tunnel is not
- CAPWAP encryption uses Datagram Transport Layer Security (DTLS)—type of TLS that uses UDP instead of TCP
- There are various WLC deployment options that meet different needs: unified, cloud, embedded, and Mobility Express
- Unified WLC is dedicated hardware appliance; Cisco offers various hardware models that can support anywhere, from few hundred LWAPS to as many as 6,000 LWAPs and 64,000 clients
- Cloud WLC is VM deployed on server in cloud
- Depending on hardware resources available to VM, it can support up to 6,000 LWAPs and 64,000 clients
- Embedded WLC is integrated into switch
- Embedded WLCs are more suitable for smaller deployments, supporting up to 200 APs and 4,000 clients
- Mobility Express WLC is integrated into AP, supporting up to 100 LWAPs and 2,000 clients
- LWAPs can operate in various modes, some of which provide network service to clients and some that play network management role
- Default LWAP operational mode is Local, in which LWAP provide BSSs for clients to connect to, tunneling their traffic to WLC via CAPWAP
- FlexConnect offers more flexible approach in which LWAP can locally switch client traffic between wired and wireless LANs—no need to tunnel it to WLC
- FlexConnect can be enabled on per-SSID basis
- LWAP operating in Bridge mode can form wireless mesh with other LWAPs without directly connecting each LWAP to wired network
- LWAPs in Bridge mode can also form bridge connecting two wired LANs
- Flex + Bridge mode adds FlexConnect on top of Bridge mode, allowing LWAPs in mesh to locally switch client traffic without tunneling it to WLC
- In Monitor mode, LWAP doesn't transmit from its radios
- It is dedicated to analyzing RF environment and detecting rogue devices
- In Rogue Detector mode, LWAP's radios are entirely disabled
- It is dedicated to analyzing traffic on wired LAN to detect rogue devices
- In Sniffer mode, LWAP captures all wireless traffic on specific channel and sends it to WLC for analysis
- In SE-Connect mode, LWAP is dedicated to RF spectrum analysis on all channels, feeding data to spectrum analysis software like Cisco Spectrum Expert
- In addition to autonomous and lightweight APs, there is third option that can be considered middle ground between two: cloud-based
- Cloud-based AP architecture uses cloud SaaS platform to streamline management of APs
- Cisco's offering is Cisco Meraki
- Meraki APs communicate with Meraki cloud platform over internet in encrypted tunnel
- Each AP sends RF information, client statistics, and various kinds of other information to Meraki cloud over this tunnel
- Admin can log in to Meraki dashboard—web browser-based tool—to centrally manage APs
- User data is not tunneled to cloud; it goes straight to wired LAN
- Cloud-managed network devices (e.g., Meraki's APs, switches, and firewalls) offer centralized approach to network management
- Configuration, monitoring, and troubleshooting are all handled through cloud-based platform like Meraki dashboard
- Cloud-based management solutions like Meraki offer simplicity, efficiency, and scalability that is beneficial for many modern enterprises
- However, it might not be ideal for organizations with highly specialized or complex networking requirements
