# WAN Architectures

## Overview

In the previous chapter, we covered local area networks (LANs) of various types and scales, from SOHO networks, to two- and three-tier campus LANs and even specialized data center networks that are essential for hosting an enterprise's key servers. But LANs are just one piece of the puzzle; most enterprise networks are not confined to a single physical location. Take, for example, a multinational corporation that has its headquarters in New York, manufacturing facilities in China, and regional offices scattered across Europe. Each of these locations will have its own local network, tailored for its specific needs. But these dispersed networks need to function as a unified whole, communicating and sharing resources securely and efficiently. Similarly, consider a retail chain with hundreds of stores, each with its own point-of-sale system, security cameras, guest Wi-Fi, and other network-connected devices. These stores also need to be integrated into a centralized system for inventory management, security monitoring, and data analytics. How can all of these geographically diverse LANs be connected to form a coherent whole? What role does the public internet play in all of this?

## WAN Fundamentals

### WAN Definition

- WAN is network that extends over large geographic area, often spanning distances between cities or even countries
- Enterprises use WANs to connect their various LANs
- Whether they are offices, retail stores, data centers, or any other kind of LAN
- Enterprises of all kinds use WANs
- Enterprise WAN connecting multiple LANs via service provider network infrastructure
- Figure represents WAN service provider network as gray box
- CCNA covers WANs from perspective of customer (enterprise connecting their LANs over WAN), not service provider
- If you're interested in details of how service provider networks work, consider CCNP Service Provider certification in future

### WAN Purpose

- Using WAN, hosts in one LAN can communicate with hosts in another LAN
- Example: end-user devices in office LANs can access files and applications hosted on servers in data center
- There are various WAN technologies that make this possible

## WAN Technologies

### Leased Lines

- Leased line is dedicated physical connection between two sites
- Providing fixed bandwidth that is reserved for that specific connection
- Four leased lines providing dedicated connections between each of four office sites and central data center in hub-and-spoke topology
- As mentioned in previous chapter, star and hub-and-spoke both refer to topology in which all devices connect to one central device
- Star is commonly used in LAN context, and hub-and-spoke in WAN context

### Leased Line Characteristics

- Because connection is typically not shared with other customers, available bandwidth is consistent
- Connection won't get clogged up with other customers' traffic
- Dedicated nature of leased line also provides security benefits—it's truly private connection
- However, leased lines have their downsides compared to more modern solutions: higher cost and lower bandwidth
- Due to their price, hub-and-spoke topologies are more common than mesh topologies
- Hub-and-spoke topology shown requires 4 leased lines, whereas full mesh would require 10
- Considering that each leased line can cost hundreds or even thousands of dollars per month, full mesh can often be cost prohibitive

### Serial Leased Lines

- Traditionally, leased lines use serial connections, not Ethernet
- Briefly mentioned serial connections when covering OSPF point-to-point network type
- Different standards of serial leased lines exist:
  - **North America**: T1 (1.544 Mbps), T2 (6.312 Mbps), T3 (44.736 Mbps), T4 (274.176 Mbps), T5 (400.352 Mbps)
  - **Europe (and others)**: E1 (2.048 Mbps), E2 (8.448 Mbps), E3 (34.368 Mbps), E4 (139.264 Mbps), E5 (565.148 Mbps)
- In many countries, leased lines are considered legacy technology and have been largely replaced by Ethernet connections
- However, leased lines can still be found in networks all over world
- These days, term leased line can be used more broadly to refer to any dedicated connection, such as fiber-optic Ethernet connection
- But from CCNA perspective, leased line is specifically dedicated serial connection

## Multiprotocol Label Switching (MPLS)

### MPLS Overview

- As you're well aware by now, routers forward packets based on their destination IP address
- However, that isn't always case
- Multiprotocol Label Switching (MPLS) is common WAN technology that uses labels (not IP addresses) to route packets to their destination
- MPLS label is additional header that is added to message by router at edge of MPLS network
- Typically, router belonging to WAN service provider
- MPLS label is inserted between Layer 2 and Layer 3 headers
- Due to label's position between Layer 2 and Layer 3 headers, MPLS is often called Layer 2.5 protocol

### MPLS Multiprotocol

- Multiprotocol refers to fact that MPLS can encapsulate variety of packet types—not just IP packets
- However, in modern networks, MPLS usually carries IP (IPv4 or IPv6) packets

