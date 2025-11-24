# Simple Network Management Protocol

## Overview

Simple Network Management Protocol (SNMP) provides a standard way to monitor and manage network devices. SNMP allows centralized collection of status and performance data and, when permitted, remote configuration changes. Routers, switches, servers, printers, and many other devices support SNMP.

## SNMP components

### Network Management Station (NMS)

- Runs SNMP management software
- Sends queries and configuration changes to devices
- Receives responses and alerts
- Often a dedicated server, sometimes a workstation

### Managed devices

- Devices that run an SNMP agent
- For CCNA, focus on Cisco routers and switches
- Maintain local data in a Management Information Base (MIB)
- Can send notifications for important events

### Management Information Base (MIB)

- Logical database of management information on each device
- Organized as variables representing device state
- Examples:
  - Interface status
  - CPU and memory utilization
  - Temperature and environmental data
  - Routing protocol status
- Each variable is identified by an Object Identifier (OID)

### Object Identifiers (OIDs)

- Numeric identifiers that uniquely name MIB variables
- Organized in a tree structure
- Example: `1.3.6.1.2.1.2.2.1.8` (interface operational status)
- NMS software usually maps OIDs to human readable names

### Vendor specific OIDs

- Vendors extend the standard MIB tree with their own branches
- Cisco and others provide MIB files that describe these OIDs
- NMS can import MIB files to interpret vendor specific data

## SNMP operations

SNMP defines operations that work with MIB variables.

### Read operations (Get)

- Network Management Station sends Get requests to read variables
- Device responds with values in a Response message
- Periodic Get operations provide monitoring data over time

### Write operations (Set)

- Network Management Station sends Set requests to change variables
- Device updates configuration or state when allowed
- Examples:
  - Changing a DNS server address
  - Triggering a configuration backup
- Many variables are read only and reject Set requests

### Notification operations (Trap and Inform)

- Managed devices send messages when specific events occur
- Trap:
  - Unacknowledged notification
  - Sent once and not retransmitted
- Inform:
  - Similar to Trap but requires acknowledgment
  - Device retransmits until a Response is received
  - More reliable when using SNMPv2 or SNMPv3

## SNMP entities

### SNMP manager

- Runs on the NMS
- Sends Get and Set requests to agents
- Listens on UDP port 162
- Receives Responses, Traps, and Informs

### SNMP agent

- Runs on each managed device
- Listens on UDP port 161
- Accesses the local MIB
- Sends Responses and notifications to the manager

### SNMP application

- Software interface used by operators
- Often provides dashboards, graphs, and alerting rules
- Examples include commercial and open source monitoring systems

## SNMP message types

### Message classes

SNMP messages can be grouped into four classes:

- Read
- Write
- Notification
- Response

### Read class

- Get
  - Requests specific OIDs and their values
- GetNext
  - Returns the next OID in the tree after a given one
  - Supports walking the MIB tree
- GetBulk (SNMPv2 and later)
  - Retrieves multiple OIDs in one request
  - More efficient than many GetNext calls

### Write class

- Set
  - Writes new values for writable OIDs
  - Read only OIDs reject Set requests

### Notification class

- Trap
  - One way notification from agent to manager
  - No acknowledgment or retransmission

- Inform (SNMPv2 and later)
  - Notification that requires acknowledgment
  - Manager replies with a Response
  - Agent retransmits Inform until a Response is received

### Response messages

- Response
  - Used by agents to answer Get, GetNext, GetBulk, and Set
  - Used by managers to acknowledge Inform
  - Carries requested data or status information

## SNMP versions

### SNMPv1

- Original version
- Supports Get, GetNext, Set, Trap, and Response
- Uses community strings for basic authentication
- No encryption

### SNMPv2c

- Adds GetBulk and Inform
- Keeps community string model from v1
- Widely deployed but still sends data in clear text

### SNMPv3

- Focuses on security improvements
- Adds user based access, integrity checks, and optional encryption
- No new data operations compared to v2c

## SNMP security

### Community strings (v1 and v2c)

- Shared passwords used between managers and agents
- Two main types:
  - Read only (RO)
  - Read write (RW)
- Typical configuration:

  ```cisco
  snmp-server community PUBLIC RO
  snmp-server community PRIVATE RW
  ```

- Optionally tied to an ACL to restrict source addresses
- Community strings are sent in clear text and should be avoided in production networks

### SNMPv3 security model

SNMPv3 replaces community strings with users and security levels.

Improvements:

- User based access instead of shared community strings
- Message integrity to detect tampering
- Authentication using hashed credentials
- Encryption of message contents when configured

Security levels:

- NoAuthNoPriv  
  No authentication and no encryption.

- AuthNoPriv  
  Authentication, but no encryption.

- AuthPriv  
  Authentication and encryption.

Typical configuration pattern on Cisco IOS:

```cisco
snmp-server group NMS-GRP v3 priv
snmp-server user nms-user NMS-GRP v3 auth sha AuthPW priv aes 256 PrivPW
snmp-server host 192.0.2.50 version 3 priv nms-user
snmp-server enable traps
```

- Group defines security level and access policy
- User binds credentials to the group
- Host statement defines the NMS that receives notifications
- `snmp-server enable traps` enables trap generation

## Quick review

- SNMP uses an NMS with a manager process to monitor SNMP agents on managed devices.  
- Devices store management data in a MIB and identify each variable with an OID.  
- Get and Set operations read and write MIB variables, while Trap and Inform deliver asynchronous notifications.  
- SNMP managers listen on UDP port 162, and agents listen on UDP port 161.  
- SNMPv1 and SNMPv2c use community strings and do not provide encryption.  
- SNMPv3 introduces user based access, integrity checks, authentication, and optional encryption, with security levels NoAuthNoPriv, AuthNoPriv, and AuthPriv.  
- In secure networks, SNMPv3 with AuthPriv and ACL restricted access is preferred over community based versions.  
