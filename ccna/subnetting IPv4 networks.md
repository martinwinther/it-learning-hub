# Subnetting IPv4 Networks

## Overview

Subnetting is the process of dividing a larger network address block into smaller networks called subnets. Subnetting allows for more efficient use of the IPv4 address space and enables network administrators to create networks of appropriate sizes for different organizational needs.

## What is Subnetting?

### The Problem with Classful Addressing

Classful addressing, defined in RFC 791 (1981), established rigid rules for IPv4 address allocation:

- **Class A addresses**: Begin with 0b0, use /8 prefix length (16,777,214 usable addresses)
- **Class B addresses**: Begin with 0b10, use /16 prefix length (65,534 usable addresses)
- **Class C addresses**: Begin with 0b110, use /24 prefix length (254 usable addresses)

#### Limitations

- **Too Large for Small Networks**: A Class C network (254 addresses) is far more than needed for a home network or small office
- **Too Small for Enterprise**: A Class C network is too small for most enterprise networks, requiring a Class B
- **Waste of Addresses**: A Class B network (65,534 addresses) is far more than even very large networks require
- **Address Exhaustion**: The IPv4 address pool was rapidly depleting due to inefficient allocation

### Classless Inter-Domain Routing (CIDR)

CIDR, introduced in 1993, replaced classful addressing with a flexible system:

#### Key Features

- **Flexible Prefix Lengths**: Prefix lengths are not restricted to /8, /16, or /24
- **Variable Network/Host Boundary**: The boundary between network and host portions can be anywhere
- **CIDR Notation**: The /X notation (e.g., /23, /26, /28) indicates the prefix length
- **Subnetting**: Allows division of address blocks into subnets of appropriate sizes

#### Benefits

- **Efficient Address Use**: Create subnets only as large as needed
- **Reduced Waste**: Minimize unused IP addresses
- **Flexibility**: Support networks of any size requirement
- **Scalability**: Better support for the growing internet

### Subnetting Process

#### Basic Concept

- **Address Block**: A range of IP addresses that can be divided into subnets (e.g., 192.168.1.0/24)
- **Subnetting**: Dividing the address block into smaller networks
- **Borrowing Bits**: Extending the network portion by borrowing bits from the host portion
- **Subnet Creation**: Changing the binary value of borrowed bits to create different subnets

#### Example: Dividing /24 Address Block

A 192.168.1.0/24 address block can be divided:

- **/24**: One subnet with 256 addresses (254 usable)
- **/25**: Two subnets with 128 addresses each (126 usable each)
- **/26**: Four subnets with 64 addresses each (62 usable each)
- **/27**: Eight subnets with 32 addresses each (30 usable each)
- **/28**: Sixteen subnets with 16 addresses each (14 usable each)

**Rule**: For each bit borrowed, the number of subnets doubles, but the addresses per subnet halves.

## The Five Attributes of a Subnet

Every subnet has five key attributes that must be identified:

### Network Address

- **Definition**: The first address of a subnet, with host portion all 0s
- **Purpose**: Identifies the subnet itself
- **Example**: In 192.168.1.64/26, the network address is 192.168.1.64

### Broadcast Address

- **Definition**: The last address of a subnet, with host portion all 1s
- **Purpose**: Used for broadcasting to all hosts in the subnet
- **Example**: In 192.168.1.64/26, the broadcast address is 192.168.1.127

### First Usable Address

- **Definition**: The first address that can be assigned to a host
- **Calculation**: Network address + 1
- **Example**: In 192.168.1.64/26, the first usable address is 192.168.1.65

### Last Usable Address

- **Definition**: The last address that can be assigned to a host
- **Calculation**: Broadcast address - 1
- **Example**: In 192.168.1.64/26, the last usable address is 192.168.1.126

### Maximum Number of Hosts

- **Definition**: The number of IP addresses available to assign to hosts
- **Formula**: 2^y – 2, where y is the number of host bits
- **Subtraction Reason**: Network and broadcast addresses cannot be assigned to hosts
- **Example**: In 192.168.1.64/26, with 6 host bits: 2^6 – 2 = 62 hosts

### Finding Subnet Attributes

To find a subnet's network address from a host IP:

1. **Write in Binary**: Convert the IP address to binary
2. **Set Host Bits to 0**: Change all host bits to 0
3. **Convert Back**: Convert the result back to dotted decimal

**Example**: PC1 has IP address 172.16.20.27/28