### MPLS Efficiency

- MPLS labels offer more efficient way to route packets through network, reducing burden on routers
- Instead of examining entire packet header and performing lookup in routing table for each hop
- Routers simply read fixed-length MPLS label and forward packet based on predetermined path

### MPLS Shared Infrastructure

- Service provider's MPLS network with four connected LANs belonging to two separate customers
- This is important point about MPLS: as opposed to leased line, which provides dedicated connection between two sites
- Service provider's MPLS network is shared infrastructure over which multiple customers can connect

### MPLS Router Roles

There are three main roles that routers can play in MPLS WAN:

- **CE router**: Router located at customer's premises that connects customer's network to service provider's network. This is typically under control of customer, not service provider
- **PE router**: Router located at edge of service provider's network that connects to customer's network. PE routers are responsible for assigning and removing labels to/from customer's packets
- **P router**: Router that is internal to service provider's network. Router doesn't connect to customer's network directly but is responsible for forwarding labeled packets across service provider's network

### MPLS VPNs

- Although customers connect to same MPLS infrastructure, MPLS labels offer secure way to segregate traffic of each customer through virtual private networks (VPNs)
- By assigning unique labels to different customer data streams, MPLS ensures that each customer's traffic is kept separate and isolated within their own VPN
- Despite sharing same MPLS infrastructure
- Let's look at two types of MPLS VPNs: L2VPN and L3VPN

### MPLS Layer 2 VPN (L2VPN)

- In MPLS Layer 2 VPN (L2VPN), service provider network is transparent to CE routers
- In effect, service provider network functions like giant switch, forwarding frames between each customer's CE routers (hence "Layer 2" in name)
- Two customers connect their remote sites using service provider's MPLS L2VPN service
- To exchange routing information, each customer's routers form dynamic routing protocol neighbor relationships with each other over MPLS infrastructure
- In example, Customer A uses OSPF to exchange routing information between its Site 1 and Site 2 routers
- And Customer B uses EIGRP between its routers
- Service provider network functions like switch, forwarding OSPF/EIGRP messages between routers
- Customers can use private IP addresses for their connections
- Service provider's MPLS infrastructure isn't internet—public addresses aren't necessary
- Both customers can use same subnet for their connection
- This isn't problem; it doesn't matter if they overlap
- Although they connect to shared MPLS infrastructure, each VPN functions as isolated, private network

### MPLS Layer 3 VPN (L3VPN)

- MPLS Layer 3 VPNs (L3VPN) take different approach from L2VPNs
- Instead of service provider network acting like giant switch connecting CE routers
- Service provider routers actively participate in routing process
- PE routers form dynamic routing protocol relationships with CE routers
- Two customers connect their remote sites using service provider's MPLS L3VPN service
- CE routers form dynamic routing protocol neighbor relationships with PE routers
- As in L2VPN example, customers use overlapping private addresses in this example
- This is not problem; customer networks are isolated from each other despite connecting to same MPLS infrastructure

### MPLS L3VPN VRF

- In MPLS L3VPNs, service provider routers (specifically, PE routers) maintain separate routing table for each customer
- Ensuring traffic separation and security
- This is achieved using Virtual Routing and Forwarding (VRF)—topic we'll cover in next chapter
- Customer's CE routers and service provider's PE routers establish routing protocol adjacencies
- Allowing for exchange of routing information
- As result, underlying infrastructure of service provider becomes extension of customer's IP network
- Offloading some of routing complexities to service provider

### MPLS Service Selection

- Appropriate MPLS service—L2VPN or L3VPN—depends on needs and preferences of each customer
- If customer wants to maintain complete control over their routing policies, L2VPN is likely better choice
- Example: security policy might dictate that routing must be strictly controlled
- And information about internal networks should not be advertised to service provider routers
- If customer is comfortable with letting service provider participate in routing process (and sharing routing information with service provider), L3VPN might be appropriate

### MPLS Connection Options

- MPLS is technology used by WAN service providers to enable customers to connect their remote sites
- But how can customers connect their devices (CE routers) to service provider's MPLS infrastructure (PE routers)?
- There are various options:
  - **Ethernet**: This is most common option, as Ethernet supports high speeds and long distances (especially fiber-optic Ethernet)
  - **Leased line**: Serial leased line can be used to connect CE and PE routers
  - **Wireless (cellular 3G/4G/5G networks)**: This option is convenient for temporary setups, mobile operations, and remote locations where wired access is impractical

