# Dynamic and VLAN Trunking Protocols

## Overview

Dynamic Trunking Protocol (DTP) and VLAN Trunking Protocol (VTP) automate parts of VLAN deployment on Cisco switches. Understanding how they negotiate trunk links, synchronize VLAN databases, and introduce security risk is essential for reliable interswitch connectivity.

## Dynamic Trunking Protocol (DTP)

### Administrative vs Operational Mode

- **Administrative mode**: Configured with `switchport mode <option>`
- **Operational mode**: Result of DTP negotiation (access or trunk)
- `switchport mode access` and `switchport mode trunk` force the same operational mode and bypass negotiation results

### Port Mode Options

- `access`: Forces access mode; does not send DTP messages
- `trunk`: Forces trunk mode; still transmits DTP messages so neighbors can join the trunk
- `dynamic auto`: Default on Cisco switches; listens for DTP messages and forms a trunk if the peer requests it
- `dynamic desirable`: Actively attempts to form a trunk with the peer

### Common Negotiation Outcomes

- `dynamic auto` + `dynamic auto` ➝ Access link
- `dynamic auto` + `dynamic desirable` ➝ Trunk link
- `dynamic desirable` + `dynamic desirable` ➝ Trunk link
- `trunk` + `dynamic auto` or `trunk` + `dynamic desirable` ➝ Trunk link
- `access` + `trunk` ➝ Invalid or unstable; avoid this combination

### Verification Commands

- `show interfaces <interface> switchport` displays administrative mode, operational mode, and negotiation status
- `show interfaces trunk` confirms which interfaces are operating as trunks

### Disabling DTP

- Attackers can spoof DTP to form unauthorized trunks and reach every VLAN
- Best practices:
  - Force access ports with `switchport mode access`
  - For trunk ports, use `switchport mode trunk` and add `switchport nonegotiate`
  - Administratively disable unused interfaces
- Disabling DTP reduces control-plane noise and removes an avenue for VLAN hopping

## VLAN Trunking Protocol (VTP)

### Purpose and Scope

- Cisco-proprietary protocol used to synchronize the VLAN database (`vlan.dat`) across switches
- Propagates VLAN creation, deletion, and renaming events through trunk links
- Only active when switches share the same VTP domain name

### VTP Synchronization Workflow

- Configure the domain with `vtp domain <name>`
- Create, modify, or delete VLANs on a VTP server; the configuration revision number increments
- Switches accept updates only from peers with a higher revision number
- `show vtp status` reveals domain, operating mode, revision number, VLAN count, and supported versions

### VTP Modes

- **Server (default)**: Full control over VLAN database; advertises changes and accepts updates
- **Client**: Cannot edit VLANs; otherwise behaves like a server for synchronization
- **Transparent**: Maintains its own VLAN database, forwards VTP messages, does not synchronize (revision number stays 0)
- **Off**: Completely disables VTP participation; no forwarding of VTP messages
- Configure mode with `vtp mode <server|client|transparent|off>`

### VTP Versions

- **Version 1**: Default on many devices; supports normal-range VLANs (1–1005)
- **Version 2**: Adds Token Ring support; otherwise similar to version 1
- **Version 3**: Preferred when VTP is used; adds off mode, primary server concept, and extended-range VLAN support (1006–4094)
- Set the version with `vtp version <1|2|3>`

### Version 3 Enhancements

- **Primary server role**: Only the primary can modify VLANs; prevent rogue switches from overwriting the database
- **Extended-range VLAN propagation**: Shares VLANs beyond the normal range
- **Off mode support**: Explicitly disables VTP without relying on transparent mode workarounds
- Promote a secondary server with the privileged EXEC command `vtp primary`

## VTP Risks and Safeguards

### Risks

- A newly connected switch with a higher revision number can overwrite the VLAN database of the entire domain
- Legacy versions allow any server-level switch to inject changes, even unintentionally

### Safeguards

- Reset revision numbers before installing lab or staged switches (change domain, toggle mode transparent/off, or erase `vlan.dat`)
- Use version 3 with a designated primary server to avoid accidental overwrites
- If VTP is unnecessary, configure `vtp mode off` and manage VLANs locally
- Document domain names, passwords (if configured), and revision resets in deployment runbooks

## Troubleshooting Checklist

- **Unexpected access link**: Verify administrative modes (`show interfaces switchport`) on both sides
- **Native VLAN mismatch**: Inspect `show interfaces trunk` output
- **Missing VLANs**: Confirm domain membership, revision number, and VTP mode
- **Revision lockouts**: Reset revision numbers before integrating new switches
- **Extended VLANs missing**: Ensure VTP version 3 is running and a primary server is defined

## Summary

- DTP negotiates trunk formation based on administrative modes; disable it unless dynamic trunks are required
- Use explicit `access` or `trunk` mode together with `switchport nonegotiate` to harden switchports
- VTP synchronizes VLAN information within a domain; understand domain names, revision numbers, and operating modes
- Version 3 introduces primary servers, extended-range VLAN support, and an explicit off mode—prefer it when VTP is enabled
- When VTP is not needed, disable it and manage VLANs per switch to eliminate synchronization risk