1. Binary: 10101100.00010000.00010100.00011011
2. Set host bits (last 4) to 0: 10101100.00010000.00010100.00010000
3. Decimal: 172.16.20.16 (network address)

## Subnet Masks

### Definition

A subnet mask is a 32-bit value that indicates which bits in an IP address are part of the network portion and which are part of the host portion:

- **Bit Set to 1**: Indicates a network bit
- **Bit Set to 0**: Indicates a host bit
- **Structure**: Series of 1s followed by series of 0s (for standard masks)

### Subnet Mask Table for /24+ Prefix Lengths

| Prefix Length | Subnet Mask (Binary) | Subnet Mask (Decimal) | Max Hosts (2^y-2) |
|---|---|---|---|
| /24 | 11111111.11111111.11111111.00000000 | 255.255.255.0 | 254 |
| /25 | 11111111.11111111.11111111.10000000 | 255.255.255.128 | 126 |
| /26 | 11111111.11111111.11111111.11000000 | 255.255.255.192 | 62 |
| /27 | 11111111.11111111.11111111.11100000 | 255.255.255.224 | 30 |
| /28 | 11111111.11111111.11111111.11110000 | 255.255.255.240 | 14 |
| /29 | 11111111.11111111.11111111.11111000 | 255.255.255.248 | 6 |
| /30 | 11111111.11111111.11111111.11111100 | 255.255.255.252 | 2 |
| /31 | 11111111.11111111.11111111.11111110 | 255.255.255.254 | 2* |
| /32 | 11111111.11111111.11111111.11111111 | 255.255.255.255 | 1* |

\* Special cases (see below)

### Special Prefix Lengths

#### /31 Prefix Length

- **Purpose**: Point-to-point links (connections between two routers)
- **Exception**: Does not have network or broadcast addresses
- **Usage**: Both addresses are usable for router interfaces
- **Advantage**: More efficient than /30 (consumes 2 addresses instead of 4)
- **Configuration**: Cisco IOS displays a warning when using /31 on non-point-to-point interfaces

#### /32 Prefix Length

- **Purpose**: Typically used in routing table entries for specific host routes
- **Rare Interface Configuration**: Rarely configured on interfaces
- **Exception**: Used in OSPF for loopback interfaces

## Fixed-Length Subnet Masking (FLSM)

### FLSM Overview

Fixed-Length Subnet Masking (FLSM) divides an address block into subnets of equal sizes. All subnets have the same prefix length.

### FLSM Process

1. **Determine Required Subnets**: Identify how many subnets are needed
2. **Calculate Borrowed Bits**: Determine how many bits to borrow (2^x = number of subnets)
3. **Calculate New Prefix Length**: Original prefix length + borrowed bits
4. **List Subnets**: Count up in binary with borrowed bits to list all subnets

### Subnetting /24 Address Blocks

#### One Bit Borrowed (/25)

Borrowing 1 bit from 192.168.1.0/24 creates 2 subnets:

- **192.168.1.0/25**: 128 addresses (126 usable)
- **192.168.1.128/25**: 128 addresses (126 usable)

#### Two Bits Borrowed (/26)

Borrowing 2 bits from 192.168.1.0/24 creates 4 subnets:

- **192.168.1.0/26**: 64 addresses (62 usable)
- **192.168.1.64/26**: 64 addresses (62 usable)
- **192.168.1.128/26**: 64 addresses (62 usable)
- **192.168.1.192/26**: 64 addresses (62 usable)

#### Pattern Recognition

- **Subnet Count**: 2^x where x = borrowed bits
- **Counting Method**: Count up in binary (00, 01, 10, 11) for borrowed bits
- **Subnet Size**: Each subnet size is determined by remaining host bits

### Subnetting /16 Address Blocks

The process is identical to subnetting /24 blocks, but involves multiple octets:

#### Example: Subnetting 192.168.0.0/16

Borrowing 2 bits creates 4 /18 subnets:

- **192.168.0.0/18**: 16,382 usable addresses
- **192.168.64.0/18**: 16,382 usable addresses
- **192.168.128.0/18**: 16,382 usable addresses
- **192.168.192.0/18**: 16,382 usable addresses

#### Key Principles

- **Same Process**: Number of subnets = 2^x (x = borrowed bits)
- **Host Calculation**: Max hosts = 2^y – 2 (y = remaining host bits)
- **Network Address**: Host portion all 0s (regardless of original block size)

