# Cisco Discovery Protocol and Link Layer Discovery Protocol

## Overview

Layer 2 discovery protocols let directly connected devices share basic information about themselves. This helps with topology mapping, documentation, and troubleshooting. Two protocols matter for CCNA:

- Cisco Discovery Protocol (CDP): Cisco proprietary
- Link Layer Discovery Protocol (LLDP): IEEE standard (802.1AB)

Both advertise information such as hostname, interface, capabilities, and software version to neighbors on the same link.

## Cisco Discovery Protocol (CDP)

### CDP basics

- Cisco proprietary Layer 2 discovery protocol
- Runs on Cisco routers, switches, and many other Cisco devices
- Enabled by default on most Cisco platforms
- Sends periodic advertisement messages out each CDP-enabled interface
- Listens for CDP advertisements from neighbors
- Typical advertised information:
  - Device ID (hostname)
  - Port ID (neighbor interface)
  - Local interface
  - Platform and capabilities
  - Software version
  - Management IP address

CDP frames use multicast MAC address `0100.0ccc.cccc`. They are processed locally and not forwarded beyond directly connected neighbors.

### CDP neighbor table

Each device maintains a CDP neighbor table:

- Populated from received CDP advertisements
- Stores:
  - Device ID
  - Local interface
  - Port ID (neighbor interface)
  - Capabilities
  - Platform
  - Holdtime

Entries remain until the holdtime expires or new advertisements refresh them.

### CDP timers

Two main timers control CDP behavior:

- Advertisement timer
  - How often CDP sends messages
  - Default: 60 seconds
  - Command: `cdp timer seconds`
- Holdtime
  - How long a neighbor keeps the entry after advertisements stop
  - Default: 180 seconds
  - Command: `cdp holdtime seconds`

Each new advertisement resets the holdtime for that neighbor.

### CDP configuration

CDP can be controlled globally and per interface.

Global:

- Enable: `cdp run` (default)
- Disable: `no cdp run`
- Set advertisement timer: `cdp timer seconds`
- Set holdtime: `cdp holdtime seconds`
- CDP version:
  - Default is CDPv2
  - Disable v2 advertisements (use v1 only): `no cdp advertise-v2`

Interface:

- Enable on interface: `cdp enable` (default)
- Disable on interface: `no cdp enable`

Disabling on an interface stops both sending and receiving CDP messages on that interface.

### CDP verification

Common commands:

- `show cdp neighbors`
  - Lists neighbors and basic data
  - Columns: Device ID, Local Interface, Holdtime, Capability, Platform, Port ID
- `show cdp neighbors detail`
  - Detailed view of all neighbors
  - Includes hostname, platform, capabilities, IP address, software version, native VLAN, duplex
- `show cdp entry NAME`
  - Detailed view of a single neighbor
- `show cdp`
  - Shows CDP status, version, and timers
- `show cdp interface [interface]`
  - CDP status per interface
- `show cdp traffic`
  - Counters for CDP packets sent and received

### CDP capability codes

Codes shown in the Capability column of `show cdp neighbors`:

- R: Router
- T: Transparent bridge
- B: Source route bridge
- S: Switch
- H: Host
- I: IGMP
- r: Repeater
- P: Phone
- D: Remote
- C: CVTA
- M: Two-port MAC relay

Memorizing all codes is less important than recognizing routers, switches, and phones.

### CDP security and usage

CDP exposes information that can help attackers:

- Hostname and platform
- Software version
- IP addressing and VLAN details

Typical practices:

- Disable CDP on interfaces facing untrusted networks:
  - `interface G0/0`
  - `no cdp enable`
- Consider disabling globally in very sensitive environments
- Leave enabled on internal links where topology discovery and troubleshooting are important

CDP is very useful for:

- Building or validating network diagrams
- Identifying what is connected to each interface
- Checking neighbor software versions and platforms

## Link Layer Discovery Protocol (LLDP)

### LLDP basics

- Vendor-neutral Layer 2 discovery protocol
- Defined in IEEE 802.1AB
- Supported by many vendors, including Cisco
- Similar purpose to CDP but standardized

Cisco devices support both CDP and LLDP at the same time. LLDP is disabled by default on Cisco IOS.

LLDP frames use multicast MAC address `0180.c200.000e`. Like CDP, LLDP messages stay on the local link and are not forwarded further.

### LLDP timers

