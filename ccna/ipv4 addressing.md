# IPv4 Addressing

## Overview

IPv4 addressing identifies hosts and networks at Layer 3. Routers read the IPv4 header to forward packets between networks, and subnetting defines how those addresses are grouped into networks.

## IPv4 header essentials

The IPv4 header is usually 20 bytes, with optional fields increasing it up to 60 bytes. Key fields for CCNA:

- Version  
  - Indicates IP version  
  - IPv4 uses value 4

- IHL (Internet Header Length)  
  - Length of header in 32 bit words  
  - Typical value is 5 (20 bytes)  
  - Values greater than 5 indicate that options are present

- DSCP and ECN  
  - Used for Quality of Service (QoS) and congestion notification  
  - Historically grouped as Type of Service (ToS)

- Total Length  
  - Length of the entire packet in bytes (header plus payload)

- Identification, Flags, Fragment Offset  
  - Used for fragmentation when packets exceed the outgoing interface MTU  
  - DF (Don’t Fragment) and MF (More Fragments) flags control behavior

- Time To Live (TTL)  
  - Limits how long a packet can exist in the network  
  - Decremented by 1 at each router hop  
  - Packet is discarded when TTL reaches 0

- Protocol  
  - Identifies the next layer protocol  
  - Common values:  
    - 1: ICMP  
    - 6: TCP  
    - 17: UDP  
    - 89: OSPF

- Header Checksum  
  - Error check for the IPv4 header  
  - Recalculated at each router

- Source and Destination Address  
  - 32 bit IPv4 addresses for sender and receiver

- Options  
  - Optional and rarely used  
  - Present only when IHL is greater than 5

## Binary and decimal basics

IPv4 uses binary values internally. For CCNA, focus on 8 bit (one octet) values.

### Decimal system

- Base 10  
- Digits 0 through 9  
- Each position is a power of 10: 1, 10, 100, 1000, and so on

### Binary system

- Base 2  
- Digits 0 and 1  
- Each position is a power of 2: 1, 2, 4, 8, 16, 32, 64, 128

One octet can represent values from 0 to 255.

| Bit position | 7   | 6   | 5   | 4   | 3  | 2  | 1  | 0  |
|-------------|-----|-----|-----|-----|----|----|----|----|
| Value       | 128 | 64  | 32  | 16  | 8  | 4  | 2  | 1  |

### Converting binary to decimal

- Write down the bit values that are set to 1  
- Add them together

Example:

- `00101111`  
  - Bits set: 32, 8, 4, 2, 1  
  - 32 + 8 + 4 + 2 + 1 = 47

### Converting decimal to binary (subtraction method)

Example for 206:

- 206 − 128 = 78 → bit 7 = 1  
- 78 − 64 = 14 → bit 6 = 1  
- 32 does not fit → bit 5 = 0  
- 16 does not fit → bit 4 = 0  
- 14 − 8 = 6 → bit 3 = 1  
- 6 − 4 = 2 → bit 2 = 1  
- 2 − 2 = 0 → bit 1 = 1  
- Remaining bit 0 = 0  

Result: 206 = `11001110`

## IPv4 address structure

An IPv4 address is a 32 bit value written in dotted decimal as four octets. Each address has:

- Network portion  
- Host portion  

Devices in the same IPv4 subnet share the same network portion and have unique host portions.

### Prefix length

Prefix length notation indicates how many bits belong to the network portion.

- Written as `/X`  
- X is the number of network bits

Examples:

- `/8`  → first octet is network, remaining 24 bits are host  
- `/16` → first two octets are network  
- `/24` → first three octets are network  

Any remaining bits belong to the host portion.

### Netmasks

Netmasks are 32 bit values that mark network bits with 1 and host bits with 0.

Examples:

- `/8`  → `255.0.0.0`  
- `/16` → `255.255.0.0`  
- `/24` → `255.255.255.0`  

A bit that is 1 in the mask means the corresponding bit in the address is part of the network portion.

## Configuring IPv4 on routers

Router interfaces are usually configured manually with IPv4 addresses.

Example:

```cisco
interface GigabitEthernet0/0
 ip address 192.0.2.1 255.255.255.0
 no shutdown
```

Useful show commands:

- `show ip interface brief`  
  Interface status and assigned addresses

- `show ip interface <name>`  
  Detailed settings and mask information

End hosts typically use DHCP to obtain addresses automatically, while routers use static addressing on LAN interfaces.

## Attributes of an IPv4 network

Important values for a subnet:

- Network address  
- Broadcast address  
- First usable host address  
- Last usable host address  
- Maximum number of hosts  

### Network and broadcast addresses

- Network address  
  - All host bits set to 0  
  - Identifies the subnet itself  

- Broadcast address  
  - All host bits set to 1  
  - Used to send to all hosts in the subnet  

Neither address is assigned to a host.

### Maximum number of hosts

For a subnet with `y` host bits:

- Number of host addresses: `2^y`  
- Usable host addresses: `2^y − 2`  
  - One for network address  
  - One for broadcast address  

### First and last usable addresses

- First usable: network address plus 1  
- Last usable: broadcast address minus 1  

Often the first usable address is given to the default gateway, but that is only a convention.

## IPv4 address classes (historical)

Early IPv4 networks used fixed “classful” address ranges:

| Class | First octet range | Default prefix | Notes                       |
|-------|-------------------|----------------|-----------------------------|
| A     | 0–127             | /8             | Few very large networks     |
| B     | 128–191           | /16            | Medium sized networks       |
| C     | 192–223           | /24            | Many small networks         |
| D     | 224–239           | n/a            | Multicast                   |
| E     | 240–255           | n/a            | Experimental                |

Classful networking is obsolete. Modern networks use classless addressing with variable prefix lengths (CIDR). For CCNA, class ranges are still useful for recognizing older designs and special ranges.

### Special ranges

- `0.0.0.0/8`  
  Reserved

- `127.0.0.0/8`  
  Loopback  
  Traffic sent to these addresses never leaves the local device.

## Quick review

- IPv4 header carries source and destination addresses and control fields such as TTL, protocol, and checksum.  
- TTL prevents packets from looping forever by being decremented at each hop until it reaches 0.  
- Common protocol numbers: ICMP 1, TCP 6, UDP 17, OSPF 89.  
- Binary uses powers of 2; one octet ranges from 0 to 255.  
- An IPv4 address has a network portion and a host portion defined by prefix length or netmask.  
- Network address has all host bits set to 0; broadcast address has all host bits set to 1.  
- Number of usable host addresses is `2^y − 2`, where `y` is the number of host bits.  
- Classful ranges (A, B, C) are historical; current designs use classless addressing with variable length prefixes.
