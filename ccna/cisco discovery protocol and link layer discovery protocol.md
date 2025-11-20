# Cisco Discovery Protocol and Link Layer Discovery Protocol

## Overview

Layer 2 discovery protocols enable network devices to share information about themselves with their directly connected neighbors. This information helps network engineers map out networks, identify devices, understand network topology, and troubleshoot connectivity issues. The two main Layer 2 discovery protocols are Cisco Discovery Protocol (CDP), which is Cisco-proprietary, and Link Layer Discovery Protocol (LLDP), which is an industry-standard protocol. Both protocols serve similar purposes but differ in their implementation and vendor support.

## Cisco Discovery Protocol (CDP)

### CDP Fundamentals

- Cisco-proprietary Layer 2 discovery protocol
- Runs on Cisco network devices such as routers and switches
- Enabled by default on Cisco devices
- Devices periodically send CDP advertisement messages out of their interfaces
- Devices listen for CDP advertisements from neighboring devices
- Shares information including hostname, capabilities, port ID, IP address, software version, and more

### CDP Message Transmission

- CDP messages sent to multicast MAC address 0100.0ccc.cccc
- Switches do not flood CDP messages like regular multicast frames
- Switch receives CDP frame for itself and processes it
- CDP messages are not forwarded beyond directly connected neighbors

### CDP Neighbor Table

- Device maintains table of CDP neighbors
- Neighbors are devices from which CDP messages have been received
- Information stored includes device ID, local interface, port ID, capabilities, platform, and holdtime

### CDP Timers

- **Advertisement timer**: How often device sends CDP messages
  - Default: 60 seconds
  - Configure with: `cdp timer seconds`
- **Holdtime**: How long neighbor keeps device in neighbor table after ceasing to receive CDP messages
  - Default: 180 seconds
  - Configure with: `cdp holdtime seconds`
  - Each time device receives CDP advertisement, holdtime resets to 180 seconds
  - If holdtime counts down to 0, neighbor removes device from table

### CDP Versions

- Two versions: CDPv1 and CDPv2
- Modern Cisco devices send CDPv2 advertisements by default
- Use `no cdp advertise-v2` to enable CDPv1 (for compatibility with very old devices)
- Differences between versions are outside CCNA exam scope

### CDP Configuration

#### Global Configuration

- Enable CDP globally: `cdp run` (enabled by default)
- Disable CDP globally: `no cdp run`
- Configure advertisement timer: `cdp timer seconds`
- Configure holdtime: `cdp holdtime seconds`
- Enable/disable CDPv2: `[no] cdp advertise-v2`

#### Interface Configuration

- Enable CDP on interface: `cdp enable` (enabled by default)
- Disable CDP on interface: `no cdp enable`
- Disabling on interface prevents both sending and receiving CDP messages

### CDP Verification Commands

- `show cdp neighbors`: Lists CDP neighbors and basic information
  - Shows Device ID, Local Interface, Holdtime, Capability, Platform, Port ID
  - Local Interface: Interface on local device where neighbor is connected
  - Port ID: Interface on neighbor device where local device is connected
- `show cdp neighbors detail`: Shows detailed information about all CDP neighbors
  - Includes hostname, platform, capabilities, IP address, software version, native VLAN, duplex, and more
- `show cdp entry name`: Shows same information as `show cdp neighbors detail` for specified neighbor only
- `show cdp`: Shows basic CDP information (status, timers, version)
- `show cdp interface [interface]`: Shows CDP status and information for specific interface or all interfaces
- `show cdp traffic`: Shows statistics about CDP messages sent and received

### CDP Capability Codes

- R: Router
- T: Trans Bridge
- B: Source Route Bridge
- S: Switch
- H: Host
- I: IGMP
- r: Repeater
- P: Phone
- D: Remote
- C: CVTA
- M: Two-port Mac Relay

### CDP Security Considerations

- CDP shares significant information about device
- Information includes software version, which could be used to identify vulnerabilities
- Malicious users could exploit CDP information for targeted attacks
- Consider disabling CDP globally or on specific interfaces where not necessary
- Balance security needs with operational requirements

### Network Mapping with CDP

- Use CDP to map network topology when documentation is incomplete
- Run `show cdp neighbors` on multiple devices
- Use Local Interface and Port ID columns to determine connections
- Build network diagram from CDP neighbor information
- Useful when physical access to devices is not available

## Link Layer Discovery Protocol (LLDP)

### LLDP Fundamentals

- Industry-standard Layer 2 discovery protocol
- Defined in IEEE 802.1AB
- Vendor-neutral protocol that can be implemented by any vendor
- Cisco routers and switches support both CDP and LLDP
- Serves similar purpose to CDP but as industry standard
- Not enabled by default on Cisco devices

### LLDP Message Transmission

- LLDP messages sent to multicast MAC address 0180.c200.000e
- Switches do not flood LLDP messages
- Switch receives LLDP frame for itself and processes it
- LLDP messages are not forwarded beyond directly connected neighbors

### LLDP Configuration

#### Global Configuration

- Enable LLDP globally: `lldp run`
- Disable LLDP globally: `no lldp run`
- Configure advertisement timer: `lldp timer seconds` (default: 30 seconds)
- Configure holdtime: `lldp holdtime seconds` (default: 120 seconds)
- Configure reinitialization delay: `lldp reinit seconds` (default: 2 seconds)

#### Interface Configuration

