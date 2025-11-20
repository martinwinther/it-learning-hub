# Network Time Protocol

## Overview

Network Time Protocol (NTP) enables devices across a network to synchronize their clocks to a common time source. Accurate and consistent timekeeping is critical for network operations, including security protocols, event logging, and troubleshooting. NTP uses a hierarchical model where devices synchronize their clocks to authoritative time sources, ensuring all network devices maintain accurate and synchronized time. NTP is used by network infrastructure devices like routers and switches, as well as end devices like PCs, smartphones, and servers.

## Importance of Accurate Time

### Event Logging

- Network devices create log entries for various events
- Examples: interface up/down, OSPF neighbor state changes, user logins
- Each log entry includes timestamp indicating when event occurred
- Accurate timestamps essential for correlating events between devices
- View logs with `show logging` command

### Security Protocols

- Many security protocols rely on time-based mechanisms
- Transport Layer Security (TLS) requires accurate time
- Certificate validation depends on current time
- Authentication protocols may use time-based tokens

### Troubleshooting

- Correlating log entries between devices requires synchronized clocks
- Without synchronized time, identifying cause of issues is difficult
- Accurate timestamps help identify sequence of events
- Essential for forensic analysis of security incidents

## Manual Time Configuration

### Software Clock

- All Cisco routers and switches have internal software clock
- View current time with `show clock` command
- View detailed information with `show clock detail`
- Asterisk (*) indicates time is not authoritative
- Set software clock with: `clock set hh:mm:ss month day year`
- Command executed from privileged EXEC mode, not global config mode

### Hardware Calendar

- Some devices have battery-powered hardware clock called calendar
- Keeps time even when device is shut off
- View calendar time with `show calendar` command
- Set calendar with: `calendar set hh:mm:ss month day year`
- Sync calendar to clock: `clock update-calendar`
- Sync clock to calendar: `clock read-calendar`

### Time Zone Configuration

- Default time zone is Coordinated Universal Time (UTC)
- Change time zone with: `clock timezone name hours-offset minutes-offset`
- Configured in global config mode
- Hours-offset and minutes-offset are relative to UTC
- Example: `clock timezone JST 9 0` for Japan Standard Time (UTC+9)

### Daylight Saving Time

- Some countries adjust clocks forward in spring and back in fall
- Called daylight saving time (DST) or summer time
- Configure with: `clock summer-time name recurring start-date-time end-date-time`
- Example: `clock summer-time EDT recurring 2 Sun Mar 2:00 1 Sun Nov 2:00`
- Configured in global config mode

## NTP Fundamentals

### NTP Operation

- NTP clients send NTP requests to UDP port 123 on NTP servers
- NTP allows accuracy within 1 millisecond on LAN
- Accuracy within 10-100 milliseconds over WAN or internet
- Devices can be NTP clients, NTP servers, or both simultaneously

### NTP Hierarchy

- Uses hierarchical model for time synchronization
- At top are reference clocks (stratum 0): atomic clocks, GPS clocks
- Stratum indicates "distance" from reference clock
- Lower stratum value means closer to reference clock
- Upper stratum limit is 15; stratum 16 indicates unreliable time source

### Stratum Levels

- **Stratum 0**: Reference clocks (atomic clocks, GPS clocks)
- **Stratum 1**: NTP servers that learn time directly from reference clocks (primary servers)
- **Stratum 2**: NTP servers that learn time from stratum 1 servers
- **Stratum 3**: NTP servers that learn time from stratum 2 servers
- Pattern continues up to stratum 15
- Devices prefer lower stratum servers over higher stratum servers

### Primary and Secondary Servers

- **Primary server**: Gets time directly from reference clock (stratum 1)
- Not NTP clients of reference clocks; directly connect via specialized hardware
- **Secondary server**: Gets time from another NTP server (stratum 2 or higher)
- Secondary servers are both NTP clients and NTP servers simultaneously

### Multiple Time Sources

- Devices can be clients of multiple NTP servers (recommended)
- Provides redundancy and fault tolerance
- If one server goes down, client can still learn time from another
- Clients use algorithms to analyze time reports from each server
- Discard outliers and select best time source

### NTP Peering

- Two NTP servers can form peer relationship
- Allows bidirectional exchange of time information
- Unlike client-server relationship where client syncs solely based on server
- Peering provides redundancy and fault tolerance
- Each peer uses other's time data as additional reference point
- Improves overall accuracy of timekeeping

## NTP Configuration

### Client/Server Mode

- Configure device as NTP client: `ntp server ip-address [prefer]`
- `prefer` keyword tells device to favor specified server when deciding which to sync to
- Does not guarantee selection; other factors like stratum still considered
- Device becomes both NTP client and NTP server (client/server mode)
- Can configure multiple servers for redundancy

### NTP Verification

- `show ntp associations`: View information about NTP time sources
  - Shows address, ref clock, stratum, when, poll, reach, delay, offset, disp
  - `*` indicates sys.peer (currently synced server)
  - `+` indicates candidate (reliable but not currently used)
  - `~` indicates configured
- `show ntp status`: View device's NTP status
  - Shows if clock is synchronized
  - Shows device's stratum in NTP hierarchy
  - Shows reference time source
- NTP synchronization can take 15-20 minutes
- Tip: Manually configure correct time before configuring NTP to speed up process

### NTP Server Mode

- Device automatically functions as NTP server when configured as client
- Other devices can use it as their NTP server
- No additional configuration needed for basic server functionality
- Device's stratum is one higher than server it syncs to

### Loopback Interface for NTP Server

- Recommended practice: use loopback interface for NTP server address
- Provides stable, reliable interface not dependent on physical port
- Configure clients to use loopback IP address as NTP server
- Configure source interface: `ntp source loopback0`
- If physical port goes down, clients can still sync via loopback

