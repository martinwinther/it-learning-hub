# IPv6 Addressing

## Overview

IPv6 is the successor to IPv4 and uses 128 bit addresses instead of 32 bit. It provides a vastly larger address space and removes the need for large scale NAT in many designs. IPv4 is still widely used, but IPv6 support is now expected on modern networks and devices.

## Why IPv6 is needed

### IPv4 address exhaustion

- IPv4 uses 32 bit addresses (about 4.3 billion addresses)
- Many ranges are reserved or unusable as public addresses
- Growth of the internet, mobile devices, and IoT has consumed most public IPv4 space
- Regional Internet Registries (RIRs) have already reached depletion stages for IPv4 blocks

### IPv6 address space

- IPv6 uses 128 bit addresses
- Number of addresses is 2^128
- Address space is effectively inexhaustible for practical network design
- Allows consistent subnet sizes (for example /64) without worrying about running out

IPv4 and IPv6 serve the same basic purpose: provide end to end addressing at Layer 3. Both are carried in Ethernet frames and handed to the appropriate upper layer protocols.

## Number system review for IPv6

IPv6 addresses are written in hexadecimal. Hex and binary conversions are useful for reading and writing addresses.

### Hexadecimal basics

- Base 16 number system
- Digits: 0–9 and a–f
- One hex digit represents 4 bits
- One hextet (group of 4 hex digits) represents 16 bits

### Binary and hex conversion

For IPv6, think in 4 bit groups:

- Hex to binary: replace each hex digit with its 4 bit value  
  Example: `0x2f` → `0010 1111`
- Binary to hex: group bits into 4s and convert each group  
  Example: `1011 0100` → `0xb4`

This is enough to follow IPv6 address calculations at CCNA level.

## IPv6 header essentials

IPv6 uses a fixed 40 byte header with these key fields:

- Version  
  - Always 6 for IPv6

- Traffic Class  
  - 8 bits used for QoS (DSCP and ECN)

- Flow Label  
  - 20 bits to identify a flow of packets that should receive similar handling

- Payload Length  
  - Length of the payload after the IPv6 header

- Next Header  
  - Identifies the next protocol or extension header  
  - Common values: ICMPv6 (58), TCP (6), UDP (17), OSPF (89), EIGRP (88)

- Hop Limit  
  - Similar to IPv4 TTL  
  - Decremented at each router hop and packet is dropped at 0

- Source Address and Destination Address  
  - 128 bit IPv6 source and destination addresses

Options are moved into extension headers, so the basic header stays the same size.

## IPv6 address format and abbreviation

### Basic format

- 128 bit address written in hexadecimal
- Divided into 8 groups of 16 bits (hextets)
- Hextets separated by colons

Example:

- `2001:0db8:0000:0001:20a1:0000:0000:00ff`

### Abbreviation rules

Two rules are used to shorten addresses.

#### Rule 1: remove leading zeros

- In each hextet, leading zeros can be omitted
- At least one digit must remain if the hextet is not all zeros  
  Example: `020a` → `20a`

#### Rule 2: compress all zero hextets with `::`

- A sequence of one or more all zero hextets can be replaced with `::`
- `::` can appear only once in an address
- Use it for the longest run of all zero hextets

Example:

- `2001:0db8:0000:0000:0000:0000:1280:34bd`  
  Abbreviated: `2001:db8::1280:34bd`

Combined example:

- `2001:0db8:0000:0000:002f:0001:0000:34bd`  
  Abbreviated: `2001:db8::2f:1:0:34bd`

RFC 5952 provides guidelines for a consistent style: lowercase a–f, no leading zeros, and `::` used on the longest zero sequence.

## IPv6 prefixes

### Prefix length and network portion

IPv6 uses prefix length notation similar to IPv4 CIDR.

- Written as `/X` where X is number of bits in the prefix
- Remaining bits are the interface identifier (host portion)

Typical LAN subnet:

- `/64` prefix
- First 64 bits identify the network
- Last 64 bits identify the interface

Example:

- Address: `2001:db8:1:2:a:b:c:d/64`  
  Prefix: `2001:db8:1:2::/64`

To write the prefix, set the host portion to all zeros and abbreviate.

## IPv6 configuration on Cisco routers

### Enabling IPv6 routing

- Global configuration:
  - `ipv6 unicast-routing`
- Required so the router will forward IPv6 packets
- Without this, the router can have IPv6 addresses but will not route between interfaces

### Manual address configuration

On an interface:

```cisco
interface GigabitEthernet0/0
 ipv6 address 2001:db8:1:1::1/64
 no shutdown
```

