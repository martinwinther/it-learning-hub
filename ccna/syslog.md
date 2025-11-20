# Syslog

## Overview

Syslog is a standard for message logging in computers and provides mechanisms to collect information about devices and monitor their health. Like SNMP, Syslog helps network administrators monitor network devices, but there are significant differences between the two protocols. SNMP is like a network health report, proactively polling devices at regular intervals to gather mostly quantitative metrics—numerical statistics like traffic rates, CPU utilization, error rates, etc. SNMP is also often used for event-based alerting using Trap and Inform messages. Syslog, on the other hand, is like a journal that the device keeps—a logbook that records significant (and not so significant) events that occur on a device. Syslog generally focuses on qualitative information—descriptive information that provides context or insight into what's happening on the device. This is especially useful when you need to dive deep into troubleshooting or forensic analysis. SNMP might alert you that a router is down, but Syslog can tell you the sequence of events that led to the failure.

## Real-Time Logging

### Console Line Logging

- Cisco IOS displays Syslog messages to users connected to CLI via console line by default
- Controlled with `logging console` command, which is enabled by default
- Can disable logging to console line with `no logging console`
- Device will then stop showing log messages to users connected to console line

### VTY Line Logging

- Logging to VTY lines is enabled by default
- Applies to users connected to CLI via Telnet or SSH
- Result of `logging monitor` command that is configured by default
- Can disable with `no logging monitor`
- Despite `logging monitor` being enabled by default, no log messages displayed by default when connected via VTY lines
- Additional command required: `terminal monitor` issued in privileged EXEC mode
- Must use `terminal monitor` every time you connect to CLI via VTY line
- Command only applies to one session
- If you disconnect and reconnect, must use command again
- If multiple users connected to VTY lines simultaneously, each user must use command

### Disabling Real-Time Messages

- Command to stop displaying messages for particular session: `terminal no monitor`
- Not `no terminal monitor` but `terminal no monitor`
- May choose to use this if device generating significant number of messages
- Makes it difficult to work in CLI when messages constantly interrupting

### Synchronous Logging

- By default, if Syslog message displayed as you are typing command, command is cut off
- Additional characters you type are displayed on same line as Syslog message
- If you hit Enter, command will execute correctly
- Default behavior doesn't lead to very good user experience
- Can be especially distracting and confusing when using long and complex commands
- Solution: use Ctrl-l keyboard shortcut to reprint command on new line
- Better solution: `logging synchronous` command
- With `logging synchronous` configured on console and VTY lines, command you are typing will be automatically reprinted on new line if it gets cut off by Syslog message
- Major quality-of-life improvement when working in CLI
- Highly recommended to configure on console and VTY lines of devices

## Log Storage

### Logging Buffer

- Cisco IOS devices store Syslog messages in RAM by default
- Called logging buffer
- Controlled with `logging buffered [bytes]` command, which is enabled by default
- Optional bytes argument allows you to specify how much memory to allocate to buffer
- Default size depends on device model
- Example: Catalyst 2960 switch's buffer is 4,096 bytes by default (enough for about 35-40 log messages)
- Catalyst 9300 switch uses default size of 102,400 bytes (102.4 kilobytes)
- Default settings are fairly conservative
- In most cases, there will be enough room to expand buffer to store more messages
- Before increasing size of buffer, use `show memory` to view device's current memory usage
- Ensure device has sufficient memory
- After buffer fills up, messages are added to and removed from buffer in first in, first out (FIFO) manner

### Viewing Logs

- Use `show logging` command to view logs stored in buffer
- Command also displays information about device's Syslog settings in general
- Output is quite large, especially with large buffer
- Most recent logs are displayed at bottom of output
- If there are quite a few messages stored in buffer, may have to press spacebar quite a few times to get to most recent messages
- Console, monitor (VTY line), and buffer logging are all enabled by default
- Thanks to `logging console`, `logging monitor`, and `logging buffered` commands that are part of device's default configuration
- If you use `no logging console` to disable console logging, output will state "Console logging: disabled"