## Internet Connections

### Internet Overview

- Internet is vast, interconnected "network of networks" that spans globe
- Enabling exchange of information among billions of devices
- It is foundational infrastructure that supports countless applications and services
- Such as email, web browsing, and streaming
- Internet is network of networks—thousands of ISP networks and customer networks connected to share resources

### Internet Perspective

- Internet has become so ubiquitous in most of our lives that we take it for granted
- Details of how it works—inner workings of ISP networks—are beyond scope of CCNA exam
- However, understanding internet from perspective of ISP's customers (enterprise or consumer connected to internet) is essential
- Just as there are numerous ways to connect to service provider's MPLS infrastructure
- Multiple methods exist for customer to connect to their ISP's internet infrastructure

## Internet Connection Methods

### Digital Subscriber Line (DSL)

- Digital subscriber line (DSL) is technology that transmits digital data over standard telephone lines
- Common method of connecting to internet
- DSL modem (modulator-demodulator) is required to convert data into format suitable to be sent over phone lines
- Modem might be separate device, or it might be incorporated into wireless home router
- SOHO network connecting to internet via DSL
- DSL modem translates between Ethernet and signaling used on telephone lines
- Splitter is used to allow both telephone and modem to connect to single phone line
- Splitter is also called DSL filter, as it serves to filter DSL and telephone signals to prevent interference between them
- While it's older technology, DSL is still prevalent in many areas, especially in SOHO networks
- One major advantage of DSL is that it uses existing telephone lines
- So customers can connect without need to install new cabling to their premises

### Cable Internet

- Cable internet, also called cable TV (CATV) internet, is similar to DSL in that it takes advantage of preexisting infrastructure
- Cable TV lines that already connect to many homes—to connect to internet
- As with DSL, modem is required to translate between Ethernet and signaling used on CATV lines
- SOHO network connecting to internet via same CATV line used for television
- Cable modem translates between Ethernet and signaling used on CATV lines
- Splitter is used to allow both TV and modem to connect to single CATV line

### Fiber-Optic Ethernet

- Another option for internet connectivity that is gaining in popularity is fiber-optic Ethernet
- Unlike DSL and cable internet, which use existing telephone and CATV lines
- Fiber-optic connections require installation of fiber-optic cables to customer's premises
- Furthermore, device called optical network terminal (ONT) or optical network unit (ONU) is typically needed
- To convert light signals from fiber into electrical signals used by copper UTP cables
- SOHO network connecting to internet via fiber-optic Ethernet
- ONT/ONU converts between light and electrical signals
- While installation of fiber-optic cables might seem like drawback due to initial investment required
- Benefits are significant; fiber-optic connections offer much higher speeds than DSL or CATV
- As demand for high-speed internet continues to grow, fiber-optic Ethernet is increasingly popular in both SOHO and enterprise networks
- In urban areas and new residential developments, fiber is quickly becoming standard
- With many ISPs offering fiber-to-the-home (FTTH) services

### Wireless 3G/4G/5G

- Final option we'll cover is wireless 3G, 4G, and 5G
- These stand for third, fourth, and fifth generation, respectively
- If you have mobile phone with data plan, it likely supports one or more of these technologies for mobile internet access
- You might have heard of Long-Term Evolution (LTE) as well
- LTE is considered part of 4G family of standards
- While initially LTE did not meet strictest definitions of 4G
- Advancements in LTE technology have led to its widespread acceptance as 4G standard
- So terms are sometimes used interchangeably
- Wireless 3G/4G/5G internet access
- Devices wirelessly connect to cell tower, which connects to ISP infrastructure
- Typical setup where mobile phones connect to internet via cell tower
- Which then connects to ISP
- Also shows another use case for these technologies: router with appropriate radio can connect to internet in same manner
- Providing internet access for devices in its connected LAN
- 3G and 4G are rarely used as LAN's primary internet connection
- They are more common for temporary setups, mobile operations, remote locations, or as backup connection
- However, more recently, newer 5G standard has gained prominence as primary internet connection in many networks

## Internet Connection Redundancy

### Redundancy Overview