### Subnetting /8 Address Blocks

Subnetting /8 blocks follows the same process, with more available host bits (24 host bits):

#### Example: Subnetting 10.0.0.0/8

Borrowing 12 bits creates 4,096 /20 subnets:

- **10.0.0.0/20**: First subnet
- **10.255.224.0/20**: Second-to-last subnet
- **10.255.240.0/20**: Last subnet

#### Important Note

Borrowed bits can cross octet boundaries. This doesn't change the subnetting process; IP addresses are just 32 bits to computers.

### FLSM Scenarios

#### Scenario 1: Four Equal Subnets

**Given**: 172.25.190.0/23 address block, create 4 equal subnets

**Solution**:

1. **Borrowed Bits**: Need 2^2 = 4 subnets, so borrow 2 bits
2. **New Prefix Length**: /23 + 2 = /25
3. **Subnets**:
   - 172.25.190.0/25
   - 172.25.190.128/25
   - 172.25.191.0/25
   - 172.25.191.128/25
4. **Hosts per Subnet**: 2^7 – 2 = 126 hosts

#### Scenario 2: Required Number of Subnets

**Given**: 10.224.0.0/11 address block, create 2,000 subnets

**Solution**:

1. **Borrowed Bits**: 2^11 = 2,048 subnets (closest power of 2 ≥ 2,000)
2. **New Prefix Length**: /11 + 11 = /22
3. **Hosts per Subnet**: 2^10 – 2 = 1,022 hosts

#### Key Points

- **Power of 2 Limitation**: Subnet count must be a power of 2
- **Extra Subnets**: Common to have slightly more subnets than needed
- **Extra Addresses**: Each subnet often has slightly more addresses than needed
- **Future Planning**: Extra capacity allows for network growth

## Variable-Length Subnet Masking (VLSM)

### VLSM Overview

Variable-Length Subnet Masking (VLSM) allows creation of subnets with different prefix lengths (varying sizes) from the same address block. This maximizes address space efficiency.

### Why VLSM?

#### Problems with FLSM

- **Wasted Addresses**: Subnets may be much larger than needed
- **Inefficiency**: Small subnets (like point-to-point links) waste many addresses
- **Real-World Needs**: Different network segments require different sizes

#### Benefits of VLSM

- **Efficient Use**: Create subnets only as large as needed
- **Flexibility**: Match subnet sizes to actual requirements
- **Conservation**: Minimize wasted IP addresses
- **Real-World Standard**: Most production networks use VLSM

### VLSM Process

#### Step-by-Step Method

1. **List Requirements**: Identify all subnets needed and their host requirements
2. **Sort by Size**: Order subnets from largest to smallest
3. **Assign Largest First**: Assign the largest subnet at the start of the address block
4. **Assign Next Largest**: Assign the next largest subnet immediately after the previous one
5. **Continue Process**: Repeat until all subnets are assigned

#### Example Scenario

**Given**: 10.89.100.0/24 address block

**Requirements**:

- Toronto LAN A: 122 hosts
- Tokyo LAN A: 59 hosts
- Toronto LAN B: 30 hosts
- Tokyo LAN B: 11 hosts
- WAN connection: 2 hosts

**Total Required**: 226 addresses (sufficient for /24 with 254 addresses)

#### VLSM Solution

1. **Toronto LAN A (122 hosts)**:
   - Need 7 host bits (2^7 – 2 = 126 ≥ 122)
   - Prefix: /25
   - Subnet: 10.89.100.0/25 (128 addresses, 10.89.100.0 - 10.89.100.127)

2. **Tokyo LAN A (59 hosts)**:
   - Need 6 host bits (2^6 – 2 = 62 ≥ 59)
   - Prefix: /26
   - Subnet: 10.89.100.128/26 (64 addresses, 10.89.100.128 - 10.89.100.191)

3. **Toronto LAN B (30 hosts)**:
   - Need 5 host bits (2^5 – 2 = 30 ≥ 30)
   - Prefix: /27
   - Subnet: 10.89.100.192/27 (32 addresses, 10.89.100.192 - 10.89.100.223)

4. **Tokyo LAN B (11 hosts)**:
   - Need 4 host bits (2^4 – 2 = 14 ≥ 11)
   - Prefix: /28
   - Subnet: 10.89.100.224/28 (16 addresses, 10.89.100.224 - 10.89.100.239)

