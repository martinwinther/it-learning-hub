# VLANs

## Overview

Virtual LANs (VLANs) segment a single physical LAN into multiple logical broadcast domains. They deliver finer control over security, performance, and management compared to a flat network.

## Why VLANs Matter

Segmenting networks at multiple layers improves control and scalability.

### Layer 3 Segmentation with Subnets

- Subnets separate IP networks and force interdepartment traffic through routers
- Routers can enforce policy and provide audit points
- Without VLANs, Layer 2 remains a single broadcast domain even if multiple subnets exist

### Layer 2 Segmentation with VLANs

- VLANs break a LAN into multiple broadcast domains on the same switch
- Broadcast and unknown unicast traffic is contained within each VLAN
- Security policies align with both Layer 2 and Layer 3 boundaries
- A one-to-one relationship between subnets and VLANs is the default design pattern for CCNA scenarios

## VLAN Configuration Basics

### VLAN Ranges and Defaults

- Total VLAN space: 0–4095 (2^12 values)
- Usable VLANs: 1–1001 and 1006–4094 (4090 values)
- VLAN 1 is the default VLAN; all switch ports start in VLAN 1
- VLANs 1002–1005 are reserved for legacy technologies (FDDI, Token Ring) and cannot be repurposed

### Creating and Naming VLANs

- `show vlan brief` displays the VLAN database and assigned ports
- Create VLANs with `vlan <id>` from global configuration mode
- Assign descriptive names with `name <text>` inside VLAN configuration mode
- Disable a VLAN without deleting it using `shutdown`
- Remove a VLAN with `no vlan <id>`

## Access Ports

### Definition

- An access port carries traffic for exactly one VLAN (untagged)
- Best practice: disable Dynamic Trunking Protocol (DTP) negotiation by forcing access mode

### Configuration Workflow

1. `interface range g0/0-3`
2. `switchport mode access`
3. `switchport access vlan <id>`

### Operational Notes

- If a VLAN does not exist, `switchport access vlan` creates it automatically
- Hosts are unaware of VLAN IDs; membership is enforced on the switch port
- Use `show mac address-table` to confirm learned MAC addresses per VLAN

## Trunk Ports

### Purpose and Vocabulary

- Connect switches (and sometimes routers) using links that carry multiple VLANs
- Also known as tagged ports because frames are labeled with their VLAN ID
- Access ports are untagged ports that strip VLAN tags before forwarding frames to end hosts

### IEEE 802.1Q Tag

- 4-byte field inserted between the Source and EtherType fields
- Tag Protocol Identifier (TPID): 0x8100 indicates the frame is tagged
- Tag Control Information (TCI) fields:
  - Priority Code Point (PCP): 3 bits for Quality of Service
  - Drop Eligible Indicator (DEI): 1 bit for congestion handling
  - VLAN Identifier (VID): 12 bits that store the VLAN number

### Trunk Configuration Steps

1. `switchport trunk encapsulation dot1q` (required on models that still support ISL)
2. `switchport mode trunk`
3. Optionally control allowed VLANs with `switchport trunk allowed vlan <list>`

### Managing Allowed VLAN Lists

- Default: all VLANs (1-4094) are allowed
- Provide explicit lists to limit broadcast domains
- Keywords:
  - `add`: append VLANs without overwriting existing ones
  - `remove`: delete specific VLANs from the allowed list
  - `none`: block all VLANs (administratively down)
  - `except`: allow all VLANs except those listed
- Always use `add` when modifying an existing list to avoid accidental outages

### Native VLAN

- Frames in the native VLAN cross the trunk without a tag
- Untagged frames received on a trunk are placed into the native VLAN
- Default native VLAN: VLAN 1 (per port, changeable)
- Align native VLANs on both ends to prevent VLAN hopping
- Security best practice: assign an unused VLAN (for example, VLAN 999) as the native VLAN and prune it from active networks

### Verification Commands

- `show vlan brief`: lists access ports and their VLANs
- `show interfaces trunk`: verifies trunk status, encapsulation, allowed VLANs, and native VLAN
- `show mac address-table`: confirms MAC addresses learned per VLAN

## Inter-VLAN Routing

VLANs isolate Layer 2 traffic, so routing is required for inter-VLAN communication.

### Router Per VLAN (Legacy)

- Each VLAN connects to a unique physical router interface
- Scales poorly due to port consumption

### Router on a Stick (ROAS)

- Creates a single trunk link between the switch and router
- Router subinterfaces act as default gateways for each VLAN
- Configuration outline:
  - Enable the physical interface with `no shutdown`
  - For each VLAN: `interface g0/0.<vlan>` ➝ `encapsulation dot1q <vlan>` ➝ `ip address <gateway>`
  - Optionally append `native` in the `encapsulation dot1q` command to support a native VLAN
  - `show ip interface brief` confirms subinterface status

### Multilayer Switch with SVIs

- Enables routing directly on the switch
- Steps:
  1. `ip routing`
  2. `interface vlan <id>` ➝ `ip address <gateway>` ➝ `no shutdown`
  3. Repeat for each VLAN
- `show ip route` displays connected and local routes installed for each SVI

## Troubleshooting Checklist

- **Native VLAN mismatch**: Compare `show interfaces trunk` output on both ends
- **Missing VLAN**: Ensure VLAN exists in the database on every switch carrying it
- **Allowed VLAN pruning**: Confirm lists include required VLANs, especially after using `remove`
- **Access port mode**: Verify `switchport mode access` to prevent DTP negotiation surprises
- **Routing health**: Check default gateways (ROAS subinterfaces or SVIs) are up/up

## Summary

- VLANs provide Layer 2 segmentation that complements subnetting at Layer 3
- Access ports belong to a single VLAN and operate without tags
- Trunk ports use 802.1Q tagging, explicit allowed VLAN lists, and a carefully managed native VLAN
- Inter-VLAN routing is delivered through router-on-a-stick designs or multilayer switches with SVIs
- Consistent verification (`show vlan brief`, `show interfaces trunk`, `show ip interface brief`, `show ip route`) keeps VLAN deployments healthy
