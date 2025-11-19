# Dynamic Routing

## Overview

Dynamic routing is a process by which routers share information about the network with each other, allowing them to build their routing tables automatically without manual configuration. Routers use routing protocols to exchange routing information and calculate routes. Dynamic routing provides adaptability and scalability advantages over static routing, making it essential for modern networks.

## Advantages of Dynamic Routing

### Adaptability

- Routers automatically adapt to network changes, such as link failures
- If a route becomes invalid, routers automatically calculate alternate paths
- Network resilience improves with minimal downtime
- No manual intervention required when network topology changes

### Scalability

- Dynamic routing protocols easily scale to support large and complex networks
- Manual static route configuration becomes impractical as networks grow
- Routers automatically share routing information, reducing administrative overhead
- Supports networks with dozens or hundreds of routers

### Comparison with Static Routing

- Static routes are predictable and provide control over exact paths
- Dynamic routes adapt automatically but may not always follow the exact path you want
- Both static and dynamic routing can be used together on a single router
- Static routes are useful for specific scenarios where path control is critical

## Routing Protocol Categories

### Interior Gateway Protocols (IGP)

- Used to exchange routing information within a single autonomous system (AS)
- An AS is the network of a single organization
- IGPs are used for routing within an organization's network
- Examples: RIP, EIGRP, OSPF, IS-IS

### Exterior Gateway Protocols (EGP)

- Used to exchange routing information between different autonomous systems
- Used between an enterprise and an ISP or between two ISPs
- The only EGP in common use today is Border Gateway Protocol (BGP)
- Designed for larger-scale routing between organizations

### Gateway Terminology

- Gateway is an old term for a router
- Still used in contexts like default gateway
- Modern terminology uses router, but gateway persists in some contexts

## Routing Protocol Algorithm Types

### Distance-Vector Protocols

- Routers share information about known networks and their metric to reach those networks
- Each router doesn't have a complete map of the network
- Routers only know the metric and next-hop router for each destination
- Also called "routing by rumor"
- Examples: RIP, EIGRP

#### Routing Information Protocol (RIP)

- Industry-standard distance-vector protocol
- Very simple protocol, usually only used in very small networks and labs
- Uses hop count as metric (number of routers to destination)

#### Enhanced Interior Gateway Routing Protocol (EIGRP)

- Cisco-developed advanced distance-vector protocol
- More advanced than RIP
- Sometimes called an advanced distance-vector protocol
- Most functionality released to public in RFC 7868
- Generally only runs on Cisco routers (few other vendors have implemented it)
- Uses complex metric calculation based on bandwidth and delay

### Link-State Protocols

- Each router creates a connectivity map of the network
- Routers share information about connected links and their state
- Information shared with all routers in the network, not just neighbors
- Each router uses the map to calculate best routes to each destination
- Requires more CPU and memory resources than distance-vector protocols
- Examples: OSPF, IS-IS

#### Open Shortest Path First (OSPF)

- Industry-standard link-state protocol
- Major topic on the CCNA exam
- Uses cost metric based on bandwidth
- Can divide network into areas to overcome resource limitations

#### Intermediate System to Intermediate System (IS-IS)

- Industry-standard link-state protocol
- Most commonly used in service-provider networks (ISP networks)
- Not a topic on the CCNA exam

### Path-Vector Protocols

- Border Gateway Protocol (BGP) uses path-vector algorithm
- Makes routing decisions based on series of autonomous systems
- AS-to-AS logic rather than router-to-router
- Designed for larger-scale routing between organizations

## Route Selection

### Two Meanings of Route Selection

Route selection has two main meanings:

#### Routing Table Population

- Process of selecting which routes the router will enter into its routing table
- Router uses administrative distance (AD) and metrics to select routes
- Only the best route to each destination enters the routing table

#### Packet Forwarding

- Process of selecting the best route in the routing table to forward a particular packet
- Router selects the most specific matching route (longest prefix match)
- AD and metric values are not considered during packet forwarding

### Metrics

- A metric is a measure of the efficiency of a route
- Used to compare routes to the same destination learned via the same routing protocol
- Each routing protocol calculates metrics differently:
  - **RIP**: Hop count (number of routers in path)
  - **EIGRP**: Complex formula based on bandwidth and delay (default uses bandwidth and delay)
  - **OSPF**: Cost value calculated from bandwidth of each link in path
- Lower metric values are preferable
- Metrics cannot be directly compared between different routing protocols

### Administrative Distance (AD)

- AD is a value that indicates how preferred a routing protocol is
- Lower AD value indicates a more trustworthy routing protocol
- Used to compare routes to the same destination learned via different routing protocols
- Default AD values:
  - Connected: 0
  - Static: 1
  - External BGP (eBGP): 20
  - EIGRP: 90
  - OSPF: 110
  - IS-IS: 115
  - RIP: 120
  - Internal BGP (iBGP): 200
  - Unusable route: 255

### Equal-Cost Multi-Path (ECMP)

- If multiple routes to the same destination have the same metric (and same AD), all routes are added to routing table
- Router load-balances traffic over the routes
- Traffic is distributed evenly across the equal-cost paths

