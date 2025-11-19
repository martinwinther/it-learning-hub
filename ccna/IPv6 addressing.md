# IPv6 Addressing

## Overview

IPv6 is the next version of the Internet Protocol, designed to address IPv4 address exhaustion. IPv6 provides a much larger address space (128 bits vs 32 bits), ensuring sufficient addresses for current and future network connectivity needs. While IPv4 is still dominant, IPv6 adoption is growing, and modern network engineers must be familiar with both protocols.

## Why IPv6 is Needed

### IPv4 Address Exhaustion

- IPv4 addresses are 32 bits, providing 2^32 (4,294,967,296) unique addresses
- Not all addresses are available (class D for multicast, class E for experimental)
- Even with efficient use, billions of addresses are insufficient for modern connectivity needs
- Problem called IPv4 address exhaustion has been ongoing for years

### Regional Internet Registries (RIRs)

- IP address assignments controlled by Internet Assigned Numbers Authority (IANA)
- IANA distributes address space to five RIRs:
  - AFRINIC: Africa
  - APNIC: Asia-Pacific region
  - ARIN: Canada, United States, parts of Caribbean, Antarctica
  - LACNIC: Most of Caribbean and Latin America
  - RIPE NCC: Europe, West Asia, Central Asia, Russia
- RIRs are running out of IPv4 addresses (ARIN in 2015, RIPE NCC in 2019, LACNIC in 2020)

### IPv6 Address Space

