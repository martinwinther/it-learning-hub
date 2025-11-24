# Rapid Spanning Tree Protocol

## Overview

Rapid Spanning Tree Protocol (RSTP, 802.1w) is a link layer protocol that improves on the slow convergence of the original Spanning Tree Protocol (STP, 802.1D). STP can take about 50 seconds to react to some failures. RSTP uses a synchronization process and new port roles to converge in a few seconds or less in most cases.

Modern Cisco switches usually run Rapid PVST+, which combines RSTP behavior with a separate spanning tree instance per VLAN.

## STP versions

### Standard and Cisco variants

- STP (802.1D)  
  Single spanning tree for the whole bridged domain. Timer based convergence.

- PVST+  
  Cisco version of 802.1D. One spanning tree per VLAN.

- RSTP (802.1w)  
  Rapid spanning tree. Single instance. Faster convergence. Uses new port roles and sync.

- Rapid PVST+  
  Cisco version of 802.1w. One rapid tree per VLAN. Common default on Catalyst switches.

- MSTP (802.1s)  
  Multiple Spanning Tree Protocol. Groups VLANs into a small number of instances. Uses RSTP mechanics inside each instance.

### Checking and setting STP mode

- `show spanning-tree`  
  - `Spanning tree enabled protocol ieee` usually indicates PVST+  
  - `Spanning tree enabled protocol rstp` indicates Rapid PVST+
- Configure mode in global config:
  - `spanning-tree mode pvst`
  - `spanning-tree mode rapid-pvst`
  - `spanning-tree mode mst`

## RSTP and STP comparison

### Core behavior

- STP  
  - Timer driven (hello, forward delay, max age).  
  - Ports can sit in listening and learning states for a long time.

- RSTP  
  - Uses a sync process between neighbors.  
  - Ports on point to point links can move to forwarding almost immediately when conditions are safe.  
  - Still falls back to STP style timers when needed for compatibility.

### BPDU handling

- STP  
  - Root bridge sends BPDUs on designated ports.  
  - Other switches relay root BPDUs.

- RSTP  
  - Every switch sends BPDUs on its designated ports every two seconds.  
  - BPDUs serve as keepalives and carry role and state information.

### Root and designated selection

The rules for root bridge election, root port choice and designated port choice are the same in STP and RSTP.

- Root bridge: lowest bridge ID.  
- Root port: lowest total path cost toward the root, then lowest neighbor bridge ID, then neighbor port ID, then local port ID.  
- Designated port on a segment: lowest path cost, then lowest bridge ID, then local port ID.

## RSTP port states and roles

### Port states

STP uses blocking, listening, learning and forwarding. RSTP reduces this to three states.

- Discarding  
  No user traffic forwarded. Combines old blocking and listening states.

- Learning  
  Does not forward user traffic. Learns MAC addresses.

- Forwarding  
  Forwards user traffic and learns MAC addresses.

New ports start in discarding. Root and designated ports move to forwarding through the sync process when possible. If sync is not possible, ports follow a timer based path similar to STP.

### Port roles

RSTP defines four roles.

- Root port  
  One per nonroot switch. Forwarding state. Best path toward root bridge.

- Designated port  
  One per segment. Forwarding state. Forwards away from the root bridge onto the segment.

- Alternate port  
  Backup path toward the root. Discarding state. Takes over if the current root port fails.

- Backup port  
  Backup for a designated port on the same switch and segment. Discarding state. Rare in modern designs because hubs are no longer common.

Any forwarding port is either root or designated. Any nonforwarding port is alternate or backup.

Use `show spanning-tree` to view port roles:

- `Root` = root port  
- `Desg` = designated port  
- `Altn` = alternate port  
- `Back` = backup port

## RSTP convergence and timers

### Topology change detection

- STP  
  - May wait up to max age (20 seconds by default) before reacting to a missing BPDU.

- RSTP  
  - Considers a neighbor lost after three missed BPDUs.  
  - Default hello interval is two seconds.  
  - Detection time is about six seconds on point to point links.

After detection, an alternate port can move to forwarding through the sync process. If the failed port goes down physically, RSTP can start sync immediately and converge in less than a second on point to point links.

### STP compatibility

- RSTP interoperates with classic STP.  
- If an RSTP switch detects that a neighbor only speaks 802.1D, it falls back to timer based behavior on that port.  
- Mixed networks work, but lose the fast convergence across the mixed links.

## RSTP link types and edge ports

### Link types

RSTP classifies each port into one of three link types.

- Point to point  
  - Full duplex link between two switches.  
  - Can use the sync mechanism to move to forwarding quickly.

- Shared  
  - Half duplex link, usually involving a hub.  
  - Must follow STP style timer based transitions.

- Edge  
  - Port that connects to a single end host.  
  - Can move immediately to forwarding, similar to PortFast behavior.

### Automatic and manual settings

- Full duplex ports default to point to point.  
- Half duplex ports default to shared.  
- Edge ports are set manually.

