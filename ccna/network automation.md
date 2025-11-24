
# Network Automation

## Overview

Network automation uses software to perform network tasks that would otherwise require manual configuration. It ranges from simple scripts to full automation platforms and is increasingly common in enterprise networks.

## Network automation fundamentals

### Definition

- Broad term for techniques that automate network operations
- Not tied to one specific tool or vendor
- Uses software workflows to make repeatable, low error changes across many devices

### Benefits

- Efficiency  
  - Configuration changes can be applied to many devices in a short time
- Accuracy  
  - Reduces typos and inconsistent configuration
- Scalability  
  - Supports large networks without a linear increase in manual effort
- Consistency  
  - Ensures that devices of the same role share the same baseline configuration
- Cost control  
  - Reduces time spent on repetitive tasks

### Simple scripting example

Common use case:

- A Python script connects to a list of devices with SSH libraries such as Netmiko
- Script applies a set of configuration commands
- Script saves the configuration and logs any failures

As long as the script is tested, it can roll out standard changes more reliably than manual per device work.

## Three logical planes of networking

Network device functions can be grouped into three logical planes.

### Data plane

- Handles actual forwarding of frames and packets
- Examples on a switch:
  - Forward or flood frames based on MAC address table
  - Apply port security, DHCP snooping, Dynamic ARP Inspection
  - Add or remove 802.1Q tags on trunk ports
- Examples on a router:
  - Forward packets based on routing table
  - Encapsulate packets into appropriate Layer 2 frames
  - Apply access lists and QoS at the forwarding level

### Control plane

- Builds the information that the data plane uses
- Not directly forwarding user data, but supports forwarding decisions
- Examples:
  - OSPF and other routing protocols building the routing table
  - STP and related protocols selecting forwarding and blocking ports
  - ARP and IPv6 Neighbor Discovery building neighbor tables
  - MAC address learning building the MAC address table

### Management plane

- Provides access to configure, monitor, and manage devices
- Typical protocols:
  - SSH and Telnet for CLI access
  - Syslog for logging
  - SNMP for monitoring
  - NTP for time synchronization
- Changes made via the management plane (for example CLI commands) affect control plane behavior, which then influences data plane forwarding

## Software defined networking (SDN)

### Traditional distributed control plane

- Each router or switch runs its own control plane protocols
- Example: every router runs OSPF, exchanges LSAs, and calculates its own routing table
- Control plane intelligence is distributed across devices

### Centralized control plane

- SDN centralizes some or all control plane functions in a controller
- Controller has a global view of the network
- Controller calculates forwarding decisions or policies
- Devices focus on data plane forwarding based on instructions from the controller

### SDN layers

SDN designs are usually described as three layers:

- Application layer  
  - Applications that express network requirements and policy  
  - Examples: security policy tools, monitoring and analytics tools

- Control layer  
  - SDN controller that translates application intent into device instructions  
  - Maintains a global view of topology and policy

- Infrastructure layer  
  - Physical and virtual network devices (switches, routers, access points, firewalls)  
  - Execute forwarding based on instructions from the controller

### SDN interfaces

Communication between layers uses APIs and control protocols.

- Northbound interface (NBI)  
  - Between application and control layers  
  - Commonly REST APIs over HTTP or HTTPS

- Southbound interface (SBI)  
  - Between control and infrastructure layers  
  - Examples:
    - OpenFlow for direct data plane control
    - NETCONF for configuration management
    - OpFlex in Cisco ACI environments
    - SSH or SNMP for device management

## Cisco SDN solutions

### Common terms

- Underlay  
  - Physical network that forwards IP packets
- Overlay  
  - Virtual network built on top of the underlay, often using tunnels
- Fabric  
  - Combination of underlay and overlay as a single system

### SD Access

- Cisco SDN solution for campus LANs
- Uses VXLAN tunnels to build an overlay on top of the physical campus underlay
- Cisco Catalyst Center acts as the controller and management platform
- Automates policy, segmentation, and user access across wired and wireless networks

### SD WAN

- Cisco SDN solution for WAN connectivity
- Builds an overlay of IPsec tunnels over transports such as internet, MPLS, and cellular
- Separate controllers handle:
  - Device onboarding
  - Control plane (route and policy distribution)
  - Management and monitoring
- Focuses on application aware routing and secure connectivity between sites and cloud

### Application Centric Infrastructure (ACI)

- Cisco SDN solution for data centers
- Uses VXLAN overlay over a spine leaf underlay
- Application Policy Infrastructure Controller (APIC) is the controller
- APIC translates application policies into switch configurations across the fabric

## Intent based networking

- Intent based networking (IBN) builds on SDN concepts
- Engineer defines desired network behavior as policy or intent
- Controller determines the specific device configurations needed
- Focus shifts from individual device CLI to higher level policies such as:
  - Which users or devices can talk to each other
  - Which applications receive higher priority
  - Which segments require stricter security

## AI and ML in networking

### Core ideas

- Artificial intelligence (AI) in networking means using algorithms to analyze data, detect patterns, and support decisions
- Machine learning (ML) is a subset of AI that learns from data rather than explicit per case rules
- Deep learning (DL) uses neural networks for more complex pattern recognition

### Predictive AI in network operations

Typical uses:

- Traffic forecasting for capacity planning
- Predictive maintenance by spotting device health trends
- Anomaly detection and early warning for security issues
- Identifying congestion or chronic performance hot spots

### Generative AI in network operations

Possible uses:

- Drafting configuration snippets or automation scripts
- Creating or updating network documentation
- Assisting in network design proposals
- Generating diagrams from inventory and topology data

Outputs still require validation by network engineers before deployment.

### Example: Cisco Catalyst Center AI features

- Endpoint analytics to classify and profile connected devices
- Radio resource management recommendations for wireless networks
- Machine reasoning for automated root cause analysis and suggested fixes

## Quick review

- Network automation applies software and scripting to network tasks for efficiency and consistency.  
- Data, control, and management planes separate forwarding, decision making, and management functions on devices.  
- SDN centralizes the control plane in a controller and uses NBIs and SBIs to connect applications and devices.  
- Cisco SDN offerings include SD Access for campus, SD WAN for WAN, and ACI for data centers, all using overlay tunnels on a physical underlay.  
- Intent based networking lets engineers describe desired outcomes while the controller implements the details.  
- AI and ML in networking support predictive analytics, anomaly detection, and assisted configuration and documentation.
