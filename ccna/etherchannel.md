# EtherChannel

## Overview

EtherChannel combines multiple physical links into a single logical link, allowing redundant connections to remain active without causing Layer 2 loops. This maximizes bandwidth utilization, improves network resilience, and simplifies management by treating multiple physical ports as one logical interface.

## The Problem EtherChannel Solves

### STP Limitation

- STP blocks redundant links to prevent Layer 2 loops
- Adding multiple links between switches doesn't increase usable bandwidth if STP disables them
- Only one link remains active, creating a bottleneck

### EtherChannel Solution

- Combines multiple physical links into a single logical link
- STP treats the group of links as one unit, allowing all links to remain active
- Increases total bandwidth while maintaining loop-free topology
- Logical interfaces are called **port channels** in Cisco IOS

## How EtherChannel Works

### Logical Interface Creation

- Physical ports are grouped into a channel group
- A logical port channel interface (e.g., Port-channel1, Po1) is automatically created
- Frame-switching and STP logic treat all member ports as one entity
- STP output shows only port channel interfaces, not individual physical ports

### Loop Prevention

- BUM (Broadcast, Unknown unicast, Multicast) frames received on one member port are not flooded out of other ports in the same EtherChannel
- This prevents Layer 2 loops even though all ports can forward frames

### STP Integration

- EtherChannel does not eliminate the need for STP
- In larger LANs, some EtherChannels may still be blocked by STP to prevent loops
- STP cost calculation considers combined bandwidth of member ports

## EtherChannel Configuration Methods

### Dynamic EtherChannel

- Uses a protocol to negotiate EtherChannel formation between switches
- Protocols verify configuration parameters match before forming EtherChannel
- **Recommended approach**: Provides safety checks to prevent misconfiguration

### Static Configuration Method

- Forces EtherChannel formation without negotiation
- No protocol messages exchanged
- **Use with caution**: Higher risk of misconfiguration leading to loops
- Required in some cases (e.g., connecting to wireless LAN controllers)

## Port Aggregation Protocol (PAgP)

### PAgP Overview

- Cisco-proprietary EtherChannel negotiation protocol
- Supports up to 8 physical links in a single EtherChannel
- Uses two modes: **desirable** and **auto**

### PAgP Modes

- **desirable**: Actively attempts to form an EtherChannel by sending PAgP messages
- **auto**: Does not actively attempt to form an EtherChannel but responds to PAgP messages from a desirable-mode neighbor

### PAgP Mode Combinations

- **desirable + desirable** = EtherChannel forms
- **desirable + auto** = EtherChannel forms
- **auto + auto** = EtherChannel does not form

### PAgP Configuration