Notes:

- Prefix length is always written with `/`, not a dotted mask
- Abbreviated forms are accepted
- Show commands display addresses in abbreviated RFC 5952 style

### Multiple addresses per interface

- An interface can have multiple IPv6 addresses
- Each is configured with its own `ipv6 address` command
- To remove one address, use the `no ipv6 address` form with the full address

### Link local addresses

- Range: `fe80::/10`, commonly seen as `fe80::/64` on interfaces
- Required on every IPv6 enabled interface
- Used for neighbor discovery and some routing protocols
- Can be automatically generated (often using modified EUI‑64) or manually configured:

```cisco
interface GigabitEthernet0/0
 ipv6 address fe80::1 link-local
```

Each interface must have exactly one link local address.

### Modified EUI‑64 interface IDs

- Method to auto generate the 64 bit interface ID from a 48 bit MAC address
- Basic process:
  - Split the MAC into two halves
  - Insert `fffe` in the middle
  - Flip the universal/local bit (the 7th bit of the address)

Example configuration:

```cisco
interface GigabitEthernet0/0
 ipv6 address 2001:db8:1:1::/64 eui-64
```

Router derives the lower 64 bits from the MAC address.

## IPv6 address types

### Global unicast addresses

- Globally unique, routable on the internet
- Common range: `2000::/3`
- Structure (typical):
  - Global routing prefix
  - Subnet ID
  - 64 bit interface ID
- Similar role to public IPv4 addresses
- `2001:db8::/32` reserved for examples and documentation

### Unique local addresses (ULAs)

- Private IPv6 addresses for internal use
- Range: `fc00::/7`, practically used as `fd00::/8`
- Not routed on the public internet
- Structure:
  - `fd` prefix
  - 40 bit global ID (ideally random)
  - 16 bit subnet ID
  - 64 bit interface ID
- Similar concept to private IPv4 ranges

### Link local addresses (LLAs)

- Range: `fe80::/10`, used as `fe80::/64` on interfaces
- Valid only on the local link
- Not routed between segments
- Used for neighbor discovery and some routing protocols
- Required on every IPv6 interface

### Multicast addresses

- Range: `ff00::/8`
- One to many communication
- Different scopes define how far packets travel (link local, site local, organization, global)

Common link local multicast groups:

- All nodes: `ff02::1`
- All routers: `ff02::2`
- OSPF routers: `ff02::5` and `ff02::6`
- RIPng routers: `ff02::9`
- EIGRP for IPv6 routers: `ff02::a`

IPv4 equivalent is the class D range `224.0.0.0/4`.

### Anycast addresses

- Same address configured on multiple devices
- Packets are delivered to the nearest device (by routing metrics)
- No special address format; uses normal unicast addresses
- Useful for services that exist in multiple locations (DNS, CDN nodes)

### Special addresses

- Unspecified address: `::`
  - All zeros
  - Used as a source before a host knows its address
  - Used as default route prefix `::/0`

- Loopback address: `::1`
  - Stays on the local device
  - Used to test IPv6 stack and local services

## Troubleshooting and verification

### Basic commands

- `show ipv6 interface brief`
  - Lists interfaces and their IPv6 addresses
- `show ipv6 interface <name>`
  - Detailed per interface IPv6 information
- `show ipv6 neighbors`
  - Neighbor table (similar role to IPv4 ARP table)
- `ping ipv6 <address>` or `ping <address>`
  - Tests IPv6 connectivity

### Common issues

- IPv6 routing disabled
  - Check for `ipv6 unicast-routing`
- Wrong prefix length
  - Verify interface configurations and matching prefixes
- Link local problems
  - Make sure devices are on the same link and have LLAs
- Multicast based protocols failing
  - Confirm correct multicast groups and link local scope

## Quick review

- IPv6 uses 128 bit addresses written in hexadecimal hextets separated by colons.  
- Address space is large enough to use /64 prefixes for most LAN subnets.  
- Abbreviation rules remove leading zeros and allow one `::` to compress all zero hextets.  
- Routers need `ipv6 unicast-routing` before they can route IPv6 packets.  
- Interfaces can have multiple IPv6 addresses and always need a link local address.  
- Global unicast (`2000::/3`) is similar to public IPv4, ULAs (`fd00::/8`) are similar to private IPv4.  
- Multicast (`ff00::/8`) supports one to many communication; link local groups like `ff02::1` and `ff02::2` are common.  
- Special addresses include the unspecified address `::`, loopback `::1`, and the default route `::/0`.
