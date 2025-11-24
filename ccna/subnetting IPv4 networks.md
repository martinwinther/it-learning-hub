# Subnetting IPv4 Networks

## Overview

Subnetting divides a larger IPv4 network into smaller subnets by extending the network prefix. This allows efficient use of address space and creates subnets of appropriate sizes for different parts of a network. CIDR notation (`/X`) indicates how many bits are used for the network prefix.

## Classful addressing and CIDR

### Classful addressing limits

Original classful IPv4 addressing used fixed prefix lengths:

- Class A: /8
- Class B: /16
- Class C: /24

Problems:

- Class C (/24) often too large for very small networks.
- Class C too small for many enterprise networks.
- Class B (/16) much larger than most networks need.
- Result was wasted addresses and faster exhaustion of IPv4 space.

### CIDR and classless subnetting

Classless Inter Domain Routing (CIDR) introduced flexible prefix lengths.

Key ideas:

- Prefix length can be any value from /0 to /32.
- Network and host boundary is not tied to classes.
- `a.b.c.d/X` notation indicates how many bits form the network prefix.
- Subnetting divides an address block into smaller blocks with longer prefixes.

Example with 192.168.1.0/24:

- /24 → 1 subnet, 256 addresses (254 usable).
- /25 → 2 subnets, 128 addresses each (126 usable).
- /26 → 4 subnets, 64 addresses each (62 usable).
- /27 → 8 subnets, 32 addresses each (30 usable).
- /28 → 16 subnets, 16 addresses each (14 usable).

Rule:

- Each borrowed bit doubles the number of subnets.
- Each borrowed bit halves the number of addresses per subnet.

## Subnet attributes

Every subnet has five key attributes:

### Network address

- First address in the subnet.
- Host bits all 0.
- Represents the subnet itself.
- Example: 192.168.1.64/26 has network address 192.168.1.64.

### Broadcast address

- Last address in the subnet.
- Host bits all 1.
- Used for broadcasts to all hosts in the subnet.
- Example: 192.168.1.64/26 has broadcast address 192.168.1.127.

### First and last usable addresses

- First usable: network address + 1.
- Last usable: broadcast address − 1.
- Example: 192.168.1.64/26:
  - First usable: 192.168.1.65.
  - Last usable: 192.168.1.126.

### Maximum number of hosts

- Formula: `2^y − 2`, where `y` is the number of host bits.
- Subtract 2 for network and broadcast addresses.
- Example: /26 has 6 host bits → `2^6 − 2 = 62` usable addresses.

### Finding the network address from a host IP

Procedure:

1. Convert IP address to binary.
2. Set all host bits to 0.
3. Convert back to decimal.

Example: 172.16.20.27/28

- Host bits are the last 4 bits.
- Set last 4 bits to 0 → 172.16.20.16.
- Network address: 172.16.20.16/28.

## Subnet masks and prefix lengths

### Subnet mask definition

A subnet mask is a 32 bit value that marks network bits and host bits:

- Mask bit 1 → network bit.
- Mask bit 0 → host bit.
- Masks are a run of 1s followed by a run of 0s.

### Common masks for /24 and longer

| Prefix | Mask (decimal)      | Mask (binary, last octet) | Host bits | Max hosts (2^y − 2) |
|--------|---------------------|---------------------------|-----------|---------------------|
| /24    | 255.255.255.0       | 00000000                  | 8         | 254                 |
| /25    | 255.255.255.128     | 10000000                  | 7         | 126                 |
| /26    | 255.255.255.192     | 11000000                  | 6         | 62                  |
| /27    | 255.255.255.224     | 11100000                  | 5         | 30                  |
| /28    | 255.255.255.240     | 11110000                  | 4         | 14                  |
| /29    | 255.255.255.248     | 11111000                  | 3         | 6                   |
| /30    | 255.255.255.252     | 11111100                  | 2         | 2                   |
| /31    | 255.255.255.254     | 11111110                  | 1         | special             |
| /32    | 255.255.255.255     | 11111111                  | 0         | special             |

Wildcard mask for ACLs is the inverse of the subnet mask (255 minus each octet).

### Special prefix lengths

#### /31 for point to point links

- Two addresses in the subnet.
- No dedicated network or broadcast address.
- Both addresses used for router interfaces.
- Efficient alternative to /30 on point to point links.

#### /32 host routes

- Single address.
- Used in routing tables to represent specific hosts.
- Common for loopbacks and static host routes.

