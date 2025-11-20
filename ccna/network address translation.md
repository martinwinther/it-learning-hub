# Network Address Translation

## Overview

IPv4 address exhaustion is a major problem and has been for a long time. IPv6 is the long-term solution, but IPv4 is still dominant to this day thanks to a few solutions that have been very effective in extending IPv4's lifespan. One solution is subnetting with Classless Inter-Domain Routing (CIDR), which allows more flexibility than the rigid classful addressing system. Two more important solutions that, combined, have proven essential in preserving the IPv4 address space are private IPv4 addressing and Network Address Translation (NAT). Three ranges of IPv4 addresses have been reserved for free use in private networks without the need to be globally unique, and NAT provides a way to translate those private addresses into public addresses for communication over the internet.

## Private IPv4 Addresses

### RFC 1918 Address Ranges

- Private IPv4 addresses are IPv4 addresses that can be freely used by any organization or individual for their internal networks
- They do not have to be globally unique
- Three private IPv4 address ranges are defined in RFC 1918, Address Allocation for Private Internets:
  - 10.0.0.0/8 (10.0.0.0–10.255.255.255)
  - 172.16.0.0/12 (172.16.0.0–172.31.255.255)
  - 192.168.0.0/16 (192.168.0.0–192.168.255.255)
- Make sure you know the three ranges defined by RFC 1918
- Additionally, remember the name RFC 1918; these addresses are often called RFC 1918 addresses

### Private Address Characteristics

- Private IPv4 addresses can be freely used for internal networks and do not have to be globally unique
- Multiple organizations can use same private address ranges without conflict
- Because networks are never directly connected; their addresses don't have to be unique
- Example: Three LANs all using 192.168.0.0/16 range with overlapping subnets is not a problem
- They are never directly connected, so addresses don't have to be unique

### Public IPv4 Addresses

- IPv4 addresses that are not in RFC 1918 ranges (or another reserved range) are public IPv4 addresses
- These addresses must be globally unique because they are used to communicate over internet
- If two internet-connected hosts have same IP address, other routers won't be able to determine which of two hosts is intended recipient of packet destined for their shared address
- Anycast addresses are exception to this rule; they are purposefully assigned to multiple hosts
- Public IPv4 addresses in examples are from reserved ranges: 192.0.2.0/24, 198.51.100.0/24, and 203.0.113.0/24
- These are reserved for use in documentation and examples but are often used to represent public addresses

### Private Address Routing

- Private IPv4 addresses are not routable over internet
- Packets sourced from or destined for private addresses will be discarded by Internet Service Provider (ISP)
- If you have Windows PC, use `ipconfig` to check your PC's IPv4 address
- It's almost certainly a private address
- So how can your PC communicate over internet despite having private address?
- Answer is NAT

## Network Address Translation (NAT)

### NAT Overview

- Network Address Translation (NAT) is process of modifying packet's source and/or destination IP addresses
- Typically performed by router (or firewall) at network's perimeter
- Router that connects internal network to internet
- By translating private IP addresses to public IP addresses, NAT allows hosts with private IP addresses to communicate over internet
- NAT was designed to translate between private and public IP addresses
- Private–private and public–public translations are technically possible too
- However, use cases for private–private and public–public NAT are more limited than private–public NAT
- For CCNA exam, can assume that NAT is private–public

### NAT Process

- When host in internal network communicates with host in external network via NAT-enabled router, there are four addresses involved from standpoint of router:
  1. IP address of internal host before NAT (inside local)
  2. IP address of internal host after NAT (inside global)
  3. IP address of external host before NAT (outside local)
  4. IP address of external host after NAT (outside global)
- Cisco uses four terms to describe each of these addresses: inside local, inside global, outside local, and outside global

### Inside/Outside Distinction

- Cisco uses terms inside and outside to refer to internal and external networks, respectively
- Inside address is IP address of host located in router's inside (internal) network
- Outside address is IP address of host located in outside (external) network
- Similarly, hosts in inside network are called inside hosts
- Hosts in outside network are called outside hosts
- Router's interface connects to internal/inside network
- Router's interface connects to external/outside network—the internet
- For consistency, will use terms inside and outside since they are terms that Cisco uses in context of NAT
- Their meanings are same as internal and external
- All of these terms are dependent on perspective
- From router's perspective, PC1 is inside host and 8.8.8.8 is outside host
- From perspective of 8.8.8.8 and its router, opposite is true

