# Syslog

## Overview

Syslog is a standard for message logging on network devices and servers. It records events such as interface state changes, logins, configuration changes, and system errors. SNMP often provides numeric status and counters, while Syslog records descriptive messages that help with troubleshooting and event analysis.

## Real-time logging

### Console logging

- Syslog messages are displayed on the console line by default.
- Controlled with:

  ```cisco
  logging console
  ```

- Disable console logging:

  ```cisco
  no logging console
  ```

- Console logging applies to users connected via the physical console port.

### VTY logging

- Logging to VTY lines is enabled by default with:

  ```cisco
  logging monitor
  ```

- Messages are not shown until the current session enables monitoring:

  ```cisco
  terminal monitor
  ```

- `terminal monitor` must be entered per session on Telnet or SSH.
- To stop Syslog output in a VTY session:

  ```cisco
  terminal no monitor
  ```

### Synchronous logging

- Without synchronous logging, Syslog messages can interrupt commands being typed.
- `logging synchronous` reprints the interrupted command on a new line:

  ```cisco
  line console 0
   logging synchronous
  line vty 0 4
   logging synchronous
  ```

- Improves usability when many messages are generated.

## Log storage

### Logging buffer

- Devices store Syslog messages in RAM in a logging buffer.
- Enabled by default with:

  ```cisco
  logging buffered [bytes]
  ```

- Optional `bytes` value sets buffer size.
- When the buffer is full, older messages are overwritten (FIFO behavior).

### Viewing logs

- Use `show logging` to view stored messages and logging configuration:

  ```cisco
  show logging
  ```

- Output includes:
  - Buffer contents.
  - Current logging destinations.
  - Severity settings for each destination.

### Remote Syslog server

- Devices can send Syslog messages to a central server.
- Governed by the `logging trap` command:

  ```cisco
  logging trap informational
  logging host 192.0.2.50
  ```

- `logging host` (or `logging ip-address`) defines the server.
- Messages are sent to UDP port 514 on the server.
- Central logging simplifies correlation across many devices.

### Syslog ports

- Standard Syslog uses UDP port 514.
- Syslog over TLS (encrypted) uses TCP port 6514.
- Details of Syslog over TLS are beyond CCNA scope.

## Syslog message format

### Components

Typical Syslog format on Cisco IOS:

```text
seq:timestamp: %facility-severity-mnemonic: description
```

- `seq`  
  Optional sequence number.

- `timestamp`  
  Optional date and time or uptime.

- `facility`  
  Part of the system that generated the message (for example, LINK, SEC_LOGIN).

- `severity`  
  Numeric level 0–7 embedded in the message tag.

- `mnemonic`  
  Short code describing the event, such as UPDOWN or CHANGED.

- `description`  
  Text that explains what happened.

### Sequence numbers

- Sequence numbers are optional.
- Enable with:

  ```cisco
  service sequence-numbers
  ```

- Useful when reviewing large numbers of messages.

### Timestamps

- Timestamps are controlled with:

  ```cisco
  service timestamps log datetime
  ```

- Two main base options:
  - `datetime` – use date and time.
  - `uptime` – use device uptime.

- Useful extensions:

  ```cisco
  service timestamps log datetime localtime
  service timestamps log datetime msec
  service timestamps log datetime localtime msec
  ```

- Local time is useful for single-site environments.
- UTC is often preferred in multi time zone environments.

### Facility

- Indicates the internal source of the message.
- Example: `LINK` for interface up and down events.
- Helps categorize events in monitoring tools.

### Severity

- Numeric severity level from 0 (most severe) to 7 (least severe).
- Also shown as part of the message tag, for example `LINK-3-UPDOWN`.

### Mnemonic and description

- Mnemonic is a short identifier such as `UPDOWN` or `LOGIN_SUCCESS`.
- Description provides the full text of the event and any parameters.

## Syslog severity levels

### Levels 0–7

- 0 Emergencies  
  System is unusable.

- 1 Alerts  
  Action must be taken immediately.

- 2 Critical  
  Critical conditions.

- 3 Errors  
  Error conditions.

- 4 Warnings  
  Warning conditions.

- 5 Notifications  
  Normal but significant conditions.

- 6 Informational  
  Informational messages.

- 7 Debugging  
  Debug level messages.

Lower numeric values indicate more severe events.

### Default severity per destination

- Console logging:

  ```cisco
  logging console
  ```

  Default: level 7 (debugging). Logs levels 0–7.

- Monitor (VTY) logging:

  ```cisco
  logging monitor
  ```

  Default: level 7 (debugging). Logs levels 0–7 when `terminal monitor` is enabled.

- Buffer logging:

  ```cisco
  logging buffered
  ```

  Default: level 7 (debugging). Logs levels 0–7.

- Trap logging (Syslog server):

  ```cisco
  logging trap informational
  ```

  Default: level 6 (informational). Logs levels 0–6.

### Adjusting severity

- Use a numeric level or keyword at the end of each command:

  ```cisco
  logging console warnings
  logging monitor 4
  logging buffered 64000 notifications
  logging trap errors
  ```

- A destination configured at level `X` logs messages with level `X` and all more severe levels (0 to `X`).

## Debug command and Syslog

### Debug overview

- `debug` commands display real-time detailed information.
- Debug messages use Syslog severity level 7 (debugging).
- Debug output is CPU intensive and can affect performance.

### Relationship to Syslog

- Debug messages are:
  - Displayed on the console when console logging includes level 7.
  - Displayed on VTY sessions only if `terminal monitor` is enabled and monitor logging includes level 7.
  - Logged to buffer or Syslog server only when those destinations are configured for level 7.

- Basic pattern:

  ```cisco
  debug spanning-tree events
  no debug all
  ```

- `no debug all` or `undebug all` stops all debugging.

## Quick review

- Syslog records descriptive event messages for routers, switches, and other devices.  
- Real-time logging can appear on the console and VTY lines, controlled by `logging console`, `logging monitor`, `terminal monitor`, and `terminal no monitor`.  
- Logging buffer and `show logging` provide local storage and viewing of recent messages.  
- Devices can send Syslog messages to a central server with `logging host` and `logging trap`.  
- Syslog messages contain facility, severity, mnemonic, and description, with optional sequence numbers and timestamps.  
- Severity levels run from 0 (emergencies) to 7 (debugging), and destinations log events at their configured level and more severe levels.  
- `service timestamps log` and `service sequence-numbers` improve message correlation.  
- Debug messages use severity level 7 and are controlled with `debug` and `no debug all`.  