- Enable LLDP transmission: `lldp transmit` (enabled by default when LLDP is globally enabled)
- Disable LLDP transmission: `no lldp transmit`
- Enable LLDP reception: `lldp receive` (enabled by default when LLDP is globally enabled)
- Disable LLDP reception: `no lldp receive`
- Can control transmission and reception separately
- Allows device to send but not receive, or receive but not send

### LLDP Timers

- **Advertisement timer**: How often device sends LLDP messages
  - Default: 30 seconds (half of CDP's default)
  - Configure with: `lldp timer seconds`
- **Holdtime**: How long neighbor keeps device in neighbor table after ceasing to receive LLDP messages
  - Default: 120 seconds (shorter than CDP's default)
  - Configure with: `lldp holdtime seconds`
- **Reinitialization delay**: How long interface waits before sending LLDP messages after LLDP is activated
  - Default: 2 seconds
  - Configure with: `lldp reinit seconds`
  - Beneficial when interface is bouncing between up and down states
  - Provides time for port to stabilize before sending LLDP messages

### LLDP Verification Commands

- `show lldp neighbors`: Lists LLDP neighbors and basic information
  - Shows Device ID, Local Interface, Hold-time, Capability, Port ID
  - Similar format to `show cdp neighbors`
- `show lldp neighbors detail`: Shows detailed information about all LLDP neighbors
  - Includes system name, system description, chassis ID, port ID, capabilities, management addresses, and more
- `show lldp entry name`: Shows same information as `show lldp neighbors detail` for specified neighbor only
- `show lldp`: Shows basic LLDP information (status, timers)
- `show lldp interface [interface]`: Shows LLDP status for specific interface or all interfaces
  - Shows Tx (transmission) and Rx (reception) status
  - Shows Tx state and Rx state
- `show lldp traffic`: Shows statistics about LLDP messages sent and received

### LLDP Capability Codes

- R: Router
- B: Bridge (equivalent to CDP's S for Switch)
- T: Telephone
- C: DOCSIS Cable Device
- W: WLAN Access Point
- P: Repeater
- S: Station
- O: Other

### CDP vs LLDP

- **CDP**: Cisco-proprietary, enabled by default, works only with Cisco devices
- **LLDP**: Industry-standard, disabled by default, works with any vendor's devices
- Both can run simultaneously on same device (redundant but possible)
- Choose CDP if network uses only Cisco devices
- Choose LLDP if network uses mix of vendors
- Commands are very similar; mostly replace `cdp` with `lldp`

## Real-World Applications

- **Network documentation**: Map out network topology when documentation is incomplete
- **Troubleshooting**: Identify connected devices and interfaces quickly
- **Device discovery**: Find all Cisco devices in network
- **Interface identification**: Determine which interfaces connect to which devices
- **Software version tracking**: Identify devices running specific software versions
- **Network inventory**: Build inventory of network devices and their capabilities
- **Multi-vendor networks**: Use LLDP in networks with mixed vendor equipment
- **Remote network mapping**: Map network when physical access is not available

## Troubleshooting

### Common Issues

- **No neighbors showing**: Verify protocol is enabled globally and on interface
- **Neighbor disappeared**: Check holdtime; neighbor may have stopped sending advertisements
- **Wrong information displayed**: Verify both devices have protocol enabled
- **Security concerns**: Consider disabling on interfaces connected to untrusted networks

### Troubleshooting Steps

1. Verify protocol is enabled: `show cdp` or `show lldp`
2. Check interface status: `show cdp interface` or `show lldp interface`
3. Verify neighbor is sending messages: `show cdp traffic` or `show lldp traffic`
4. Check timers: Verify advertisement timer and holdtime are appropriate
5. Verify interface is up: Check interface status with `show ip interface brief`

## Best Practices

- Use CDP in Cisco-only networks
- Use LLDP in multi-vendor networks
- Disable discovery protocols on interfaces connected to untrusted networks for security
- Document network topology using discovery protocol information
- Regularly review neighbor tables to detect unauthorized devices
- Use discovery protocols to verify network changes
- Balance security needs with operational benefits
- Consider disabling globally if security is primary concern
- Use discovery protocols for network inventory and documentation

## Summary

- Layer 2 discovery protocols enable devices to share information with directly connected neighbors
- CDP is Cisco-proprietary and enabled by default; LLDP is industry-standard and disabled by default
- CDP messages sent to multicast MAC 0100.0ccc.cccc; LLDP messages sent to 0180.c200.000e
- CDP default timers: 60 seconds advertisement, 180 seconds holdtime
- LLDP default timers: 30 seconds advertisement, 120 seconds holdtime, 2 seconds reinitialization delay
- Enable CDP globally with `cdp run`; enable LLDP globally with `lldp run`
- Configure timers with `cdp timer`, `cdp holdtime`, `lldp timer`, `lldp holdtime`, `lldp reinit`
- Disable on interfaces with `no cdp enable` or `no lldp transmit`/`no lldp receive`
- Use `show cdp neighbors` and `show lldp neighbors` to view neighbor information
- Use `show cdp neighbors detail` and `show lldp neighbors detail` for detailed information
- Use `show cdp entry name` and `show lldp entry name` for specific neighbor information
- Use `show cdp` and `show lldp` to view protocol status and timers
- Use `show cdp interface` and `show lldp interface` to view interface status
- Use `show cdp traffic` and `show lldp traffic` to view message statistics
- Local Interface column shows interface on local device; Port ID shows interface on neighbor
- CDP and LLDP share similar information: hostname, capabilities, platform, IP address, software version
- Choose CDP for Cisco-only networks; choose LLDP for multi-vendor networks
- Consider security implications of sharing device information via discovery protocols

