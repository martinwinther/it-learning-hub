# IPv6 Routing

## Overview

IPv6 routing fundamentals are largely identical to IPv4 routing. Routers build routing tables, forward packets using longest prefix match, and can learn routes through static or dynamic routing. However, IPv6 uses Neighbor Discovery Protocol (NDP) instead of ARP for address resolution, and IPv6 static routing is the focus for CCNA exam (IPv6 dynamic routing is not included).

## Neighbor Discovery Protocol (NDP)

### NDP Overview

- IPv6 uses NDP instead of ARP for Layer 2 address resolution
- NDP maps Layer 3 (IPv6) addresses to Layer 2 (MAC) addresses
- NDP also provides additional functions: router discovery and duplicate address detection
- NDP is component of ICMPv6 (ICMP for IPv6)

### Solicited-Node Multicast Addresses

- Special multicast addresses used by some NDP functions
- Generated from unicast address (global unicast, unique local, or link-local)
- Generation: prepend ff02::1:ff to last six hexadecimal digits of unicast address
- Example: 2001:db8:123::1 → ff02::1:ff00:1
- Example: fe80::99ff:fe12:1234 → ff02::1:ff12:1234

### Address Resolution

- Uses two ICMPv6 messages:
  - **Neighbor Solicitation (NS)**: ICMPv6 type 135 (equivalent to ARP request)
  - **Neighbor Advertisement (NA)**: ICMPv6 type 136 (equivalent to ARP reply)
- Process:
  1. Host sends NS message to neighbor's solicited-node multicast address
  2. Target neighbor replies with unicast NA message containing its MAC address
- NS messages include Target Address field in payload to identify intended recipient
- IPv6 neighbor table stores L3-L2 address mappings (view with `show ipv6 neighbors`)

### Router Discovery

- Allows hosts to automatically discover routers on local network
- Also learns network characteristics (such as network prefix)
- Uses two ICMPv6 messages:
  - **Router Solicitation (RS)**: ICMPv6 type 133
  - **Router Advertisement (RA)**: ICMPv6 type 134
- RS messages sent to "all routers" multicast address (ff02::2)
- RA messages sent to "all nodes" multicast address (ff02::1)
- Routers send RA messages periodically, even without receiving RS

### Stateless Address Autoconfiguration (SLAAC)

- Allows host to automatically generate its own IPv6 address
- Stateless: no central server tracking address assignments (unlike DHCP)
- Process:
  1. Host sends RS message
  2. Router replies with RA message containing network prefix
  3. Host combines learned prefix with Modified EUI-64 interface ID
- Configure on Cisco router: `ipv6 address autoconfig`
- `ipv6 address autoconfig default` also inserts default route using router's link-local address as next hop

### Duplicate Address Detection (DAD)

- Checks if IPv6 address is unique on network before host uses it
- Performed whenever interface is configured with IPv6 address
- Also performed when IPv6-enabled interface initializes (enters up/up state)
- Process:
  1. Host sends NS message to its own solicited-node multicast address
  2. If no response after waiting period, address is unique
  3. If NA message received in response, address is duplicate and cannot be used
- Duplicate addresses marked as [DUP] in show commands

## IPv6 Routing Table

### Route Types

- **Connected routes**: Routes to networks interfaces are connected to
  - Automatically added for each interface with IP address in up/up state
  - Tell router to forward packets directly to destination host
- **Local routes**: Routes to exact IP address configured on router's interface
  - Automatically added for each IP address configured
  - Tell router to receive packet for itself (continue de-encapsulation)
- **Static routes**: Manually configured routes
- **Dynamic routes**: Learned via routing protocols (not CCNA exam topic for IPv6)

### Host Routes vs Network Routes

- **Host route**: Route to single destination IP address
  - IPv6 host routes use /128 prefix length
  - Local routes are examples of host routes
- **Network route**: Route to more than one destination IP address
  - Any route with /127 or shorter prefix length
  - Connected routes are examples of network routes

### Link-Local Addresses in Routing Table

- Link-local addresses do not have connected or local routes
- Traffic to/from link-local addresses doesn't need routing (never leaves local link)
- Link-local addresses can be used as next-hop addresses in routes
- Link-local addresses cannot be used as destination of routes

### Multicast Route

- Router automatically inserts route to ff00::/8 (multicast address range)
- Route specifies Null0 interface (packets dropped)
- Prevents router from forwarding multicast packets by default
- Does not prevent router from sending/receiving multicast packets (e.g., NDP)

### Route Selection

- Router looks up packet's destination IP address in routing table
- Selects most specific matching route (longest prefix match)
- Same process as IPv4 routing
- If no matching route, router drops packet

## IPv6 Static Routes

### Static Route Types

Three configuration methods:

1. **Recursive static route**: Specifies only next-hop IP address
   - Command: `ipv6 route destination-prefix next-hop`
   - Requires recursive routing table lookups to forward packet
2. **Directly connected static route**: Specifies only exit interface
   - Command: `ipv6 route destination-prefix exit-interface`
   - **Does not work on Ethernet interfaces** (works on serial interfaces)
   - IPv4 relies on proxy ARP; IPv6 has no equivalent proxy NDP