### Local/Global Distinction

- When inside host sends packet to destination in outside network, source IP address of that packet is IP address configured on inside host—a private IP address
- But what about after router uses NAT to translate source IP address of inside host's packet to public IP address?
- Address after translation still represents inside host, so it remains inside address
- But another distinction is needed to differentiate between pre- and post-NAT addresses: local/global distinction
- Local address is address before router translates it
- Global address is address after router translates it
- In other words, local address is host's address from perspective of inside network
- Global address is host's address from perspective of outside network

### Local vs Public Addresses

- Local addresses and global addresses might seem similar to private addresses and public addresses
- However, concepts don't always overlap
- Example: 8.8.8.8 (a public address) is both local address and global address from router's perspective
- Local and global are NAT-specific terms that have specific meanings
- Local addresses are used on inside of NAT network
- Global addresses are used on outside of NAT network
- NAT translates local addresses to global addresses when traffic flows from inside to outside of network and vice versa
- Regardless of whether addresses are private or public

### Four NAT Address Terms

When we combine inside/outside and local/global distinctions, we get four terms:

- **Inside local**: IP address of host located in inside network from perspective of inside network
- **Inside global**: IP address of host located in inside network from perspective of outside network
- **Outside local**: IP address of host located in outside network from perspective of inside network
- **Outside global**: IP address of host located in outside network from perspective of outside network

### Source NAT

- In typical NAT example, router only performs source NAT on inside host's packet
- It only translates packet's source IP address
- Router does not perform destination NAT on inside host's packet
- It does not translate packet's destination IP address
- Destination NAT is not part of CCNA exam
- If router does not perform destination NAT, outside local and outside global addresses will be identical

### NAT Configuration Requirement

- To configure NAT, must specify router's inside and outside interfaces
- Use `ip nat {inside | outside}` command in interface config mode
- Because router's interface is configured with `ip nat inside` command, hosts on that interface are inside hosts
- Because router's interface is configured with `ip nat outside` command, hosts on that interface are outside hosts

## Types of NAT

### Three NAT Types

There are three types of NAT to learn for CCNA exam:

- **Static NAT**: Static one-to-one translations
- **Dynamic NAT**: Dynamic one-to-one translations
- **Dynamic PAT** (Port Address Translation): Dynamic many-to-one translations

Each type has its own use cases, but dynamic PAT is by far the most widely used, potentially allowing thousands of hosts to share a single public IP address.

## Static NAT

### Static NAT Overview

- Static NAT involves statically configuring one-to-one mappings of inside local (private) addresses to inside global (public) addresses
- By mapping inside host's private IP address to public IP address, inside host is able to communicate over internet
- To allow another inside host to communicate over internet, second public IP address is needed
- This is limitation of static NAT—it is one to one
- As such, it does not help with problem of IPv4 address exhaustion
- Although it is sometimes used to allow particular hosts to communicate over internet

### Static NAT Configuration

- First step is to configure inside and outside interfaces with `ip nat {inside | outside}` in interface config mode
- After that, all that's left to do is create static mappings
- Use `ip nat inside source static inside-local inside-global` command
- Example: `ip nat inside source static 10.0.0.11 192.0.2.1`
- Maps inside local address 10.0.0.11 to inside global address 192.0.2.1

### Static NAT Command Keywords

- `inside` keyword tells router to perform translations for IP addresses originating from inside network
- Specifically, router will translate inside local addresses to inside global addresses as packets move from inside network to outside network
- `source` keyword that follows tells router to translate source IP address of packets coming from hosts on inside network
- So when router forwards packet from inside host, it will translate packet's source IP address from inside local to inside global
- However, it's important to remember that reverse is true of reply from outside host
- When reply comes from outside host and is destined for inside global address, router will translate packet's destination IP address back to inside local address
- Allowing packet to be correctly delivered to inside host

