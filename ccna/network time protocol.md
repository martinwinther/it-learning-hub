# Network Time Protocol

## Overview

Network Time Protocol (NTP) synchronizes device clocks to a common time source. Accurate time is important for logging, security protocols, and troubleshooting. NTP uses a hierarchical model with reference clocks at the top and network devices at lower levels.

## Why accurate time matters

### Event logging

- Network devices log events such as interface changes, routing updates, and logins
- Each entry includes a timestamp
- Correlating events across devices requires synchronized clocks
- Logs are viewed with commands such as `show logging`

### Security protocols and certificates

- Many security mechanisms use time checks
- TLS certificate validation depends on current time
- Time based authentication tokens require correct time
- Incorrect time can cause otherwise valid connections to fail

### Troubleshooting and forensics

- Sequence of events is easier to follow when timestamps align
- Cross device analysis during incidents relies on consistent time
- Accurate time supports reliable forensic investigations

## Manual time configuration

NTP is the main method in production, but basic manual time settings are still useful.

### Software clock

- Every Cisco device has a software clock
- View current time:
  - `show clock`
  - `show clock detail`
- An asterisk `*` in `show clock detail` indicates time is not authoritative
- Set time in privileged EXEC mode:
  - `clock set hh:mm:ss month day year`

### Hardware calendar

- Some platforms have a battery backed hardware calendar
- Calendar keeps time when the device is powered off
- Commands:
  - View calendar: `show calendar`
  - Set calendar: `calendar set hh:mm:ss month day year`
  - Copy software clock to calendar: `clock update-calendar`
  - Copy calendar to software clock: `clock read-calendar`

### Time zone and daylight saving

- Default time zone is UTC
- Configure time zone:
  - `clock timezone NAME hours-offset minutes-offset`
- Configure daylight saving time:
  - `clock summer-time NAME recurring start-date-time end-date-time`
- These commands are entered in global configuration mode

## NTP fundamentals

### Operation

- NTP uses UDP port 123
- Devices can act as NTP clients, servers, or both
- NTP can achieve millisecond accuracy on a LAN
- Accuracy is lower over WAN and internet links

### Hierarchy and stratum

- NTP uses stratum values to indicate distance from a reference clock
- Stratum 0
  - Reference clocks such as atomic clocks and GPS sources
- Stratum 1
  - Servers that take time directly from stratum 0
- Stratum 2 and higher
  - Servers that learn time from lower stratum servers
- Valid stratum range is 1 through 15
- Stratum 16 indicates an unusable time source
- Devices prefer servers with lower stratum values

### Primary and secondary servers

- Primary NTP server
  - Learns time directly from a reference clock
  - Operates at stratum 1
- Secondary NTP server
  - Learns time from another NTP server
  - Often serves other devices while acting as a client upstream

### Multiple servers and peering

- Devices can use multiple NTP servers for redundancy
- NTP algorithms compare multiple time sources and select the best one
- Outlier sources are discarded
- NTP peering:
  - Two servers use `ntp peer` to exchange time information in both directions
  - Peering improves resilience when no single upstream source is ideal

## NTP configuration

### Client and server mode

- Configure a device as an NTP client:

  ```cisco
  ntp server 192.0.2.10
  ntp server 192.0.2.11 prefer
  ```

- `prefer` marks a server as the preferred choice when several are usable
- An NTP client that is synchronized can also act as an NTP server for other devices
- Most devices are in client and server mode at the same time

### Verification

- `show ntp status`
  - Shows whether the clock is synchronized
  - Shows local stratum and reference time source
- `show ntp associations`
  - Lists known NTP sources and their state
  - Symbols:
    - `*` current time source (sys.peer)
    - `+` candidate that is considered reliable
    - `~` configured but not yet selected

NTP can take some time to reach full synchronization. Manually setting the approximate time before enabling NTP can help it converge faster.

### NTP server behavior

- When a device synchronizes with an upstream server, it becomes:
  - A client of that server
  - A server for its own clients
