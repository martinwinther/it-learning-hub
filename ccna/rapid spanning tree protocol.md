# Rapid Spanning Tree Protocol

## Overview

Rapid Spanning Tree Protocol (RSTP) addresses the slow convergence of the original Spanning Tree Protocol (STP). While STP can take up to 50 seconds to converge after a topology change, RSTP uses a synchronization mechanism to transition ports to the forwarding state almost immediately, reducing convergence time to just over 6 seconds or less than 1 second in some cases.

## STP Versions

### Standard and Cisco-Proprietary Versions

- **STP (802.1D)**: Original standard; creates a single spanning tree for the entire LAN
- **PVST+**: Cisco-proprietary enhancement of 802.1D; creates a separate spanning tree for each VLAN
- **RSTP (802.1w)**: Standard rapid version; much faster convergence than 802.1D; creates a single spanning tree
- **Rapid PVST+**: Cisco-proprietary enhancement of 802.1w; creates a separate spanning tree for each VLAN; runs on modern Cisco switches
- **MSTP (802.1s)**: Multiple Spanning Tree Protocol; groups multiple VLANs into each spanning tree instance; uses RSTP mechanics for fast convergence

### Configuring STP Mode

- Use `show spanning-tree` to check which version is running:
  - `Spanning tree enabled protocol ieee` indicates PVST+
  - `Spanning tree enabled protocol rstp` indicates Rapid PVST+
- Configure with `spanning-tree mode {pvst | rapid-pvst}` in global configuration mode
- Default mode depends on switch model and IOS version

### PVST+ and Rapid PVST+ Considerations

- **Benefit**: Each VLAN can have a unique spanning tree topology, allowing traffic balancing across different links
- **Downside**: In LANs with many VLANs, each switch runs multiple STP instances, sending separate BPDUs for each VLAN
- This can tax CPU and memory resources; MSTP may be preferred for large-scale deployments

## RSTP vs STP: Key Differences

### Fundamental Difference

- **STP**: Timer-based protocol; ports can take up to 50 seconds to begin forwarding
- **RSTP**: Uses a synchronization mechanism; switches communicate to bring ports immediately to forwarding state without waiting for timers

### BPDU Transmission

- **STP**: Only the root bridge sends BPDUs; other switches forward them out of designated ports
- **RSTP**: All switches send BPDUs out of their designated ports every 2 seconds, whether they received a BPDU from the root bridge or not

### Root Bridge Election and Port Selection

The algorithm for root bridge election, root port selection, and designated port selection is identical in STP and RSTP:

- **Root bridge election**: Lowest bridge ID (BID)
- **Root port selection**:
  - Lowest root cost
  - Lowest neighbor BID
  - Lowest neighbor port ID
  - Lowest local port ID (tiebreaker when multiple ports on same switch connect to same segment)
- **Designated port selection**:
  - Port on switch with lowest root cost
  - Port on switch with lowest BID
  - Lowest local port ID (tiebreaker)

## RSTP Port Costs

### Short vs Long Costs

- **Short costs**: Original STP port costs (up to 10 Gbps)
- **Long costs**: RSTP-introduced costs to accommodate higher speeds (up to 10 Tbps)

### Port Cost Values

| Speed | Short Cost | Long Cost |
|-------|------------|-----------|
| 10 Mbps | 100 | 2,000,000 |
| 100 Mbps | 19 | 200,000 |
| 1 Gbps | 4 | 20,000 |
| 10 Gbps | 2 | 2,000 |
| 100 Gbps | - | 200 |
| 1 Tbps | - | 20 |
| 10 Tbps | - | 2 |

### Configuring Path Cost Method

- View current method: `show spanning-tree pathcost method`
- Configure method: `spanning-tree pathcost method {short | long}` in global configuration mode
- Default method depends on switch model and software version

## RSTP Port States

### State Comparison

| STP Port State | RSTP Port State |
|----------------|-----------------|
| Blocking | Discarding |
| Listening | Discarding |
| Learning | Learning |
| Forwarding | Forwarding |

### State Transitions