### Syslog Server

- In addition to locally saving log messages, can configure device to send them to central Syslog server
- Very useful, especially in large networks with many devices
- Storing logs in central location simplifies process of viewing and correlating those logs
- Eliminates need to log in to each device one by one
- Logging to Syslog server is governed by `logging trap` command
- Not to be confused with SNMP Trap message type
- `logging trap` is enabled by default
- For device to actually send Syslog messages to server, need to tell device which server to send messages to
- Configure with `logging [host] ip-address` command
- Device will then send Syslog messages to UDP port 514 on specified server
- In addition to other destinations (console line, VTY lines, and buffer)
- `host` keyword in command is optional
- `logging ip-address` and `logging host ip-address` both have same effect
- Regardless of which command you configure, it will be saved in running-config as `logging host ip-address`

### Syslog Ports

- Standard Syslog uses UDP port 514
- More secure, encrypted version called Syslog over TLS (Transport Layer Security) uses TCP port 6514
- Details of Syslog over TLS beyond scope of CCNA exam
- Be aware that Syslog can use both UDP 514 and TCP 6514

## Syslog Message Format

### Message Components

Syslog message format: `seq:timestamp: %facility-severity-mnemonic: description`

- **Sequence number**: Optional field indicating order of log messages
- **Timestamp**: Optional field indicating when message was generated
- **Facility**: Mandatory field indicating source of message within device
- **Severity**: Mandatory field indicating how urgent or critical message is
- **Mnemonic**: Mandatory field providing specific descriptor of event
- **Description**: Mandatory field providing detailed explanation of event

### Sequence Numbers

- First two fields are sequence number and timestamp
- These two fields are optional
- Whether they are present or absent by default can vary depending on device
- In many cases, sequence numbers are not included by default, but timestamps are
- Can enable sequence numbers with `service sequence-numbers` command in global config mode
- After issuing command, sequence numbers will be added to any future Syslog messages generated by device
- Past messages are not affected

### Timestamps

- Can control timestamps with `service timestamps log` command in global config mode
- Command includes various keywords that allow you to control how timestamps are displayed
- Two main options:
  - `service timestamps log datetime`: Timestamps log messages with date and time when event occurred
  - `service timestamps log uptime`: Timestamps log messages with device's uptime when event occurred
- `datetime` is generally more useful option of the two
- Enables you to identify exactly when events occurred and correlate logs across different devices

### Timestamp Options

- `datetime` keyword has further options you can configure
- `service timestamps log datetime localtime`: Configure device to timestamp Syslog messages in local time zone
- By default, Syslog messages are timestamped in UTC
- In international network with devices in multiple time zones, default behavior is generally preferred
- Makes correlating logs between devices in different time zones easier
- May prefer to have messages timestamped with local time; `localtime` option allows you to do this
- Can also add milliseconds to timestamps with `service timestamps log datetime msec` command
- Format of timestamps will be hh:mm:ss.msec
- All timestamps shown in examples have included milliseconds, but they are optional
- If you don't include `msec` option in command, they will not be displayed
- Can combine `localtime` and `msec` options if you want
- `service timestamps log datetime localtime msec` will timestamp Syslog messages using local time and will also include milliseconds

### Facility

- First mandatory component is facility
- Value that indicates source of message within device
- Specifies service, application, or other component that generated message
- Example: LINK facility indicates message was generated by one of device's links
- Usually indicates interface's status changing to up or down

### Severity

- Next component is severity
- Numerical value indicating how urgent or critical message is
- Lower value is more severe
- Eight severity levels defined (0-7)

### Mnemonic

- Short text string that provides more specific descriptor of event that triggered Syslog message
- Acts as code that briefly identifies reason or area within facility that generated message
- Example: UPDOWN mnemonic indicates message was generated by interface state changing to up or down

### Description

- Final part is description
- Provides more detailed explanation of event that triggered message
- Example: "Interface FastEthernet0/1, changed state to down" gives details of what really happened