- Command: `channel-group <group-number> mode {desirable | auto}` in interface configuration mode
- Group number is locally significant (doesn't need to match on both switches)
- Example: `channel-group 1 mode desirable`

### PAgP Verification Commands

- `show etherchannel summary`: View EtherChannel status and flags
- `show pagp neighbor`: View information about PAgP neighbors

## Link Aggregation Control Protocol (LACP)

### LACP Overview

- IEEE standard (802.3ad) EtherChannel negotiation protocol
- Supports up to 16 physical links in a single EtherChannel
- Only up to 8 links can be active simultaneously; remaining links act as standby (hot-standby)
- Can run on any vendor's switches (not Cisco-only)

### LACP Modes

- **active**: Actively attempts to form an EtherChannel by sending LACP messages (equivalent to PAgP desirable)
- **passive**: Does not actively attempt to form an EtherChannel but responds to LACP messages from an active-mode neighbor (equivalent to PAgP auto)

### LACP Mode Combinations

- **active + active** = EtherChannel forms
- **active + passive** = EtherChannel forms
- **passive + passive** = EtherChannel does not form

### LACP Configuration

- Command: `channel-group <group-number> mode {active | passive}` in interface configuration mode
- Example: `channel-group 1 mode active`

### LACP Verification Commands

- `show etherchannel summary`: View EtherChannel status and flags
- `show lacp neighbor`: View information about LACP neighbors

## Static EtherChannel

### Static EtherChannel Overview

- No negotiation protocol used
- Both sides must be configured in **on** mode
- Forms EtherChannel regardless of neighboring device state
- Higher risk of misconfiguration

### Static EtherChannel Configuration

- Command: `channel-group <group-number> mode on` in interface configuration mode
- Both switches must use **on** mode for EtherChannel to form

### When to Use

- Required for some devices (e.g., wireless LAN controllers)
- Not recommended for general use; prefer dynamic protocols

## EtherChannel Mode Compatibility

### Valid Combinations

| Mode 1 | Mode 2 | Result |
|--------|--------|--------|
| Desirable | Desirable | Yes |
| Desirable | Auto | Yes |
| Auto | Auto | No |
| Active | Active | Yes |
| Active | Passive | Yes |
| Passive | Passive | No |
| On | On | Yes |

### Invalid Combinations

- PAgP modes (desirable/auto) cannot form EtherChannel with LACP modes (active/passive)
- Dynamic modes (PAgP/LACP) cannot form EtherChannel with static mode (on)
- Protocols are like languages: devices must use the same protocol to communicate

## Port Configuration Requirements

### Settings That Must Match

All ports in the same EtherChannel must have identical settings:

- **Speed**: All ports must operate at the same speed
- **Duplex**: All ports must use the same duplex setting
- **Operational mode**: All ports must be access or trunk (cannot mix)
- **Allowed VLANs**: When in trunk mode, allowed VLANs must match
- **Native VLAN**: When in trunk mode, native VLAN must match
- **Access VLAN**: When in access mode, access VLAN must match

### Configuration Inheritance

- Commands configured on the port channel interface are inherited by member ports
- Commands configured on member ports are inherited by the port channel interface
- **Best practice**: Configure settings on the port channel interface after EtherChannel is formed
- Configuring member ports directly can cause the EtherChannel to flap (briefly go down)

### Suspended Ports

- If a port's settings don't match other ports in the EtherChannel, it enters a **suspended** state
- Suspended ports cannot participate in the EtherChannel or forward frames
- Port automatically recovers when settings match other member ports

## EtherChannel Load Balancing

### Load Balancing by Flow

- Frames are load-balanced over physical links by **flow**
- A **flow** is a communication between two nodes
- All frames in the same flow use the same physical link
- Different flows can use different links

### Load Balancing Parameters

- Configure with `port-channel load-balance <parameters>` in global configuration mode
- Common parameters:
  - `src-mac`: Source MAC address
  - `dst-mac`: Destination MAC address
  - `src-dst-mac`: Combination of source and destination MAC addresses
  - `src-ip`: Source IP address (for encapsulated IP packets)
  - `dst-ip`: Destination IP address (for encapsulated IP packets)
  - `src-dst-ip`: Combination of source and destination IP addresses (default on many switches)

### Non-IP Traffic

- For frames that don't encapsulate IP packets, switches use MAC address-based load balancing
- Typically uses source XOR destination MAC address

### Verification

- `show etherchannel load-balance`: View current load-balancing parameters

### Load Balancing Considerations

- Load balancing may not always distribute traffic evenly across all links
- Changing parameters can help improve distribution
- Example: Using only destination MAC address may cause all traffic to default gateway to use same link

## Bandwidth vs Speed

### Bandwidth

- Total number of bits that can be transferred per second
- EtherChannel bandwidth = sum of all member link bandwidths
- Example: Four 1 Gbps links = 4 Gbps total bandwidth

### Speed

- Maximum speed of any individual communication
- Adding links doesn't increase individual link speed
- Example: Four 1 Gbps links still means each flow maxes at 1 Gbps

### Analogy

- Like adding lanes to a highway: increases total capacity but doesn't change speed limit
- Can reduce congestion, allowing traffic to flow at maximum speed more consistently

## Layer 2 vs Layer 3 EtherChannels

### Layer 2 EtherChannel

- Consists of switch ports that switch frames
- Most common use case
- Provides redundancy and increased bandwidth for inter-switch links
- STP treats as single logical port
- Configured with `switchport mode {access | trunk}` on port channel interface

### Layer 3 EtherChannel

- Consists of routed ports that route packets
- Used on multilayer switches or routers
- Provides load balancing and simplified management for Layer 3 connections
- No STP involvement (routed ports don't cause Layer 2 loops)
- Configuration steps:
  1. Use `no switchport` on member ports before adding to EtherChannel
  2. Add ports to channel group: `channel-group <group-number> mode {active | passive | on}`
  3. Configure IP address on port channel interface (not member ports)

### Layer 3 EtherChannel Benefits

- Load-balance packets over multiple links
- Easier management: configure IP addressing and routing for one logical interface
- Simplified routing table entries

## Verification Commands

### General EtherChannel Status

- `show etherchannel summary`: View all EtherChannels, protocols, member ports, and status flags
- `show interfaces port-channel <number>`: View detailed information about a specific port channel interface
- `show spanning-tree`: View STP status (shows port channel interfaces, not member ports)

### Protocol-Specific Commands

- `show pagp neighbor`: View PAgP neighbor information
- `show lacp neighbor`: View LACP neighbor information

### Load Balancing

- `show etherchannel load-balance`: View current load-balancing parameters

### Status Flags

Common flags in `show etherchannel summary` output:

- **D**: Down
- **P**: Bundled in port-channel
- **I**: Stand-alone (independent)
- **s**: Suspended
- **H**: Hot-standby (LACP only)
- **R**: Layer 3 EtherChannel
- **S**: Layer 2 EtherChannel
- **U**: In use (operational)

## Troubleshooting EtherChannel

### Common Issues

- **EtherChannel not forming**: Check that both sides use compatible modes (same protocol, valid combination)
- **Ports suspended**: Verify all member ports have matching settings (speed, duplex, mode, VLANs)
- **Uneven load distribution**: Review load-balancing parameters; consider changing to better distribute traffic
- **EtherChannel flaps**: Avoid configuring member ports directly; use port channel interface instead

### Best Practices

- Use dynamic EtherChannel (PAgP or LACP) instead of static when possible
- Configure settings on port channel interface after EtherChannel is formed
- Ensure all member ports have identical settings before adding to EtherChannel
- Use LACP for multi-vendor environments
- Verify EtherChannel status with `show etherchannel summary` after configuration

## Real-World Applications

- **Data center inter-switch links**: Maximize bandwidth between core switches
- **Access layer redundancy**: Provide redundant paths from access switches to distribution layer
- **Server connectivity**: Aggregate multiple links to high-traffic servers
- **Multi-vendor environments**: Use LACP for interoperability between different switch vendors
- **Layer 3 redundancy**: Use Layer 3 EtherChannels for redundant routed connections

## Summary

- EtherChannel combines multiple physical links into a single logical link, allowing all links to remain active
- Dynamic EtherChannels use PAgP (Cisco-proprietary) or LACP (IEEE standard) to negotiate formation
- PAgP supports up to 8 links; LACP supports up to 16 links (8 active, 8 standby)
- Static EtherChannels use **on** mode but are not recommended due to safety concerns
- All member ports must have matching settings (speed, duplex, mode, VLANs)
- Frames are load-balanced by flow over physical links
- Layer 2 EtherChannels are for switch ports; Layer 3 EtherChannels are for routed ports
- Configure settings on port channel interface to ensure consistency and prevent flapping
- EtherChannel increases total bandwidth but not individual link speed
- Always verify EtherChannel status and use dynamic protocols when possible
