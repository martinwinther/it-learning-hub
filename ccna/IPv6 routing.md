# IPv6 Routing

## Overview

IPv6 routing fundamentals match IPv4 routing. Routers build routing tables, forward packets using longest prefix match, and learn routes through connected, static, and dynamic methods. IPv6 uses Neighbor Discovery Protocol (NDP) instead of ARP for address resolution. For CCNA, static IPv6 routing and NDP behavior are the primary focus.

## Neighbor Discovery Protocol (NDP)

### NDP basics

- IPv6 uses NDP instead of ARP for Layer 2 address resolution
- NDP maps IPv6 addresses to MAC addresses
- NDP also supports router discovery and duplicate address detection
- NDP is part of ICMPv6

### Solicited node multicast addresses

- Special multicast addresses used by NDP
- Derived from a unicast address (global, unique local, or link local)
- Creation rule: prepend `ff02::1:ff` to the last 24 bits of the unicast address
- Examples:
  - `2001:db8:123::1` → `ff02::1:ff00:1`
  - `fe80::99ff:fe12:1234` → `ff02::1:ff12:1234`

### Address resolution

NDP uses two ICMPv6 message types for address resolution:

- Neighbor Solicitation (NS): type 135, similar role to ARP request
- Neighbor Advertisement (NA): type 136, similar role to ARP reply

Process:

1. Host sends NS to the target's solicited node multicast address
2. Target replies with a unicast NA that carries its MAC address
3. IPv6 neighbor table stores the mapping, visible with `show ipv6 neighbors`

### Router discovery

Router discovery uses ICMPv6 messages:

- Router Solicitation (RS): type 133, sent to `ff02::2` (all routers)
- Router Advertisement (RA): type 134, sent to `ff02::1` (all nodes)

Behavior:

- Hosts send RS to discover routers and prefixes
- Routers send RA periodically and in response to RS
- RAs advertise prefixes and flags used for address configuration

### Stateless Address Autoconfiguration (SLAAC)

SLAAC allows a host to form its own IPv6 address without a stateful server.

Basic flow:

1. Host receives RA with prefix information
2. Host combines advertised prefix with a 64 bit interface identifier (often EUI‑64 based)
3. Host performs Duplicate Address Detection before using the address

On Cisco routers:

- `ipv6 address autoconfig` creates an address from RA information
- `ipv6 address autoconfig default` also installs a default route using the router link local address as next hop

### Duplicate Address Detection (DAD)

DAD checks that an address is unique on the link before use.

- Performed when an interface gains an IPv6 address or transitions to up state
- Host sends NS to its own solicited node multicast address
- If no NA is received, the address is considered unique
- If an NA is received, the address is marked duplicate and not used
- Duplicate addresses appear with a [DUP] tag in some show outputs

## IPv6 routing table

### Route types

Common IPv6 route types:

- Connected routes
  - Added automatically for each interface with an IPv6 address in up state
  - Represent directly reachable networks
- Local routes
  - Added for each IPv6 address configured on an interface
  - Represent the exact address on the router itself (/128)
- Static routes
  - Manually configured
- Dynamic routes
  - Learned with routing protocols (beyond CCNA scope for IPv6)

### Host and network routes

- Host route
  - Prefix length /128
  - Matches a single address
  - Local routes are host routes
- Network route
  - Prefix length /127 or shorter
  - Matches a range of addresses
  - Connected network routes are examples

### Link local addresses and routing

- Link local range: `fe80::/10`
- Link local addresses never leave the local link
- No connected or local routes appear for link local addresses
- Link local addresses can be used as next hops in static routes
- Link local addresses cannot be used as destination prefixes in routes

### Multicast route entry

- IPv6 routing table includes a route to `ff00::/8` pointing to Null0
- This prevents forwarding of multicast packets by default
- Router can still send and receive multicast packets on local interfaces

### Route selection

