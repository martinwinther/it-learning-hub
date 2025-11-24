# First Hop Redundancy Protocols

## Overview

First Hop Redundancy Protocols (FHRPs) provide a redundant default gateway for hosts in a LAN. Multiple routers share a virtual default gateway, so if one router fails, another can take over without requiring changes on the hosts.

## Problem FHRPs solve

### Default gateway as single point of failure

- Hosts send traffic for remote networks to a default gateway
- Default gateway IP is configured manually or learned via DHCP
- Hosts ARP for the gateway IP and cache its MAC address
- If the gateway router or its interface fails, hosts lose connectivity to external networks

### Basic redundancy without FHRP

- Multiple routers can exist on the subnet
- Hosts still point at a single gateway IP
- Moving hosts to another router requires manual changes or new DHCP leases
- This is slow and error prone

FHRPs provide a virtual gateway that can move between routers automatically.

## FHRP operation

### Virtual IP address

- FHRP group shares a virtual IP (VIP)
- VIP is used as default gateway for hosts in the VLAN
- All routers in the group know the VIP
- Only the active router forwards traffic for the VIP

### Virtual MAC address

- Group also shares a virtual MAC address
- Active router responds to ARP for the VIP using the virtual MAC
- Hosts build an ARP entry mapping VIP to the virtual MAC
- Switches learn the virtual MAC on the port toward the active router

### Hello messages and roles

- Routers in a group send periodic hello messages
- Hello messages use a multicast group address
- Roles:
  - Active or master router forwards packets for the VIP
  - Standby or backup router is ready to take over
- If hello messages from the active router stop, another router takes over

Terminology differs by protocol (HSRP uses active and standby, VRRP uses master and backup).

### Failover and gratuitous ARP

- When the active router fails, a standby or backup takes over the role
- New active router starts forwarding for the VIP
- New active sends gratuitous ARP (GARP) frames
  - Uses VIP and virtual MAC
  - Updates switch MAC tables so the virtual MAC now points to the new port
- Hosts keep using the same VIP and virtual MAC

### Preemption

- Preemption allows a higher priority router to take over the active role
- Useful when one router is preferred as the active gateway
- Default behavior varies:
  - HSRP: preemption disabled by default
  - VRRP: preemption enabled by default
  - GLBP: AVG preemption disabled by default, AVF preemption enabled by default

## FHRP types

Cisco platforms commonly support three FHRPs.

### Hot Standby Router Protocol (HSRP)

- Cisco proprietary
- Uses active and standby roles
- Preemption disabled by default
- Two versions: HSRPv1 and HSRPv2

#### HSRPv1

- Multicast address: 224.0.0.2 (all routers)
- Virtual MAC: `0000.0c07.acXX` (XX is group number)
- Group numbers: 0 to 255
- IPv4 only

#### HSRPv2

- Multicast address: 224.0.0.102
- Virtual MAC: `0000.0c9f.fXXX` (XXX is group number)
- Group numbers: 0 to 4095
- Supports IPv4 and IPv6

Load balancing with HSRP:

- Achieved per subnet
- One router can be active for some VLANs and standby for others
- Another router can use the opposite pattern

### Virtual Router Redundancy Protocol (VRRP)

- Open standard (IETF)
- Master and backup roles
- Preemption enabled by default
- Multicast address: 224.0.0.18
- Virtual MAC: `0000.5e00.01XX` (XX is group number)
- Load balancing done per subnet by using different masters in different VLANs

VRRP is preferred in multi vendor environments.

### Gateway Load Balancing Protocol (GLBP)

- Cisco proprietary
- Provides redundancy and per host load balancing
- Roles:
  - Active Virtual Gateway (AVG)
  - Active Virtual Forwarders (AVFs)
- AVG assigns up to four AVFs
- AVG can also act as an AVF

GLBP addressing:

- Multicast address: 224.0.0.102
- Virtual MAC: `0007.b400.XXYY` (XX is group number, YY is AVF number)

GLBP load balancing:

- Single VIP, multiple virtual MAC addresses
- AVG replies to ARP requests with different virtual MACs
- Hosts are spread across AVFs
- Traffic is balanced within a single VLAN

## FHRP comparison

| Characteristic       | HSRP                | VRRP                 | GLBP                            |
|----------------------|---------------------|----------------------|----------------------------------|
| Standard or vendor   | Cisco proprietary   | Open standard        | Cisco proprietary                |
| Roles                | Active / Standby    | Master / Backup      | AVG / AVF                        |
| Default preemption   | Disabled            | Enabled              | AVG: disabled, AVF: enabled      |
| Load balancing       | Per subnet          | Per subnet           | Per host                         |
| Multicast address v2 | 224.0.0.102         | 224.0.0.18           | 224.0.0.102                      |
| Virtual MAC format   | `0000.0c9f.fXXX`    | `0000.5e00.01XX`     | `0007.b400.XXYY`                 |

## Basic HSRP configuration

### Requirements

Each router in the HSRP group needs:

- Unique IP address on the interface
- Same HSRP version
- Same group number
- Same VIP

Hosts in the VLAN use the VIP as their default gateway.

### Example configuration

```cisco
interface GigabitEthernet0/0
 ip address 10.0.0.2 255.255.255.0
 standby version 2          ! Use HSRPv2
 standby 1 ip 10.0.0.1      ! VIP for group 1
 standby 1 priority 110     ! Higher priority than default 100
 standby 1 preempt          ! Take over active role when up
 no shutdown
```

Points to remember:

- Group number and VIP must match on routers in the same HSRP group
- HSRPv1 and HSRPv2 are not interoperable in the same group
- Priority is optional unless a specific active router is desired
- Preemption is needed only on routers that should retake the active role

### Active router selection

Active router for a group is chosen by:

1. Highest HSRP priority
2. Highest IP address (if priorities tie)

## Verification and troubleshooting

### Verification commands

- `show standby brief`
  - Group, VIP, local state, active and standby addresses
- `show standby`
  - Detailed HSRP information including timers and preemption
- `show ip interface brief`
  - Interface status and IP addressing

### Troubleshooting notes

- Failover does not occur:
  - Check hello and hold timers
  - Confirm group number and VIP match on all routers
- Both routers think they are active:
  - Verify group configuration and version
  - Look for mismatched subnets or VLANs
- Hosts cannot reach external networks:
  - Confirm hosts use the VIP as default gateway
  - Check ARP tables for the VIP and virtual MAC
- Preemption does not work as expected:
  - Confirm `standby <group> preempt` is configured on the higher priority router

## Quick review

- FHRPs provide a redundant default gateway by sharing a VIP and virtual MAC across routers.
- Active or master router forwards traffic and responds to ARP for the VIP.
- Standby or backup router monitors hello messages and takes over on failure, sending gratuitous ARP.
- HSRP and GLBP are Cisco proprietary, VRRP is an open standard.
- HSRP and VRRP provide per subnet load balancing by varying which router is active per VLAN.
- GLBP provides per host load balancing within a single subnet by using multiple virtual MAC addresses.
- HSRP version 2 supports more groups and IPv6 and uses multicast 224.0.0.102.
- Basic HSRP config uses `standby version`, `standby <group> ip`, `standby <group> priority`, and `standby <group> preempt`.
- `show standby brief` and `show standby` are primary verification commands.