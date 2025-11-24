# Dynamic and VLAN Trunking Protocols

## Overview

Dynamic Trunking Protocol (DTP) negotiates trunk links between Cisco switches. VLAN Trunking Protocol (VTP) can synchronize VLAN databases across switches in the same VTP domain. Both affect interswitch connectivity and both introduce potential security risk.

## Dynamic Trunking Protocol (DTP)

### Administrative and operational mode

- Administrative mode:
  - Configured by the `switchport mode` command
  - Options: `access`, `trunk`, `dynamic auto`, `dynamic desirable`
- Operational mode:
  - Actual state of the port (access or trunk)
  - Result of negotiation and configuration

Notes:

- `switchport mode access` forces access mode
- `switchport mode trunk` forces trunk mode
- These modes ignore DTP negotiation results for the local port

### Port mode options

- `access`
  - Forces access mode
  - Does not send DTP frames
- `trunk`
  - Forces trunk mode
  - Still sends DTP frames unless `switchport nonegotiate` is used
- `dynamic auto`
  - Listens for DTP
  - Becomes a trunk only if the neighbor asks for a trunk
  - Default on many Cisco switches
- `dynamic desirable`
  - Sends DTP and tries to form a trunk with the neighbor

### Negotiation outcomes

Common combinations:

- `dynamic auto` + `dynamic auto` → access link
- `dynamic auto` + `dynamic desirable` → trunk link
- `dynamic desirable` + `dynamic desirable` → trunk link
- `trunk` + `dynamic auto` or `trunk` + `dynamic desirable` → trunk link
- `access` + `trunk` → misconfiguration and unstable behavior

In real networks, static trunk configuration is preferred for predictable behavior.

### Verifying trunk status

Useful commands:

- `show interfaces <interface> switchport`
  - Shows administrative mode, operational mode, and negotiation status
- `show interfaces trunk`
  - Lists interfaces currently operating as trunks
  - Shows allowed VLAN list and native VLAN

### Hardening DTP

DTP frames can be abused to form unintended trunks and reach multiple VLANs.

Recommendations:

- On access ports:
  - `switchport mode access`
  - Disable unused ports
- On trunk ports:
  - `switchport mode trunk`
  - `switchport nonegotiate` to stop sending DTP
- Avoid `dynamic auto` and `dynamic desirable` on production switchports

Disabling DTP on trunks and forcing access mode on end host ports reduces VLAN hopping risk.

## VLAN Trunking Protocol (VTP)

### Role and scope

- Cisco proprietary protocol
- Synchronizes VLAN information between switches in the same VTP domain
- Updates the VLAN database file (`vlan.dat`) over trunk links
- Only active when the domain name matches and VTP is enabled

VTP is optional. Many designs avoid it and manage VLANs on each switch independently.

### VTP modes

- Server
  - Default mode
  - Can create, modify, and delete VLANs
  - Advertises changes and accepts updates
- Client
  - Cannot edit VLANs
  - Receives VLAN information from servers
  - Forwards VTP advertisements
- Transparent
  - Maintains its own VLAN database
  - Forwards VTP advertisements
  - Does not update its own VLANs based on received advertisements
  - Revision number remains zero
- Off (version 3 only)
  - Does not participate in VTP
  - Does not forward VTP advertisements

Configuration:

- `vtp mode server`
- `vtp mode client`
- `vtp mode transparent`
- `vtp mode off` (version 3)

### VTP versions

- Version 1
  - Supports normal range VLANs (1 to 1005)
  - Default on many older devices
- Version 2
  - Adds Token Ring support
  - Otherwise similar to version 1
- Version 3
  - Adds off mode
  - Adds primary server concept
  - Supports extended range VLANs (1006 to 4094)

Set the version with `vtp version <1|2|3>`.

### VTP operation

Basic workflow:

- All switches in the same domain use `vtp domain <name>`
- A change to the VLAN database on a server increments the configuration revision number
- VTP advertisements carry the new revision and VLAN information
- Switches accept VTP updates only when the received revision number is higher
- `show vtp status` displays domain, mode, version, revision, number of VLANs

Transparent mode:

- Does not update its own VLAN database from VTP
- Still forwards VTP messages so other switches can receive them

### VTP version 3 additions

- Primary server role
  - Only the primary server can modify the VLAN database
  - Reduces risk that an accidental configuration on another server overwrites VLANs
  - Set with the `vtp primary` command
- Extended VLAN support
  - Propagates VLANs in the extended range
- Off mode
  - Clean way to disable VTP participation

## VTP risks and safeguards

### Risks

- A newly added switch with a higher revision number in the same domain can overwrite VLANs on existing switches
- Old VTP versions allow any switch in server mode to change the domain VLANs
- Misconfigured VTP domain names can prevent VLAN synchronization and cause missing VLANs on trunks

### Safeguards

- Reset the revision number before adding a switch to a production domain
  - Change the VTP domain to a different name and then back
  - Change the switch to transparent or off mode and back
  - Delete `vlan.dat` and reload if appropriate for the environment
- Use VTP version 3 where VTP is required and configure a single primary server
- If VTP is not required, set `vtp mode off` or `vtp mode transparent` and manage VLANs locally
- Document domain names, passwords, and revision reset procedures

## Troubleshooting notes

- Unexpected access link between switches:
  - Check `show interfaces switchport` on both sides
  - Verify modes and native VLAN configuration
- Missing VLANs across trunks:
  - Confirm VTP domain name, mode, and revision with `show vtp status`
  - Check that VLANs exist in the local database with `show vlan brief`
  - Verify allowed VLAN list on trunks with `show interfaces trunk`
- Extended VLANs not propagating:
  - Confirm VTP version is 3
  - Ensure a primary server is configured
- Revision number issues when adding a switch:
  - Reset revision number before connecting to the production domain

## Quick review

- DTP negotiates whether a link becomes an access port or a trunk.
- Administrative mode is configured with `switchport mode`; operational mode is the result on the wire.
- Use static `access` and `trunk` modes with `switchport nonegotiate` on trunks to avoid unwanted DTP negotiation.
- VTP can synchronize VLAN databases between switches in the same domain and version.
- VTP modes: server, client, transparent, and off in version 3.
- VTP version 3 adds a primary server role, extended range VLAN support, and an off mode.
- A higher VTP revision number can overwrite VLANs. Always reset revision numbers on lab or replacement switches before connecting them to production.
- When VTP is unnecessary, disable it and manage VLANs per switch to remove a class of synchronization errors.