## Syslog Severity Levels

### Eight Severity Levels

Syslog messages are categorized by their severity—how urgent or critical the logged event is. There are eight severity levels, and a lower value indicates a more severe event. In addition to a numerical value, each severity level also has a keyword that you can use when configuring severity levels in Cisco IOS:

- **0 - Emergencies**: System is unusable
- **1 - Alerts**: Action must be taken immediately
- **2 - Critical**: Critical conditions
- **3 - Errors**: Error conditions
- **4 - Warnings**: Warning conditions
- **5 - Notifications**: Normal but significant conditions
- **6 - Informational**: Informational messages
- **7 - Debugging**: Debug-level messages

### Severity Level Details

- First two severity levels (0-1) are reserved for particularly serious events
- System crashes, critical hardware failures, and other events that demand immediate attention
- Next three severity levels (2-4) are used for events that should be addressed but do not necessarily require immediate action
- Described by RFC 5424 as critical, error, and warning conditions, respectively
- Example: Interface unexpectedly going down is categorized at severity level 3 (LINK-3-UPDOWN)
- Next two levels (5-6) are usually used for routine operational status messages or notifications of minor changes
- Don't typically affect performance or security
- Example: User logging into CLI is categorized at severity level 5 (SEC_LOGIN-5-LOGIN_SUCCESS)
- Interface being manually disabled with `shutdown` command is also severity level 5 (LINK-5-CHANGED)
- Final severity level (7) is unique
- Reserved for messages that are generated as result of `debug` command
- Allows you to track events in detail as they occur

### Controlling Severity Levels

- Can control types of events logged to each destination based on their severity levels
- Console, VTY lines, buffer, and Syslog server
- Example: To avoid filling up device's logging buffer, may want to only store logs for more severe events in buffer

### Default Severity Levels

- `logging console`, `logging monitor`, `logging buffered`, and `logging trap` commands on their own enable logging to each destination with default severity levels
- Logging to console, monitor, and buffer is enabled at level 7 (debugging) by default
- Means that events with that severity level or numerically lower (more severe) will be logged
- Because level 7 is numerically highest, all events will be logged to console, monitor, and buffer by default (severity levels 0-7)
- Trap logging (to Syslog server) is enabled at severity level 6 (informational) by default
- Means that events of severity level 6 or lower will be logged to server
- Level 7 events will not be logged to server
- This choice of default settings minimizes unnecessary network traffic to Syslog server

### Modifying Severity Levels

- To modify which severity levels are logged to each destination, can add optional level argument to end of each command
- Can specify either numerical value or keyword
- Example: `logging console 4` and `logging console warnings` both enable console logging for severity levels 4 and lower (0-4)
- Table summarizes commands with optional severity argument:
  - Console line: `logging console [severity]`
  - VTY lines (monitor): `logging monitor [severity]` and `terminal monitor`
  - Logging buffer: `logging buffered [bytes] [severity]`
  - Syslog server (trap): `logging trap [severity]` and `logging [host] ip-address`

## Debug Command

### Debug Overview

- `debug` command allows you to view detailed real-time information about various operations on Cisco IOS device
- Includes data about network activity, internal processes, and other specific events
- Can use this command to troubleshoot difficult problems or learn more about how device is functioning
- Command includes countless keywords that allow you to specify what kind of information you want to see
- Example: `debug spanning-tree events` can be used to display real-time messages about STP-related events
- Such as changes in port roles and states

### Debug Output

- Debug messages are processed by device's CPU
- Debugging can be quite resource intensive
- Recommended that you be very careful about using this command on live network
- Avoid overwhelming device
- Feel free to experiment with `debug` command in lab
- Beyond scope of CCNA exam
- Just need to understand its relationship to Syslog severity levels
- Debugging-level events will not be logged unless severity level 7 (debugging) is enabled

## Real-World Applications

