# Router and Switch Interfaces

## Overview

Router and switch interfaces are the connection points that link devices and networks. Correct interface configuration, verification, and troubleshooting are core skills for CCNA level networking.

## Router interfaces

### Interface types

- Ethernet interfaces  
  - FastEthernet (10/100 Mbps)  
  - GigabitEthernet (10/100/1000 Mbps)  
  - TenGigabitEthernet and higher for uplinks and core links  
  - Typical names: `GigabitEthernet0/0`, `GigabitEthernet0/1`

- Serial interfaces  
  - Point to point WAN links in lab and some legacy environments  
  - DCE side provides clocking with a `clock rate` command  
  - Typical names: `Serial0/0/0`, `Serial0/0/1`

- Management ports  
  - Console port for local out of band access  
  - Auxiliary port on some platforms for modem based remote access

### Basic router interface configuration

Example IPv4 LAN interface:

```cisco
interface GigabitEthernet0/0
 description LAN
 ip address 192.168.1.1 255.255.255.0
 no shutdown
```

Key points:

- `ip address` with mask defines the subnet.  
- `no shutdown` enables the interface administratively.  
- `description` is useful for documentation.

### Interface status and verification

Common commands:

- `show ip interface brief`  
  - Summary of interfaces, IP addresses, and up/down status.

- `show interfaces <name>`  
  - Detailed counters, duplex, speed, and errors.

- `show ip interface <name>`  
  - Layer 3 details such as ACLs and helper addresses.

### Router interface states

- Line protocol up, interface up  
  - Interface is enabled and physically connected.

- Line protocol down, interface up  
  - Layer 1 is working, but keepalives, encapsulation, or clocking may be wrong.

- Interface down, line protocol down  
  - Interface is shut, cable unplugged, or hardware problem.

- Administratively down  
  - Interface disabled with the `shutdown` command.

## Switch interfaces

### Switch interface types and naming

- Access switches provide many Ethernet ports for end devices.  
- Typical names:
  - `FastEthernet0/1`
  - `GigabitEthernet0/1`
  - `GigabitEthernet1/0/1`
  - `TenGigabitEthernet1/0/1`
- SFP or SFP+ slots accept fiber or copper modules for uplinks.

### Access port configuration

Example of a port for a single VLAN:

```cisco
interface GigabitEthernet0/1
 description User PC
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 no shutdown
```

- Traffic is untagged in VLAN 10.  
- PortFast is used for host facing access ports.

### Trunk port configuration

Example of a link between switches:

```cisco
interface GigabitEthernet0/24
 description Uplink to Core
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
 no shutdown
```

- Carries multiple VLANs.  
- Uses 802.1Q tagging.  
- Allowed VLAN list should be limited to required VLANs.

### VLAN creation and assignment

Creating VLANs:

```cisco
vlan 10
 name Sales
vlan 20
 name Marketing
```

Assigning a range of ports to a VLAN:

```cisco
interface range GigabitEthernet0/1 - 10
 switchport mode access
 switchport access vlan 10
 no shutdown
```

Verification commands:

- `show interfaces status`  
  - Port status, VLAN, duplex, and speed.

- `show vlan brief`  
  - VLANs and which ports are in each VLAN.

- `show interfaces trunk`  
  - Trunk ports and allowed VLAN lists.

## Interface management and configuration storage

### Show commands summary

Router focused:

- `show ip interface brief`  
- `show interfaces`  
- `show ip route`  
- `show running-config`

Switch focused:

- `show interfaces status`  
- `show vlan brief`  
- `show mac address-table`  
- `show spanning-tree`

### Saving configuration

Save the running configuration so it survives reloads:

```cisco
copy running-config startup-config
```

Back up configuration to an external server:

```cisco
copy running-config tftp://192.0.2.10/r1-backup.cfg
```

## Interface security overview

### Port security on access ports

Basic example:

```cisco
interface GigabitEthernet0/1
 switchport mode access
 switchport access vlan 10
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security mac-address sticky
```

- Limits number of MAC addresses on the port.  
- Uses sticky learning to save seen MAC addresses.  
- Restrict mode drops violating traffic and logs events.

### ACLs on routed interfaces

Simple standard ACL example:

```cisco
access-list 10 permit 192.168.1.0 0.0.0.255
access-list 10 deny any
interface GigabitEthernet0/0
 ip access-group 10 in
```

- ACL 10 controls inbound traffic on the interface.  
- Standard ACLs match source IPv4 addresses.

## Troubleshooting interfaces

### Physical layer checks

- Confirm cables are connected and undamaged.  
- Check interface LEDs for link and activity.  
- Use `show interfaces` to look for errors, CRCs, and collisions.  
- Test with a known good cable and port when in doubt.

### Data link and VLAN checks

- Verify encapsulation and keepalives on serial links.  
- Check trunk configuration and allowed VLANs.  
- Ensure access ports are in the correct VLAN.  
- Confirm native VLAN settings match on both ends of a trunk.

### Network layer checks

- Verify IP addressing and masks.  
- Confirm default gateway on hosts.  
- Use `ping` and `traceroute` to test reachability.  
- Check routing tables with `show ip route` when traffic crosses subnets.

## Quick review

- Router interfaces connect different networks and require correct IP addressing and status.  
- Switch interfaces connect local devices, use VLANs, and can operate as access or trunk ports.  
- Key commands include `show ip interface brief`, `show interfaces`, `show interfaces status`, `show vlan brief`, and `show interfaces trunk`.  
- Port security and ACLs provide basic protection at the interface level.  
- Troubleshooting starts at the physical layer and moves up through data link and network layers, checking cabling, VLANs, and IP settings.