- In many SOHO networks, temporarily losing access to internet might be annoying and inconvenient
- But it probably wouldn't be catastrophe
- However, this is not case for larger enterprises
- For which even short outage can have major negative effects in terms of reputation and revenue
- In such networks, it is essential to have redundant internet connections
- Internet connection designs, from single-homed (no redundancy) to dual multi-homed (high redundancy)

### Single-Homed Design

- In single-homed design, there is one connection to one ISP
- This is common in SOHO networks
- If you have internet access at home, it's probably using single-homed design

### Dual-Homed Design

- Simple way to improve redundancy of such design is to add second connection to same ISP
- If there is problem with one connection, other can be used instead
- This is called dual-homed design
- Dual-homed design shows two routers, each with one connection to ISP
- Another option is to have two connections from single router
- However, dual-router design provides better redundancy
- If hardware failure causes one router to go down, other one is still available
- Although dual-homed design provides superior redundancy to single-homed design
- It still relies on single ISP
- If that ISP has issues, both connections may be affected

### Multi-Homed Design

- To avoid such situations, can employ multi-homed design
- Which has one connection to each of two (or possibly more) ISPs
- If one ISP has issues, network can still operate via other ISP's connection

### Dual Multi-Homed Design

- For most enterprises, multi-homed design provides sufficient redundancy
- However, networks for which continuous internet connectivity is absolutely critical may opt for dual multi-homed design
- Two connections to each of two (or more) ISPs
- This provides highest level of redundancy
- Just as redundancy increases in order we examined these designs (single-homed, dual-homed, multi-homed, dual multi-homed)
- So do cost and complexity
- Although dual multi-homed design provides highest redundancy
- Its higher cost and complexity mean that it is not always best choice

## Internet as WAN

### Internet WAN Question

- So far, we've covered couple of WAN technologies (leased lines and MPLS) and different types of internet connections
- You might be wondering: "Is internet a WAN?"
- Answer to that question is "both yes and no"

### Internet WAN Definition

- Definition of WAN given earlier in this chapter is "network that extends over large geographic area"
- In that sense, internet absolutely is WAN—it extends across entire globe
- However, term WAN is typically used in context of private network that connects remote sites (branch offices, data centers, etc.) of specific organization

### Internet Security

- While internet can serve that purpose, its public nature goes against private aspect of most WANs
- Although you can connect remote sites over internet, additional steps are necessary to keep communications secure: should use VPNs
- Just as MPLS can create VPNs over shared infrastructure
- There are multiple techniques to create VPNs over public internet

## Virtual Private Networks (VPNs)

### VPN Types

- Site-to-site VPN: Common protocol is IPsec. Use case is permanent connection between two sites. Serves many hosts within connected sites
- Remote access VPN: Common protocol is TLS. Use case is on-demand access to enterprise resources. Serves one host with VPN client installed

### Site-to-Site VPN

- Site-to-site VPN is VPN between two devices for purpose of (as name suggests) connecting two sites over non-private network (such as internet)
- Most common protocol used for site-to-site VPNs is Internet Protocol Security (IPsec)
- Which creates secure VPN tunnel—virtual pathway—between two devices
- Allowing for secure, private communications over public internet
- Site-to-site IPsec VPN provides secure virtual pathway between two sites
- Traffic is encrypted only when sent over internet

### Tunneling Concept

- Although message is shown going through IPsec tunnel, keep in mind that bits still physically pass through internet connection
- Tunnel is virtual pathway, but it doesn't create new physical path for bits to travel over
- Concept of tunneling can be hard to wrap your head around at first
- Basically, it's process of encapsulating packet inside of another packet
- Tunnel is created by encapsulating packet inside of another packet
- Outer packet provides "tunnel" for inner packet to travel through without being exposed to internet
- Process:
  1. R1 receives packet destined for SRV1
  2. R1 encrypts packet, concealing both its intended destination and its contents
  3. R1 encapsulates that encrypted packet inside of another packet that is destined for R2
  4. R1 forwards that packet over internet toward R2
  5. R2 receives packet and de-encapsulates it, revealing encrypted packet inside
  6. R2 decrypts internal packet
  7. R2 forwards decrypted packet to its intended destination, SRV1

### IPsec Encapsulation

