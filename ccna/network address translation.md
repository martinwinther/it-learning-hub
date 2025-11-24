
# Network Address Translation

## Overview

Network Address Translation (NAT) translates IPv4 source and destination addresses at the edge of a network. Combined with private IPv4 addressing, NAT allows many internal hosts to communicate with external networks while using a limited number of public IPv4 addresses.

## Private and public IPv4 addresses

### RFC 1918 private ranges

RFC 1918 defines three private IPv4 ranges that can be used freely inside networks:

- 10.0.0.0/8 (10.0.0.0–10.255.255.255)
- 172.16.0.0/12 (172.16.0.0–172.31.255.255)
- 192.168.0.0/16 (192.168.0.0–192.168.255.255)

These addresses are reused by many organizations. They do not need to be globally unique because they are not routed on the public internet.

### Public address characteristics

- Any IPv4 address that is not in a private or reserved range is a public address
- Public addresses must be globally unique
- Public addresses are used for internet reachable devices
- Documentation ranges:
  - 192.0.2.0/24
  - 198.51.100.0/24
  - 203.0.113.0/24

Packets sourced from or destined to private addresses are normally dropped by service provider routers. NAT is the mechanism that makes communication possible for internal private hosts.

## NAT concepts

### Purpose of NAT

- Allow private addressed hosts to reach public networks
- Conserve public IPv4 addresses by sharing them
- Provide a basic level of address hiding

NAT is usually performed on a border router or firewall that connects the inside network to the outside network.

### Inside and outside

NAT uses the terms inside and outside:

- Inside: addresses in the internal network
- Outside: addresses in external networks, such as the internet

Interfaces are marked as:

- `ip nat inside` on the internal side
- `ip nat outside` on the external side

Once interfaces are marked, hosts reachable through them are considered inside hosts or outside hosts.

### Local and global

NAT also uses local and global:

- Local address
  - Address as seen on the local (inside) network
- Global address
  - Address as seen on the outside network

Important combinations:

- Inside local
  - Address of an inside host as used inside the network
  - Typically a private IPv4 address
- Inside global
  - Address of that same inside host as seen in the outside network
  - Typically a public IPv4 address
- Outside local
  - Address of an outside host as seen from the inside network
  - Often the same as outside global in simple designs
- Outside global
  - Address of an outside host as used in the outside network
  - Usually a public IPv4 address

For common CCNA scenarios, outside local and outside global are identical because destination addresses are not translated.

### Source NAT focus

In most edge use cases the device performs source NAT:

- Translates the source address of packets leaving the inside network
- Reverse translation is applied to the destination address of return traffic

Destination NAT (changing the destination address of incoming packets) exists but is not a core CCNA topic.

## NAT configuration basics

### Interface roles

On a Cisco router:

```cisco
interface GigabitEthernet0/0
 ip address 192.0.2.2 255.255.255.0
 ip nat outside
!
interface GigabitEthernet0/1
 ip address 10.0.0.1 255.255.255.0
 ip nat inside
```

- Inside interface connects to private network
- Outside interface connects to public network or provider

NAT rules use these roles when selecting which traffic to translate.

## Static NAT

### Static NAT overview

Static NAT creates a fixed one to one mapping between an inside local address and an inside global address.

- One inside host is permanently mapped to one public address
- Used when a specific internal host must have a consistent reachable address
- Does not conserve public addresses because each mapping uses one public address

### Static NAT configuration

Basic example:

```cisco
interface GigabitEthernet0/0
 ip address 192.0.2.2 255.255.255.0
 ip nat outside
!
interface GigabitEthernet0/1
 ip address 10.0.0.1 255.255.255.0
 ip nat inside
!
ip nat inside source static 10.0.0.11 192.0.2.10
```

- Inside local: 10.0.0.11
- Inside global: 192.0.2.10

When traffic leaves 10.0.0.11, the source address becomes 192.0.2.10. Replies sent to 192.0.2.10 are translated back to 10.0.0.11.