5. **WAN Connection (2 hosts)**:
   - Need 2 host bits (2^2 – 2 = 2 ≥ 2)
   - Prefix: /30
   - Subnet: 10.89.100.240/30 (4 addresses, 10.89.100.240 - 10.89.100.243)

**Remaining Addresses**: 10.89.100.244 - 10.89.100.255 (12 addresses unused)

### VLSM Best Practices

#### Calculating Host Bits Needed

- **Formula**: Find minimum y where 2^y – 2 ≥ required hosts
- **Start Large**: Begin with the largest subnet requirement
- **Sequential Assignment**: Assign subnets sequentially without gaps
- **Documentation**: Keep track of assigned address ranges

#### Efficiency Considerations

- **Router Addresses**: Include router IP addresses in host counts
- **Future Growth**: Consider slight oversizing for expansion
- **Point-to-Point Links**: Use /30 or /31 for router connections
- **Minimize Waste**: Calculate precisely to avoid large unused blocks

## Real-World Applications

### Enterprise Networks

- **Department Segmentation**: Different departments may need different subnet sizes
- **VLAN Assignment**: Each VLAN typically gets its own subnet
- **Remote Offices**: Small branch offices need smaller subnets than headquarters
- **WAN Links**: Point-to-point connections use minimal address space

### Service Provider Networks

- **Customer Allocations**: Assign appropriately sized blocks to customers
- **Address Conservation**: Maximize efficient use of provider address space
- **Flexible Deployment**: Support customers with varying size requirements

### Small Office/Home Office (SOHO)

- **Home Networks**: Small subnets sufficient for residential use
- **Small Businesses**: Medium-sized subnets for office envaddironments
- **Guest Networks**: Separate smaller subnets for guest access

## Troubleshooting Subnetting

### Common Issues

#### Incorrect Network Address Calculation

- **Problem**: Misidentifying the network address
- **Solution**: Always set host bits to 0s in binary
- **Verification**: Ensure host portion is all 0s

#### Wrong Broadcast Address

- **Problem**: Incorrectly calculating broadcast address
- **Solution**: Set host bits to all 1s
- **Verification**: Ensure host portion is all 1s

#### Host Count Errors

- **Problem**: Forgetting to subtract 2 (network and broadcast)
- **Solution**: Always use formula 2^y – 2
- **Verification**: Check that network and broadcast are excluded

#### Subnet Overlap

- **Problem**: Assigning overlapping address ranges
- **Solution**: In VLSM, assign subnets sequentially without gaps
- **Verification**: Verify no address appears in multiple subnets

### Verification Commands

#### Cisco IOS Commands

```cisco
show ip interface brief          # Verify configured IP addresses
show ip route                    # View routing table entries
show ip interface                # Detailed interface information
ping                             # Test connectivity
```

## Best Practices

### Subnet Design

- **Documentation**: Maintain clear documentation of all subnet assignments
- **Naming Convention**: Use consistent naming for subnets
- **Addressing Scheme**: Follow a logical addressing scheme
- **Growth Planning**: Reserve some address space for future expansion

### Efficiency

- **Use VLSM**: Prefer VLSM over FLSM for production networks
- **Right-Size Subnets**: Create subnets only as large as needed
- **Minimize Waste**: Avoid creating unnecessarily large subnets
- **Regular Review**: Periodically review and optimize address allocation

### Practice

- **Hands-On Practice**: Subnetting is a skill that requires practice
- **Practice Tools**: Use online subnetting calculators and practice sites
- **Exam Preparation**: Master both FLSM and VLSM for CCNA exam
- **Binary Skills**: Maintain proficiency in binary/decimal conversion

## Summary

Subnetting IPv4 networks is essential for network engineering:

- **Purpose**: Efficient use of IPv4 address space by creating appropriately sized networks
- **CIDR**: Classless addressing system enabling flexible prefix lengths
- **Five Attributes**: Network address, broadcast address, first/last usable, max hosts
- **FLSM**: Fixed-length subnets of equal sizes (learning tool and exam requirement)
- **VLSM**: Variable-length subnets of varying sizes (production standard)
- **Subnet Masks**: 32-bit values indicating network vs. host bits
- **Special Cases**: /31 for point-to-point links, /32 for host routes
- **Practice Required**: Subnetting is a skill requiring hands-on practice

Mastering subnetting provides the foundation for efficient network design and proper IP address management in any network environment.