- Tunneling IP packet with IPsec
- IP packet is encrypted, encapsulated with IPsec header and new IP header, and then forwarded
- Site-to-site VPN tunnel is permanent virtual connection between two devices
- It remains until you remove relevant configurations
- Tunnel allows hosts in remote sites to communicate with each other without need to create VPN for themselves
- Hosts can send unencrypted data to their site's router
- Which will encrypt data and forward it through tunnel to remote site
- Thanks to cryptographic technologies employed by IPsec, only two routers that have formed tunnel—R1 and R2, in our example—can decrypt packets encrypted by each other
- Only R2 can decrypt R1's encrypted packets, and only R1 can decrypt R2's encrypted packets

### IPsec Protocol Suite

- IPsec is actually suite of protocols, rather than single protocol
- There is some variability in how IPsec works depending on which protocols (and which operational mode) are used
- But those details are beyond scope of CCNA exam

### IPsec Limitations

- IPsec on its own has some limitations
- One of those limitations is that it doesn't support broadcast and multicast traffic—only unicast
- This limitation can affect routing protocols like OSPF
- Which rely on multicast messages (sent to multicast addresses 224.0.0.5 and 224.0.0.6)

### Generic Routing Encapsulation (GRE)

- One solution to this limitation is to combine IPsec with another tunneling protocol called Generic Routing Encapsulation (GRE)
- Like IPsec, GRE tunnels packets by encapsulating them with additional headers
- However, GRE does not encrypt original packet, so it is not secure
- Attacker who gets access to message traveling in GRE tunnel can read message's contents
- However, GRE has advantage of supporting broadcast and multicast messages

### GRE over IPsec

- To take advantage of both flexibility of GRE and security of IPsec, can use GRE over IPsec
- This does add some extra complexity, but it's common solution if you need to send multicast packets (i.e., OSPF messages to exchange routing information) over tunnel
- GRE over IPsec works by encapsulating IP packet with GRE and IP headers
- Encrypting GRE packet, and encapsulating encrypted packet with IPsec and IP headers
- Yes, this means that there are three IP headers in total:
  - Original IP packet's header
  - IP header added by GRE
  - IP header added by IPsec
- Interior packet might be unicast, broadcast, or multicast
- But GRE packet itself is always unicast; it's always destined for router at other end of tunnel
- This means that GRE can always be encapsulated by IPsec
- GRE over IPsec creates tunnel within tunnel
- Original IP packet travels in GRE tunnel, which is contained in IPsec tunnel
- This combines flexibility of GRE with security of IPsec

### Dynamic Multipoint VPN (DMVPN)

- Second downside of IPsec is that it can be labor intensive to configure and manage IPsec tunnels
- Especially with large number of routers
- Each time you add new branch or location to your network
- Have to set up individual VPN tunnels between that new location and all other existing locations
- Leading to substantial increase in configuration complexity
- And increased likelihood of configuration errors
- Dynamic Multipoint VPN (DMVPN), developed by Cisco, is solution that facilitates creation of full mesh of tunnels between routers
- With DMVPN, you only have to configure hub-and-spoke topology of tunnels
- DMVPN will do rest to create full mesh
- DMVPN automatically creates full mesh of IPsec tunnels after configuring hub-and-spoke topology
- DMVPN doesn't have to use IPsec; it uses unencrypted GRE tunnels by default
- However, IPsec is recommended for secure, encrypted VPN tunnels over internet
- Unencrypted GRE tunnels are not secure
- DMVPN hub router distributes information to each spoke router about how to form IPsec tunnels with other routers
- This allows routers to create full mesh of IPsec tunnels without requiring manual configuration of each tunnel

### Full Mesh vs Hub-and-Spoke

- Full-mesh topology provides couple of key advantages
- First is redundancy; if failure causes one tunnel to go down, other tunnels can be used to reach destination
- Second is reduced latency
- Because routers in each site can communicate directly with each other
- Latency is reduced compared to hub-and-spoke topology (in which traffic between spoke routers must pass through hub router)
- However, hub-and-spoke topology has its advantages, too
- Because all traffic between two sites has to pass through hub site
- It's easy to implement restrictions on those communications (for example, with firewall at hub site)
- Despite advantages of full-mesh, security requirements may dictate that hub-and-spoke topology is appropriate

### Remote Access VPN

- Site-to-site VPN is permanent virtual connection between two routers
- Providing secure encrypted communication pathway for hosts connected to each router
- Remote access VPN, on other hand, is on-demand VPN that allows end user to securely access company's internal resources over internet
- Protocol of choice is typically Transport Layer Security (TLS), but IPsec is also option
- Remote access TLS VPNs provide secure access to company's internal resources over internet

