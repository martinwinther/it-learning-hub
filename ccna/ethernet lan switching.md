# Ethernet LAN Switching

## Overview

Ethernet LAN switching is a fundamental concept in computer networking that enables efficient communication within local area networks. Switches operate at Layer 2 (Data Link Layer) of the OSI model and use MAC addresses to make intelligent forwarding decisions, creating dedicated communication paths between devices and improving network performance compared to older hub-based networks.

## Ethernet Fundamentals

### What is Ethernet?

Ethernet is a family of networking technologies defined by IEEE 802.3 standards that govern how devices communicate over wired connections. It specifies both the physical characteristics of cables and connectors as well as the data formatting rules for communication.

### Ethernet Frame Structure

Ethernet frames contain several key components:

- **Preamble**: Synchronization pattern (7 bytes)
- **Start Frame Delimiter**: Marks beginning of frame (1 byte)
- **Destination MAC Address**: Target device address (6 bytes)
- **Source MAC Address**: Sending device address (6 bytes)
- **EtherType/Length**: Protocol type or frame length (2 bytes)
- **Data**: Actual payload (46-1500 bytes)
- **Frame Check Sequence**: Error detection (4 bytes)

### MAC Addresses

Media Access Control (MAC) addresses are unique 48-bit identifiers assigned to network interfaces:

- **Format**: 12 hexadecimal digits (e.g., 00:1A:2B:3C:4D:5E)
- **Organizationally Unique Identifier (OUI)**: First 3 bytes identify manufacturer
- **Device Identifier**: Last 3 bytes are unique to the device
- **Unicast vs Multicast**: First bit determines address type
- **Locally Administered**: Second bit indicates if address is locally assigned

## Switching Concepts

### How Switches Work

Switches learn MAC addresses by examining the source address of incoming frames and maintain a MAC address table (also called CAM table) that maps MAC addresses to switch ports.

#### Learning Process

1. **Frame Reception**: Switch receives frame on a port
2. **Source Learning**: Switch records source MAC address and port in MAC table
3. **Destination Lookup**: Switch checks MAC table for destination address
4. **Forwarding Decision**: Switch forwards frame based on lookup result

#### Forwarding Decisions

- **Known Unicast**: Forward frame to specific port
- **Unknown Unicast**: Flood frame to all ports except source port
- **Broadcast**: Flood frame to all ports except source port
- **Multicast**: Forward based on multicast configuration

### MAC Address Table

The MAC address table contains dynamic entries learned from traffic and static entries configured by administrators:

#### Dynamic Entries

- **Learning**: Automatically populated from frame source addresses
- **Aging**: Entries expire after inactivity (default 300 seconds)
- **Port Movement**: Entries update when devices move to different ports

#### Static Entries

- **Manual Configuration**: Administratively configured entries
- **Permanent**: Never age out
- **Security**: Prevents unauthorized devices on specific ports

### Switch Operation Modes

#### Store-and-Forward

- **Process**: Receives entire frame before forwarding
- **Error Checking**: Validates frame integrity
- **Latency**: Higher due to complete frame reception
- **Reliability**: Better error detection

#### Cut-Through

- **Process**: Begins forwarding after reading destination address
- **Speed**: Lower latency
- **Error Handling**: Limited error detection
- **Performance**: Faster but less reliable

#### Fragment-Free

- **Process**: Reads first 64 bytes before forwarding
- **Compromise**: Balance between speed and error detection
- **Collision Detection**: Catches most errors in first 64 bytes

## VLANs (Virtual LANs)

### VLAN Concepts

Virtual LANs logically segment a physical switch into multiple broadcast domains, allowing network administrators to group devices regardless of their physical location.

#### Benefits

- **Security**: Isolate traffic between different groups
- **Performance**: Reduce broadcast domain size
- **Flexibility**: Group devices by function rather than location
- **Management**: Easier network administration

#### VLAN Types

- **Data VLANs**: Carry user-generated traffic
- **Voice VLANs**: Dedicated to IP telephony traffic
- **Management VLANs**: Used for switch management traffic
- **Native VLANs**: Default VLAN for untagged traffic

### VLAN Configuration

#### Creating VLANs

```text
Switch(config)# vlan 10
Switch(config-vlan)# name Sales
Switch(config-vlan)# exit
Switch(config)# vlan 20
Switch(config-vlan)# name Engineering
```

#### Assigning Ports to VLANs

```text
Switch(config)# interface fastethernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
Switch(config-if)# exit
```

#### VLAN Trunking

Trunk ports carry traffic for multiple VLANs using VLAN tags:

- **802.1Q**: Industry standard for VLAN tagging
- **ISL**: Cisco proprietary (deprecated)
- **Native VLAN**: Untagged traffic on trunk ports