### Master Mode (Server Mode)

- Configure device as primary NTP server: `ntp master [stratum]`
- Uses device's own internal clock as reference clock
- Called server mode (as opposed to client/server mode)
- Default stratum is 7 (device becomes stratum 8 server)
- Can optionally specify stratum value
- Not meant to replace `ntp server` command; use together
- Provides backup time source if external servers become unavailable
- Useful in isolated networks without internet access

### Symmetric Active Mode (Peering)

- Configure NTP peers: `ntp peer ip-address`
- Configure on both devices, specifying other device's IP address
- Each peer acts as time source for the other
- Provides bidirectional exchange of time information
- Called symmetric active mode

### NTP Modes Summary

- **Client/Server mode** (`ntp server`): Device becomes client of NTP server and server for other clients
- **Server mode** (`ntp master`): Device becomes primary NTP server using local clock as reference
- **Symmetric active mode** (`ntp peer`): Two devices become NTP peers, each using other as time source

### Calendar Synchronization

- NTP syncs only software clock by default, not hardware calendar
- Configure: `ntp update-calendar` to make NTP periodically update calendar
- Ensures hardware calendar remains accurate

## NTP Authentication

### Purpose of Authentication

- Public NTP servers are open with no security checks
- In secure environments, need to ensure clients only sync to authorized servers
- Prevents malicious servers from providing incorrect time data
- Authentication verifies server's identity (not attacker with spoofed IP address)

### Authentication Configuration

#### Server Configuration

1. Make device NTP server: `ntp master`
2. Create authentication key: `ntp authentication-key key-number md5 key`
   - `key-number`: Numerical identifier for key
   - `key`: Actual password
   - Newer IOS versions support hashing protocols beyond MD5
3. Specify key as trusted: `ntp trusted-key key-number`
   - Required step; key cannot be used without this

#### Client Configuration

1. Create same authentication key: `ntp authentication-key key-number md5 key`
   - Both key-number and key must match server's configuration
2. Specify key as trusted: `ntp trusted-key key-number`
3. Configure server with authentication: `ntp server ip-address key key-number`
   - Client includes key in NTP messages to server
   - Server includes same key in messages to client
   - If key number or key doesn't match, client refuses to sync

### Peer Authentication

- Configure authentication between NTP peers similarly
- Replace `ntp server ip-address key key-number` with `ntp peer ip-address key key-number`
- Configure on both peers
- Both key-number and key must match on both devices

### Authentication Notes

- `ntp authenticate` command often included in examples but usually not necessary
- Not needed when using `ntp server ip-address key key-number` command
- Required for other NTP modes beyond CCNA scope (passive, broadcast client, multicast client)

## Real-World Applications

- **Network-wide time synchronization**: Ensure all devices have synchronized time
- **Security compliance**: Meet requirements for accurate timestamps in logs
- **Troubleshooting**: Correlate events across multiple devices using timestamps
- **Forensic analysis**: Analyze security incidents with accurate time information
- **Certificate validation**: Ensure certificates are validated correctly based on current time
- **Multi-site networks**: Synchronize time across geographically distributed networks
- **High-availability environments**: Maintain consistent time across redundant systems

## Troubleshooting

### Common Issues

- **Clock not synchronizing**: Verify NTP server is reachable
- **Slow synchronization**: Manually set time before configuring NTP
- **Authentication failures**: Verify key-number and key match on both devices
- **Wrong time source selected**: Check stratum values and prefer keyword
- **Calendar out of sync**: Configure `ntp update-calendar`

### Troubleshooting Steps

1. Verify NTP status: `show ntp status`
2. Check associations: `show ntp associations`
3. Verify server reachability: Ping NTP server
4. Check authentication: Verify keys match on client and server
5. Review clock: `show clock detail` to see time source
6. Verify configuration: Check NTP server and authentication settings

## Best Practices

- Configure multiple NTP servers for redundancy
- Use `prefer` keyword for primary time source
- Use loopback interface for NTP server address
- Configure `ntp source` to specify source interface
- Use `ntp master` as backup if external servers unavailable
- Configure NTP authentication in secure environments
- Manually set time before configuring NTP to speed synchronization
- Configure time zone and DST if applicable
- Sync hardware calendar with software clock
- Monitor NTP associations regularly
- Use lower stratum servers when possible
- Document NTP server addresses and authentication keys

## Summary

- Accurate time is critical for event logging, security protocols, and troubleshooting
- View software clock with `show clock`; set with `clock set hh:mm:ss month day year`
- View hardware calendar with `show calendar`; set with `calendar set hh:mm:ss month day year`
- Sync calendar to clock with `clock update-calendar`; sync clock to calendar with `clock read-calendar`
- Configure time zone with `clock timezone name hours-offset minutes-offset`
- Configure DST with `clock summer-time name recurring start-date-time end-date-time`
- NTP clients send requests to UDP port 123 on NTP servers
- NTP uses hierarchical model with stratum levels (0-15)
- Stratum 0: Reference clocks; Stratum 1: Primary servers; Stratum 2+: Secondary servers
- Configure client/server mode with `ntp server ip-address [prefer]`
- Device automatically functions as NTP server when configured as client
- Use loopback interface for NTP server address for stability
- Configure `ntp source interface` to specify source interface
- Configure master mode with `ntp master [stratum]` for backup time source
- Configure peering with `ntp peer ip-address` on both devices
- Verify with `show ntp associations` and `show ntp status`
- Configure authentication with `ntp authentication-key key-number md5 key` and `ntp trusted-key key-number`
- Use `ntp server ip-address key key-number` to authenticate server
- Both key-number and key must match on client and server
- NTP synchronization can take 15-20 minutes; manually set time first to speed up