- When an RSTP port is first enabled, it enters the **discarding** state
- **Alternate and backup ports**: Remain in discarding state to prevent loops
- **Root and designated ports**: Transition to forwarding state in one of two ways:
  1. **Sync mechanism succeeds**: Port immediately transitions to forwarding (no timers)
  2. **Sync mechanism fails**: Port transitions discarding → learning (15 seconds) → forwarding (15 seconds), similar to STP

### Compatibility

- RSTP and STP are compatible
- A port on an RSTP-enabled switch connected to an STP-enabled switch will operate like a regular STP port (timer-based transitions)

## RSTP Port Roles

### Four Port Roles

- **Root port**: Forwarding port that points toward the root bridge; provides the switch's only active path to the root
- **Designated port**: Forwarding port that points away from the root bridge; each segment must have exactly one designated port
- **Alternate port**: Provides an alternative path toward the root bridge; ready to take over if the root port fails
- **Backup port**: Provides a backup path to the same segment as a designated port on the same switch (rare, occurs with hubs)

### Alternate Port Rules

- Any port that is not a root or designated port is an alternate port if the switch is **not** the designated bridge for that segment
- In almost all cases, a port that is neither root nor designated will be an alternate port

### Backup Port Rules

- Any port that is not a root or designated port is a backup port if the switch **is** the designated bridge for that segment
- Only occurs when two ports on the same switch are connected to the same segment (via a hub)
- Extremely rare in modern networks (hubs are obsolete)

### Viewing Port Roles

Use `show spanning-tree` to view port roles:

- `Root` = Root port
- `Desg` = Designated port
- `Altn` = Alternate port
- `Back` = Backup port

## RSTP Convergence

### Topology Change Detection

- **STP**: Waits 20 seconds (max age timer) after ceasing to receive BPDUs before reacting
- **RSTP**: Waits until a port misses three BPDUs (6 seconds by default) before reacting

### Convergence Scenarios

- **Hardware failure without port down**: Next-best port can sync and immediately move to forwarding state (~6 seconds total)
- **Hardware failure with port down**: Port immediately initiates sync process (<1 second total downtime)

## RSTP Link Types

### Three Link Types

- **Point-to-point**: Full-duplex ports that can use RSTP sync mechanism to immediately transition to forwarding state
- **Shared**: Half-duplex ports that cannot use RSTP sync mechanism; must transition through states like standard STP (30 seconds)
- **Edge**: Ports connected to end hosts that can use PortFast to immediately transition to forwarding state

### Automatic Detection

- Full-duplex ports automatically use point-to-point link type
- Half-duplex ports automatically use shared link type
- Edge link type must be manually configured with `spanning-tree portfast` (not automatically determined)

### Manual Configuration

- Point-to-point: `spanning-tree link-type point-to-point` in interface configuration mode
- Shared: `spanning-tree link-type shared` in interface configuration mode
- Edge: `spanning-tree portfast` in interface configuration mode

### Viewing Link Types

Use `show spanning-tree` to view link types:

- `P2p` = Point-to-point
- `Shr` = Shared
- `Edge` = Edge (may appear as `P2p Edge` or `Shr Edge`)

### Edge Port Characteristics

- Edge ports don't trigger topology change process when transitioning to forwarding state
- RSTP doesn't notify neighbors of activity on edge ports (no risk of loops from end hosts)

## Topology Change Process

### STP Triggers

- When any port transitions to the forwarding state
- When a port in learning or forwarding state transitions to blocking or disabled state

### RSTP Triggers

- Only when a port with a non-edge link type (point-to-point or shared) transitions to the forwarding state
- Does not trigger when:
  - An edge port transitions to the forwarding state
  - Any port transitions to the discarding state

## Optional STP Features

### Root Guard

- **Purpose**: Prevents external switches from becoming the root bridge
- **Use case**: Service provider networks where customer switches should not affect the STP topology
- **Behavior**: When a Root Guard-enabled port receives a superior BPDU, it enters the **root-inconsistent** state, effectively disabling the port
- **Recovery**: Port automatically recovers when superior BPDUs are no longer received
- **Configuration**: `spanning-tree guard root` in interface configuration mode
- **Verification**: Port status shows `BKN` (broken) and `ROOT_Inc` (root-inconsistent)