LLDP uses similar timers to CDP:

- Advertisement timer
  - How often LLDP messages are sent
  - Default: 30 seconds
  - Command: `lldp timer seconds`
- Holdtime
  - How long a neighbor keeps the entry after advertisements stop
  - Default: 120 seconds
  - Command: `lldp holdtime seconds`
- Reinitialization delay
  - Delay before LLDP starts sending messages after being enabled
  - Default: 2 seconds
  - Command: `lldp reinit seconds`

The shorter default advertisement and holdtime values make LLDP react a bit faster than CDP by default.

### LLDP configuration

Global:

- Enable LLDP: `lldp run`
- Disable LLDP: `no lldp run`
- Adjust timers with:
  - `lldp timer seconds`
  - `lldp holdtime seconds`
  - `lldp reinit seconds`

Interface:

- Enable transmit: `lldp transmit`
- Enable receive: `lldp receive`
- Disable transmit: `no lldp transmit`
- Disable receive: `no lldp receive`

Transmit and receive can be controlled independently per interface. For example, an interface can send LLDP but not accept LLDP from the neighbor.

### LLDP verification

Common commands:

- `show lldp neighbors`
  - Neighbor summary
  - Similar layout to `show cdp neighbors`
- `show lldp neighbors detail`
  - Detailed view of all LLDP neighbors
  - Includes system name, description, chassis ID, port ID, capabilities, management addresses
- `show lldp entry NAME`
  - Detailed view of a single neighbor
- `show lldp`
  - Global LLDP status and timers
- `show lldp interface [interface]`
  - LLDP status per interface, including transmit and receive state
- `show lldp traffic`
  - Counters for LLDP packets sent and received

### LLDP capability codes

Common capability codes:

- R: Router
- B: Bridge (switch)
- T: Telephone
- C: DOCSIS cable device
- W: WLAN access point
- P: Repeater
- S: Station
- O: Other

As with CDP, knowing router, switch, and phone codes is usually enough for CCNA.

## CDP and LLDP comparison

Key differences:

- CDP
  - Cisco proprietary
  - Enabled by default
  - Works only between Cisco devices
- LLDP
  - IEEE 802.1AB standard
  - Disabled by default on Cisco devices
  - Works across vendors

Both protocols can run on the same interface at the same time. In a Cisco-only network, CDP alone is often enough. In multi-vendor networks, LLDP is the standard choice.

Commands are similar. Often, `cdp` in a command is replaced with `lldp` for the equivalent LLDP command.

## Operational use cases

Typical uses for CDP and LLDP:

- Topology discovery and documentation
- Verifying which device connects to which interface
- Validating uplinks during changes and migrations
- Locating devices by hostname or IP
- Building an inventory of device types and software versions

In production networks:

- Enable on internal links where discovery is helpful
- Disable on interfaces facing the internet, guest networks, or other untrusted segments
- Use neighbor output as a quick cross-check against formal documentation

## Troubleshooting checklist

When neighbors do not show up as expected:

1. Confirm the protocol is globally enabled:
   - `show cdp` or `show lldp`
2. Check that the interface is up and in the correct VLAN:
   - `show ip interface brief`
3. Verify protocol status on the interface:
   - `show cdp interface` or `show lldp interface`
4. Look at traffic counters:
   - `show cdp traffic` or `show lldp traffic`
5. Check timers if entries appear and then disappear:
   - Holdtime may be expiring without new advertisements

If only one side sees the neighbor, check transmit and receive settings on both ends.

## Quick review

- CDP and LLDP are Layer 2 discovery protocols that advertise device information to directly connected neighbors.
- CDP is Cisco proprietary and enabled by default; LLDP is an IEEE standard and disabled by default on Cisco IOS.
- CDP uses multicast MAC `0100.0ccc.cccc` with default timers of 60 seconds (advertisement) and 180 seconds (holdtime).
- LLDP uses multicast MAC `0180.c200.000e` with default timers of 30 seconds (advertisement), 120 seconds (holdtime), and 2 seconds (reinit).
- Global enable commands:
  - CDP: `cdp run`
  - LLDP: `lldp run`
- Key verification commands:
  - `show cdp neighbors` and `show cdp neighbors detail`
  - `show lldp neighbors` and `show lldp neighbors detail`
- Disable discovery where information leakage is a concern, especially on interfaces facing untrusted networks.
