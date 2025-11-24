# WAN Architectures

## Overview

Wide area networks (WANs) connect geographically separated local area networks. Enterprise sites such as offices, retail stores, and data centers use WAN services to exchange data securely and reliably across cities, countries, or continents.

## WAN fundamentals

### WAN definition

- WAN is a network that extends over a large geographic area.
- Enterprises use WANs to connect their LANs at different sites.
- Examples of sites:
  - Headquarters and branch offices
  - Stores and warehouses
  - Data centers and cloud on ramps
- CCNA focuses on WANs from the customer perspective, not on internal service provider design.

### WAN purpose

- Allow hosts in one LAN to communicate with hosts in another LAN.
- Provide predictable performance and availability between sites.
- Use different access technologies depending on cost, speed, and location.

## WAN technologies

### Leased lines

- Dedicated physical connection between two sites.
- Fixed bandwidth reserved for that customer.
- Often used in hub and spoke designs with a central data center.

Characteristics:

- Consistent bandwidth because the circuit is not shared.
- Private connection that is not shared with other customers.
- Typically higher cost and lower bandwidth compared to newer options.
- Hub and spoke topologies are common because full mesh requires many circuits.

### Serial leased lines

- Traditionally implemented as serial connections rather than Ethernet.
- Different regional standards:

  - North America: T1 (1.544 Mbps), T3 (44.736 Mbps)
  - Europe and others: E1 (2.048 Mbps), E3 (34.368 Mbps)

- In many regions, serial leased lines are now considered legacy.
- Modern leased services often use Ethernet over fiber but the term leased line is still used.
- For CCNA, leased line usually refers to a dedicated serial connection.

## Multiprotocol Label Switching (MPLS)

### MPLS overview

- MPLS is a common WAN service used by providers to connect customer sites.
- Uses labels inserted between Layer 2 and Layer 3 headers.
- Labels identify a forwarding path across the provider network.
- MPLS is sometimes described as a Layer 2.5 technology.

### Multiprotocol capability

- MPLS can carry different kinds of payloads.
- In practice, it usually transports IPv4 and IPv6 packets.

### MPLS forwarding efficiency

- Edge routers add labels at the ingress of the MPLS cloud.
- Core routers forward based on labels instead of full IP lookups.
- This can simplify forwarding decisions and improve scalability.

### Shared infrastructure

- MPLS provides a shared provider network.
- Multiple customers use the same physical infrastructure.
- Logical separation is provided by label based VPNs.

### MPLS router roles

- Customer edge (CE) router  
  - Located at customer site.  
  - Connects customer network to provider network.  
  - Managed by the customer in many designs.

- Provider edge (PE) router  
  - Located at the edge of the provider network.  
  - Connects to CE routers.  
  - Adds and removes labels on customer traffic.

- Provider (P) router  
  - Internal provider router.  
  - Forwards labeled packets inside the MPLS core.  
  - Does not connect directly to customer networks.

### MPLS VPNs

- MPLS supports virtual private networks that keep customer traffic separate.
- Two main types in CCNA scope:
  - Layer 2 VPN (L2VPN)
  - Layer 3 VPN (L3VPN)

#### MPLS Layer 2 VPN (L2VPN)

- Provider network appears as a large Layer 2 switch.
- CE routers build routing adjacencies directly with each other.
- Customer routing protocols and addressing are not visible to the provider.
- Overlapping customer IP ranges are possible because VPNs are isolated.

#### MPLS Layer 3 VPN (L3VPN)

- Provider participates in Layer 3 routing.
- CE routers form routing adjacencies with PE routers.
- PE routers hold per customer routing tables using VRF instances.
- Provider backbone becomes an extension of the customer IP network.

#### Choosing L2VPN vs L3VPN

- L2VPN  
  - Customer keeps full control of routing.  
  - Provider does not see internal routes.  

- L3VPN  
  - Provider handles routing between sites.  
  - Reduces customer routing complexity but shares route information with provider.

### Access to MPLS

- CE routers connect to PE routers using different access methods:

  - Ethernet (copper or fiber)
  - Serial leased lines (legacy)
  - Wireless 3G, 4G, or 5G links for backup or remote sites

## Internet connections

### Internet overview

- The internet is a global network of networks.
- Built from many ISP networks and customer networks interconnected together.
- Provides general reachability rather than private per customer circuits.

### Internet access methods

#### Digital Subscriber Line (DSL)

- Uses existing telephone lines for data.
- Requires a DSL modem to convert Ethernet to telephone line signaling.
- Often used in SOHO environments.
- Advantage: reuse of existing copper phone wiring.

#### Cable internet

- Uses cable TV (CATV) coaxial infrastructure.
- Requires a cable modem to convert between Ethernet and CATV signaling.
- Common in residential and SOHO networks.

#### Fiber optic Ethernet

- Uses fiber optic cabling to the customer premises.
- Requires an optical network terminal or unit to convert light to electrical signals.
- Supports high bandwidth and low latency.
- Increasingly common in urban and new build areas as fiber to the home or business.

