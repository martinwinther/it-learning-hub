# Transmission Control Protocol and User Datagram Protocol

## Overview

TCP and UDP are the two main Layer 4 (Transport Layer) protocols in the TCP/IP model. They provide addressing and session multiplexing via port numbers, allowing data to reach the correct application process on destination hosts. TCP provides connection-oriented, reliable communication with flow control, while UDP provides lightweight, connectionless communication. Understanding when to use each protocol is essential for network engineers.

## Layer 4 Role in TCP/IP Model

### Layer Responsibilities

- **Layer 1 (Physical)**: Physical components (cables, signals)
- **Layer 2 (Data Link)**: Hop-to-hop communication using MAC addresses
- **Layer 3 (Network)**: End-to-end addressing using IP addresses
- **Layer 4 (Transport)**: Ensures data reaches correct application process on destination host
- **Application Layer**: Provides services to end users

### Layer 4 Purpose

- Not enough for data to reach correct destination host
- Data must reach correct application process on destination host
- Layer 4 provides addressing (ports) to identify specific applications
- Layer 4 can also provide additional services (reliability, flow control, etc.)

## Port Numbers

### Port Concept

- Port is number ranging from 0 to 65535
- Used to address message to specific application process on destination host
- Not a physical port on device
- Layer 4 addressing system (similar to MAC addresses at Layer 2, IP addresses at Layer 3)

### Port Ranges

Port numbers assigned by IANA and divided into three ranges:

- **Well-known ports (0-1023)**:
  - Reserved for most common protocols
  - Strictly controlled and assigned by IANA
  - Also called system ports
- **Registered ports (1024-49151)**:
  - Protocols may be registered with IANA
  - Registration avoids conflicts between different protocols
  - Also called user ports
- **Ephemeral ports (49152-65535)**:
  - Not controlled or assigned by IANA
  - Dynamically selected by client devices as source ports
  - Also called dynamic or private ports

### Common Port Numbers

**TCP Ports:**
- FTP data: 20
- FTP control: 21
- SSH: 22
- Telnet: 23
- SMTP: 25
- DNS: 53
- HTTP: 80
- POP3: 110
- IMAP: 143
- HTTPS: 443

**UDP Ports:**
- DNS: 53
- DHCP server: 67
- DHCP client: 68
- TFTP: 69
- NTP: 123
- SNMP agent: 161
- SNMP manager: 162
- Syslog: 514

### Session Multiplexing

- Process of keeping track of multiple communication sessions
- Each session identified by unique combination of source IP, source port, destination IP, destination port, and protocol
- Client selects random ephemeral port for each session
- Allows multiple applications on same host to communicate with same server simultaneously
- Example: Multiple web browsers can have separate sessions with same web server

### Sockets and Five-Tuples

- **Socket**: Combination of IP address, port number, and Layer 4 protocol
  - Server socket: 203.0.113.1, TCP port 443
  - Client socket: 192.168.1.1, TCP port 50000
- **Five-tuple**: Pair of sockets consisting of:
  - Client IP address
  - Client port number
  - Server IP address
  - Server port number
  - Layer 4 protocol (TCP or UDP)

## Transmission Control Protocol (TCP)

### TCP Overview

- Connection-oriented protocol providing reliable communication
- Provides addressing, session multiplexing, connection-oriented communication, data sequencing, reliable communication, and flow control
- TCP header is minimum 20 bytes (can be up to 60 bytes with options)

### Connection-Oriented Communication

- Hosts must establish connection before exchanging data
- After data exchange, hosts terminate connection
- Three-step process:
  1. Connection establishment
  2. Data exchange
  3. Connection termination

### TCP Three-Way Handshake

- Connection establishment uses SYN and ACK flags
- Process:
  1. Client sends segment with SYN flag
  2. Server responds with segment with SYN and ACK flags
  3. Client sends segment with ACK flag
- Called three-way handshake because it involves three messages

### TCP Connection Termination

- Uses FIN and ACK flags
- Usually occurs in four separate messages (four-way handshake):
  1. Host sends segment with FIN flag
  2. Other host replies with ACK segment
  3. Other host sends its own FIN segment
  4. First host replies with ACK segment
- Sometimes can occur in three messages (FIN, ACK-FIN, ACK)

### Data Sequencing

- TCP provides means to rearrange segments that arrive out of order
- Uses Sequence Number field in TCP header
- Each host sets random initial sequence number during connection establishment
- Sequence number incremented as host sends data
- Sequence and acknowledgment numbers are measures of bytes, not segment count

### Reliable Communication

- TCP confirms that each segment is received
- Uses Acknowledgment Number field in TCP header
- Receiver acknowledges receipt by setting acknowledgment number to sequence number of next segment it expects to receive
- If sender doesn't receive acknowledgment within retransmission timeout, it retransmits segment
- TCP checksum field provides error detection; segments with errors are discarded and retransmitted

### Flow Control

- Mechanism preventing sender from overwhelming receiver
- Ensures sender only sends as much data as receiver can handle
- Implemented through Window Size field in TCP header
- Receiver tells sender how much data to send before waiting for acknowledgment
- Window size can be adjusted dynamically throughout session
- Each host specifies its own window size in every TCP segment
- Called sliding window because window size adjusts dynamically

### TCP Overhead

TCP features come at cost of additional overhead:

- **Data overhead**: TCP header is 20-60 bytes (vs UDP's 8 bytes)
- **Processing overhead**: Additional CPU and memory for connection management, acknowledgments, flow control
- **Time overhead**: Connection establishment adds latency; waiting for acknowledgments can slow transmission

## User Datagram Protocol (UDP)

### UDP Overview

- Provides Layer 4 addressing and session multiplexing via port numbers
- Defining characteristics stem from what it doesn't provide:
  - Not connection-oriented (no connection establishment)
  - Does not provide reliable communication (no acknowledgments or retransmissions)
  - Does not provide data sequencing (no sequence numbers)
  - Does not provide flow control (no window size mechanism)
- UDP header is only 8 bytes (very lightweight)

### UDP Characteristics

- Hosts do not establish connection before communication
- Sending host simply sends data
- No mechanism for acknowledging received messages
- No mechanism for retransmitting lost messages
- No sequence numbers; if messages arrive out of order, UDP provides no mechanism to reorder
- No flow control; UDP sends data as quickly as it can
- Has checksum field for error detection, but messages with errors are discarded (no retransmission)

### Datagram Model

- Datagram is basic unit of transfer that is self-contained and independent
- UDP uses datagram model: sends data in discrete chunks (datagrams) independent of each other
- Contrast to TCP: treats data as continuous stream, breaks into segments (boundaries have no correlation with data structure)

## TCP vs UDP Comparison

| Characteristic | TCP | UDP |
|----------------|-----|-----|
| Connection-oriented | Yes | No |
| Data sequencing | Yes | No |
| Reliable communication | Yes | No |
| Flow control | Yes | No |
| Overhead | More | Less |
| Preferred for | Data integrity critical, delivery of all segments required | Speed/efficiency priority, some packet loss acceptable |

## When to Use TCP

### Situations Requiring TCP

- **File transfers**: Entire file must arrive intact, with all bytes in correct order
- **Web browsing**: HTTP/HTTPS use TCP to ensure web content reliably delivered in correct order
- **Email**: SMTP, POP3, IMAP use TCP to ensure emails not lost and arrive correctly
- **Situations where**: Data integrity is critical, delivery of all segments is required, minor latency acceptable

## When to Use UDP

### Real-Time Applications

- **Video streaming**: Most recent data most valuable, lost data quickly becomes irrelevant
- **Online gaming**: Fast transmission needed, some packet loss acceptable
- **Voice/video calling**: Better to have minor temporary degradation than delay waiting for retransmissions
- **General principle**: Most recent data is most valuable, lost data quickly becomes irrelevant

### Simple Query-Response Protocols

- **DNS**: Short requests and responses don't require TCP features
- **Overhead of TCP connection setup not worth it for single small exchange**
- Would only delay exchange by introducing latency

### When Reliability Provided by Other Means

- **TFTP (Trivial File Transfer Protocol)**: Has own built-in reliability mechanism
- Receiver must acknowledge each TFTP message
- Does not need to rely on TCP for reliable delivery
- **Application Layer protocols**: May provide their own reliability mechanisms

## Real-World Applications

- **Web services**: HTTPS (TCP port 443) for secure web browsing
- **Email services**: SMTP (TCP port 25), POP3 (TCP port 110), IMAP (TCP port 143)
- **File transfers**: FTP (TCP ports 20/21), TFTP (UDP port 69)
- **Remote access**: SSH (TCP port 22), Telnet (TCP port 23)
- **Name resolution**: DNS (TCP/UDP port 53)
- **Network management**: SNMP (UDP ports 161/162), Syslog (UDP port 514)
- **Time synchronization**: NTP (UDP port 123)
- **Video/voice services**: Real-time applications using UDP

## Troubleshooting TCP and UDP

### Common Issues

- **Connection failures**: Check if TCP three-way handshake completes
- **Port conflicts**: Verify no other service using same port
- **Firewall blocking**: Check firewall rules for TCP/UDP ports
- **Performance issues**: TCP flow control may be limiting throughput
- **Packet loss**: UDP applications may experience degradation

### Verification Commands

- `netstat`: View active TCP/UDP connections and listening ports
- `show tcp brief`: View TCP connections on Cisco devices
- `show ip sockets`: View listening ports on Cisco devices
- Packet captures: Analyze TCP handshakes, UDP datagrams

## Best Practices

- Use TCP when data integrity and complete delivery are critical
- Use UDP for real-time applications where speed is priority
- Understand port number ranges (well-known, registered, ephemeral)
- Know common port numbers for troubleshooting
- Monitor TCP window sizes for performance optimization
- Use appropriate protocol for application requirements
- Consider overhead when choosing between TCP and UDP
- Document port usage in network documentation

## Summary

- TCP and UDP are main Layer 4 protocols providing addressing and session multiplexing
- Ports are numbers 0-65535 used to address messages to specific applications
- Well-known ports (0-1023) reserved for common protocols
- Registered ports (1024-49151) can be registered with IANA
- Ephemeral ports (49152-65535) used by clients as source ports
- Session multiplexing allows multiple sessions between same hosts
- TCP is connection-oriented, provides reliable communication, data sequencing, and flow control
- TCP three-way handshake (SYN, SYN-ACK, ACK) establishes connections
- TCP four-way handshake (FIN, ACK, FIN, ACK) terminates connections
- TCP uses sequence and acknowledgment numbers for reliable delivery
- TCP flow control uses window size to prevent overwhelming receiver
- UDP is connectionless, unreliable, no sequencing, no flow control
- UDP header is 8 bytes (vs TCP's 20-60 bytes)
- TCP preferred for file transfers, web browsing, email (data integrity critical)
- UDP preferred for real-time applications, simple query-response, when reliability provided elsewhere
- TCP has more overhead (data, processing, time) than UDP
- Choose protocol based on application requirements: integrity vs speed

