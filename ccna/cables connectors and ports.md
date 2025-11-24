# Cables, Connectors and Ports

## Overview

Ethernet is the standard for most wired LANs. It covers physical media, connectors, signaling, and how bits move between devices. For CCNA, focus on cable types, speeds, distances, and where each is used.

## Network standards

### Communication requirements

For two devices to communicate, they must agree on:

- How to format data on the wire
- Cable and connector specifications
- Signaling method on the medium (electrical or optical)
- Rules for sending and receiving

### IEEE standards

The IEEE 802 working groups define LAN and wireless standards.

Key families:

- **IEEE 802.3**: Ethernet over copper and fiber
- **IEEE 802.11**: Wi-Fi

Ethernet is a family of related standards under IEEE 802.3. It specifies both the physical layer details and how bits are encoded on the link.

## Binary communication

### Bits and bytes

- **Bit**: smallest unit, 0 or 1
- **Byte**: 8 bits
- All data sent on a link is a stream of bits.

### Signaling on copper

On copper, bits are represented by changes in voltage on the wire pairs. Network adapters convert frames into electrical signals and back again.

### Speed units

Network speed is measured in bits per second.

- **Kbps**: kilobit per second, 1,000 bits per second
- **Mbps**: megabit per second, 1,000 Kbps
- **Gbps**: gigabit per second, 1,000 Mbps
- **Tbps**: terabit per second, 1,000 Gbps

## Copper UTP connections

Most Ethernet LAN links use copper unshielded twisted pair (UTP) with 8P8C connectors, often called RJ45.

### UTP cable construction

#### Connectors

- **8P8C (RJ45)**: 8 positions, 8 contacts
- Plugs on cable ends, jacks on devices and patch panels

#### Cable types

- **UTP (Unshielded Twisted Pair)**
  - No metal shielding
  - Pairs of wires are twisted to reduce electromagnetic interference (EMI)
- **STP (Shielded Twisted Pair)**
  - Has additional shielding to reduce EMI
  - Used in more noisy environments

Each cable has 8 individual conductors arranged as 4 twisted pairs.

### IEEE 802.3 copper standards

| Speed    | Ethernet name       | IEEE task group | Informal name | Maximum cable length |
|----------|---------------------|-----------------|---------------|----------------------|
| 10 Mbps  | Ethernet            | 802.3           | 10BASE-T      | 100 m                |
| 100 Mbps | Fast Ethernet       | 802.3u          | 100BASE-T     | 100 m                |
| 1 Gbps   | Gigabit Ethernet    | 802.3ab         | 1000BASE-T    | 100 m                |
| 10 Gbps  | 10 Gigabit Ethernet | 802.3an         | 10GBASE-T     | 100 m                |

All UTP-based Ethernet standards listed here support 100 meters maximum per segment. Longer runs need fiber or repeaters.

### Cable categories

Higher speeds require newer cable categories.

| Speed    | Ethernet informal name | Typical cable category |
|----------|------------------------|------------------------|
| 10 Mbps  | 10BASE-T               | Cat 3                  |
| 100 Mbps | 100BASE-T              | Cat 5                  |
| 1 Gbps   | 1000BASE-T             | Cat 5e or Cat 6        |
| 10 Gbps  | 10GBASE-T              | Cat 6a or better       |

Real networks often deploy Cat 5e, Cat 6, or Cat 6a for new installations.

### Wire pair usage and pins

#### Pairs used

- **10BASE-T and 100BASE-T**
  - Use 2 of the 4 wire pairs
- **1000BASE-T and 10GBASE-T**
  - Use all 4 pairs

#### Straight-through and crossover

For 10BASE-T and 100BASE-T, only two pairs carry data.

**Straight-through cable**

- Pins 1 and 2 on one end connect to pins 1 and 2 on the other
- Pins 3 and 6 on one end connect to pins 3 and 6 on the other
- Used between different device types (PC to switch, router to switch)

**Crossover cable**