Key commands:

```cisco
interface GigabitEthernet0/1
 spanning-tree portfast
 spanning-tree link-type point-to-point
```

Or:

```cisco
interface GigabitEthernet0/1
 spanning-tree link-type shared
```

`show spanning-tree` displays link types as `P2p`, `Shr`, or `P2p Edge` and similar strings.

### Edge port behavior

- Edge ports do not trigger topology change events when they move to forwarding.  
- RSTP does not try to sync the topology on edge ports.  
- This avoids unnecessary reconvergence when hosts connect or disconnect.

## RSTP and topology changes

### STP triggers

In classic STP, a topology change is signaled when:

- A port moves to forwarding.  
- A port in learning or forwarding moves to blocking or disabled.

### RSTP triggers

RSTP signals a topology change when:

- A non edge port (point to point or shared) moves to forwarding.

RSTP does not treat these as change events:

- Edge ports moving to forwarding.  
- Ports moving into discarding.

This reduces unnecessary flooding of topology change notifications in normal host activity.

## Optional protection features

These features enhance the basic loop prevention behavior. They are often used together with Rapid PVST+.

### Root Guard

- Protects against an unexpected switch becoming root.  
- When a port with Root Guard receives a superior BPDU, the port moves to the root inconsistent state.  
- Traffic on that port stops until superior BPDUs stop.  
- Configure on ports that face untrusted switches, such as toward customer equipment in a provider network.

```cisco
interface GigabitEthernet0/1
 spanning-tree guard root
```

### Loop Guard

- Protects against loops when BPDUs stop arriving due to a fault.  
- When a Loop Guard port stops receiving BPDUs, it moves to the loop inconsistent state instead of transitioning to forwarding.  
- Port recovers when BPDUs resume.  
- Useful on nonedge ports that should always see BPDUs, for example alternate ports.

```cisco
interface GigabitEthernet0/1
 spanning-tree guard loop
```

Root Guard and Loop Guard are not used on the same port at the same time.

### BPDU Guard

- Works with PortFast on edge ports.  
- If a BPDU is received on a BPDU Guard port, the port is error disabled.  
- Helps prevent accidental or malicious connection of a switch on an edge port.

```cisco
interface GigabitEthernet0/1
 spanning-tree portfast
 spanning-tree bpduguard enable
```

A common pattern is to enable BPDU Guard globally on all PortFast ports:

```cisco
spanning-tree portfast default
spanning-tree portfast bpduguard default
```

### BPDU Filter

- Prevents BPDUs from being sent or received on a port.  
- Interface level form:

  ```cisco
  interface GigabitEthernet0/1
   spanning-tree bpdufilter enable
  ```

  This completely disables STP on the port and is risky if the port is ever cabled to a switch.

- Global form for PortFast ports:

  ```cisco
  spanning-tree portfast bpdufilter default
  ```

  In this mode, the port does not send BPDUs. If it receives a BPDU, PortFast and BPDU Filter are disabled and the port behaves like a normal STP port. This is safer in case a switch is accidentally connected.

BPDU Guard and BPDU Filter are often used together with PortFast on access ports, with the global defaults preferred over per port filter where possible.

## Verification and troubleshooting

### Key show commands

- `show spanning-tree`  
  - Root bridge, port roles, port states, link types and timers.

- `show spanning-tree summary`  
  - Mode, features and per VLAN status.

- `show spanning-tree interface <name>`  
  - Detailed status for a single port.

- `show spanning-tree detail`  
  - Extra information, including last topology change.

### Common issues

- Slow convergence  
  - RSTP not enabled.  
  - Links are half duplex and treated as shared.  
  - Legacy STP neighbors causing fallback to timer based behavior.

- Ports not forwarding as expected  
  - Port is alternate or backup rather than root or designated.  
  - Protection feature such as Root Guard or Loop Guard is active.

- Unexpected root bridge  
  - Bridge priority not set on the intended root.  
  - Root Guard missing on edge uplinks toward untrusted devices.

- Loops or err disable events  
  - BPDU Filter misapplied on a link between switches.  
  - BPDU Guard shutting down edge ports where a switch was connected.

## Quick review

- RSTP (802.1w) speeds up convergence compared to classic STP by using a sync process and new port roles.  
- Modern Cisco switches often run Rapid PVST+, which applies RSTP behavior per VLAN.  
- RSTP uses three port states (discarding, learning, forwarding) and four roles (root, designated, alternate, backup).  
- Link types (point to point, shared, edge) control how quickly ports can move to forwarding.  
- Edge ports use PortFast behavior and do not trigger topology changes.  
- RSTP interoperates with STP, but mixed links lose the rapid behavior.  
- Root Guard, Loop Guard, BPDU Guard and BPDU Filter add protection against misconfigurations and loops.  
- `show spanning-tree` and related commands are the main tools to verify roles, states, link types and STP mode.
