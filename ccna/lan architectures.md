# LAN Architectures

## Overview

We have delved into the details of protocols like IPv4 and IPv6, Ethernet, Spanning Tree Protocol, and many others in previous chapters. Now it's time to zoom out. Instead of focusing on individual technologies, let's take a holistic view of real-world network architectures—the blueprints for how computer networks are designed and built. Although there are standard best practices in network design, many factors such as budget, scale, and specific needs influence the "right" approach; there are few universal correct answers to questions of network design. In the beginning stages of your networking career, you probably won't be designing networks. However, to configure and troubleshoot networks, understanding the architectural principles behind them is essential.

## Network Topologies

### Topology Definition

- Topology is how devices are arranged and connected together in network
- Some common topologies consistently emerge across different networks
- Common patterns of device connections

### Star Topology

- In star topology, all devices connect to one central device
- Most common example of star topology is group of end hosts connected to switch
- Another name for star topology is hub-and-spoke topology
- Central device is hub, and devices connecting to it are spokes
- Star is more commonly used in LAN context
- Hub-and-spoke in WAN context

### Full Mesh Topology

- In full mesh, each device in topology is directly connected to each of other devices
- Full-mesh topologies provide high reliability because there are multiple possible paths to each destination
- If there is problem with one path, multiple other paths are available
- Can calculate number of connections between devices in full mesh with formula N(N-1)/2, where N is number of devices
- Example: with six devices, there are 15 links
- Although they appear as direct connections, in reality, these would likely be secure virtual private network (VPN) connections over service provider's network

### Partial Mesh Topology

- There is also partial mesh, in which certain devices, but not all, are directly connected to each other
- You'll see this pattern between switches in access layer and distribution layer of campus LAN

### Hybrid Topology

- Most networks are combination of these common topologies and others—hybrid topology
- These terms are all commonly used to describe how devices are connected in networks
- Keep eye out for these recurring patterns as we examine different network architectures

## Campus LAN Architecture

### Campus LAN Definition

- Campus LAN is network that is designed to serve networking needs of local users within certain area
- Although term campus evokes idea of network spread across multiple buildings in close proximity, like university campus or office park
- In this context, it doesn't imply any particular geographic size
- Campus LAN could be small site with single switch or multibuilding campus stretching across office park

### Three-Layer Hierarchy

Cisco campus LANs use hierarchical design, dividing network into three modular layers:

- **Access layer**: Provides access to network for end hosts
- **Distribution layer**: Aggregates connections from access layer and provides connectivity to WAN and internet
- **Core layer**: Aggregates connections between distribution layers in large LANs

### Modular Design

- Cisco campus LAN architecture is not one-size-fits-all
- Depending on site, one, two, or all three layers might be present
- Layers are modular, allowing for flexible scalability
- These modular pieces are sometimes called blocks
- As network expands, additional access and/or distribution blocks can be added as needed

## Two-Tier Campus LAN

### Two-Tier Overview

- CCNA exam topics list states that you must be able to describe two- and three-tier campus LANs
- We will start small, with two-tier campus LANs
- This kind of design is also called collapsed core because core layer is absent
- Only access and distribution layers are present
- Another way to think of collapsed core is that core and distribution layers are combined into one
- For this reason, second layer of two-tier LAN is sometimes called core-distribution layer

### Access Layer

- Access layer is typically where end hosts connect to network
- That includes end-user devices like PCs and phones
- Security devices like security cameras and door locks
- Servers, and others
- Given that, here are some features you can expect to find in access layer of campus LAN:
  - QoS marking is often done here. As mentioned in chapter on QoS, marking should be done early in packet's life
  - Security services such as Port Security, DHCP Snooping, and DAI should be used here to secure point where users connect to network
  - Switches will likely support PoE to provide electrical power to devices like IP phones, wireless access points, security cameras, etc.

### Distribution Layer