### Static NAT Verification

- After configuring static NAT, can use `show ip nat translations` to view router's translation table
- One potentially confusing aspect of this command's output is that leftmost column is Inside global, followed by Inside local
- Static entry is created in table for each mapping
- Other columns are empty until inside host communicates with outside host
- When inside host communicates with outside host, additional dynamic entries are created in NAT table
- These dynamic entries are tied to static mapping but track state of individual communication sessions
- Whereas static entries are permanent, dynamic entries will be removed after certain period of inactivity
- Can use `clear ip nat translation *` in privileged EXEC mode to manually clear all dynamic entries from NAT translation table

## Dynamic NAT

### Dynamic NAT Overview

- Dynamic NAT is similar to static NAT in that it involves one-to-one mappings of inside local addresses to inside global addresses
- Difference is in how mappings are assigned
- In static NAT, you statically configure each mapping one by one
- In dynamic NAT, router dynamically creates mappings itself from pool of available addresses

### Dynamic NAT Configuration Steps

Dynamic NAT configuration consists of three main steps:

1. Define range of inside local (private) addresses with ACL
2. Define range of inside global (public) addresses with NAT pool
3. Map ACL to NAT pool

### Step 1: Define Inside Local Addresses

- Create ACL to identify range of inside local addresses to be translated
- Packets that are permitted by ACL will be translated
- Packets that are denied by ACL will not be translated; they will be forwarded as is
- However, if their source IP address is private IP address, they will be dropped by ISP
- ACL isn't being used to decide which packets should be forwarded and which should be blocked
- It is only being used to decide which packets should be translated with NAT
- This is another common use for ACLs, which are quite versatile
- Example: `access-list 1 permit 10.0.0.0 0.0.0.255`
- Permits all IP addresses from 10.0.0.0 through 10.0.0.255 but denies all other IP addresses via implicit deny
- Router will use NAT to translate packets with source IP address in permitted range
- Packets with source IP address that is not in that range will not be translated

### Step 2: Define Inside Global Addresses

- Next step is to specify range of inside global addresses—public IPv4 addresses that will be used for communication over internet
- This is done by creating NAT pool with `ip nat pool name start-ip end-ip prefix-length length` command
- `start-ip` and `end-ip` arguments identify range
- Example: `192.0.2.1 192.0.2.5` specifies range of five public addresses: 192.0.2.1–192.0.2.5
- In real network, cannot freely use any public IPv4 addresses you want
- Public addresses must be globally unique, and their assignment is governed by IANA and RIRs
- To receive range of public IP addresses, enterprise must apply to ISP or directly to RIR
- In `ip nat pool` command, must also specify prefix length
- This is used to ensure that all addresses in specified range are in same subnet
- Example: Specified 192.0.2.1–192.0.2.5 range with /29 prefix length
- This implies 192.0.2.0/29 subnet (all host bits set to 0), which includes all addresses from 192.0.2.0 to 192.0.2.7
- Specified range (192.0.2.1–192.0.2.5) is included in that subnet, so command succeeds
- Otherwise, command would be rejected
- Can also use `netmask netmask` instead of `prefix-length length`

### Step 3: Map ACL to Pool

- Final step is to combine ACL and pool with NAT statement
- Mapping range of inside local addresses (ACL) to range of inside global addresses (pool)
- Command is `ip nat inside source list acl pool pool`
- Example: `ip nat inside source list 1 pool POOL1`
- Maps ACL 1 to POOL1
- After that command, dynamic NAT configuration is complete

### Dynamic NAT Operation

- When router forwards packet from host with IP address in range specified by ACL, it will translate source IP address to one of available inside global addresses
- On first come, first served basis
- Dynamic NAT is one to one, just like static NAT
- Multiple inside local addresses cannot be translated to same inside global address at same time
- Inside global addresses are assigned on first-come, first-served basis
- If pool dries up, other hosts' packets will not be able to be translated—they will be dropped!
- Those hosts will have to wait for inside global address to become available again
- This is major downside of dynamic NAT

### Dynamic NAT Limitations

