# The TCP/IP Networking Model

## Overview

Networking models describe the functions needed for communication between hosts. The main models are the OSI reference model and the TCP/IP model. OSI is used mostly for terminology and teaching, while TCP/IP matches how modern networks actually operate.

## Conceptual models of networking

### From vendor specific to open models

Early networks used proprietary stacks from individual vendors. Standard, vendor neutral models changed this by:

- Allowing devices from different vendors to interoperate
- Providing standard protocols at each layer
- Giving a common language for design and troubleshooting

### Layered structure

Networking models are divided into layers, each responsible for specific functions. Benefits of a layered model:

- Modularity between functions
- Clear separation of responsibilities
- Easier troubleshooting by isolating problems to layers
- Flexibility to change protocols at one layer without affecting others

## OSI reference model (seven layers)

The OSI model is a seven layer conceptual model defined by ISO. It is not used directly in production networks but remains important for language and exam questions.

| Layer | Name         | Main function                             |
|-------|--------------|--------------------------------------------|
| 7     | Application  | Network services to applications          |
| 6     | Presentation | Data format, translation, encryption      |
| 5     | Session      | Session setup and management              |
| 4     | Transport    | End to end transport, reliability         |
| 3     | Network      | Logical addressing and routing            |
| 2     | Data Link    | Framing, local delivery, error detection  |
| 1     | Physical     | Signaling, cabling, connectors            |

OSI layer numbers and names are still widely used when describing problems and protocols.

## TCP/IP model

The Internet Protocol Suite (TCP/IP) is the model used in real networks. It groups functions into fewer layers than OSI.

### Four layer and five layer views

Two common views of the TCP/IP model:

- Four layer: Link, Internet, Transport, Application
- Five layer (used in many CCNA discussions):
  - Layer 1: Physical
  - Layer 2: Data Link
  - Layer 3: Network
  - Layer 4: Transport
  - Layer 7: Application

The five layer view aligns layer numbers with OSI, which keeps the familiar Layer 1 to Layer 7 terminology.

### OSI to TCP/IP mapping

| OSI layers             | TCP/IP (5 layer) | Example protocols          |
|------------------------|------------------|----------------------------|
| 7 Application          | Application      | HTTP, HTTPS, FTP, SSH      |
| 6 Presentation         | Application      |                            |
| 5 Session              | Application      |                            |
| 4 Transport            | Transport        | TCP, UDP                   |
| 3 Network              | Network          | IPv4, IPv6                 |
| 2 Data Link            | Data Link        | Ethernet, 802.11 (Wi-Fi)   |
| 1 Physical             | Physical         | Copper, fiber, radio       |

## TCP/IP layer functions

The goal of the TCP/IP model is to allow an application on one host to communicate with an application on another host. Each layer has its own role in that path.

### Layer 1: Physical

- Defines physical media, connectors, and signaling
- Handles bit level transmission on cables, fiber, or radio
- Examples: UTP cabling, optical fiber, Wi-Fi radio parameters

### Layer 2: Data Link

- Provides local (hop to hop) delivery across a single link
- Uses MAC addresses for local addressing
- Defines frames, error detection, and media access rules
- Examples: Ethernet, 802.11 (Wi-Fi)

### Layer 3: Network

- Provides end to end delivery between hosts on different networks
- Uses logical addresses (IP addresses)
- Performs routing and path selection
- Supports subnetting and hierarchical addressing

Important addressing behavior:

- Destination MAC address can change at each hop
- Destination IP address remains the same from source to destination

### Layer 4: Transport

- Delivers data to the correct application process on the destination host
- Uses port numbers to identify application sessions
- May provide reliability and flow control (TCP) or simple, low overhead delivery (UDP)

Typical protocols:

- TCP – reliable, connection oriented, ordered delivery
- UDP – connectionless, no built in reliability, low overhead

### Layer 7: Application

- Interface between applications and the network
- Provides network services used by software
- Examples: HTTP, HTTPS, FTP, DNS, SSH

These protocols are not the applications themselves but services that applications use.

## Encapsulation and de-encapsulation

Data is encapsulated as it moves down the stack for transmission and de-encapsulated as it moves up the stack on reception.

### Encapsulation steps (sending host)

1. Application layer produces application data.
2. Transport layer adds a Layer 4 header (TCP or UDP) with source and destination ports. This forms a segment.
3. Network layer adds a Layer 3 header with source and destination IP addresses. This forms a packet.
4. Data Link layer adds a Layer 2 header and trailer with source and destination MAC addresses. This forms a frame.
5. Physical layer sends the bits that make up the frame across the medium.

The process of adding headers and trailers at each layer is encapsulation.

### De-encapsulation steps (receiving host)

1. Physical layer receives signals and rebuilds the bit stream.
2. Data Link layer reads and removes the Layer 2 header and trailer.
3. Network layer reads and removes the Layer 3 header.
4. Transport layer reads and removes the Layer 4 header.
5. Application layer processes the remaining data.

Each layer examines its own header, makes decisions, and passes the payload up to the next layer.

## Protocol Data Units (PDUs)

Each layer has a preferred name for its data unit.

- Segment – Layer 4 PDU (transport layer)
- Packet – Layer 3 PDU (network layer)
- Frame – Layer 2 PDU (data link layer)

Payload relationships:

- A frame contains a packet as its payload.
- A packet contains a segment as its payload.
- A segment contains application data as its payload.

## Layer interactions

### Adjacent layer interaction

Inside a host, each layer provides services to the layer above it:

- Layer 1 provides a medium for Layer 2 frames.
- Layer 2 delivers frames so that Layer 3 can move packets between hosts.
- Layer 3 delivers packets so that Layer 4 can manage end to end sessions.
- Layer 4 delivers data so that the Application layer can support user software.

### Same layer interaction

Same layers on different devices communicate using common protocols:

- Application to application using protocols such as HTTP or SSH
- Transport to transport using TCP or UDP headers and acknowledgments
- Network to network using IP headers and routing decisions
- Data Link to Data Link using frame formats and MAC addressing

The headers added by each layer carry information used by the matching layer on the other device.

## Quick review

- OSI is a seven layer conceptual model used for terminology; TCP/IP is the model used in real networks.  
- The five layer TCP/IP view maps to Physical, Data Link, Network, Transport, and Application layers.  
- Data is encapsulated as it moves down the stack and de-encapsulated as it moves up.  
- Layer 2 uses MAC addresses for local delivery; Layer 3 uses IP addresses for end to end delivery; Layer 4 uses port numbers for application delivery.  
- PDUs are called frames at Layer 2, packets at Layer 3, and segments at Layer 4, with each PDU carrying the higher layer PDU as its payload.  
- Adjacent layers interact inside a host, while same layers communicate between hosts using shared protocols.  