- With more than two or three access switches at site, directly interconnecting them all quickly becomes impractical
- Instead, distribution switches are used to aggregate connections from access switches
- Distribution layer also typically connects to corporate WAN and/or internet
- Distribution layer usually serves as border between Layer 2 and Layer 3 of TCP/IP model
- Connections from distribution layer to access switches are Layer 2 connections (trunk links)
- But connections to other parts of network are Layer 3 connections (routed ports configured with `no switchport`)
- Distribution switches are multilayer switches that support both Layer 2 and Layer 3 features

### Distribution Layer Configuration

- To provide redundant IP address that hosts in each VLAN can use as their default gateway
- Distribution switches should use first hop redundancy protocol like HSRP on each of their SVIs
- Furthermore, routing protocol like OSPF can be used to share routing information with rest of network
- Example configuration shows how you might configure SVI of distribution switch:
  - Configure VLAN SVI
  - Configure IP address
  - Configure HSRP virtual IP
  - Increase SVI's HSRP priority
  - Enable OSPF on SVI

### Multiple Distribution Blocks

- As two-tier campus LAN expands, may need to add additional block of distribution switches
- Perhaps company is opening another office in new building
- And number of access switches is more than current distribution switches can handle
- Current switches don't have enough available ports
- Connections between distribution switches form full mesh
- And connections between access and distribution switches form partial mesh
- Access switches connect to each distribution switch but not to each other

## Three-Tier Campus LAN

### Three-Tier Overview

- Large campus LANs often face challenge of managing connectivity as they grow
- Full mesh between distribution switches might work well for smaller networks with couple of distribution blocks
- However, with three, four, or even more distribution blocks, this approach quickly escalates in complexity and cost
- In campus LAN with three or more distribution blocks, should consider adding core layer
- Making three-tier architecture
- Adding core layer can greatly reduce number of connections required
- Another option to reduce number of connections required is to use partial mesh between distribution switches instead of full mesh
- However, Cisco's recommendation is to add core when there are three or more distribution blocks

### Core Layer

- Just as distribution layer aggregates connections from access layer
- Core layer aggregates connections from distribution layer
- Using high-end switches, focus of core layer is speed and reliability
- It should forward packets as quickly as possible
- And be able to maintain consistent connectivity throughout LAN even if failures occur
- CPU-intensive operations like security features (DAI, etc.) and QoS marking, which can slow down forwarding process
- Should be avoided at core layer
- Switches in core layer should trust and forward packets based on packets' existing QoS markings
- All connections between core and distribution layers should be Layer 3 connections
- We don't want STP disabling links that could otherwise be used to forward packets
- Routing protocol like OSPF should be used to share routing information between distribution and core switches

### Three-Tier Example

- Three-tier campus LAN with core layer connecting three distribution blocks
- One distribution block is used to connect to network services like wireless LAN controller, WAN, and internet
- To avoid cluttering up diagrams, only few access switches and end hosts are shown in each diagram
- In large network, there could be 20+ access switches in each access block
- Each with 40+ end hosts connected

## Data Center Networks

### Data Center Definition

- Data center is facility—either its own building or dedicated space in building
- Where organization centralizes its IT infrastructure
- Particularly servers and network infrastructure devices that support them
- Data centers are vital for many modern enterprise networks
- Often housing thousands of servers, storage devices, and network devices

### Traditional Three-Tier Data Center

- Data center networks traditionally used three-tier architecture similar to campus LANs we saw in previous section
- Note that distribution layer is typically called aggregation layer in data center context
- Their function is basically same
- Three-tier data center LAN consists of access layer, aggregation layer, and core layer
- In data center network, each group of servers and access and aggregation switches that support them are called pod

### East-West Traffic

- Rise of virtual servers and distributed applications led to increase in amount of east-west traffic in data centers
- East-west traffic is traffic flowing between servers within same data center
- For example, communication between server in pod 1 and server in pod 3
- North-south traffic is traffic entering and exiting data center (via WAN or internet)
- Traditional three-tier architecture proved to be less than ideal for these kinds of applications
- Especially if traffic had to traverse multiple layers to reach another server in same data center
- This produces bottlenecks and variability in server-to-server latency
- Leading to unpredictability in application performance