- Packets that are permitted by ACL but can't be translated due to lack of addresses in pool will be dropped
- Packets that are denied by ACL will be forwarded as is, without being translated
- Likely resulting in them being dropped by ISP due to their private IP addresses
- Remember this distinction!
- Of types of NAT you need to know for CCNA exam, dynamic NAT has fewest real-world use cases
- Like static NAT, it only provides one-to-one translations
- However, unlike static NAT, it doesn't let you control translations
- If number of inside hosts is larger than available pool of inside global addresses, there's no easy way to control which hosts get to access internet and which have to wait
- Obtaining enough public IP addresses to support all inside hosts simply isn't feasible for most enterprises these days
- Given state of IPv4 address exhaustion problem

## Dynamic Port Address Translation (PAT)

### PAT Overview

- Dynamic Port Address Translation (PAT) is type of NAT that translates both IP addresses and TCP/UDP port numbers (if necessary) to provide many-to-one mappings of inside local to inside global addresses
- By using unique port number for each communication session, single public IP address can be shared by many inside hosts at same time
- NAT-enabled router uses port numbers to keep track of each individual session
- There are 65,536 (2^16) port numbers in total
- Meaning that single public IP address can theoretically support tens of thousands of sessions from inside hosts
- Actual number will depend on number of factors, such as router's memory capacity
- It is this type of NAT that, combined with private IPv4 address ranges, has greatly extended IPv4's lifespan

### ICMP and PAT

- ICMP doesn't use port numbers like TCP and UDP
- But many ICMP message types use 16-bit Identifier field for similar purpose
- When translating ICMP packets (i.e., ping), Identifier plays role that TCP/UDP port numbers do

### PAT with NAT Pool

- One way to configure dynamic PAT is to simply add `overload` keyword to end of dynamic NAT statement
- In fact, another name for PAT is NAT overload
- Example: `ip nat inside source list 1 pool POOL1 overload`
- Adds `overload` keyword to NAT statement

### PAT Port Translation

- When router translates packet, it will keep pre- and post-translation port numbers same if possible
- However, if packet's pre-translation port number is already in use for another session, router will translate port number to available one
- Once session's first packet has been translated, same port number is used for rest of session
- Each individual packet doesn't need unique port number
- Router will use up all available port numbers for one inside global address before translating to next available address in pool

### PAT Reply Handling

- When router receives reply packets, it is able to identify which session packets belong to
- Thanks to unique port numbers
- Router can then translate each packet's inside global address back to appropriate inside local address

### PAT with Interface IP Address

- Although dynamic PAT can be configured with pool, PAT's many-to-one translation capabilities mean that many organizations require only single public IP address, not pool of them
- And if router is connected to internet, router already has public IP address assigned to it
- IP address of internet-connected interface
- With PAT, router can translate inside hosts' IP addresses to IP address of router's own interface
- This is how dynamic PAT is most often configured
- Because it allows inside hosts to communicate over internet using IP address already configured on router
- No additional public addresses are needed

### PAT Interface Configuration

- As in previous examples, must first configure inside and outside interfaces with `ip nat {inside | outside}` in interface config mode
- Then, as in dynamic NAT, configure ACL to determine which IP addresses should be translated
- This ACL functions same as ones in NAT configurations covered earlier
- Packets that are permitted by ACL will be translated before being forwarded
- Packets that are denied by ACL will be forwarded as is
- If packet is permitted by ACL but can't be translated due to lack of addresses or port numbers, packet will be dropped
- However, you likely won't encounter this with dynamic PAT because so many port numbers are available
- All that remains is to configure NAT statement itself
- Syntax in this case is `ip nat inside source list acl interface interface overload`
- This tells router to use PAT to translate packets permitted by ACL to IP address of specified interface
- Port numbers are used to keep track of each session, including router's own sessions

### PAT Verification

- Can view router's translation table with `show ip nat translations`
- Shows inside local addresses all translated to same inside global address
- But all have unique source ports, allowing router to keep track of them
- Can use `show ip nat statistics` to view statistics such as total number of active translations, peak translations, packets translated, etc.