### Remote Access VPN Characteristics

- Unlike site-to-site VPN, which provides virtual pathway for multiple hosts connected to routers that establish VPN
- Remote access VPN establishes VPN connection from each individual end-user device to company's firewall or router
- This means that while multiple devices can simultaneously connect via remote access VPN
- Each device has its own encrypted tunnel that is not shared with other devices
- End-user device runs piece of software called VPN client
- Cisco's offering is called Cisco AnyConnect Secure Mobility Client (usually just "AnyConnect")
- But other vendors have their own offerings
- This software allows device to create its own tunnel to company's firewall or router
- Providing secure communication pathway to reach resources on company's internal network (i.e., file servers)
- Remote access VPNs are particularly useful in remote work situations, which have become increasingly common

### TLS Protocol

- TLS, commonly used for remote access VPNs, is also protocol that secures Hypertext Transfer Protocol Secure (HTTPS)
- Which is used to securely access web pages
- Whereas remote access VPN creates TLS VPN tunnel between your device and firewall/router
- HTTPS creates TLS VPN tunnel between your device and web server that hosts web page you are accessing
- For exam, know that remote access VPN allows single device to securely access internal resources through TLS tunnel
- Details of TLS protocol itself are beyond scope of CCNA

## Real-World Applications

- **Enterprise connectivity**: Connecting remote offices and data centers
- **Retail networks**: Integrating point-of-sale systems across multiple locations
- **Remote work**: Providing secure access to corporate resources
- **Disaster recovery**: Maintaining connectivity during outages
- **Cost optimization**: Balancing performance and cost

## Troubleshooting

### Common Issues

- **Connectivity problems**: Verify WAN connection and routing configuration
- **VPN tunnel failures**: Check IPsec/GRE configuration and authentication
- **Performance issues**: Monitor bandwidth utilization and latency
- **Redundancy failures**: Verify failover mechanisms

### Troubleshooting Steps

1. Verify WAN connection: Check physical connectivity and link status
2. Test routing: Verify routing protocols and default routes
3. Check VPN tunnels: Verify tunnel status and encryption
4. Monitor performance: Check bandwidth and latency metrics
5. Test redundancy: Verify failover mechanisms

## Best Practices

- Choose appropriate WAN technology based on requirements
- Implement redundant connections for critical sites
- Use VPNs for secure connectivity over internet
- Monitor WAN performance and utilization
- Document WAN architecture and configurations
- Plan for scalability and growth
- Test failover and redundancy mechanisms
- Consider cost vs. performance tradeoffs

## Summary