- Pins 1 and 2 on one end connect to pins 3 and 6 on the other end
- Swaps transmit and receive pairs
- Traditionally used to connect similar devices directly (switch to switch, PC to PC, router to router)

#### Device pin roles (10/100 Mbps)

| Device type | Transmit (Tx) pins | Receive (Rx) pins |
|-------------|--------------------|-------------------|
| Router      | 1 and 2            | 3 and 6           |
| Firewall    | 1 and 2            | 3 and 6           |
| PC/Server   | 1 and 2            | 3 and 6           |
| Switch      | 3 and 6            | 1 and 2           |

This is why straight-through works for PC to switch and why crossover was required between similar device types at 10/100 Mbps.

#### Auto MDI-X

Modern switches and NICs support Auto MDI-X.

- Interface detects whether transmit and receive need to be swapped
- Automatically adjusts pin roles
- Removes the need to worry about straight-through versus crossover in most cases

## Fiber-optic connections

Copper UTP is limited to 100 meters and is sensitive to EMI. For longer runs and higher immunity to interference, fiber-optic cables are used.

### Fiber signaling

- Uses light instead of electrical voltage
- Light travels through a glass (or plastic) core
- Requires careful handling because of the delicate fibers

### Duplex operation and transceivers

- Typical Ethernet fiber links use two strands
  - One strand for transmit
  - One strand for receive
- Network devices use pluggable transceivers, for example **SFP** modules
- Correct pairing of transmit to receive between devices is required

### Fiber cable structure

Layers in a typical fiber cable:

1. **Core**: glass that carries the light
2. **Cladding**: reflects light back into the core
3. **Buffer**: protects the fiber
4. **Outer jacket**: mechanical protection

### Fiber types

#### Multimode fiber (MMF)

- Uses LED-based optics
- Typical distances: up to a few hundred meters depending on speed and grade
- Lower cost than single-mode

#### Single-mode fiber (SMF)

- Uses laser-based optics
- Supports distances of many kilometers
- Transceivers and cabling are more expensive than MMF

SMF supports longer distances than MMF but with higher optics cost.

## UTP versus fiber

### Cost and distance

- UTP
  - Lower cable and interface cost
  - Distance limit of 100 meters per segment
- Fiber
  - Higher cost, mainly due to SFP or other optics
  - Much longer supported distances

### Typical usage

**UTP use cases**

- End host to access switch
- Short runs in offices and wiring closets
- Most client devices have only RJ45 copper ports

**Fiber use cases**

- Switch to switch uplinks
- Links between floors and buildings
- Data center aggregation and core
- Where higher speeds and longer distances are needed

### EMI and security

- UTP
  - Susceptible to electromagnetic interference
  - Can leak signals into nearby cables or equipment
- Fiber
  - Immune to EMI
  - Does not radiate signals, which improves security and reliability

## Real-world patterns

### Small office and home

- Mostly Cat 5e or Cat 6 UTP
- Few links approach 100 meters
- Switches and routers often have only RJ45 ports

### Enterprise networks

- UTP from access switches to users
- Fiber for uplinks, building risers, and backbone
- Higher speeds and more redundancy in core and distribution layers

### Data centers

- Mixed copper and fiber, heavy use of fiber in aggregation and core
- 10 Gbps and higher speeds are common
- Often multiple paths and redundant links

## Quick review

- IEEE 802.3 defines Ethernet over copper and fiber.
- Bits are sent as voltage changes on copper and as light on fiber.
- UTP uses twisted pairs to reduce EMI and RJ45 connectors to terminate cables.
- 10/100BASE-T use 2 pairs and 1000BASE-T and above use all 4 pairs.
- Straight-through versus crossover mattered at 10/100 Mbps but Auto MDI-X has mostly removed this concern.
- Fiber is used where 100 meters is not enough or EMI immunity is important.
- MMF uses LEDs for medium distances, SMF uses lasers for long distances.
- UTP is cheaper and common to end hosts, fiber is common for infrastructure links and long runs.