#### Wireless 3G, 4G, and 5G

- Uses cellular networks for internet access.
- Phones and routers connect to cell towers that connect into ISP networks.
- Common for mobile and temporary setups.
- 5G is increasingly used as a primary internet connection in some deployments.

## Internet connection redundancy

### Design types

- Single homed  
  - One connection to one ISP.  
  - Common in SOHO environments.  
  - No redundancy.

- Dual homed  
  - Two connections to one ISP, often via two routers.  
  - Protects against single connection or router failure.  
  - Still depends on a single ISP.

- Multi homed  
  - One connection to each of two or more ISPs.  
  - Survives an outage of a single ISP.

- Dual multi homed  
  - Two or more connections to each of two or more ISPs.  
  - Highest redundancy with the most cost and complexity.

## Internet as WAN

### Internet and WAN definition

- WAN definition: network that covers a large geographic area.
- By this definition, the internet is a WAN.
- In enterprise design, WAN usually refers to a private network that connects an organization’s sites.
- Internet is public, so extra mechanisms are needed to create secure private connectivity.

### VPN requirement

- Plain internet connectivity does not provide privacy between sites.
- Virtual private networks are used to create secure tunnels over the internet.
- Main categories:
  - Site to site VPN
  - Remote access VPN

## Virtual private networks (VPNs)

### Site to site VPN

- VPN between two routers or firewalls.
- Typically always on and used to connect entire sites.
- Common protocol: IPsec.
- Creates an encrypted tunnel across the public network.

### Tunneling concept

- Original IP packet is encrypted and encapsulated inside a new IP packet.
- Outer IP header addresses the other end of the tunnel.
- Inner IP header addresses the actual destination host.
- The tunnel is logical; traffic still traverses the same physical internet paths.

### IPsec overview and limits

- IPsec is a suite of protocols that provide encryption, integrity, and authentication.
- Used widely for site to site VPNs.
- In tunnel mode, encrypts the original IP packet and adds a new IP header.
- IPsec protects unicast traffic and does not directly support multicast or broadcast.

### GRE and GRE over IPsec

- Generic Routing Encapsulation (GRE) encapsulates packets to form tunnels.
- GRE supports unicast, multicast, and broadcast traffic.
- GRE alone does not encrypt traffic.
- GRE over IPsec combines:
  - GRE for flexibility and multicast support.
  - IPsec for encryption and security.
- Result is a secure tunnel that can carry routing protocols and other multicast traffic.

### Dynamic Multipoint VPN (DMVPN)

- Cisco technology that simplifies large VPN topologies.
- Uses a hub and spoke configuration to dynamically build additional tunnels.
- Hub router distributes information so spokes can form direct IPsec tunnels to each other.
- Provides full mesh connectivity without manual configuration of every tunnel.
- Default tunnels are GRE based and can be protected with IPsec for security.

### Full mesh and hub and spoke

- Full mesh  
  - Every site has a direct tunnel to every other site.  
  - Provides better redundancy and lower latency.  

- Hub and spoke  
  - All site to site traffic passes through a central hub.  
  - Simplifies policy enforcement and inspection at the hub.  

Design choice depends on redundancy, latency, and security requirements.

### Remote access VPN

- Per host VPN connections from end user devices to a central firewall or VPN gateway.
- Each device has its own tunnel.
- Common protocol: TLS with an installed VPN client.
- Often used for remote work so users can reach internal resources from the internet.

### TLS role

- TLS secures connections for HTTPS and many remote access VPN solutions.
- In HTTPS, TLS protects web traffic between client and web server.
- In remote access VPNs, TLS protects tunnel traffic between client and VPN gateway.

## Troubleshooting pointers

Common WAN and VPN issues:

- WAN connectivity
  - Interface down or line protocol down
  - Provider circuit issues
  - Duplex or speed mismatches

- Routing problems
  - Missing routes
  - Incorrect default gateway
  - Asymmetric routing through redundant links

- VPN problems
  - IPsec phase 1 or phase 2 not established
  - Mismatched policies or keys
  - GRE tunnel interfaces down

Useful IOS commands:

```cisco
show interfaces
show ip route
show ip interface brief
show crypto isakmp sa
show crypto ipsec sa
```

## Quick review

- WANs connect multiple LANs across large geographic areas using leased lines, MPLS, and internet based connectivity.  
- Leased lines provide dedicated point to point circuits with predictable bandwidth at higher cost.  
- MPLS provides shared infrastructure with label based forwarding and supports L2 and L3 VPNs using CE, PE, and P router roles.  
- Internet access for enterprises uses technologies such as DSL, cable, fiber, and cellular, often with redundant designs.  
- The internet can act as the transport for an enterprise WAN when combined with VPN technologies.  
- Site to site VPNs often use IPsec, with GRE over IPsec enabling multicast and routing protocol support.  
- DMVPN reduces configuration effort for large VPN topologies by dynamically building IPsec tunnels.  
- Remote access VPNs allow individual devices to connect securely over the internet, typically protected by TLS.  