- Wide area network (WAN) is network that extends over large geographic area, often spanning distances between cities or even countries
- Enterprises use WANs to connect their various LANs
- Leased line is dedicated physical connection between two sites, providing fixed bandwidth that is reserved for that specific connection
- Leased lines are secure because they are private; they are not shared with other customers
- However, they are typically more expensive and offer lower bandwidth than more modern solutions
- Leased lines traditionally use serial connections, not Ethernet
- However, service providers sometimes offer fiber-optic Ethernet leased lines
- Multiprotocol Label Switching (MPLS) is common WAN technology that uses labels (not IP addresses) to route packets to their destination
- MPLS label is additional header that is added between Layer 2 and Layer 3 headers of message
- Unlike leased line, service provider's MPLS network is shared infrastructure over which multiple customers can connect
- There are three main roles that routers can play in MPLS WAN: customer edge (CE), provider edge (PE), and provider (P)
- CE router is located at customer's premises and connects customer's network to service provider's network
- It is typically under control of customer, not service provider
- PE router is located at edge of service provider's network and connects to customer's network
- PE routers are responsible for assigning and removing labels to/from customer's packets
- P router is internal to service provider's network and doesn't connect to customer's network directly
- P routers are responsible for forwarding labeled packets across service provider's network
- Although customers connect to same MPLS infrastructure, MPLS labels offer secure way to segregate traffic of each customer through virtual private networks (VPNs)
- There are two main types of MPLS VPNs: L2VPN and L3VPN
- In MPLS Layer 2 VPN (L2VPN), service provider network is transparent to CE routers
- In effect, service provider network functions like giant switch, forwarding frames between each customer's CE routers
- To exchange routing information, CE routers form dynamic routing protocol neighbor relationships with each other over MPLS infrastructure
- In MPLS Layer 3 VPN (L3VPN), service provider routers actively participate in routing process
- PE routers form dynamic routing protocol neighbor relationships with CE routers
- In both cases (L2VPNs and L3VPNs), MPLS is underlying technology that enables VPN, although implementation is different
- Internet is vast, interconnected "network of networks" that spans globe, connecting thousands of internet service providers (ISPs) and their customers
- There are various methods for connecting to ISP
- Digital subscriber line (DSL) is technology that transmits digital data over standard telephone lines and is common method of connecting to internet
- DSL modem (modulator-demodulator) is required to convert data into format suitable to be sent over phone lines
- Modem might be separate device, or it might be incorporated into wireless home router
- One major advantage of DSL is that it uses existing telephone lines, so customers can connect to internet without need to install new cabling
- Cable internet is similar to DSL in that it takes advantage of preexisting infrastructure: cable TV lines that already connect to many homes
- Just as DSL uses modem, cable modem is required to translate between Ethernet and signaling used on CATV lines
- Fiber-optic Ethernet connections are another common internet connection method
- Unlike DSL and cable internet, which use existing telephone and CATV lines, fiber-optic connections require installation of fiber-optic cables
- Furthermore, device called optical network terminal (ONT) or optical network unit (ONU) is typically needed to convert light signals from fiber into electrical signals used by copper UTP cables
- As demand for high-speed internet grows, fiber-optic Ethernet is increasingly common internet connection method in both SOHO and enterprise networks
- Another option is wireless 3G, 4G/LTE (Long-Term Evolution), and 5G; these stand for third, fourth, and fifth generation, respectively
- Mobile phones often use 3G/4G/5G for internet access
- Router with appropriate radio can also use these technologies to connect to internet
- Redundant internet connections are imperative for enterprises that rely on continuous internet connectivity
- Single-homed internet connect design involves one connection to one ISP
- This does not provide redundancy but is common in SOHO networks
- Dual-homed design involves two connections to one ISP; this adds some redundancy but is still vulnerable to issues that affect ISP as whole
- Multi-homed design involves one connection to each of two (or more) ISPs, providing resilience to issues that affect one of ISPs
- Dual multi-homed design involves two connections to each of two (or more) ISPs
- This provides highest level of redundancy but is not necessary for most networks
- Is internet a WAN? Yes and no
- Internet is WAN in that it extends over large geographic area—entire globe
- However, term WAN is typically used in context of private network that connects organization's sites
- Public nature of internet makes it inappropriate for WAN connections without additional security measures: should use VPNs
- Site-to-site VPN is VPN between two devices (routers) for purpose of connecting two sites over non-private network (such as internet)
- Most common protocol used for site-to-site VPNs is Internet Protocol Security (IPsec)
- Which creates secure VPN tunnel—virtual pathway—between two devices, allowing for secure, private communications over public internet
- Tunneling involves encapsulating packet inside of another packet
- Outer packet provides tunnel for inner packet to travel through without being exposed to internet
- IPsec encrypts original packet before encapsulating it with IPsec header and new IP header
- IPsec only supports unicast traffic
- To support broadcast and multicast traffic, can combine IPsec with Generic Routing Encapsulation (GRE)
- GRE creates tunnels that support various kinds of traffic but doesn't encrypt contents
- By combining GRE with IPsec, take advantage of GRE's flexibility and IPsec's security; this is called GRE over IPsec
- Configuring full mesh of IPsec tunnels between routers is labor intensive and prone to configuration errors
- Dynamic Multipoint VPN (DMVPN) is solution that facilitates creation of full mesh of tunnels between routers
- With DMVPN, only have to configure hub-and-spoke topology of tunnels
- Hub router will then distribute information to spoke routers, allowing them to form full mesh of tunnels with each other
- Remote access VPN is on-demand VPN that allows end user to securely access company's internal resources over internet
- Protocol of choice is typically Transport Layer Security (TLS)
- Remote access VPN establishes VPN connection from each individual end-user device to company's firewall or router
- While multiple devices can simultaneously connect, each device has its own encrypted tunnel that is not shared
- End-user device runs piece of software called VPN client
- Cisco's offering is called Cisco AnyConnect Secure Mobility Client, or just AnyConnect
- This software allows device to create its own tunnel to company's firewall or router