- IPv6 uses longest prefix match, same as IPv4
- Router chooses the most specific route that matches the destination
- If no route matches, the packet is dropped

## IPv6 static routes

### Static route styles

Three configuration patterns are important:

1. Recursive static route
   - Specifies only next hop address
   - Form: `ipv6 route prefix next-hop`
   - Router performs a lookup on the next hop address to find exit interface

2. Directly connected static route
   - Specifies only exit interface
   - Form: `ipv6 route prefix exit-interface`
   - Valid on serial or point-to-point links
   - Not usable on Ethernet segments

3. Fully specified static route
   - Specifies both exit interface and next hop
   - Form: `ipv6 route prefix exit-interface next-hop`
   - Recommended for IPv6, especially on Ethernet

### Directly connected static route limitations

For IPv6 on Ethernet interfaces:

- Static routes that specify only an exit interface appear in the routing table
- Traffic using these routes often fails
- Neighbor table shows incomplete (INCMP) entries
- There is no IPv6 equivalent to proxy ARP to resolve the next hop
- Use fully specified static routes on Ethernet instead

### Link local next hops

- Link local addresses can serve as next hop addresses
- These addresses are valid only on the local link
- Static routes that use link local next hops must be fully specified
- IOS requires an exit interface with a link local next hop

Example:

```cisco
ipv6 route 2001:db8:10::/64 GigabitEthernet0/0 fe80::1
```

Transit links that only carry traffic between routers often use link local only addressing, with static routes pointing to link local next hops.

### Default route

- IPv6 default route uses prefix `::/0`
- Equivalent to `0.0.0.0/0` in IPv4
- Commonly points toward an upstream router or ISP

Example:

```cisco
ipv6 route ::/0 2001:db8:1::2
```

or with explicit exit interface:

```cisco
ipv6 route ::/0 GigabitEthernet0/0 2001:db8:1::2
```

### Floating static routes

- Static routes normally have administrative distance (AD) 1
- Floating static routes use a higher AD to act as backups
- Configured by adding AD at the end of the command

Example:

```cisco
ipv6 route ::/0 2001:db8:1::2 5
```

- Route above is used only if no better route exists
- Commonly used as backup default routes

## Troubleshooting IPv6 routing

### Common issues

- IPv6 routing disabled
  - `ipv6 unicast-routing` missing
- Directly connected static routes on Ethernet
  - Route present but traffic fails
  - Neighbor table shows incomplete entries
- Link local next hop errors
  - Static route configured without exit interface
- Duplicate or misconfigured addresses
  - DAD failures, incorrect prefixes, or wrong interfaces

### Verification commands

- `show ipv6 route`
  - Full IPv6 routing table
- `show ipv6 route connected`
  - Only connected routes
- `show ipv6 route static`
  - Only static routes
- `show ipv6 neighbors`
  - Neighbor table (similar to IPv4 ARP table)
- `show ipv6 interface brief`
  - Interfaces and IPv6 addresses
- `ping ipv6 <address>` or `ping <address>`
  - Connectivity tests

Basic troubleshooting sequence:

1. Confirm `ipv6 unicast-routing` is enabled
2. Check interface status and addresses
3. Verify presence of expected routes
4. Check neighbor table for resolved next hops
5. Test connectivity with `ping`

## Quick review

- IPv6 routing uses the same longest prefix match logic as IPv4.  
- NDP replaces ARP and uses NS and NA messages for address resolution.  
- RS and RA messages provide router discovery and support SLAAC.  
- IPv6 routing tables contain connected, local, static, and dynamic routes.  
- Host routes use /128; any shorter prefix describes a network.  
- Link local addresses do not have routes but can be used as next hop addresses.  
- Directly connected static routes are not reliable on Ethernet; fully specified static routes are preferred.  
- Default route is `::/0` and floating static routes use higher administrative distance for backup.  
- Core verification uses `show ipv6 route`, `show ipv6 neighbors`, `show ipv6 interface brief`, and `ping`.
