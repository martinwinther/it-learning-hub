# Ethernet LAN Switching

## Overview

Ethernet LAN switching forwards frames inside a local network based on MAC addresses. Switches operate at Layer 2 and build a MAC address table that maps MAC addresses to ports. This allows efficient forwarding, separation of collision domains, and better performance than hubs.

## Ethernet fundamentals

### Ethernet definition

- Ethernet is defined by IEEE 802.3
- Specifies:
  - Physical media and signaling
  - Frame format and addressing
  - Basic access rules on a shared medium

### Ethernet frame fields

Key fields in an Ethernet frame:

- Destination MAC address
- Source MAC address
- EtherType or length
- Data
- Frame Check Sequence (FCS)

The switch uses destination MAC to decide where to forward. FCS is used to detect errors. Preamble and start frame delimiter exist on the wire but are not usually shown in command output.

### MAC addresses

- 48 bit identifiers written in hexadecimal
- Often shown as six byte pairs, for example `00:11:22:33:44:55`
- First part: Organizationally Unique Identifier (OUI), identifies the vendor
- Second part: device specific value
- Stored in network interface hardware but can be overridden in software
- Unicast, multicast, and broadcast types exist

## Switching behavior

### MAC address table

Switches keep a MAC address table (CAM table) that maps MAC addresses to ports and VLANs.

Each entry includes:

- MAC address
- Interface
- VLAN
- Type (dynamic or static)

Dynamic entries:

- Learned from sources of incoming frames
- Aged out after an idle timer (default 300 seconds on many switches)

Static entries:

- Manually configured
- Not aged out
- Used in some security and special cases

### Learning and forwarding

When a frame arrives:

1. Switch records the source MAC and incoming port in the MAC table
2. Switch looks up the destination MAC and VLAN in the table
3. If found (known unicast):
   - Frame is forwarded out the single matching port
4. If not found (unknown unicast):
   - Frame is flooded out all ports in the same VLAN except the incoming port

Broadcast frames are flooded to all ports in the VLAN except the source port. Multicast behavior is similar unless special multicast features are configured.

### Aging and movement

- If a device is silent, its MAC entry eventually ages out
- If a frame with a known MAC source arrives on a different port in the same VLAN, the switch updates the entry to the new port

## Switching methods

### Store and forward

- Receives the entire frame before forwarding
- Verifies FCS
- Drops frames with errors
- Higher latency than cut through but better error handling
- Default on modern Cisco switches

### Cut through

- Starts forwarding after reading destination MAC
- Lower latency
- Forwards bad frames because FCS is not checked before forwarding
- Less common in general purpose switches

### Fragment free

- Reads first 64 bytes before forwarding
- Catches most collision related errors
- Trade off between speed and error checking

## VLANs

### VLAN concepts

Virtual LANs split a switch into multiple Layer 2 broadcast domains.

Effects:

- Each VLAN has its own MAC table and broadcast domain
- Broadcasts stay inside a VLAN
- Devices in different VLANs need a router or Layer 3 switch to communicate

Benefits:

- Traffic isolation and basic security
- Smaller broadcast domains
- Flexible logical grouping of devices

### VLAN types

Common VLAN roles:

- Data VLAN
- Voice VLAN
- Management VLAN
- Native VLAN on trunks

VLAN 1 is the default VLAN on many Cisco switches but is often avoided for user traffic in production networks.

### Access ports

Access ports carry traffic for a single VLAN.

Basic configuration:

```text
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 10
```

The switch forwards untagged frames from this port in VLAN 10.

### Trunk ports and 802.1Q

Trunks carry traffic for multiple VLANs over one link.

- 802.1Q is the common tagging method
- Each frame carries a VLAN tag, except frames in the native VLAN

Basic trunk configuration:

```text
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

Notes:

- Native VLAN frames are sent untagged on the trunk
- Native VLAN should match on both sides of the trunk
- Only allowed VLANs can pass over the trunk

## Spanning Tree Protocol (STP)

### Purpose

Redundant links create Layer 2 loops. STP prevents loops by blocking some links while leaving redundancy available.

Problems without STP:

- Broadcast storms
- MAC table instability
- Multiple copies of frames

### Root bridge

STP selects a single root bridge.

- Each switch has a bridge ID (priority plus MAC)
- Lowest bridge ID becomes root
- Default priority is 32768
- Administrators usually lower priority on the desired root

### Port roles and states

Key roles:

- Root port
  - One per non root switch
  - Best path toward the root bridge
- Designated port
  - One per segment
  - Best path for that segment toward the root
- Alternate or blocked port
  - Backup path that does not forward user traffic

Common states in classic STP:

- Blocking
- Listening
- Learning
- Forwarding
- Disabled

RSTP (Rapid STP) collapses some states but the basic idea is the same: some ports forward while others block to prevent loops.

### STP variants

- STP (802.1D): original version
- RSTP (802.1w): faster convergence, default on many modern switches
- MSTP (802.1s): supports multiple instances mapped to VLANs

For CCNA, focus on the concepts of root bridge selection, port roles, and loop prevention. Detailed MSTP configuration is beyond the basics.

## Basic switch security

### Port security

Port security restricts what MAC addresses can use an access port.

Example:

```text
interface FastEthernet0/1
 switchport mode access
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation shutdown
```

Violation actions:

- Protect
- Restrict
- Shutdown

Port security is usually applied on access ports toward end hosts.

### DHCP snooping and DAI (brief)

- DHCP snooping:
  - Identifies trusted DHCP sources
  - Builds a binding table of IP, MAC, VLAN, and interface
- Dynamic ARP Inspection (DAI):
  - Uses the DHCP snooping binding table
  - Drops ARP messages that do not match

Detailed behavior of DHCP snooping and DAI is covered in separate notes. At switching level, remember they are features configured on access switches to protect against DHCP and ARP based attacks.

## Troubleshooting switching issues

### Common problems

- Port down or err disabled
- Wrong VLAN on access port
- Trunk not negotiated or wrong allowed VLAN list
- Port blocked by STP
- Duplex or speed mismatch

### Useful show commands

Typical checks:

```text
show mac address-table
show vlan brief
show interfaces status
show interfaces switchport
show spanning-tree
show port-security
```

These commands help confirm VLAN membership, trunk status, STP state, and learned MAC addresses.

## Quick review

- Switches forward frames using MAC address tables built from source addresses.
- Unknown unicast, broadcast, and some multicast frames are flooded within a VLAN.
- VLANs create separate broadcast domains on a switch. Inter VLAN traffic needs Layer 3 routing.
- Access ports carry one VLAN. Trunk ports carry multiple VLANs with 802.1Q tags and a native VLAN.
- STP prevents Layer 2 loops by blocking some ports and electing a root bridge.
- Basic switch security features include port security, DHCP snooping, and Dynamic ARP Inspection.
- Core troubleshooting uses show commands to check MAC tables, VLANs, interfaces, and STP.
