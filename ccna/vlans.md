# VLANs

## Overview

Virtual LANs (VLANs) split a single physical LAN into multiple logical broadcast domains. VLANs reduce unnecessary traffic, improve security, and make it easier to group hosts by function instead of physical location.

## VLAN concepts

### Layer 2 and Layer 3 relationship

- VLANs provide Layer 2 segmentation.
- Subnets provide Layer 3 segmentation.
- Typical design pairs one subnet with one VLAN.
- Devices in the same VLAN share a broadcast domain.
- Devices in different VLANs require routing to communicate.

### Broadcast containment

- Broadcasts and unknown unicasts stay inside the originating VLAN.
- VLANs reduce the size of each broadcast domain.
- Smaller broadcast domains improve stability and troubleshooting.

## VLAN ranges and defaults

- VLAN ID space: 0–4095 (12 bits).
- Usable VLANs: 1–1001 and 1006–4094.
- VLAN 1:
  - Default VLAN.
  - All switch ports start in VLAN 1.
- VLANs 1002–1005:
  - Reserved for legacy technologies.
  - Not used for normal data VLANs.

Useful command:

```cisco
show vlan brief
```

Lists VLANs and the access ports assigned to each.

## Creating and naming VLANs

Basic steps:

```cisco
configure terminal
vlan 10
 name USERS
vlan 20
 name SERVERS
end
```

- VLANs can be shut down without deleting them:

  ```cisco
  vlan 99
   shutdown
  ```

- Remove a VLAN:

  ```cisco
  no vlan 99
  ```

Deleting a VLAN removes it from the VLAN database. Ports that were in that VLAN revert to an inactive state until assigned to another VLAN.

## Access ports

### Definition

- Access ports carry traffic for a single VLAN.
- Frames are not tagged when sent to end hosts.
- End hosts are unaware of VLAN IDs.

### Configuration pattern

```cisco
interface range GigabitEthernet0/1 - 4
 switchport mode access
 switchport access vlan 10
```

Notes:

- `switchport mode access` disables Dynamic Trunking Protocol negotiation.
- If the VLAN does not exist, some platforms create it automatically when assigned.
- Use `show mac address-table` to confirm learned MAC addresses per VLAN.

## Trunk ports

### Purpose

- Trunks carry multiple VLANs over a single link.
- Used between switches, and between switches and routers or firewalls.
- Frames are tagged with VLAN IDs on the trunk.

### 802.1Q tagging

- Inserts a 4 byte tag into the Ethernet frame.
- Tag fields:
  - Tag Protocol Identifier (TPID): 0x8100.
  - Priority Code Point (PCP): 3 bits for QoS.
  - Drop Eligible Indicator (DEI): 1 bit.
  - VLAN Identifier (VID): 12 bits for the VLAN number.

### Trunk configuration

Basic pattern:

```cisco
interface GigabitEthernet0/24
 switchport trunk encapsulation dot1q   ! only on platforms that support multiple encapsulations
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

Managing allowed VLAN lists:

- `add`: add VLANs without overwriting the list.
- `remove`: remove specific VLANs.
- `none`: block all VLANs.
- `except`: allow all except the listed VLANs.

Example:

```cisco
switchport trunk allowed vlan add 40
```

Use `add` to avoid accidentally removing existing VLANs.

### Verification

```cisco
show interfaces trunk
```

- Confirms trunk status.
- Shows allowed VLANs.
- Shows native VLAN.

## Native VLAN

- Native VLAN frames cross the trunk without tags.
- Untagged frames received on a trunk are placed into the native VLAN.
- Default native VLAN is VLAN 1.
- Both ends of a trunk must agree on the native VLAN.

Security practice:

- Use an unused VLAN (for example VLAN 999) as the native VLAN.
- Do not use the native VLAN for user traffic.
- Prune the native VLAN from trunks where possible.

## Inter-VLAN routing

VLANs isolate Layer 2 traffic. Routing is required for inter-VLAN communication.

### Router per VLAN (legacy)

- Each VLAN connects to a separate physical router interface.
- Consumes many router ports.
- Rare in modern designs.

### Router on a stick (ROAS)

- Single physical link between router and switch.
- Link is a trunk.
- Router subinterfaces act as default gateways for VLANs.

Example:

```cisco
interface GigabitEthernet0/0
 no shutdown

interface GigabitEthernet0/0.10
 encapsulation dot1q 10
 ip address 192.168.10.1 255.255.255.0

interface GigabitEthernet0/0.20
 encapsulation dot1q 20
 ip address 192.168.20.1 255.255.255.0
```

`show ip interface brief` confirms subinterface status.

### Multilayer switch with SVIs

- Switch performs routing between VLANs.
- Uses Switched Virtual Interfaces (SVIs) as default gateways.

Example:

```cisco
ip routing

interface vlan 10
 ip address 192.168.10.1 255.255.255.0
 no shutdown

interface vlan 20
 ip address 192.168.20.1 255.255.255.0
 no shutdown
```

Use `show ip route` to verify connected routes for each SVI.

## Troubleshooting VLANs

Common issues:

- Native VLAN mismatch  
  - Native VLAN values differ on the two ends of a trunk.

- Missing VLAN  
  - VLAN not created on all switches that should carry it.

- Trunk not operational  
  - Interfaces left in dynamic mode instead of forced trunk or access.

- Allowed VLAN pruning  
  - Required VLANs missing from `switchport trunk allowed` lists.

- Inter-VLAN routing down  
  - SVIs or router subinterfaces are administratively down or missing addresses.

Useful commands:

```cisco
show vlan brief
show interfaces trunk
show mac address-table
show ip interface brief
show ip route
```

## Quick review

- VLANs create multiple broadcast domains on a single switch.  
- Typical designs map one subnet to one VLAN.  
- Access ports carry a single VLAN and do not tag frames toward end hosts.  
- Trunk ports carry multiple VLANs using 802.1Q tagging and maintain an agreed native VLAN.  
- Inter-VLAN routing uses router on a stick or multilayer switches with SVIs.  
- Key verification commands include `show vlan brief`, `show interfaces trunk`, `show mac address-table`, and `show ip interface brief`.  