### Loop Guard

- **Purpose**: Guards against Layer 2 loops by preventing ports from erroneously transitioning to forwarding state
- **Use case**: Protects against software malfunctions that prevent BPDU transmission
- **Behavior**: When a Loop Guard-enabled port stops receiving BPDUs, it enters the **loop-inconsistent** state, disabling the port
- **Recovery**: Port automatically recovers when BPDUs are received again
- **Configuration**: `spanning-tree guard loop` in interface configuration mode
- **Verification**: Port status shows `BKN` (broken) and `LOOP_Inc` (loop-inconsistent)

### Root Guard vs Loop Guard

- **Mutually exclusive**: Cannot enable both on the same port simultaneously
- **Root Guard**: Takes action based on receiving superior BPDUs
- **Loop Guard**: Takes action based on not receiving BPDUs

### BPDU Filter

- **Purpose**: Prevents BPDUs from being sent or received on specific ports
- **Use case**: Ports connected to end hosts where STP isn't necessary

#### Interface-Level Configuration

- Command: `spanning-tree bpdufilter enable` in interface configuration mode
- Behavior:
  - Port will not send BPDUs
  - Port will ignore any BPDUs it receives
  - Effectively disables STP on the port
- **Warning**: High risk of causing Layer 2 loops if port is connected to another switch

#### Global Configuration

- Command: `spanning-tree portfast bpdufilter default` in global configuration mode
- Behavior:
  - Enables BPDU Filter on all PortFast-enabled ports
  - Port will not send BPDUs
  - If port receives a BPDU, PortFast and BPDU Filter are disabled; port operates as normal STP/RSTP port
- **Safer option**: Automatically disables if a switch is detected

## Verification Commands

- `show spanning-tree`: View STP/RSTP status, port roles, states, and link types
- `show spanning-tree pathcost method`: View which cost calculation method is in use
- `show spanning-tree summary`: View summary of all VLANs and their STP status

## Troubleshooting RSTP

### Common Issues

- **Slow convergence**: Verify RSTP is enabled (`show spanning-tree`); check link types (should be point-to-point for switch-to-switch links)
- **Ports not forwarding**: Check port roles and states; verify sync mechanism is working (point-to-point links)
- **Unexpected root bridge**: Verify bridge priorities; check for Root Guard blocking superior BPDUs
- **Loops forming**: Check for BPDU Filter misconfiguration; verify Loop Guard is enabled on alternate ports

### Best Practices

- Enable Rapid PVST+ on all switches: `spanning-tree mode rapid-pvst`
- Configure PortFast on edge ports: `spanning-tree portfast`
- Enable BPDU Guard on edge ports: `spanning-tree bpduguard enable`
- Use Root Guard on ports facing untrusted networks
- Use Loop Guard on alternate ports to prevent loops
- Avoid BPDU Filter unless absolutely necessary and only on confirmed end-host ports

## Real-World Applications

- **Enterprise networks**: Rapid PVST+ provides fast convergence while maintaining per-VLAN topology control
- **Service provider networks**: Root Guard prevents customer switches from disrupting provider topology
- **Data centers**: Fast convergence is critical for high availability; RSTP reduces downtime during topology changes
- **Large-scale deployments**: Consider MSTP to reduce resource consumption when many VLANs share the same topology

## Summary

- RSTP (802.1w) and Rapid PVST+ provide much faster convergence than STP (802.1D) and PVST+
- RSTP uses three port states (discarding, learning, forwarding) compared to STP's four states
- RSTP introduces alternate and backup port roles, replacing STP's nondesignated role
- RSTP link types (point-to-point, shared, edge) determine how ports transition to forwarding state
- RSTP convergence can be as fast as less than 1 second compared to STP's 50 seconds
- Root Guard prevents external switches from becoming root bridge
- Loop Guard prevents loops when BPDUs stop being received
- BPDU Filter should be used with extreme caution; prefer global configuration over interface-level
- Modern networks should use Rapid PVST+ for fast convergence and per-VLAN topology control