## Spine-Leaf Architecture

### Spine-Leaf Overview

- To better serve modern data center networks, spine-leaf architecture (also called Clos architecture, named after American engineer Charles Clos) has become standard
- Spine-leaf architecture provides high bandwidth with low and predictable latency for east-west traffic
- Spine-leaf architecture consists of two layers: layer of spine switches and layer of leaf switches

### Spine-Leaf Characteristics

- End hosts (servers) connect to leaf switches
- Every leaf switch connects to every spine switch
- Every spine switch connects to every leaf switch
- Leaf switches do not connect to other leaf switches
- Spine switches do not connect to other spine switches

### Consistent Latency

- Key result of this architecture is that all leaf switches are same number of hops apart
- This means that path packet takes between two servers is always:
  - Source server
  - Leaf switch
  - Spine switch
  - Leaf switch
  - Destination server
- Consistent number of hops means that there should be consistent and predictable latency between servers in network
- One exception is when two servers are connected to same leaf switch
- In which case there is no need to traverse spine switch, making latency even shorter

### Scalability

- Another benefit of spine-leaf architecture is how simple it is to scale it to support large and complex data center networks
- If you need to add more servers than current network can handle, just add more leaf switches
- Connecting each new leaf to every spine switch
- Leaf switches that connect to WAN/internet or other external networks are sometimes called border leaves

## Small Office/Home Office (SOHO) Networks

### SOHO Overview

- In some networks, complex designs we've looked at aren't necessary
- Network with only few users, each with only few devices, can often have its needs met by single network device
- Small office/home office (SOHO) network—very small network with about 1 to 10 users—is example
- Because of their size and simplicity, it's common for all networking functions in SOHO to be provided by single wireless router (also called Wi-Fi router or home router)

### Wireless Router Functions

- Wireless router combines functions of various network devices into one:
  - Router that forwards packets between LAN and internet
  - Switch for wired end-user devices to connect to
  - Firewall that blocks connections from internet
  - Wireless access point that allows wireless (Wi-Fi) clients to connect to network
- Wireless router includes Wi-Fi antennas for wireless clients
- Switch ports for wired end-user devices
- Port for internet connection

### SOHO Redundancy

- In addition to relying on single wireless router, most SOHO networks have only one internet connection
- This lack of redundancy isn't acceptable in enterprise networks like ones we covered in previous sections
- However, given nature of most SOHO networks, temporary loss of service would be more of inconvenience than emergency
- Cost savings of nonredundant setup are usually prioritized over reliability of redundant one

## Real-World Applications

- **Campus networks**: Connecting multiple buildings in office park or university campus
- **Data center networks**: Supporting thousands of servers and storage devices
- **SOHO networks**: Providing connectivity for small businesses and home offices
- **Scalability**: Designing networks that can grow with organization
- **Redundancy**: Implementing high availability in enterprise networks
- **Cost optimization**: Balancing performance and reliability with budget constraints

## Troubleshooting

### Common Issues

- **Connectivity problems**: Verify layer boundaries and routing configuration
- **Performance issues**: Check for bottlenecks at core or distribution layers
- **Redundancy failures**: Verify FHRP and routing protocol configuration
- **Scalability problems**: Consider adding core layer or additional blocks

### Troubleshooting Steps

1. Verify layer configuration: Check access, distribution, and core layer setup
2. Check routing: Verify routing protocols and default gateways
3. Test connectivity: Ping and trace routes between layers
4. Review topology: Ensure physical connections match logical design
5. Check redundancy: Verify FHRP and failover mechanisms

## Best Practices

- Use hierarchical design with clear layer boundaries
- Implement appropriate security features at access layer
- Use FHRP for redundant default gateways
- Configure routing protocols for dynamic routing
- Avoid CPU-intensive operations at core layer
- Use Layer 3 connections at core and distribution layers
- Plan for scalability from beginning
- Document network architecture and design decisions
- Test redundancy and failover mechanisms
- Consider cost vs. performance tradeoffs