### Floating Static Routes

- Static route configured with AD greater than default of 1
- Purpose is to make static route less preferred than dynamic routes
- Serves as backup route that only enters routing table if primary route fails
- Configured with: `ip route destination-network netmask next-hop ad`
- Example: `ip route 10.0.0.0 255.0.0.0 192.168.1.2 111` (AD 111 makes it less preferred than OSPF)

### Route Selection Rules

- Routes to different destinations (different network address or prefix length) are all inserted into routing table
- Routes to the same destination (same network address and prefix length) are compared using:
  - AD if learned via different protocols
  - Metric if learned via same protocol
- Most specific matching route is used for packet forwarding (longest prefix match)

## The Network Command

### Purpose

The `network` command is used by RIP, EIGRP, and OSPF to activate the routing protocol on router interfaces. The command tells the router to:

- Look for interfaces with an IP address in the specified range
- Activate the routing protocol on those interfaces
- Advertise the network prefix of the interface(s) to neighbors

### OSPF Network Command Syntax

- Enter router config mode: `router ospf process-id`
- Configure network command: `network ip-address wildcard-mask area area-id`
- Process ID is locally significant (doesn't need to match between routers)
- Can create multiple OSPF processes, but running multiple processes is extremely rare

### Wildcard Masks

- Wildcard mask looks like an inverted netmask but serves a different purpose
- A 0 bit in wildcard mask means bits must match
- A 1 bit in wildcard mask means bits don't have to match
- Used to specify a range of IP addresses (not necessarily in the same subnet)
- To calculate wildcard mask from netmask: subtract each octet from 255
- Example: /24 netmask (255.255.255.0) = wildcard mask 0.0.0.255

### Network Command Flexibility

- IP address and wildcard mask don't have to match interface's IP address and netmask
- As long as correct bits match (indicated by wildcard mask), protocol will be activated
- Recommended method: specify exact interface IP address with wildcard mask 0.0.0.0
- Shortcut for all interfaces: `network 0.0.0.0 255.255.255.255 area 0` (not recommended in production)

### Common Misconceptions

- **Misconception 1**: Wildcard mask must match interface netmask
  - **Reality**: Wildcard mask only needs to match bits indicated by 0s in the mask
- **Misconception 2**: Network command specifies which networks to advertise
  - **Reality**: Network command specifies which interfaces to activate protocol on; router then advertises those interfaces' prefixes

## Real-World Applications

- **Enterprise networks**: Dynamic routing enables automatic adaptation to network changes
- **Large-scale deployments**: Essential for networks with many routers and subnets
- **Multi-vendor environments**: Industry-standard protocols (OSPF, RIP) work across vendors
- **Service provider networks**: BGP used for routing between ISPs and enterprises
- **Redundant paths**: Automatic failover when primary paths fail
- **Load balancing**: ECMP distributes traffic across multiple equal-cost paths

## Troubleshooting Dynamic Routing

### Common Issues

- **Routes not appearing in routing table**: Check that routing protocol is activated on correct interfaces
- **Suboptimal routes**: Verify metrics and AD values are configured correctly
- **Routing loops**: Ensure consistent configuration across all routers
- **Neighbor relationships not forming**: Verify network command configuration and interface status
- **Floating static routes not working**: Ensure AD is higher than dynamic routing protocol AD

### Verification Commands

- `show ip route`: View routing table and route sources
- `show ip protocols`: View active routing protocols and their configuration
- `show ip route [protocol]`: View routes learned via specific protocol
- `show ip route [network]`: View specific route details

## Best Practices

- Use dynamic routing for networks with more than a few routers
- Configure loopback interfaces for stable router identification
- Use consistent reference bandwidth values for OSPF cost calculations
- Prefer industry-standard protocols (OSPF) for multi-vendor environments
- Use floating static routes as backup paths when needed
- Configure network commands with specific interface IPs and 0.0.0.0 wildcard mask
- Monitor routing table for unexpected route changes
- Document routing protocol choices and AD modifications

## Summary

- Dynamic routing allows routers to automatically build routing tables by sharing information
- Dynamic routing provides adaptability (automatic failover) and scalability (works in large networks)
- Routing protocols are categorized as IGPs (within AS) or EGPs (between ASes)
- Algorithm types: distance-vector (RIP, EIGRP), link-state (OSPF, IS-IS), path-vector (BGP)
- Route selection for routing table population uses AD (different protocols) and metrics (same protocol)
- Route selection for packet forwarding uses longest prefix match (most specific route)
- Metrics measure route efficiency; each protocol calculates metrics differently
- Administrative distance indicates protocol preference; lower values are more preferred
- ECMP allows load balancing across equal-cost paths
- Floating static routes provide backup paths with higher AD than dynamic routes
- Network command activates routing protocols on interfaces and advertises interface prefixes
- Wildcard masks specify IP address ranges for network command; 0 bits must match, 1 bits don't
- Recommended practice: use specific interface IPs with 0.0.0.0 wildcard mask in network commands

