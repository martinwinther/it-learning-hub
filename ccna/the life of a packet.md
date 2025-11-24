# The Life of a Packet

## Overview

The life of a packet is the end to end path a data packet follows from a source host to a destination host. Along the way it is encapsulated, switched, routed, and de-encapsulated at different layers. Understanding this flow is core CCNA knowledge and helps explain how hosts, switches, and routers work together.

## Example topology

Example IPv4 topology:

- PC1: 192.168.1.10, in subnet 192.168.1.0/24
- PC3: 192.168.3.10, in subnet 192.168.3.0/24
- R1, R2, R3: routers that connect the subnets in between
- Switches: Layer 2 devices that connect end hosts to routers

PC1 and PC3 are on different subnets, so routers forward packets between them.

## High level flow

At a high level, the packet flow looks like this:

1. PC1 builds a packet and frame, then sends the frame to the local switch.
2. The switch forwards the frame to R1 based on MAC address learning.
3. R1, R2, and R3 forward the packet between subnets based on routing tables.
4. The last router sends a frame toward PC3.
5. PC3 receives the frame, removes headers, and delivers data to the application.

Throughout this process, only Layer 2 headers change at each hop while the Layer 3 source and destination IP addresses stay the same.

## Source host processing (PC1)

### Local vs remote decision

1. Application on PC1 creates data for PC3.
2. TCP or UDP adds a transport header with source and destination port numbers.
3. IP adds a header with:
   - Source IP: 192.168.1.10
   - Destination IP: 192.168.3.10
4. PC1 checks the IP and mask to see if the destination is local or remote.
5. Because 192.168.3.10 is not in 192.168.1.0/24, PC1 sends traffic to its default gateway.

### ARP for the default gateway

PC1 needs the MAC address of the default gateway interface on R1.

- If the MAC address is unknown, PC1 sends an ARP request:
  - Broadcast frame asking "Who has 192.168.1.1?"
- R1 replies with an ARP reply that includes its MAC address.
- PC1 adds the mapping to its ARP table.

Useful IOS commands on a router:

```cisco
show arp
debug arp
```

### Frame encapsulation on PC1

PC1 builds the Ethernet frame:

- Source MAC: PC1 MAC
- Destination MAC: R1 interface MAC
- EtherType: IPv4
- Payload: IP packet that contains the TCP or UDP segment and application data

The frame is sent to the access switch.

## Switch processing

### MAC learning and forwarding

The switch performs these actions:

1. Receives the frame on an access port.
2. Learns PC1 MAC and associates it with the incoming port.
3. Looks up the destination MAC in the MAC address table.
4. If the MAC address is known, forwards the frame out the correct port.
5. If the MAC address is unknown, floods the frame on all ports in the VLAN except the incoming port.

IOS commands on a switch:

```cisco
show mac address-table
show interfaces status
```

Eventually the frame reaches the router interface with the destination MAC address.

## Router processing at each hop

Each router hop follows the same basic pattern.

### De-encapsulation and routing lookup

When R1 receives the frame:

1. Checks the destination MAC and accepts the frame.
2. Removes the Ethernet header and trailer to expose the IP packet.
3. Examines the destination IP address 192.168.3.10.
4. Searches the routing table for the best matching route.
5. Selects a route to 192.168.3.0/24 with a next hop or outgoing interface.

The same logic applies on R2 and R3. Only the routing table entries and next hop values change.

Useful routing commands:

```cisco
show ip route
show ip route 192.168.3.10
```

### Next hop resolution and re-encapsulation

Once a route is chosen, the router needs a Layer 2 destination:

1. If the next hop is another router, ARP resolves that router MAC.
2. If the network is directly connected and the destination host is in that subnet, ARP resolves the host MAC.
3. The router builds a new frame:
   - Source MAC: outgoing interface MAC
   - Destination MAC: next hop router or end host MAC
   - Payload: same IP packet from the previous hop

IP source and destination addresses do not change. Only the Layer 2 header is replaced at each hop.

## Destination host processing (PC3)

When the final router sends the frame toward PC3:

1. PC3 receives the frame on its NIC.
2. Checks the destination MAC address and accepts the frame.
3. Removes the Ethernet header and trailer to expose the IP packet.
4. Verifies the destination IP is 192.168.3.10.
5. Passes the payload to TCP or UDP based on the IP protocol field.
6. Transport layer checks port numbers and delivers the data to the correct application.

This completes the packet life cycle from PC1 to PC3.

## Encapsulation and de-encapsulation by layer

### Encapsulation order

On the sending host:

1. Application data is created.
2. Transport layer adds a TCP or UDP header.
3. Network layer adds an IP header.
4. Data link layer adds an Ethernet header and trailer.
5. Physical layer converts the frame into bits on the wire or fiber.

### De-encapsulation order

On each router and on the final destination host:

1. Physical layer receives signals and rebuilds the frame.
2. Data link layer validates the frame and removes the Ethernet header and trailer.
3. Network layer checks the IP header and decides whether to route or deliver locally.
4. Transport layer checks ports and passes data to the correct application.

Routers perform full encapsulation and de-encapsulation at Layers 1 to 3, and forward packets without inspecting application payload in normal cases.

## Troubleshooting packet flow

### Common connectivity issues

- ARP problems
  - Wrong MAC address in ARP table
  - Missing or stale ARP entries

- Routing problems
  - No route to destination network
  - Incorrect default gateway
  - Wrong next hop address

- Switching problems
  - MAC address table not learning correctly
  - Frames flooded due to unknown MAC destinations

- Interface problems
  - Interface down or administratively down
  - Speed or duplex mismatches
  - Physical cabling issues

- ACL problems
  - ACL blocking traffic on an interface
  - ACL applied in the wrong direction

### Useful verification commands

```cisco
show arp
show ip route
show mac address-table
show interfaces
show ip interface
ping
traceroute
```

### Selected debug commands

Use debug commands with caution, especially on production devices.

```cisco
debug arp
debug ip packet
```

Stop debugging with:

```cisco
no debug all
```

## Quick review

- Source hosts decide local versus remote destinations using IP and mask and send remote traffic to a default gateway.  
- ARP maps IP addresses to MAC addresses on local segments and fills ARP tables on hosts and routers.  
- Switches learn MAC addresses, build MAC tables, and forward or flood frames based on destination MAC.  
- Routers remove Layer 2 headers, look up routes in the routing table, and build new frames for the next hop while keeping IP addresses unchanged.  
- Destination hosts remove headers in reverse order and deliver data to the correct application based on port numbers.  
- Key show commands include `show arp`, `show ip route`, `show mac address-table`, `show interfaces`, and basic tests with `ping` and `traceroute`.  
