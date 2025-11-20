# Simple Network Management Protocol

## Overview

Simple Network Management Protocol (SNMP) is a protocol that facilitates the management of networks—specifically, the management of the devices that make up the network. SNMP allows an admin to centrally monitor the status of devices, trigger alerts for specific events, and even modify device configurations without having to log into a device's CLI. Various types of devices can be managed using SNMP: network devices like routers and switches, servers, user devices like PCs and laptops, printers, and many more. SNMP is widely used in networks of all sizes to provide real-time monitoring and management capabilities that are essential to modern network operations.

## SNMP Components

### Network Management Station (NMS)

- Software platform designed for monitoring and managing devices using SNMP
- Usually run on admin's PC (in smaller networks) or central server (in larger networks)
- Can have multiple NMSs for redundancy
- Interacts with managed devices to gather information and send configuration changes

### Managed Devices

- Devices that are managed using SNMP
- For our purposes, focus on Cisco routers and switches
- Each managed device organizes information about itself into Management Information Database (MIB)
- Information stored as variables in MIB
- Devices can send notifications to NMS when specific events occur

### Management Information Base (MIB)

- Database in which each managed device organizes information about itself
- Information stored as series of variables
- Examples of variables:
  - GigabitEthernet0/1 status (up or down)
  - Internal temperature of device
  - Current CPU utilization
  - State of OSPF neighbors
- Cisco routers and switches store thousands of these variables

### Object Identifiers (OIDs)

- Each variable given object identifier (OID) that uniquely identifies it
- Example: 1.3.6.1.2.1.2.2.1.8 is OID for interface operational status
- OIDs hierarchically organized into tree-like structure similar to DNS hierarchy
- Each number in OID represents different level or branch in tree
- OIDs can be complex and lengthy, making them difficult to remember
- SNMP applications translate OIDs into user-friendly, descriptive names
- Example: OID 1.3.6.1.4.1.9.9.109.1.1.1.1.4 displayed as "CPU Utilization"

### Vendor-Specific OIDs

- Vendors can define their own OIDs
- NMS might not be aware of vendor-specific OIDs by default
- Vendors (like Cisco) often provide MIB files for download
- MIB files define specific OIDs used by vendor's devices
- Can import MIB files into NMS to allow proper interpretation of OIDs

## SNMP Operations

### Reading the MIB (Get Operations)

- NMS can query managed devices to get value of one or more variables
- Uses Get message type to do so
- NMS sends Get message to managed device
- Managed device replies with Response message including requested information
- Get messages can be manually sent by administrator as needed
- Automation makes them even more powerful
- Get messages can be automated from NMS to periodically check status of various devices
- Allows NMS to actively monitor state of network, gather performance metrics, and collect information

### Modifying the MIB (Set Operations)

- NMS can modify values of MIB's variables with Set messages
- Set messages allow configuration of devices centrally from NMS
- No need to log in to CLI of each device
- Example: if new DNS server added, NMS can use Set messages to add it to each router's configuration
- Set messages can be used for more than configuration changes:
  - Initiate system reboot or shutdown
  - Make devices back up their configuration files to central file server
  - More efficient than doing so manually via each device's CLI

### Notifying the NMS (Trap Operations)

- Managed devices can be configured to send notifications to NMS when specific events occur
- Uses Trap message type
- Example: R1's G0/1 interface goes down, R1 sends Trap message to NMS
- Trap messages allow managed devices to immediately notify NMS when event occurs
- Unsolicited by NMS (unlike Get messages which are requested)
- NMS can alert admin of event with email or SMS text message
- Alerts help admin respond quickly to serious events on network

## SNMP Entity Components

### SNMP Manager

- Runs on NMS
- Interacts with SNMP agent that runs on each managed device
- Sends messages (Get, Set) to agent
- Listens on UDP port 162 for messages from agents
- Receives Response and Trap messages from agents

### SNMP Agent

- Runs on each managed device
- Interacts with SNMP manager running on NMS
- Listens for messages from manager on UDP port 161
- Responds accordingly (with requested information about device)
- Sends messages (Response, Trap) to manager
- Directly interacts with MIB to retrieve and modify variable values

### SNMP Application