### Static NAT verification

- `show ip nat translations`
  - Shows static entries in the translation table
- `clear ip nat translation *`
  - Clears dynamic entries, static entries remain

## Dynamic NAT

### Dynamic NAT overview

Dynamic NAT also provides one to one translations but assigns addresses from a pool instead of static per host mappings.

Characteristics:

- Uses an access list to match inside local addresses
- Uses a pool of inside global addresses
- Builds temporary one to one mappings when traffic is seen
- If the pool is exhausted, new sessions cannot be translated and packets are dropped

### Dynamic NAT configuration steps

1. Define which inside local addresses are eligible for translation with an ACL.
2. Define a pool of inside global addresses.
3. Link the ACL and pool in a NAT rule.

Example:

```cisco
access-list 1 permit 10.0.0.0 0.0.0.255
ip nat pool PUBLIC 192.0.2.10 192.0.2.14 prefix-length 29
ip nat inside source list 1 pool PUBLIC
```

- ACL 1 identifies inside local addresses
- Pool PUBLIC defines a range of public addresses
- NAT rule ties ACL 1 to pool PUBLIC

## Port Address Translation (PAT)

### PAT overview

Port Address Translation (PAT) allows many inside hosts to share one or a few public IP addresses.

Key points:

- Translates source IP and, if needed, source port numbers
- Also called NAT overload
- Tracks each session by a unique combination of address and port
- Uses TCP and UDP port fields, and the ICMP identifier field for ICMP

A single public address can support thousands of concurrent sessions.

### PAT with a pool

PAT can use the same pool defined for dynamic NAT by adding the `overload` keyword:

```cisco
ip nat inside source list 1 pool PUBLIC overload
```

- Inside local addresses that match ACL 1 are translated
- Many internal hosts can share the addresses in PUBLIC

### PAT with interface address

The most common deployment uses the outside interface address as the inside global address.

Example:

```cisco
access-list 1 permit 10.0.0.0 0.0.0.255
!
interface GigabitEthernet0/0
 ip address 192.0.2.2 255.255.255.0
 ip nat outside
!
interface GigabitEthernet0/1
 ip address 10.0.0.1 255.255.255.0
 ip nat inside
!
ip nat inside source list 1 interface GigabitEthernet0/0 overload
```

- All matching inside hosts share 192.0.2.2 as the inside global address
- Router uses different source ports to keep sessions separate

### PAT behavior

- Router tries to keep the same source port if it is free
- If the port is already in use, router picks another available port
- Translation table tracks inside local, inside global, and port values
- Return traffic is matched to the correct inside host by these values

## Troubleshooting NAT

### Common issues

- Inside and outside interfaces not marked correctly
- ACL does not match the intended source addresses
- Dynamic NAT pool exhausted
- Traffic not matching any NAT rule
- Overlapping or incorrect public address ranges

### Useful commands

- `show ip nat translations`
  - Shows current NAT translations
- `show ip nat statistics`
  - Shows counters, hits, misses, and active translations
- `show running-config | include ip nat`
  - Displays NAT related configuration
- `show ip interface`
  - Verifies which interfaces are inside or outside

Combined with `ping` and `traceroute`, these commands help confirm that addresses are being translated as expected.

## Quick review

- Private IPv4 ranges from RFC 1918 are 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16.  
- NAT translates between inside local and inside global addresses so private hosts can reach public networks.  
- Inside and outside refer to network location, local and global refer to pre and post translation views.  
- Static NAT provides fixed one to one mappings and is used when a host needs a consistent public address.  
- Dynamic NAT uses a pool of public addresses and ACLs, still with one to one mappings.  
- PAT (NAT overload) lets many private hosts share one or a few public addresses by translating ports.  
- NAT configuration always marks inside and outside interfaces and then defines static, dynamic, or PAT rules.  
- Core verification uses `show ip nat translations`, `show ip nat statistics`, and interface and ACL checks.