## Fixed Length Subnet Masking (FLSM)

### Concept

Fixed Length Subnet Masking uses one prefix length for all subnets in a block. All subnets have the same size.

### Process

1. Determine how many equal sized subnets are required.
2. Choose `x` so that `2^x` is at least the required number of subnets.
3. New prefix length = original prefix length + `x`.
4. List subnet network addresses by counting in increments of subnet size.

### FLSM example: /24 block

For 192.168.1.0/24:

- Borrow 1 bit → /25 → 2 subnets:

  - 192.168.1.0/25
  - 192.168.1.128/25

- Borrow 2 bits → /26 → 4 subnets:

  - 192.168.1.0/26
  - 192.168.1.64/26
  - 192.168.1.128/26
  - 192.168.1.192/26

### FLSM example: larger block

172.25.190.0/23, create four equal subnets:

- Need 4 subnets → `2^2` → borrow 2 bits.
- New prefix length: /25.
- Subnets:

  - 172.25.190.0/25
  - 172.25.190.128/25
  - 172.25.191.0/25
  - 172.25.191.128/25

Each /25 subnet has 126 usable addresses.

## Variable Length Subnet Masking (VLSM)

### VLSM concept

Variable Length Subnet Masking uses different prefix lengths within a single address block. Subnets are sized to match actual requirements. VLSM is standard practice in real networks.

### VLSM method

1. List all subnet requirements and required host counts.
2. Sort requirements from largest to smallest.
3. Starting at the beginning of the block, assign the largest subnet.
4. Assign the next largest subnet in the next free address range.
5. Continue until all requirements are met.

### VLSM worked example

Address block: 10.89.100.0/24

Requirements:

- LAN A: 122 hosts
- LAN B: 59 hosts
- LAN C: 30 hosts
- LAN D: 11 hosts
- WAN link: 2 hosts

Steps:

1. LAN A, 122 hosts  
   - Need 7 host bits → `2^7 − 2 = 126`.  
   - Prefix: /25.  
   - Subnet: 10.89.100.0/25 (hosts 10.89.100.1–10.89.100.126).

2. LAN B, 59 hosts  
   - Need 6 host bits → `2^6 − 2 = 62`.  
   - Prefix: /26.  
   - Subnet: 10.89.100.128/26 (hosts 10.89.100.129–10.89.100.190).

3. LAN C, 30 hosts  
   - Need 5 host bits → `2^5 − 2 = 30`.  
   - Prefix: /27.  
   - Subnet: 10.89.100.192/27 (hosts 10.89.100.193–10.89.100.222).

4. LAN D, 11 hosts  
   - Need 4 host bits → `2^4 − 2 = 14`.  
   - Prefix: /28.  
   - Subnet: 10.89.100.224/28 (hosts 10.89.100.225–10.89.100.238).

5. WAN link, 2 hosts  
   - Need 2 host bits → `2^2 − 2 = 2`.  
   - Prefix: /30.  
   - Subnet: 10.89.100.240/30 (hosts 10.89.100.241–10.89.100.242).

Remaining addresses: 10.89.100.243–10.89.100.255.

## Subnetting pitfalls and verification

### Common mistakes

- Wrong network address  
  Host bits not all set to 0.

- Wrong broadcast address  
  Host bits not all set to 1.

- Host count errors  
  Forgetting to subtract 2 for network and broadcast.

- Overlapping subnets  
  Address ranges assigned so that a single address appears in more than one subnet.

- Misaligned subnet boundaries  
  Starting a subnet at an address that is not a proper network address for that prefix length.

### Verification steps

- Check calculations in binary when in doubt.
- Confirm that host ranges do not overlap.
- Ensure masks match prefix lengths in device configurations.
- On Cisco IOS, use:

  ```cisco
  show ip interface brief
  show ip route
  show ip interface
  ping
  ```

## Quick review

- Subnetting extends the network prefix to create smaller subnets from a larger block.  
- CIDR removes class boundaries and allows any prefix length, written as `/X`.  
- Each subnet has a network address, broadcast address, first usable, last usable, and a maximum host count `2^y − 2`.  
- Subnet masks use 1s for network bits and 0s for host bits; common masks from /24 to /30 should be memorized.  
- /31 is efficient for point to point links and /32 represents a single host route.  
- FLSM uses equal sized subnets with the same prefix length; VLSM uses different prefix lengths to match real host requirements.  
- Typical exam problems involve calculating subnet ranges, host counts, and choosing appropriate prefixes for given host requirements.