- IPv6 addresses are 128 bits (four times IPv4's 32 bits)
- Provides 2^128 (340,282,366,920,938,463,463,374,607,431,768,211,456) addresses
- Number of IPv6 addresses is between 340 trillion and 3.4 quintillion times larger than estimated grains of sand on Earth
- Ensures sufficient address space for foreseeable future

### IPv4 vs IPv6 Purpose

- Both protocols serve same general purpose: encapsulate Layer 4 segments with header to make packets
- Provide end-to-end addressing from source to destination host
- IPv6 packets encapsulated in Ethernet frames at each hop, just like IPv4
- IPv6 adoption growing: approximately 45% of Google users access via IPv6 (up from 1% a decade ago)

## Number System Conversion

### Hexadecimal Review

- Hexadecimal uses 16 digits: 0-9 and A-F
- Single hexadecimal digit contains four bits of information (2^4 = 16)
- Essential for working with IPv6 addresses

### Binary to Hexadecimal Conversion

Three-step process:

1. Split the number into four-bit groups
2. Convert each four-bit group to decimal
3. Convert each decimal number to hexadecimal

Example: 0b1101101100101111 → 0xDB2F

### Hexadecimal to Binary Conversion

Three-step process:

1. Split up the hexadecimal digits
2. Convert each hexadecimal digit to decimal
3. Convert each decimal digit to binary

Example: 0x41AE → 0b0100000110101110

## IPv6 Header

### Header Format

- Fixed 40-byte header (IPv4 header is variable 20-60 bytes)
- Eight fields: Version, Traffic Class, Flow Label, Payload Length, Next Header, Hop Limit, Source Address, Destination Address

### Header Fields

- **Version**: 4-bit field, always set to 0b0110 (6) for IPv6
- **Traffic Class**: 8-bit field for Quality of Service (QoS), split into DSCP (6 bits) and ECN (2 bits)
- **Flow Label**: 20-bit field used to label flows (sequences of packets)
- **Payload Length**: 16-bit field indicating length of encapsulated payload
- **Next Header**: Indicates type of encapsulated message (equivalent to IPv4 Protocol field)
  - Common values: 1 (ICMP), 6 (TCP), 17 (UDP), 58 (ICMPv6), 88 (EIGRP), 89 (OSPF)
- **Hop Limit**: Equivalent to IPv4 TTL, prevents infinite packet loops
- **Source Address**: 128-bit field containing source IPv6 address
- **Destination Address**: 128-bit field containing destination IPv6 address

## IPv6 Address Structure

### Address Format

- IPv6 address is 128-bit number identifying host at Layer 3
- Written in hexadecimal, divided into eight groups of 16 bits
- Groups separated by colons
- Each group of 16 bits called a hextet (informal term, also called hexadectet)

### Prefix Length

- IPv6 typically uses /64 prefix lengths
- First 64 bits are network portion
- Last 64 bits are host portion
- Extremely inefficient (each subnet contains ~18 quintillion addresses) but acceptable due to large address space

### Address Abbreviation

Two methods to abbreviate IPv6 addresses:

#### Method 1: Remove Leading Zeros

- Remove leading zeros from each hextet
- Trailing zeros cannot be removed
- Example: 2001:0db8:0000:001b:20a1:0020:0080:34bd → 2001:db8:0:1b:20a1:20:80:34bd

#### Method 2: Omit Consecutive All-Zero Hextets

- Replace two or more consecutive all-zero hextets with double colon (::)
- Double colon can only be used once per address
- Example: 2001:2db8:0000:0000:0000:0000:1280:34bd → 2001:2db8::1280:34bd

#### Combined Abbreviation

- Both methods can be combined
- Example: 2001:0db8:0000:0000:002f:0001:0000:34bd → 2001:db8::2f:1:0:34bd

### RFC 5952 Guidelines

- All leading zeros must be removed
- Double colon must abbreviate as much as possible
- Individual all-zero hextet cannot be omitted with double colon
- If multiple choices for double colon placement, use longest series of all-zero hextets
- If equal length, replace leftmost series
- Hexadecimal characters a-f must be written in lowercase

## IPv6 Network Prefixes

### Prefix Concept

- Network prefix is combination of network address and prefix length
- Same concept as IPv4: if host has address 2001:db8:1:2:a:b:c:d/64, prefix is 2001:db8:1:2::/64
- With /64 prefix lengths, simply convert final four hextets (host portion) to all zeros

### Prefix Examples

- Host address: fd00:af89:1234:1200:0:123:4567:beef/64 → Prefix: fd00:af89:1234:1200::/64
- Host address: 2001:db8:babe:cafe:2100:101:0:1/64 → Prefix: 2001:db8:babe:cafe::/64
- Host address: 2333::efd:1212:1:1/64 → Prefix: 2333::/64

## IPv6 Configuration on Cisco Routers

### Enable IPv6 Routing

- First command: `ipv6 unicast-routing` in global config mode
- Without this command, router can configure IPv6 addresses but cannot route IPv6 packets
- IPv6 routing is not enabled by default

### Manual Address Configuration

- Command: `ipv6 address address/prefix-length` in interface config mode
- Must specify prefix length using slash notation (not dotted-decimal netmask like IPv4)
- Can configure abbreviated addresses; IOS will interpret correctly
- IOS automatically displays fully abbreviated addresses in show commands

### Multiple Addresses

- IPv4 addresses overwrite each other when configured
- IPv6 addresses do not overwrite; interface can have multiple IPv6 addresses
- To change IPv6 address, must use `no` command to remove existing address first

### Modified EUI-64

- Method to automatically generate 64-bit interface identifier (host portion)
- Command: `ipv6 address prefix/64 eui-64`
- Three-step process:
  1. Divide MAC address in half
  2. Insert 0xfffe in the middle
  3. Invert the seventh bit (third bit of second hex digit)

### Link-Local Addresses

- Automatically generated on IPv6-enabled interfaces using Modified EUI-64
- Range: fe80::/10, but following 54 bits should be 0, resulting in fe80::/64 prefix
- Each IPv6 interface must have exactly one link-local address
- Can manually configure with: `ipv6 address address link-local`
- Configuring new link-local address overwrites old one

## IPv6 Address Types

### Global Unicast Addresses

- Globally unique addresses used for communication over public internet
- Allocation controlled by IANA
- Originally defined as 2000::/3 range
- Now includes any address not specifically reserved for other purposes
- Structure:
  - 48-bit global routing prefix (assigned by RIR or ISP)
  - 16-bit subnet identifier (used to make subnets)
  - 64-bit interface identifier (host portion)
- IPv4 equivalent: public IPv4 addresses
- 2001:db8::/32 range reserved for examples in documentation

### Unique Local Addresses (ULAs)

- Private addresses that do not have to be globally unique
- Enterprises free to use in internal networks
- Cannot be used for communication over internet
- Range: fc00::/7, divided into:
  - fc00::/8: Currently reserved, not defined
  - fd00::/8: Active range for ULAs
- Structure:
  - fd prefix
  - 40-bit global ID (should be randomly generated)
  - 16-bit subnet identifier
  - 64-bit interface identifier
- IPv4 equivalent: private IPv4 addresses (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)

### Link-Local Addresses (LLAs)

- Unicast addresses used for communication on local link only
- Cannot be used for communication between different network segments
- Range: fe80::/10, but standard states following 54 bits must be 0, resulting in fe80::/64
- Automatically generated using Modified EUI-64
- Can be manually configured
- Each IPv6 interface must have exactly one LLA
- IPv4 equivalent: 169.254.0.0/16 (but IPv4 doesn't require LLAs on all interfaces)

### Multicast Addresses

- Used for one-to-multiple communication
- Range: ff00::/8 (if address begins with ff, it's multicast)
- IPv4 equivalent: class D range (224.0.0.0-239.255.255.255)
- Several scopes define how far multicast packets should travel:
  - **Interface-local** (ff01): Packet doesn't leave local device
  - **Link-local** (ff02): Packet remains on local segment, routers won't route
  - **Site-local** (ff05): Can be forwarded by routers, limited to single physical site
  - **Organization-local** (ff08): Wider scope than site-local (entire enterprise)
  - **Global** (ff0e): No boundaries, possible to route over internet

### Common Link-Local Multicast Addresses

- All nodes: ff02::1 (IPv4: 224.0.0.1)
- All routers: ff02::2 (IPv4: 224.0.0.2)
- All OSPF routers: ff02::5 (IPv4: 224.0.0.5)
- All OSPF DRs/BDRs: ff02::6 (IPv4: 224.0.0.6)
- All RIP routers: ff02::9 (IPv4: 224.0.0.9)
- All EIGRP routers: ff02::a (IPv4: 224.0.0.10)

### Anycast Addresses

- Used for one-to-one-of-multiple communication
- Same IP address shared by multiple hosts
- Address itself indistinguishable from unicast address (no reserved range)
- Packets delivered to closest host configured with address (as determined by routing)
- Useful for services over internet (e.g., CDN services like Cloudflare)
- Configure with: `ipv6 address address/prefix-length anycast`
- Marked as [ANY] in show commands

### Special Addresses

- **Unspecified address**: :: (all zeros)
  - Used as source address when device doesn't know its IPv6 address
  - IPv6 default routes configured to ::/0
  - IPv4 equivalent: 0.0.0.0
- **Loopback address**: ::1
  - Messages sent to this address looped back to local device
  - Not sent out of any interfaces
  - Used to test device's network software
  - IPv4 equivalent: 127.0.0.0/8 range

## Real-World Applications

- **Internet connectivity**: Global unicast addresses enable public internet communication
- **Enterprise networks**: ULAs provide private addressing for internal networks
- **Link-local communication**: LLAs enable neighbor discovery and local segment communication
- **Multicast services**: Video streaming, service discovery, routing protocols
- **Anycast services**: CDN services, DNS root servers, load balancing
- **Dual-stack networks**: Running both IPv4 and IPv6 simultaneously

## Troubleshooting IPv6 Addressing

### Common Issues

- **Address not configured**: Verify `ipv6 unicast-routing` is enabled
- **Duplicate addresses**: Check DAD (Duplicate Address Detection) status
- **Address abbreviation errors**: Verify following RFC 5952 guidelines
- **Link-local communication failing**: Verify interfaces are on same segment
- **Multicast not working**: Check multicast group membership

### Verification Commands

- `show ipv6 interface brief`: View IPv6 addresses on interfaces
- `show ipv6 interface [interface]`: View detailed IPv6 interface information
- `show ipv6 neighbors`: View IPv6 neighbor table (similar to ARP table)
- `ping [ipv6-address]`: Test IPv6 connectivity

## Best Practices

- Use /64 prefix lengths for simplicity (standard practice)
- Enable IPv6 routing with `ipv6 unicast-routing` before configuring addresses
- Use global unicast addresses for public internet communication
- Use ULAs for private internal networks
- Configure loopback interfaces with /128 prefix length
- Follow RFC 5952 guidelines for address representation
- Use Modified EUI-64 for automatic host portion generation when appropriate
- Manually configure link-local addresses for easier troubleshooting
- Document IPv6 addressing scheme and prefix assignments
- Plan for dual-stack operation during IPv6 migration

## Summary

- IPv6 addresses are 128 bits, providing 2^128 addresses (vs IPv4's 2^32)
- IPv6 addresses written in hexadecimal, divided into eight groups of 16 bits (hextets)
- IPv6 typically uses /64 prefix lengths (first 64 bits network, last 64 bits host)
- IPv6 addresses can be abbreviated by removing leading zeros and omitting consecutive all-zero hextets with ::
- Enable IPv6 routing with `ipv6 unicast-routing` before configuring addresses
- Configure addresses with `ipv6 address address/prefix-length`
- Multiple IPv6 addresses can exist on same interface (unlike IPv4)
- Modified EUI-64 automatically generates host portion: divide MAC in half, insert fffe, invert seventh bit
- Global unicast addresses (2000::/3) are public, globally unique addresses
- Unique local addresses (fd00::/8) are private addresses for internal networks
- Link-local addresses (fe80::/64) are for local segment communication only
- Multicast addresses (ff00::/8) provide one-to-multiple communication with various scopes
- Anycast addresses are unicast addresses configured on multiple hosts
- Unspecified address is :: (all zeros), loopback address is ::1
- Each IPv6 interface must have exactly one link-local address
- IPv6 header is fixed 40 bytes with eight fields
- Next Header field indicates encapsulated protocol type (6=TCP, 17=UDP, 58=ICMPv6, etc.)

