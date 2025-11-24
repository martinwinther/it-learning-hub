# EtherChannel

## Overview

EtherChannel combines multiple physical links into one logical interface called a port channel. STP treats the bundle as a single link, so redundant member links can all forward without creating Layer 2 loops. This increases total bandwidth and provides link redundancy while simplifying management.

## EtherChannel basics

### Problem solved

- STP blocks redundant links to prevent loops
- Multiple parallel links between switches do not increase usable bandwidth if some are blocked
- Single active link can become a bottleneck

### EtherChannel behavior

- Multiple physical interfaces join the same channel group
- Switch creates a logical `Port-channel` interface (for example, `Po1`)
- STP sees and manages the port channel as a single port
- Broadcast, unknown unicast, and multicast frames are not sent back out other ports in the same EtherChannel
- Total bandwidth is roughly the sum of the member link speeds

## Dynamic vs static EtherChannel

### Dynamic negotiation

- Uses a protocol to negotiate the bundle
- Checks that configuration parameters match before forming the EtherChannel
- Safer in most cases

Protocols:

- PAgP (Cisco proprietary)
- LACP (IEEE 802.3ad)

### Static EtherChannel

- No negotiation protocol
- Interfaces are forced into an EtherChannel
- Configuration:
  - `channel-group <number> mode on`
- Must be configured on both sides
- Higher risk of misconfiguration and loops
- Sometimes required for devices such as wireless LAN controllers

## Port Aggregation Protocol (PAgP)

### PAgP overview

- Cisco proprietary EtherChannel negotiation protocol
- Supports up to 8 active links in a bundle
- Uses PAgP packets to form and maintain the channel

### PAgP modes

- `desirable`
  - Actively sends PAgP messages
  - Tries to form an EtherChannel
- `auto`
  - Listens for PAgP
  - Forms an EtherChannel only if the neighbor uses `desirable`

Mode combinations:

- `desirable` + `desirable` → EtherChannel
- `desirable` + `auto` → EtherChannel
- `auto` + `auto` → no EtherChannel

### PAgP configuration and verification

- Interface configuration:
  - `channel-group <number> mode desirable`
  - `channel-group <number> mode auto`
- Verification:
  - `show etherchannel summary`
  - `show pagp neighbor`

## Link Aggregation Control Protocol (LACP)

### LACP overview

- IEEE 802.3ad standard
- Vendor neutral
- Supports up to 16 member links:
  - 8 active
  - 8 standby
- Common choice in multi vendor environments

### LACP modes

- `active`
  - Actively sends LACP messages
  - Equivalent to PAgP `desirable`
- `passive`
  - Listens for LACP
  - Equivalent to PAgP `auto`

Mode combinations:

- `active` + `active` → EtherChannel
- `active` + `passive` → EtherChannel
- `passive` + `passive` → no EtherChannel

### LACP configuration and verification

- Interface configuration:
  - `channel-group <number> mode active`
  - `channel-group <number> mode passive`
- Verification:
  - `show etherchannel summary`
  - `show lacp neighbor`

## Mode compatibility summary

Valid combinations between sides:

| Side A mode | Side B mode | Result       |
|------------|-------------|--------------|
| desirable  | desirable   | Forms        |
| desirable  | auto        | Forms        |
| auto       | auto        | No channel   |
| active     | active      | Forms        |
| active     | passive     | Forms        |
| passive    | passive     | No channel   |
| on         | on          | Forms (static) |

Notes:

- PAgP and LACP do not talk to each other
- Dynamic modes do not interoperate with `on`
- Both sides must use the same protocol type and compatible modes

## Port configuration requirements

### Matching settings

All member ports in the same EtherChannel must match on key settings:

- Speed
- Duplex
- Access or trunk mode
- Access VLAN (for access ports)
- Allowed VLAN list (for trunks)
- Native VLAN (for trunks)

If a member has different settings, it may be placed in a suspended state and removed from the bundle.

### Configuration approach

- Add ports to the same channel group
- Configure common settings on the port channel interface:

  ```text
  interface range Gi0/1 - 2
   channel-group 1 mode active
  !
  interface Port-channel1
   switchport mode trunk
   switchport trunk allowed vlan 10,20,30
  ```

Notes:

- Configuration on the port channel is inherited by member ports
- Best practice is to configure most settings on the port channel, not individually on each member, after the channel is up

## Load balancing

### Principle

- Switch load balances traffic across member links per flow
- A flow is usually defined by MAC or IP address fields
- All frames for the same flow use the same physical link
- Different flows can use different links

### Load balance options

- Global command:
  - `port-channel load-balance <option>`
- Common options:
  - `src-mac`
  - `dst-mac`
  - `src-dst-mac`
  - `src-ip`
  - `dst-ip`
  - `src-dst-ip`

- Verification:
  - `show etherchannel load-balance`

Traffic distribution depends on the chosen fields. A poor choice can cause uneven usage of links.

## Layer 2 and Layer 3 EtherChannel

### Layer 2 EtherChannel

- Member ports are switchports
- Used between switches or from switch to server
- STP sees a single logical port
- Configure `switchport` settings on the port channel

### Layer 3 EtherChannel

- Member ports are routed ports
- No STP participation
- Used between routers or multilayer switches

Configuration outline:

- On member interfaces:
  - `no switchport`
  - `channel-group <number> mode {active | passive | on}`
- On port channel:
  - `interface Port-channel<number>`
  - `ip address <ip> <mask>`

## Verification and troubleshooting

### Key commands

- `show etherchannel summary`
  - Lists port channels, protocol, member ports, and status flags
- `show interfaces port-channel <number>`
  - Detailed view of a specific port channel
- `show spanning-tree`
  - Shows port channels participating in STP
- `show pagp neighbor`
- `show lacp neighbor`

### Common issues

- Channel not forming
  - Check mode compatibility and that both sides use the same protocol
- Ports suspended
  - Verify speed, duplex, VLAN, and trunk settings match
- Uneven load distribution
  - Review load-balance setting
  - Consider using both source and destination fields

## Quick review

- EtherChannel bundles multiple physical links into one logical port channel to increase bandwidth and provide redundancy.
- STP treats the bundle as a single port, allowing all member links to forward without creating loops.
- Dynamic EtherChannel uses PAgP or LACP; static EtherChannel uses `mode on` with no negotiation.
- PAgP: Cisco proprietary with `desirable` and `auto` modes.
- LACP: IEEE 802.3ad with `active` and `passive` modes and support for standby links.
- All member ports must match on speed, duplex, and VLAN-related settings.
- Load balancing uses MAC or IP fields to keep each flow on a single link.
- EtherChannel can operate at Layer 2 or Layer 3 depending on whether ports are switchports or routed ports.
