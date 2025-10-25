# IPv4 Addressing

## Overview

Routers use information in the Layer 3 headers of the TCP/IP model to make routing decisions and forward packets across networks. Understanding IPv4 addressing is fundamental to network administration and troubleshooting.

## The IPv4 Header

The IPv4 header is 20 to 60 bytes in length and contains 14 fields. This header provides all the information necessary for routers to forward packets from source to destination across networks.

| Field | Bit range (inclusive) | Byte offset(s) | Length (bits) | Notes |
|---|---|---|---|---|
| Version | 0–3 | 0 (bits 0–3) | 4 | IPv4 = 4 |
| IHL | 4–7 | 0 (bits 4–7) | 4 | Internet Header Length (in 32-bit words) |
| DSCP | 8–13 | 1 (bits 0–5) | 6 | Differentiated Services Code Point |
| ECN | 14–15 | 1 (bits 6–7) | 2 | Explicit Congestion Notification |
| Total Length | 16–31 | 2–3 | 16 | Entire packet length (bytes) |
| Identification | 32–47 | 4–5 | 16 | |
| Flags | 48–50 | 6 (bits 0–2) | 3 | DF/MF flags |
| Fragment Offset | 51–63 | 6–7 (byte 6 bits 3–7; byte 7 bits 0–7) | 13 | |
| Time To Live | 64–71 | 8 | 8 | |
| Protocol | 72–79 | 9 | 8 | Next-layer protocol |
| Header Checksum | 80–95 | 10–11 | 16 | |
| Source Address | 96–127 | 12–15 | 32 | |
| Destination Address | 128–159 | 16–19 | 32 | |
| Options | 160–(IHL×32 − 1) | 20–(IHL×4 − 1) | variable | Present only if IHL > 5 |

### The Version Field

The Version field indicates the version of IP (IPv4 or IPv6). This field allows routers to determine how to process the packet:

- A value of 0b0100 (0d4) indicates IPv4
- A value of 0b0110 (0d6) indicates IPv6

### The IHL Field

The Internet Header Length (IHL) field indicates the length of the header in 4-byte increments. This field is necessary because the IPv4 header can vary in length:

- Indicates the length of the header, which varies depending on whether options are present
- If the value is greater than 5, the options field is present
- Maximum length is 15 (60 bytes)

### The DSCP and ECN Fields

The Differentiated Services Code Point (DSCP) and Explicit Congestion Notification (ECN) fields are used to prioritize certain kinds of traffic. This is called Quality of Service (QoS):

- **DSCP**: Used for traffic classification and prioritization
- **ECN**: Used for congestion notification
- Previously called (and sometimes still is) Type of Service (ToS)

### The Total Length Field

The Total Length field indicates the length of the entire packet in bytes. This includes both the header and its payload:

- Total length of the packet (header and payload)
- Not the same as IHL, which is only the header length
- Used by routers to determine packet boundaries

### The Identification, Flags, and Fragment Offset Fields

The Identification, Flags, and Fragment Offset fields support packet fragmentation. If a packet is larger than an interface's Maximum Transmission Unit (MTU), the router will divide the packet into multiple smaller packets called fragments. The standard MTU is 1500 bytes.

#### Identification Field

Identifies which original packet each fragment belongs to, allowing the destination to reassemble fragments correctly.

#### Flags Field

Used to control and identify fragments:

- **DF (Don't Fragment)**: Prevents fragmentation
- **MF (More Fragments)**: Indicates if more fragments follow

#### Fragment Offset Field

Used to indicate the position of the fragment within the original packet, enabling proper reassembly at the destination.

### The TTL Field

The Time To Live (TTL) field is used to prevent packets from looping indefinitely around the network. Each time a router forwards a packet, its TTL is decremented by 1, and if it reaches 0, the packet is dropped.

**Key Functions:**

- Prevents infinite loops in routing
- Each router decrements TTL by 1
- Packets with TTL=0 are discarded
- Helps prevent network congestion from looping packets

### The Protocol Field

The Protocol field indicates the type of message encapsulated inside of the packet, such as ICMP, TCP, UDP, or OSPF.

**Common Protocol Values:**

- **1**: ICMP (Internet Control Message Protocol)
- **6**: Transmission Control Protocol (TCP)
- **17**: User Datagram Protocol (UDP)
- **89**: Open Shortest Path First (OSPF)

### The Header Checksum Field

The Header Checksum field is used to check for errors in the IPv4 header. This ensures data integrity during transmission.

### The Source Address and Destination Address Fields

Contains the IPv4 address of the host that sent the packet and the IPv4 address of the packet's intended recipient:

- **Source Address**: Contains the host IP address of the sender
- **Destination Address**: Contains the recipient IP address

### The Options Field

The Options field is optional and variable in length—from 0 bytes (if not used) to a maximum of 40 bytes in length. This field is rarely used in modern networks.

## The Binary Number System

To understand binary numbers, you must first understand decimal numbers. The decimal number system uses 10 digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. It is also called base 10. The value of each digit position increases tenfold: 1, 10, 100, 1000, etc.

### Decimal Number System

The decimal number system uses 10 digits, 0-9. Therefore it is called base 10. Each position represents a power of 10.

### Binary Number System

The binary number system uses two digits: 0 and 1. Therefore it is called base 2. The value of each digit position increases twofold: 1, 2, 4, 8, 16, 32, 64, 128, etc.

An 8-bit binary number provides 256 possible values: from 0d0 (00000000) to 0d255 (11111111). For the CCNA exam, you must be able to convert between binary and decimal for numbers of up to 8 bits in length. You can practice at [Cisco's Binary Game](https://learningnetwork.cisco.com/s/binary-game).

| Dec. | Bin. | Dec. | Bin. | Dec. | Bin. | Dec. | Bin. |
|---:|:---:|---:|:---:|---:|:---:|---:|:---:|
| 0 | `00000000` | 64 | `01000000` | 128 | `10000000` | 192 | `11000000` |
| 1 | `00000001` | 65 | `01000001` | 129 | `10000001` | 193 | `11000001` |
| 2 | `00000010` | 66 | `01000010` | 130 | `10000010` | 194 | `11000010` |
| 3 | `00000011` | 67 | `01000011` | 131 | `10000011` | 195 | `11000011` |
| 4 | `00000100` | 68 | `01000100` | 132 | `10000100` | 196 | `11000100` |
| 5 | `00000101` | 69 | `01000101` | 133 | `10000101` | 197 | `11000101` |
| 6 | `00000110` | 70 | `01000110` | 134 | `10000110` | 198 | `11000110` |
| 7 | `00000111` | 71 | `01000111` | 135 | `10000111` | 199 | `11000111` |
| 8 | `00001000` | 72 | `01001000` | 136 | `10001000` | 200 | `11001000` |
| 9 | `00001001` | 73 | `01001001` | 137 | `10001001` | 201 | `11001001` |
| 10 | `00001010` | 74 | `01001010` | 138 | `10001010` | 202 | `11001010` |
| 11 | `00001011` | 75 | `01001011` | 139 | `10001011` | 203 | `11001011` |
| 12 | `00001100` | 76 | `01001100` | 140 | `10001100` | 204 | `11001100` |
| 13 | `00001101` | 77 | `01001101` | 141 | `10001101` | 205 | `11001101` |
| 14 | `00001110` | 78 | `01001110` | 142 | `10001110` | 206 | `11001110` |
| 15 | `00001111` | 79 | `01001111` | 143 | `10001111` | 207 | `11001111` |
| 16 | `00010000` | 80 | `01010000` | 144 | `10010000` | 208 | `11010000` |
| 17 | `00010001` | 81 | `01010001` | 145 | `10010001` | 209 | `11010001` |
| 18 | `00010010` | 82 | `01010010` | 146 | `10010010` | 210 | `11010010` |
| 19 | `00010011` | 83 | `01010011` | 147 | `10010011` | 211 | `11010011` |
| 20 | `00010100` | 84 | `01010100` | 148 | `10010100` | 212 | `11010100` |
| 21 | `00010101` | 85 | `01010101` | 149 | `10010101` | 213 | `11010101` |
| 22 | `00010110` | 86 | `01010110` | 150 | `10010110` | 214 | `11010110` |
| 23 | `00010111` | 87 | `01010111` | 151 | `10010111` | 215 | `11010111` |
| 24 | `00011000` | 88 | `01011000` | 152 | `10011000` | 216 | `11011000` |
| 25 | `00011001` | 89 | `01011001` | 153 | `10011001` | 217 | `11011001` |
| 26 | `00011010` | 90 | `01011010` | 154 | `10011010` | 218 | `11011010` |
| 27 | `00011011` | 91 | `01011011` | 155 | `10011011` | 219 | `11011011` |
| 28 | `00011100` | 92 | `01011100` | 156 | `10011100` | 220 | `11011100` |
| 29 | `00011101` | 93 | `01011101` | 157 | `10011101` | 221 | `11011101` |
| 30 | `00011110` | 94 | `01011110` | 158 | `10011110` | 222 | `11011110` |
| 31 | `00011111` | 95 | `01011111` | 159 | `10011111` | 223 | `11011111` |
| 32 | `00100000` | 96 | `01100000` | 160 | `10100000` | 224 | `11100000` |
| 33 | `00100001` | 97 | `01100001` | 161 | `10100001` | 225 | `11100001` |
| 34 | `00100010` | 98 | `01100010` | 162 | `10100010` | 226 | `11100010` |
| 35 | `00100011` | 99 | `01100011` | 163 | `10100011` | 227 | `11100011` |
| 36 | `00100100` | 100 | `01100100` | 164 | `10100100` | 228 | `11100100` |
| 37 | `00100101` | 101 | `01100101` | 165 | `10100101` | 229 | `11100101` |
| 38 | `00100110` | 102 | `01100110` | 166 | `10100110` | 230 | `11100110` |
| 39 | `00100111` | 103 | `01100111` | 167 | `10100111` | 231 | `11100111` |
| 40 | `00101000` | 104 | `01101000` | 168 | `10101000` | 232 | `11101000` |
| 41 | `00101001` | 105 | `01101001` | 169 | `10101001` | 233 | `11101001` |
| 42 | `00101010` | 106 | `01101010` | 170 | `10101010` | 234 | `11101010` |
| 43 | `00101011` | 107 | `01101011` | 171 | `10101011` | 235 | `11101011` |
| 44 | `00101100` | 108 | `01101100` | 172 | `10101100` | 236 | `11101100` |
| 45 | `00101101` | 109 | `01101101` | 173 | `10101101` | 237 | `11101101` |
| 46 | `00101110` | 110 | `01101110` | 174 | `10101110` | 238 | `11101110` |
| 47 | `00101111` | 111 | `01101111` | 175 | `10101111` | 239 | `11101111` |
| 48 | `00110000` | 112 | `01110000` | 176 | `10110000` | 240 | `11110000` |
| 49 | `00110001` | 113 | `01110001` | 177 | `10110001` | 241 | `11110001` |
| 50 | `00110010` | 114 | `01110010` | 178 | `10110010` | 242 | `11110010` |
| 51 | `00110011` | 115 | `01110011` | 179 | `10110011` | 243 | `11110011` |
| 52 | `00110100` | 116 | `01110100` | 180 | `10110100` | 244 | `11110100` |
| 53 | `00110101` | 117 | `01110101` | 181 | `10110101` | 245 | `11110101` |
| 54 | `00110110` | 118 | `01110110` | 182 | `10110110` | 246 | `11110110` |
| 55 | `00110111` | 119 | `01110111` | 183 | `10110111` | 247 | `11110111` |
| 56 | `00111000` | 120 | `01111000` | 184 | `10111000` | 248 | `11111000` |
| 57 | `00111001` | 121 | `01111001` | 185 | `10111001` | 249 | `11111001` |
| 58 | `00111010` | 122 | `01111010` | 186 | `10111010` | 250 | `11111010` |
| 59 | `00111011` | 123 | `01111011` | 187 | `10111011` | 251 | `11111011` |
| 60 | `00111100` | 124 | `01111100` | 188 | `10111100` | 252 | `11111100` |
| 61 | `00111101` | 125 | `01111101` | 189 | `10111101` | 253 | `11111101` |
| 62 | `00111110` | 126 | `01111110` | 190 | `10111110` | 254 | `11111110` |
| 63 | `00111111` | 127 | `01111111` | 191 | `10111111` | 255 | `11111111` |

### Converting Binary Numbers to Decimal

Each bit represents a number with the following values:
128 64 32 16 8 4 2 1

Add up the values of the bits that are set to 1:
00101111 = 32 + 8 + 4 + 2 + 1 = 47

The minimum value is 0 and the maximum is 255.

### Converting Decimal Numbers to Binary

#### Method 1: Subtraction

Subtracting 128 from 206 gives a remainder of 78. Write a 1 in the 128 position.
Subtracting 64 from 78 gives a remainder of 14. Write a 1 in the 64 position.
32 cannot be subtracted from 14. Write a 0 in the 32 position.
16 cannot be subtracted from 14. Write a 0 in the 16 position.
Subtracting 8 from 14 gives a remainder of 6. Write a 1 in the 8 position.
Subtracting 4 from 6 gives a remainder of 2. Write a 1 in the 4 position.
Subtracting 2 from 2 gives a remainder of 0. Write a 1 in the 2 position.
We have reached 0, so write a 0 in the remaining position.

We now have the answer: 0d206 is equivalent to 0b11001110.

#### Method 2: Addition

0 + 128 = 128. Write a 1 in the 128 position.
128 + 64 = 192. Write a 1 in the 64 position.
192 + 32 = 224, which is greater than 206. Write a 0 in the 32 position.
192 + 16 = 208, which is greater than 206. Write a 0 in the 16 position.
192 + 8 = 200. Write a 1 in the 8 position.
200 + 4 = 204. Write a 1 in the 4 position.
204 + 2 = 206. Write a 1 in the 2 position.
We have reached the original value (206). Write a 0 in the remaining position.

Use [Cisco's Binary Game](https://learningnetwork.cisco.com/s/binary-game) to practice

## IPv4 Address Structure

An IPv4 address is a 32-bit number that identifies a host at Layer 3. It is divided into four groups of 8 bits called octets and written in dotted decimal notation. IPv4 addresses are divided into two parts: the network portion and the host portion. All hosts within a LAN will have the same network portion but a unique host portion.

### Prefix Length

The size of the network portion can be indicated with a prefix length in the format /X, where X is the number of bits in the network portion. Any bits that are not part of the network portion are part of the host portion.

**Examples:**

- If /24, the network portion is 24 bits and the host portion is 8 bits
- If /8, only the first octet is the network portion
- All hosts on the same LAN share the same network portion and have unique host portions

### Netmasks

The size of the network portion can also be indicated with a netmask (also called a subnet mask). A netmask is a string of 32 bits that is paired with an IP address to indicate which bits of the IP address are the network portion and which are the host portion.

A 1 in the netmask means the bit in the same position as the IP address is part of the network portion. A 0 in the netmask means the bit in the same position as the IP address is part of the host portion.

**Common Prefix Lengths and Netmasks:**

- Prefix length: /8 = netmask: 255.0.0.0
- Prefix length: /16 = netmask: 255.255.0.0
- Prefix length: /24 = netmask: 255.255.255.0

## Configuring IPv4 Addresses on a Router

An IP address must be assigned by the engineer or admin for the device. End hosts like a PC usually receive the IP automatically using DHCP, but routers are manually configured.

### Router Configuration Commands

- **show ip interface brief**: Lists a router's interface and information about their IP addresses and status
- **show ip interface [interface-name]**: Shows more detail about each interface
- **no shutdown**: Router interfaces are disabled by default and must be enabled with this command
- **interface interface-name**: Interface configuration mode can be accessed with this command from global configuration mode
- **ip address ip-address netmask**: An interface's IPv4 address can be configured with this command in interface configuration mode

## Attributes of an IPv4 Network

A few key attributes define any IPv4 network: the network address, broadcast address, maximum number of hosts, first usable address, and last usable address of the network.

### Network Address

The network address of a network is the first address of the network, with a host portion of all 0s. It is used to identify the network and cannot be assigned to a host. An IPv4 address is a network address if all the bits of its host portion are set to 0.

### Broadcast Address

The broadcast address of a network is the last address of the network, with a host portion of all 1s. It can be used to send a message to all hosts in the network. However, to send a message to all hosts on the local network, the address 255.255.255.255 is usually used. Can be identified if all bits of the host portion are set to 1.

### Maximum Number of Hosts

The maximum number of hosts of a network is the number of IP addresses that can be assigned to hosts. The formula is 2y − 2, where y is the number of bits in the host portion. Two is subtracted for the network and broadcast addresses.

### First and Last Usable Addresses

The first usable address of a network is the first address that can be assigned to a host. The last usable address is the last address that can be assigned to a host.

- **First Usable Address**: The first address after the network address (add one to the network address). This is often assigned to the router.
- **Last Usable Address**: Found by subtracting one from the broadcast address.

## IPv4 Address Classes

Originally all IPv4 addresses used /8 prefix, this was abandoned because you could not make enough new networks. To improve that system and allow for more networks of various sizes, IPv4 addresses were organized into five classes: class A, class B, class C, class D, and class E.

IPv4 addresses can be organized into five classes: A, B, C, D, and E. Class D is reserved for multicast addresses, and Class E is reserved for experimental purposes. Addresses from classes A, B, and C are assigned to network hosts.

| Class | First octet bit pattern | First octet decimal range | Prefix length | Note |
|---|---|---|---|---|
| A | 0xxxxxxx | 0–127 | /8 | Address range: 0.0.0.0–127.255.255.255 |
| B | 10xxxxxx | 128–191 | /16 | Address range: 128.0.0.0–191.255.255.255 |
| C | 110xxxxx | 192–223 | /24 | Address range: 192.0.0.0 to 223.255.255.255 |
| D | 1110xxxx | 224–239 |  | Reserved for multicast addresses |
| E | 1111xxxx | 240–255 |  | Reserved for experimental purposes |

Class A addresses have a first octet of 0–127 and use a /8 prefix length. Class B addresses have a first octet of 128–191 and use a /16 prefix length. Class C addresses have a first octet of 192–223 and use a /24 prefix length.

| Class | First octet | Size of network portion | Size of host portion | Number of networks | Addresses per network |
|---|---|---|---|---|---|
| A | 0xxxxxxx | 8 bits | 24 bits | 128 (2^7) | 16,777,216 (2^24) |
| B | 10xxxxxx | 16 bits | 16 bits | 16,384 (2^14) | 65,536 (2^16) |
| C | 110xxxxx | 24 bits | 8 bits | 2,097,152 (2^21) | 256 (2^8) |

Networks that follow class A, B, and C rules are called classful networks. This system is now obsolete and has been replaced with classless networking, which is more flexible.

### Special Address Ranges

- **0.0.0.0/8**: Any IP address that begins with the first octet 0 is reserved.
- **127.0.0.0/8**: This range is reserved for loopback addresses. A message sent to any IP address in this range (i.e., ping 127.0.0.1) will be looped back to the local host—the device you are working on—without being transmitted over the network. This can be used to test the networking software on the local device.

## Summary

Understanding IPv4 addressing is fundamental to network administration and troubleshooting:

- **IPv4 Header**: 20-60 bytes with 14 fields providing routing information
- **Version Field**: Indicates IPv4 (4) or IPv6 (6)
- **IHL Field**: Header length in 4-byte increments
- **DSCP/ECN Fields**: Quality of Service prioritization
- **Total Length**: Entire packet length in bytes
- **Fragmentation Fields**: Support for packets larger than MTU (1500 bytes standard)
- **TTL Field**: Prevents infinite loops, decremented by each router
- **Protocol Field**: Indicates encapsulated protocol (ICMP, TCP, UDP, OSPF)
- **Header Checksum**: Error detection for header integrity
- **Source/Destination**: IPv4 addresses of sender and recipient
- **Options Field**: Optional, rarely used (0-40 bytes)

**Binary System:**

- **Decimal**: Base 10 system with digits 0-9
- **Binary**: Base 2 system with digits 0-1
- **8-bit Range**: 0-255 (256 possible values)
- **Conversion**: Essential skill for CCNA exam

**IPv4 Addressing:**

- **32-bit Address**: Four octets in dotted decimal notation
- **Network/Host Portions**: Network portion shared, host portion unique
- **Prefix Length**: /X format indicates network portion size
- **Netmasks**: 32-bit string indicating network vs host bits

**Network Attributes:**

- **Network Address**: First address (host portion all 0s)
- **Broadcast Address**: Last address (host portion all 1s)
- **Maximum Hosts**: 2y - 2 formula (subtract network and broadcast)
- **Usable Addresses**: First and last assignable to hosts

**Address Classes:**

- **Class A**: 0-127, /8 prefix, large networks
- **Class B**: 128-191, /16 prefix, medium networks  
- **Class C**: 192-223, /24 prefix, small networks
- **Class D**: 224-239, multicast addresses
- **Class E**: 240-255, experimental purposes
- **Classful vs Classless**: Classful system obsolete, replaced by flexible classless networking

The IPv4 addressing system provides the foundation for modern network communication, enabling routers to forward packets efficiently across networks while supporting various network sizes and requirements.