## Summary

- Although there are standard best practices in network design, many factors such as budget, scale, and specific needs influence "right" approach
- In star topology, all devices connect to one central device
- Most common example is group of end hosts connected to switch
- Another name for star topology is hub-and-spoke topology
- Star is more commonly used in LAN context, and hub-and-spoke in WAN context
- In full-mesh topology, each device in topology is directly connected to each of other devices
- Full mesh is often seen between distribution switches of two-tier campus LAN
- In partial-mesh topology, certain devices, but not all, are directly connected to each other
- Can find this pattern between access and distribution switches of two- or three-tier campus LAN
- Most networks are combination of these common topologies and others—hybrid topology
- Campus LAN is network that is designed to serve networking needs of local users within certain area
- Cisco campus LANs use hierarchical design, dividing network into three modular layers: access, distribution, and core
- Layers are modular, allowing for flexible scalability
- These modular pieces are sometimes called blocks
- Additional blocks can be added as network expands
- In two-tier campus LAN, only access and distribution layers are present
- For this reason, it's sometimes called collapsed-core architecture
- Access layer is typically where end hosts connect to network
- Some common features implemented at access layer are QoS, security services (i.e. Port Security, DHCP Snooping, and DAI), and PoE
- Distribution layer aggregates connections from access layer and also typically connects to corporate WAN and/or internet
- Distribution layer usually serves as border between Layer 2 and Layer 3 of TCP/IP model
- Connections to access switches are Layer 2 connections, but connections to other parts of network are Layer 3 connections
- Distribution switches typically use FHRP (like HSRP) on their SVIs to provide redundant default gateway to hosts in LAN
- And routing protocol like OSPF to share routing information with rest of network
- In campus LAN with three or more distribution blocks, should consider adding core layer—three-tier architecture
- Core layer aggregates connections from distribution layer, reducing overall number of connections required
- Focus of core layer is speed and reliability
- It should forward packets as quickly as possible and be able to maintain consistent connectivity throughout LAN even if failures occur
- CPU-intensive operations like security features and QoS marking, which can slow down forwarding process, should be avoided at core layer
- All connections should be Layer 3
- Data center is facility where organization centralizes its IT infrastructure, particularly servers and network infrastructure devices that support them
- Data center networks traditionally used three-tier architecture similar to campus LANs (with distribution layer being called aggregation layer in data center contexts)
- In data center network, each group of servers and access and aggregation switches that support them are called pod
- Rise of virtual servers and distributed applications led to increase in amount of east-west traffic in data centers
- East-west traffic is traffic flowing between servers within same data center
- North-south traffic is traffic entering and exiting data center (via WAN or internet)
- Traditional three-tier architecture is not ideal for east-west traffic
- It can lead to bottlenecks and variability in server-to-server latency
- Spine-leaf architecture has become standard in modern data center networks
- Spine-leaf architecture consists of two layers: layer of spine switches and layer of leaf switches
- End hosts (servers) connect to leaf switches
- Leaf switches that connect to WAN/internet or other external networks are sometimes called border leaves
- Every leaf switch connects to every spine switch, and every spine switch connects to every leaf switch
- Leaf switches do not connect to other leaf switches, and spine switches do not connect to other spine switches
- Result of this architecture is that all leaf switches are same number of hops apart
- They are all separated by one spine switch
- Consistent number of hops means that there should be consistent and predictable latency between servers in network
- Only exception is when two servers are connected to same leaf switch
- Spine-leaf architecture can be easily scaled by adding more leaf switches, connecting each new leaf to every spine switch
- Small office/home office (SOHO) network is very small network, usually with 1 to 10 users (i.e., small business or home network)
- It's common for all networking functions in SOHO network to be provided by single wireless router (also called Wi-Fi router or home router)
- Wireless router combines functions of various network devices into one: router, switch, firewall, wireless access point, and sometimes modem (modulator-demodulator)
- Most SOHO networks prioritize cost savings with single router and internet connection, trading off redundancy found in enterprise networks