- Piece of software that allows human to interact with SNMP
- Usually through graphical user interface (GUI)
- Through application, admin can control how to use SNMP to monitor and manage network devices
- Example: PRTG Network Monitor
- Can send SNMP Get messages periodically to monitor devices
- Can view current value of each monitored variable
- Can view graphs displaying historical data

## SNMP Message Types

### Message Classes

SNMP messages can be divided into four classes:

1. **Read**: Sent by NMS to retrieve information from managed devices
2. **Write**: Sent by NMS to modify values of one or more OIDs
3. **Notification**: Sent by managed devices to alert NMS of particular event
4. **Response**: Sent in response to previous message

### Read Class Messages

- **Get**: Simplest message type; NMS specifies one or more OIDs, managed device responds with values
- **GetNext**: Used to discover unknown OIDs; returns next OID in tree and its value
  - Allows NMS to discover available information without knowing each specific OID in advance
  - Called "walking the tree"
- **GetBulk**: Introduced in SNMPv2; efficient way to retrieve lots of information
  - Allows NMS to specify entire range of OIDs
  - More efficient than GetNext (requests many OIDs at once instead of one at a time)

### Write Class Messages

- **Set**: Allows NMS to modify value associated with specified OID
- Some OIDs are read-only—their values can't be modified with Set messages
- Read-only OIDs typically related to:
  - System information (temperature, system health)
  - Resource utilization (CPU, memory)
  - Interface statistics (current traffic rate)
- NMS can send Get messages to retrieve values but can't modify them with Set

### Notification Class Messages

- **Trap**: Simple notification message
  - When event occurs, managed device sends Trap to NMS
  - NMS is considered notified regardless of whether it actually received Trap
  - NMS does not respond to managed device that sent Trap
  - If Trap is lost, it is not retransmitted
- **Inform**: Introduced in SNMPv2; serves same purpose as Trap
  - NMS acknowledges receipt of each Inform by sending Response message
  - If managed device doesn't receive Response, it will retransmit Inform
  - More reliable than Traps
  - Should be preferred over Traps when using SNMPv2 or SNMPv3

### Response Messages

- **Response**: Single message type used by both NMS and managed devices
- Managed devices send Responses to reply to Get, GetNext, GetBulk, and Set
- NMS sends Responses to reply to Informs
- Exact contents depend on type of message it is in response to
- Response to Get includes requested OIDs and their values
- Response to Inform confirms NMS received managed device's Inform message

## SNMP Versions

### SNMPv1

- Originally defined in three RFCs in 1990: RFCs 1155, 1156, and 1157
- Included five message types: Get, GetNext, Set, Trap, and Response
- No GetBulk or Inform messages
- Included very basic security in form of community strings
- Community strings are essentially passwords used to authenticate SNMP operations

### SNMPv2c

- SNMPv2 later introduced, adding two new message types: GetBulk and Inform
- Standard did not include community string feature
- Industry demand for backward compatibility led to SNMPv2c (community-based SNMPv2)
- Uses same community string system as SNMPv1
- "c" in SNMPv2c stands for community-based

### SNMPv3

- Did not add new message types but greatly improved SNMP's security
- Added improved authentication and encryption
- Security is major concern when using SNMP
- Attacker can use SNMP both to gather information and to make changes with Set messages

## SNMP Security

### Community Strings (SNMPv1 and v2c)

- SNMPv1 and SNMPv2c use community-based security model
- SNMP community is group of SNMP managers and agents that share common authentication parameters
- Password called community string
- Two different community types: read-only (RO) and read-write (RW)

### Read-Only Community

- NMS that provides RO community string can only read information from managed device
- Can send Get, GetNext, and GetBulk requests
- Cannot modify managed device with Set messages

### Read-Write Community

- NMS that provides RW community string can both read and write
- Can send Get, GetNext, and GetBulk requests
- Can modify managed device with Set messages

### Community String Configuration

- Use `snmp-server community community-string {RO | RW} [acl]` to configure community strings
- Device will only respond to messages specifying that community string
- Can specify ACL for each community string to limit which NMSs can use it
- Device will only respond if NMS is permitted by ACL

### Trap Configuration

- Use `snmp-server enable traps` to enable all Trap messages
- Can limit traps to specific events: `snmp-server enable traps cpu` (only CPU-related traps)
- Use `snmp-server host ip-address [version 2c] community-string` to specify NMS to send Traps to
- Community string in this command determines string device will send in Trap messages
- Doesn't have to match community string specified in `snmp-server community` command
- NMS can be configured to only accept Traps/Informs that include correct community string

