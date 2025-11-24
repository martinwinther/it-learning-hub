# LAN Architectures

## Overview

LAN architectures describe how switches, routers, and hosts are arranged and interconnected. The same basic patterns appear in campus networks, data centers, and small office or home office (SOHO) environments. CCNA focuses on recognizing these patterns and understanding what each layer or device is responsible for.

## Network topologies

### Star topology

- All devices connect to a single central device
- Common in LANs: end hosts connected to one switch
- Also called hub and spoke in WAN context
- Central device is the hub, connected devices are spokes

### Full mesh topology

- Every device has a direct link to every other device
- High reliability because there are many paths
- Number of links can be calculated with N(N − 1) / 2
- Often implemented as VPN tunnels over a provider network rather than physical links
- Used for small groups of critical devices

### Partial mesh topology

- Some devices have multiple links, others only one
- Not every device connects directly to every other device
- Common pattern between access and distribution switches

### Hybrid topology

- Real networks mix star, mesh, and other patterns
- Terms above describe repeated shapes in larger designs

## Campus LAN architecture

### Campus LAN definition

- Serves local users in one site or group of nearby buildings
- Can be as small as one switch or as large as a multi building campus
- Focus is on wired and wireless access for end users and local services

### Three layer hierarchy

Cisco campus designs use three logical layers:

- Access layer  
  - Where end hosts connect
  - Provides Layer 2 access and edge security
- Distribution layer  
  - Aggregates access switches
  - Connects toward WAN and internet
  - Often the Layer 2 and Layer 3 boundary
- Core layer  
  - Aggregates distribution blocks
  - Focus on fast and reliable forwarding

### Modular design

- Each access plus distribution pair can be treated as a block
- Additional blocks can be added as the site grows
- Core layer ties blocks together in larger designs

## Two tier campus LAN

### Collapsed core overview

- Two tier design uses only access and distribution layers
- Core and distribution roles are combined in distribution switches
- Also called collapsed core design
- Common in small and medium sites

### Access layer characteristics

Typical features at the access layer:

- Host connectivity for PCs, phones, printers, cameras, and access points
- Port security and other edge security controls
- DHCP snooping, Dynamic ARP Inspection, and similar protections
- QoS marking close to the source
- Power over Ethernet for phones, access points, and cameras

### Distribution layer characteristics

- Aggregates multiple access switches
- Often connects to WAN, internet, and data center
- Usually the border between Layer 2 and Layer 3
- Links down to access switches are Layer 2 trunks
- Links up to other parts of the network are Layer 3 routed ports
- Distribution switches are multilayer and run a routing protocol such as OSPF
- First hop redundancy protocol (for example HSRP) used on SVIs for default gateways

### Multiple distribution blocks

- When access switch count or port count grows, add another distribution block
- Links between distribution switches often form a full mesh
- Access to distribution links form a partial mesh
- Access switches connect to both distribution switches in the block, not to each other

## Three tier campus LAN

### When to add a core layer

- With many distribution blocks, a full mesh between them becomes complex and expensive
- Cisco guidance is to add a core layer when there are three or more distribution blocks
- Core layer reduces the number of required links and simplifies design

### Core layer characteristics

- Aggregates all distribution blocks
- Uses high performance switches
- Priority is speed and resilience
- Uses Layer 3 links to avoid Spanning Tree blocking
- Runs a routing protocol with the distribution layer
- Avoids CPU heavy features such as detailed security inspection or QoS marking
- Trusts existing QoS markings rather than remarking

## Data center networks

### Data center definition

- Central facility for servers, storage, and supporting network devices
- Can be its own site or a dedicated space in a larger building
- Often hosts application servers, databases, virtualization clusters, and storage arrays

### Traditional three tier data center

- Similar to three tier campus design
- Layers:
  - Access layer: connects servers
  - Aggregation layer: aggregates access and applies services
  - Core layer: connects aggregation blocks and upstream networks
- Access plus aggregation plus servers is often called a pod

### East west and north south traffic

- East west traffic  
  - Flows between servers inside the same data center
  - For example, between application and database servers
- North south traffic  
  - Enters or leaves the data center
  - For example, user traffic coming from WAN or internet
- Traditional three tier design can introduce extra hops for east west traffic

## Spine leaf architecture

### Spine leaf overview

- Modern data centers often use spine leaf (Clos) architecture
- Designed to give predictable latency and high bandwidth for east west traffic
- Two layers only: spine switches and leaf switches

### Spine leaf characteristics

- Servers connect only to leaf switches
- Each leaf switch connects to every spine switch
- Each spine switch connects to every leaf switch
- Leaf switches do not connect directly to other leaves
- Spine switches do not connect directly to other spines
- Leaf switches that connect to external networks are sometimes called border leaves

### Consistent latency

- Path between servers on different leaves is always:
  - Source server  
  - Source leaf  
  - Spine  
  - Destination leaf  
  - Destination server
- Same number of hops between any two leaves
- Servers on the same leaf skip the spine and have even lower latency

### Scalability

- To add more servers, add more leaf switches
- Each new leaf connects to all spines
- Spine capacity can be increased by adding spine switches and adjusting uplink count per leaf
- Design scales in a predictable way

## Small office and home office (SOHO) networks

### SOHO overview

- Very small networks, often 1 to 10 users
- Typical for homes and small businesses
- Simpler needs than enterprise or data center networks

### Wireless router functions

- Single device often provides most services:
  - Router between LAN and internet
  - Ethernet switch for wired devices
  - Wireless access point for Wi-Fi clients
  - Basic firewall functions
  - Sometimes an integrated modem
- Good enough for small sites that do not require high availability

### SOHO redundancy

- Usually only one router and one internet connection
- No redundant paths or devices
- Outages are usually an inconvenience rather than a critical event
- Enterprise networks use more complex redundant designs to avoid downtime

## Troubleshooting and design notes

- Check which layers exist at the site: two tier or three tier
- Confirm where Layer 2 stops and Layer 3 starts
- Identify star, mesh, and spine leaf patterns in diagrams
- Look for redundant links and verify that routing and FHRP settings match the design
- In data centers, consider how many hops east west traffic takes
- In SOHO, focus on the single wireless router and internet link

## Quick review

- Common physical topologies include star, full mesh, partial mesh, and hybrids.  
- Campus LANs use access, distribution, and core layers, combined into two tier or three tier designs.  
- Two tier (collapsed core) networks use access and distribution only and are common in smaller sites.  
- Distribution layer aggregates access switches, connects toward WAN or internet, and often acts as the Layer 2 and Layer 3 boundary.  
- Three tier designs add a core layer when there are several distribution blocks, improving scalability and reducing link count.  
- Data centers now often use spine leaf architecture to provide consistent latency and bandwidth for server to server traffic.  
- SOHO networks rely on a single wireless router that combines router, switch, firewall, and access point functions, with little or no redundancy.