3. **Fully specified static route**: Specifies both exit interface and next hop
   - Command: `ipv6 route destination-prefix exit-interface next-hop`
   - Preferred method for IPv6

### Directly Connected Static Routes Limitation

- **Critical**: Directly connected IPv6 static routes do not work on Ethernet interfaces
- Routes appear in routing table but communication will fail
- Neighbor table shows INCMP (incomplete) entries
- Works on serial interfaces (legacy point-to-point connections)
- Must use fully specified routes on Ethernet interfaces

### Link-Local Next Hops

- Link-local addresses can be used as next-hop addresses in routes
- Packets sourced from/destined for link-local addresses are not routable
- Link-local next hops work because address only used for immediate next hop on local link
- **Routes with link-local next hops must be fully specified**
- IOS will reject command if exit interface not specified
- Transit links (links only carrying traffic between network parts) often use only link-local addresses

### Link-Local Address Uniqueness

- Link-local addresses must be unique only within context of single link
- Same link-local address can be used on different interfaces (on separate links)
- Allows identical link-local addresses on multiple interfaces of same router
- Can manually configure link-local addresses: `ipv6 address address link-local`

### Default Routes

- IPv6 default route is route to ::/0 (matches every possible IPv6 address)
- Equivalent to 0.0.0.0/0 in IPv4
- Most commonly used to provide route to internet
- Logic: packets not matching internal destinations are forwarded to internet
- Configure: `ipv6 route ::/0 next-hop` or `ipv6 route ::/0 exit-interface next-hop`

### Floating Static Routes

- Static route configured with non-default administrative distance (AD)
- Default AD for static routes is 1
- Configure AD at end of command: `ipv6 route destination-prefix next-hop ad`
- Example: `ipv6 route ::/0 2001:db8:1::2 2` (backup default route)
- Floating route only enters routing table if more preferred route is removed
- Used as backup routes

## Real-World Applications

- **Enterprise networks**: IPv6 static routing for internal network connectivity
- **Internet connectivity**: Default routes to ISPs for internet access
- **Backup paths**: Floating static routes provide redundancy
- **Transit links**: Link-local addressing sufficient for point-to-point connections
- **Dual-stack networks**: Running IPv4 and IPv6 routing simultaneously
- **Migration scenarios**: Static routes during IPv6 deployment

## Troubleshooting IPv6 Routing

### Common Issues

- **Routes not appearing**: Verify `ipv6 unicast-routing` is enabled
- **Directly connected routes not working**: Remember they don't work on Ethernet interfaces
- **Neighbor resolution failing**: Check NDP neighbor table with `show ipv6 neighbors`
- **Link-local next hops**: Ensure routes are fully specified
- **Duplicate addresses**: Check DAD status, verify no duplicate addresses

### Verification Commands

- `show ipv6 route`: View IPv6 routing table
- `show ipv6 route connected`: View only connected routes
- `show ipv6 route static`: View only static routes
- `show ipv6 neighbors`: View IPv6 neighbor table (address resolution)
- `show ipv6 interface brief`: View IPv6 addresses on interfaces
- `ping [ipv6-address]`: Test IPv6 connectivity

### Troubleshooting Steps

1. Verify IPv6 routing is enabled: `show ipv6 unicast-routing` or check config
2. Check routing table: `show ipv6 route`
3. Verify neighbor resolution: `show ipv6 neighbors`
4. Test connectivity: `ping [destination]`
5. Check interface status: `show ipv6 interface brief`
6. Verify static route configuration: `show ipv6 route static`

## Best Practices

- Always enable `ipv6 unicast-routing` before configuring IPv6 addresses
- Use fully specified static routes on Ethernet interfaces
- Use link-local addresses on transit links when global addresses not needed
- Configure floating static routes for backup paths
- Use default routes for internet connectivity
- Verify neighbor resolution with `show ipv6 neighbors`
- Test connectivity after configuring routes
- Document IPv6 routing configuration
- Plan for dual-stack operation during migration

## Summary

- IPv6 routing fundamentals are same as IPv4: routing tables, longest prefix match, static/dynamic routes
- IPv6 uses NDP instead of ARP for address resolution
- NDP uses Neighbor Solicitation (NS) and Neighbor Advertisement (NA) messages
- Solicited-node multicast addresses generated by prepending ff02::1:ff to last six hex digits
- NDP provides router discovery (RS/RA messages) and duplicate address detection (DAD)
- SLAAC allows hosts to automatically generate IPv6 addresses using router advertisements
- IPv6 routing table contains connected, local, static, and dynamic routes
- Host routes use /128 prefix length; network routes use /127 or shorter
- Link-local addresses don't have routes but can be used as next-hop addresses
- IPv6 static routes: recursive (next-hop only), directly connected (exit interface only), fully specified (both)
- **Directly connected IPv6 static routes do not work on Ethernet interfaces**
- Routes with link-local next hops must be fully specified
- Default route is ::/0 (equivalent to 0.0.0.0/0 in IPv4)
- Floating static routes use non-default AD to provide backup paths
- Use `show ipv6 route`, `show ipv6 neighbors`, and `ping` for troubleshooting