### Security Limitations of v1 and v2c

- Community strings sent in plaintext; not encrypted
- Not acceptable in modern networks
- Any attacker who gets copy of SNMP communications will know community strings

### SNMPv3 Security Improvements

SNMPv3 improves SNMP's security in four main ways:

1. **User-based**: Instead of community strings tied to each device, SNMPv3 grants access based on users
2. **Message integrity**: Performs checks to ensure messages weren't altered by attacker
3. **Authentication**: Username/password authentication secured with hashing algorithms
4. **Encryption**: Message contents can be encrypted so only intended recipient can read them

### SNMPv3 Security Levels

- Authentication and encryption are optional (but highly recommended)
- Three security levels:
  - **NoAuthNoPriv**: No authentication and no encryption
  - **AuthNoPriv**: Authentication, but no encryption
  - **AuthPriv**: Both authentication and encryption

### SNMPv3 Configuration

- Must specify group that specifies security level to be used
- Use `snmp-server group group-name v3 {auth | noauth | priv}` to create group
- `priv` configures AuthPriv security level
- Then assign one or more users to that group
- Use `snmp-server user username group-name v3 auth sha AuthPW priv aes 256 PrivPW`
- Can then enable Traps and specify NMS similar to SNMPv1/v2c

## Real-World Applications

- **Network monitoring**: Real-time monitoring of device status and performance
- **Performance metrics**: Collect CPU, memory, and interface utilization data
- **Event alerts**: Receive immediate notifications when problems occur
- **Configuration management**: Centrally configure devices without CLI access
- **Inventory management**: Discover and track devices in network
- **Capacity planning**: Analyze historical data to plan for future growth
- **Troubleshooting**: Quickly identify problems and their causes

## Troubleshooting

### Common Issues

- **NMS cannot communicate with device**: Verify SNMP is enabled and community strings match
- **Traps not received**: Check `snmp-server enable traps` and `snmp-server host` configuration
- **Set messages fail**: Verify RW community string is configured and used
- **Authentication fails**: Check SNMPv3 user configuration and passwords

### Troubleshooting Steps

1. Verify SNMP configuration: `show running-config | include snmp`
2. Check community strings: Verify RO and RW strings are configured correctly
3. Test connectivity: Ping NMS from managed device
4. Verify ports: Ensure UDP 161 and 162 are not blocked
5. Check ACLs: Verify ACLs on community strings allow NMS
6. Review logs: Check for SNMP-related error messages

## Best Practices

- Use SNMPv3 with AuthPriv security level in production networks
- Avoid using SNMPv1 and v2c in production (community strings sent in plaintext)
- Use ACLs to limit which NMSs can access devices
- Use Inform messages instead of Traps for reliability
- Configure appropriate trap types (don't enable all traps if not needed)
- Document SNMP community strings and user credentials securely
- Regularly review SNMP access logs
- Use dedicated management VLAN for SNMP traffic
- Monitor SNMP traffic for security threats
- Keep MIB files updated for vendor-specific OIDs

## Summary

- SNMP facilitates management of devices like routers and switches over network
- Two main components: Network Management Station (NMS) and managed devices
- Managed devices organize information into Management Information Base (MIB)
- Information stored as variables, each with unique Object Identifier (OID)
- SNMP operations: Read (Get), Write (Set), and Notify (Trap/Inform)
- SNMP entity consists of SNMP manager (on NMS) and SNMP agent (on managed device)
- Manager listens on UDP 162; agent listens on UDP 161
- SNMP message types: Get, GetNext, GetBulk, Set, Trap, Inform, Response
- Three main SNMP versions: SNMPv1, SNMPv2c, SNMPv3
- SNMPv1 and v2c use community-based security (read-only and read-write community strings)
- SNMPv3 improves security with user-based access, message integrity, authentication, and encryption
- SNMPv3 security levels: NoAuthNoPriv, AuthNoPriv, AuthPriv
- Use `snmp-server community` to configure community strings
- Use `snmp-server enable traps` to enable Trap messages
- Use `snmp-server host` to specify NMS to send Traps to
- Always use SNMPv3 with encryption in production networks
- Use Inform messages instead of Traps for reliability