```text
Switch(config)# interface fastethernet 0/24
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30
```

## Spanning Tree Protocol (STP)

### Purpose

Spanning Tree Protocol prevents loops in redundant network topologies by creating a loop-free logical topology while maintaining redundancy.

#### Problems Without STP

- **Broadcast Storms**: Loops cause continuous frame forwarding
- **MAC Address Table Instability**: Constant table updates
- **Multiple Frame Copies**: Duplicate frames reaching destinations

### STP Operation

#### Root Bridge Election

- **Bridge ID**: Combination of priority and MAC address
- **Lowest Bridge ID**: Becomes root bridge
- **Priority**: Configurable (default 32768)
- **MAC Address**: Tiebreaker for equal priorities

#### Port States

- **Blocking**: Receives BPDUs but doesn't forward traffic
- **Listening**: Participates in STP but doesn't learn MAC addresses
- **Learning**: Learns MAC addresses but doesn't forward traffic
- **Forwarding**: Normal operation, forwards traffic
- **Disabled**: Administratively disabled

#### Port Roles

- **Root Port**: Best path to root bridge on each switch
- **Designated Port**: Best path on each segment
- **Blocked Port**: Prevents loops

### STP Variants

#### RSTP (Rapid Spanning Tree Protocol)

- **Faster Convergence**: Reduced from 30-50 seconds to 1-3 seconds
- **Port States**: Blocking, Learning, Forwarding
- **Port Roles**: Root, Designated, Alternate, Backup

#### MSTP (Multiple Spanning Tree Protocol)

- **Multiple Instances**: Different VLANs can use different trees
- **Load Balancing**: Traffic distribution across multiple paths
- **Complexity**: More configuration required

## Switch Security

### Port Security

Port security limits the number of MAC addresses allowed on a switch port:

#### Configuration

```text
Switch(config)# interface fastethernet 0/1
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 2
Switch(config-if)# switchport port-security violation shutdown
```

#### Violation Actions

- **Protect**: Drop frames from unknown MAC addresses
- **Restrict**: Drop frames and send SNMP trap
- **Shutdown**: Disable port and send SNMP trap

### DHCP Snooping

Prevents unauthorized DHCP servers from operating on the network:

```text
Switch(config)# ip dhcp snooping
Switch(config)# ip dhcp snooping vlan 10
Switch(config)# interface fastethernet 0/1
Switch(config-if)# ip dhcp snooping trust
```

### Dynamic ARP Inspection (DAI)

Validates ARP packets against DHCP snooping database:

```text
Switch(config)# ip arp inspection vlan 10
Switch(config)# interface fastethernet 0/1
Switch(config-if)# ip arp inspection trust
```

## Troubleshooting Switching Issues

### Common Problems

#### Connectivity Issues

- **Port Status**: Check if port is up/up
- **VLAN Assignment**: Verify correct VLAN configuration
- **Trunk Configuration**: Ensure proper trunk setup
- **STP Blocking**: Check for blocked ports

#### Performance Issues

- **Duplex Mismatch**: Verify duplex settings
- **Speed Mismatch**: Check speed configuration
- **Collision Domains**: Identify collision issues
- **Broadcast Storms**: Monitor broadcast traffic

### Useful Commands

#### Verification Commands

```text
Switch# show mac address-table
Switch# show vlan brief
Switch# show interfaces status
Switch# show spanning-tree
Switch# show port-security
```

#### Debugging Commands

```text
Switch# debug spanning-tree events
Switch# debug ethernet switching
Switch# show mac address-table dynamic
```

## Real-World Applications

### Small Office Networks

- **Basic Switching**: Simple VLAN segmentation
- **Port Security**: Prevent unauthorized access
- **STP**: Redundant uplinks to core switch

### Enterprise Networks

- **Advanced VLANs**: Department-based segmentation
- **Trunking**: Inter-switch VLAN communication
- **Security Features**: DHCP snooping, DAI, port security
- **Redundancy**: Multiple spanning tree instances

### Data Center Networks

- **High-Performance Switching**: Low-latency switching
- **Virtualization Support**: VM-aware switching
- **Advanced Features**: VXLAN, FabricPath
- **Scalability**: Large MAC address tables

## Summary

Ethernet LAN switching is essential for modern network operation:

- **MAC Address Learning**: Switches build forwarding tables automatically
- **VLAN Segmentation**: Logical network separation for security and performance
- **Loop Prevention**: STP prevents network loops while maintaining redundancy
- **Security Features**: Port security, DHCP snooping, and DAI protect networks
- **Performance Optimization**: Dedicated communication paths improve network efficiency

Understanding these concepts is crucial for CCNA certification and effective network administration, providing the foundation for building scalable, secure, and efficient local area networks.