## Real-World Applications

- **Internet connectivity**: Allow hosts with private addresses to access internet
- **Address conservation**: Extend IPv4 address space by allowing many hosts to share public addresses
- **Security**: Hide internal network structure from outside networks
- **Network migration**: Facilitate network changes and migrations
- **Load balancing**: Distribute traffic across multiple servers
- **ISP connections**: Enable home and small business networks to connect to internet

## Troubleshooting

### Common Issues

- **Hosts cannot access internet**: Verify NAT is configured correctly and interfaces are marked inside/outside
- **Some hosts work, others don't**: Check ACL permits all hosts that need translation
- **Pool exhausted**: With dynamic NAT, verify pool has enough addresses or use PAT instead
- **Translations not appearing**: Verify traffic is actually flowing and matches ACL

### Troubleshooting Steps

1. Verify NAT configuration: `show running-config | include nat`
2. Check translation table: `show ip nat translations`
3. View NAT statistics: `show ip nat statistics`
4. Verify interfaces: Check inside/outside interfaces are configured correctly
5. Test connectivity: Ping from inside host to outside host
6. Check ACL: Verify ACL permits addresses that need translation

## Best Practices

- Use dynamic PAT instead of static or dynamic NAT for most scenarios
- Use PAT with interface IP address when only one public address is available
- Configure appropriate ACLs to identify which traffic should be translated
- Monitor NAT translation table to ensure it's working correctly
- Use `show ip nat statistics` to monitor NAT performance
- Document NAT configuration and public IP address assignments
- Consider security implications of NAT (hides internal structure)
- Plan for sufficient public addresses if using dynamic NAT
- Use static NAT only when specific hosts need consistent public addresses

## Summary

- IPv6 is long-term solution to IPv4 address exhaustion, but subnetting/CIDR, private IPv4 addresses, and NAT have greatly extended IPv4's lifespan
- Private IPv4 addresses can be freely used by any organization for their internal networks; they do not have to be globally unique
- RFC 1918 defines three private IPv4 address ranges: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16
- IPv4 addresses not in RFC 1918 range are public IPv4 addresses and must be globally unique
- Private IPv4 addresses are not routable over internet—packets sourced from or destined for private addresses will be discarded by ISP
- Network Address Translation (NAT) is process of modifying packet's source and/or destination IP addresses
- By translating private IP addresses to public IP addresses, hosts with private addresses can communicate over internet
- NAT was designed to translate between private and public IP addresses
- Cisco uses four terms: inside local, inside global, outside local, and outside global
- Terms inside and outside refer to internal and external networks, respectively
- Use `ip nat {inside | outside}` to specify router's interfaces as connecting to inside or outside networks
- Terms local and global are used to distinguish between pre- and post-NAT addresses
- Inside local: IP address of host in inside network from perspective of inside network
- Inside global: IP address of host in inside network from perspective of outside network
- Outside local: IP address of host in outside network from perspective of inside network
- Outside global: IP address of host in outside network from perspective of outside network
- If router does not perform destination NAT, outside local and outside global addresses will be identical
- Three types of NAT: static NAT (static one to one), dynamic NAT (dynamic one to one), dynamic PAT (dynamic many to one)
- Static NAT involves configuring static one-to-one mappings with `ip nat inside source static inside-local inside-global`
- Use `show ip nat translations` to view NAT translation table
- Dynamic NAT configuration: (1) Define inside local addresses with ACL, (2) Define inside global addresses with NAT pool, (3) Map ACL to pool
- Use `ip nat pool name start-ip end-ip prefix-length length` to create NAT pool
- Use `ip nat inside source list acl pool pool` to map ACL to pool
- Dynamic NAT is one to one; if pool dries up, packets will be dropped
- Dynamic PAT translates both IP addresses and port numbers to provide many-to-one mappings
- Can configure PAT with pool by adding `overload` keyword: `ip nat inside source list acl pool pool overload`
- More common to use interface IP address: `ip nat inside source list acl interface interface overload`
- Use `show ip nat statistics` to view NAT statistics
- PAT allows thousands of hosts to share single public IP address using port numbers