- The stratum of the device is one higher than the stratum of the source it uses

### Loopback as NTP source

- Loopback interfaces provide stable IP addresses for NTP servers
- Advantages:
  - Address does not change when physical interfaces go up or down
  - Clients always point to the same address

Example:

```cisco
interface Loopback0
 ip address 192.0.2.100 255.255.255.255
!
ntp source Loopback0
ntp server 198.51.100.10
```

- Clients use 192.0.2.100 as NTP server address

### Master mode

- `ntp master [stratum]` turns a device into an NTP server based on its local clock
- Default stratum used by `ntp master` is 7
- Common uses:
  - Backup time source when external servers are unavailable
  - Time source for isolated labs that lack internet access
- `ntp master` does not replace `ntp server` configuration
- Devices often use both, with external servers preferred and master mode as fallback

### NTP peering

- Symmetric active mode uses `ntp peer`:

  ```cisco
  ntp peer 192.0.2.21
  ntp peer 192.0.2.22
  ```

- Configure peering on both devices
- Each peer treats the other as another time source
- Peering provides additional resilience for server clusters

### Calendar synchronization

- By default, NTP updates only the software clock
- Use `ntp update-calendar` to copy NTP learned time to the hardware calendar
- Helps keep calendar accurate through reloads

## NTP authentication

### Purpose

- Prevents clients from trusting unauthorized NTP sources
- Reduces risk of malicious or misconfigured servers providing incorrect time
- Especially important in secure or regulated environments

### Authentication steps

NTP authentication uses keys that must match on client and server.

Common pattern:

1. Define an authentication key:

   ```cisco
   ntp authentication-key 10 md5 MySecretKey
   ```

2. Mark the key as trusted:

   ```cisco
   ntp trusted-key 10
   ```

3. Reference the key when configuring the server:

   ```cisco
   ntp server 192.0.2.10 key 10
   ```

- Key number and key string must match on both client and server
- Newer software may support hash types other than MD5

### Peer authentication

- NTP peers can also authenticate each other
- Replace `ntp server` with `ntp peer` and use the same key number and key string on both peers:

  ```cisco
  ntp peer 192.0.2.21 key 10
  ```

- Both sides use matching `ntp authentication-key` and `ntp trusted-key` commands

## Troubleshooting NTP

### Common issues

- Clock never becomes synchronized
  - NTP server unreachable or blocked by ACLs
  - Stratum of server is invalid
- Wrong server chosen
  - Another server has lower stratum
  - `prefer` keyword not used on primary server
- Authentication failures
  - Key number or key string mismatch
  - Missing `ntp trusted-key` for the key in use
- Calendar out of sync
  - `ntp update-calendar` not configured

### Troubleshooting approach

1. Check NTP status:

   ```cisco
   show ntp status
   ```

2. Review associations:

   ```cisco
   show ntp associations
   ```

3. Test reachability:
   - Use `ping` toward NTP servers

4. Check configuration:
   - `show running-config | include ntp`
   - Confirm server addresses, peer settings, and keys

5. Confirm local clock:
   - `show clock detail`
   - Verify time zone and summer time configuration

## Quick review

- Accurate time is required for reliable logging, security protocols, and troubleshooting.  
- Devices have a software clock and, on some platforms, a hardware calendar that can be synchronized with NTP.  
- NTP uses UDP port 123 and a hierarchy of stratum levels, preferring servers with lower stratum values.  
- `ntp server` configures client and server mode; devices can use multiple servers with optional `prefer`.  
- Loopback interfaces and `ntp source` provide stable addresses for devices acting as NTP servers.  
- `ntp master` allows a router or switch to act as an internal time source when external servers are not available.  
- NTP authentication uses keys defined with `ntp authentication-key` and `ntp trusted-key`, and referenced on `ntp server` or `ntp peer` lines.  
- Core verification and troubleshooting use `show ntp status`, `show ntp associations`, `show clock detail`, and reachability tests.