- **Troubleshooting**: Review sequence of events that led to network problems
- **Forensic analysis**: Analyze security incidents and network failures
- **Compliance**: Meet regulatory requirements for log retention
- **Network monitoring**: Monitor device health and performance
- **Event correlation**: Correlate events across multiple devices using timestamps
- **Change tracking**: Track configuration changes and their effects
- **Performance analysis**: Analyze network performance over time

## Troubleshooting

### Common Issues

- **No messages displayed on VTY lines**: Verify `terminal monitor` command has been issued
- **Messages interrupting commands**: Configure `logging synchronous` on console and VTY lines
- **Buffer filling up quickly**: Increase buffer size with `logging buffered bytes`
- **Messages not sent to server**: Verify `logging trap` and `logging host` are configured correctly

### Troubleshooting Steps

1. Verify logging configuration: `show logging`
2. Check severity levels: Verify appropriate severity levels are configured for each destination
3. Test console logging: Connect via console and verify messages are displayed
4. Test VTY logging: Connect via SSH/Telnet, issue `terminal monitor`, and verify messages are displayed
5. Verify Syslog server: Check server is reachable and listening on UDP 514
6. Check buffer: Use `show logging` to view messages in buffer

## Best Practices

- Configure `logging synchronous` on console and VTY lines for better user experience
- Increase logging buffer size if needed to store more messages
- Configure Syslog server for centralized log storage in larger networks
- Use appropriate severity levels for each destination to minimize unnecessary traffic
- Configure timestamps with `datetime` option for accurate event correlation
- Use UTC timestamps in multi-timezone networks for easier correlation
- Add milliseconds to timestamps for more precise timing
- Enable sequence numbers if needed for message ordering
- Regularly review logs to identify patterns and issues
- Archive old logs before buffer fills up
- Monitor Syslog server disk space

## Summary

- Syslog is standard for message logging in computers, providing mechanisms to collect information about devices and monitor their health
- Whereas SNMP provides regular polling of quantitative metrics, Syslog functions like logbook that records events that occur on device
- Syslog messages can be displayed in real time to users connected to CLI and stored locally or on centralized Syslog server
- Real-time logging to console line is controlled with `logging console` command (enabled by default)
- Real-time logging to VTY lines is controlled with `logging monitor` command (enabled by default)
- User connected to VTY line must issue `terminal monitor` command in privileged EXEC mode to view real-time messages for that session
- `logging synchronous` command can be configured in line config mode to automatically reprint command on new line if cut off by Syslog message
- Cisco devices can store Syslog messages in logging buffer in RAM
- Use `show logging` to view messages stored in logging buffer
- Logging to buffer is controlled with `logging buffered [bytes]` command (enabled by default)
- Can configure device to send Syslog messages to central Syslog server
- Logging to Syslog server is controlled with `logging trap` command (enabled by default)
- Must also specify IP address of Syslog server with `logging [host] ip-address`
- Standard Syslog uses UDP port 514; Syslog over TLS uses TCP port 6514
- Syslog message format is seq:timestamp: %facility-severity-mnemonic: description
- Sequence number and timestamp are optional components
- Facility indicates source of message within device
- Severity is numerical value indicating how urgent or critical message is (lower is more severe)
- Mnemonic is short text string providing descriptor of event
- Description provides detailed explanation of event
- Can control sequence numbers with `service sequence-numbers` command
- Can configure timestamps with `service timestamps log [datetime | uptime]`
- `datetime` keyword has further options: `localtime` and `msec`
- Eight Syslog severity levels: 0-emergencies, 1-alerts, 2-critical, 3-errors, 4-warnings, 5-notifications, 6-informational, 7-debugging
- Console, monitor, and buffer logging are enabled at level 7 (debugging) by default
- Trap logging is enabled at severity level 6 (informational) by default
- Can control severity levels logged to each destination by adding optional severity argument to each command
- `debug` command allows you to view detailed real-time information about various operations
- Debugging-level events will not be logged unless severity level 7 is enabled

