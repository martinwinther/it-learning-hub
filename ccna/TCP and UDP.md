
# Transmission Control Protocol and User Datagram Protocol

## Overview

Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) are the main Layer 4 transport protocols in the TCP/IP model. Both use port numbers to identify application processes on destination hosts. TCP provides connection-oriented, reliable transport with sequencing and flow control. UDP provides lightweight, connectionless transport with minimal overhead.

## Layer 4 role in the TCP/IP model

### Layer responsibilities

- Layer 1 – Physical: signals and cabling  
- Layer 2 – Data Link: hop to hop delivery using MAC addresses  
- Layer 3 – Network: end to end delivery using IP addresses  
- Layer 4 – Transport: delivers data to the correct application process  
- Application layer: implements application protocols and user facing services  

### Layer 4 purpose

- IP ensures delivery to the correct destination host  
- Transport layer ensures delivery to the correct application process on that host  
- Uses port numbers as a form of Layer 4 addressing  
- Can provide extra services such as reliability and flow control  

## Port numbers

### Port concept

- Port is a 16 bit number in the range 0–65535  
- Identifies an application process on a host  
- Not a physical interface port  
- Works with IP addresses and transport protocol to form a socket  

### Port ranges

Port numbers are divided into three ranges:

- Well known ports: 0–1023  
  - Reserved for common protocols  
  - Assigned and controlled by IANA  

- Registered ports: 1024–49151  
  - Used by many server applications  
  - Can be registered with IANA to avoid conflicts  

- Ephemeral ports: 49152–65535  
  - Chosen dynamically by clients as source ports  
  - Also called dynamic or private ports  

### Common TCP and UDP ports

Selected TCP ports:

- 20 – FTP data  
- 21 – FTP control  
- 22 – SSH  
- 23 – Telnet  
- 25 – SMTP  
- 53 – DNS  
- 80 – HTTP  
- 110 – POP3  
- 143 – IMAP  
- 443 – HTTPS  

Selected UDP ports:

- 53 – DNS  
- 67 – DHCP server  
- 68 – DHCP client  
- 69 – TFTP  
- 123 – NTP  
- 161 – SNMP agent  
- 162 – SNMP manager  
- 514 – Syslog  

### Session multiplexing

- Multiple transport sessions can exist between the same two hosts  
- Each session is identified by a combination of:
  - Source IP address  
  - Source port number  
  - Destination IP address  
  - Destination port number  
  - Transport protocol (TCP or UDP)  
- This five tuple uniquely identifies a session  
- Client applications typically use different ephemeral source ports for each connection  

### Sockets

- A socket is the combination of IP address, port number, and transport protocol  
- Example server socket: 203.0.113.10, TCP port 443  
- Example client socket: 192.0.2.20, TCP port 50000  
- One TCP session is a pair of sockets plus the protocol  

## Transmission Control Protocol (TCP)

### Key characteristics

- Connection oriented  
- Reliable delivery  
- Sequencing and reordering  
- Flow control  
- Full duplex communication  
- Uses a minimum 20 byte header, up to 60 bytes with options  

### Connection oriented communication

Three phases:

1. Connection establishment  
2. Data transfer  
3. Connection termination  

### TCP three way handshake

Connection establishment uses SYN and ACK flags:

1. Client sends SYN segment with an initial sequence number  
2. Server replies with SYN and ACK segment  
3. Client sends final ACK segment  

After this handshake, both sides have synchronized sequence numbers and can start data transfer.

### Connection termination

Connection termination uses FIN and ACK flags:

1. One side sends segment with FIN flag  
2. Other side replies with ACK  
3. Other side sends its own FIN segment  
4. First side replies with ACK  

This is often referred to as a four way handshake. In some cases the exchange can complete with three messages when flags are combined.

### Sequencing and reliability

- TCP treats application data as a byte stream  
- Each byte in the stream is numbered  
- Sequence number field marks the first byte in a segment  
- Acknowledgment number field indicates the next expected byte  

Reliable delivery:

- Receiver acknowledges successfully received data  
- Sender retransmits segments when acknowledgments are not received within a timeout  
- TCP checksum detects errors; corrupted segments are discarded and later retransmitted  

### Flow control and sliding window

- Flow control prevents a fast sender from overwhelming a slower receiver  
- Window size field in the header advertises how many bytes can be sent before an acknowledgment is required  
- Window size can change during a session  
- Sliding window describes this dynamic window behavior  

### TCP overhead

TCP features introduce overhead:

- Larger header compared to UDP  
- Connection setup and teardown delay first data transfer  
- Retransmissions and acknowledgments require CPU and memory resources  

## User Datagram Protocol (UDP)

### UDP key characteristics

- Connectionless  
- No sequencing  
- No built in reliability  
- No flow control  
- Uses an 8 byte header  
- Provides only basic transport and port addressing  

### Datagram model

- UDP sends independent datagrams  
- Each datagram contains all information needed for delivery  
- No relationship between successive datagrams at the protocol level  
- Lost or out of order datagrams are not corrected by UDP  

### Error detection

- UDP header includes a checksum field  
- Datagrams with checksum errors are discarded  
- No automatic retransmission at the transport layer  

## TCP and UDP comparison

| Characteristic        | TCP                         | UDP                         |
|-----------------------|-----------------------------|-----------------------------|
| Connection oriented   | Yes                         | No                          |
| Sequencing            | Yes                         | No                          |
| Reliability           | Yes                         | No                          |
| Flow control          | Yes                         | No                          |
| Header size           | 20–60 bytes                 | 8 bytes                     |
| Overhead              | Higher                      | Lower                       |
| Typical use cases     | File, web, email, control   | Voice, video, DNS, streaming |

## Application use of TCP

TCP is preferred when:

- All data must arrive and be correct  
- Order of data matters  
- Small delays from retransmission are acceptable  

Typical examples:

- Web browsing – HTTP and HTTPS  
- File transfers – FTP, SFTP, many backup tools  
- Email – SMTP, POP3, IMAP  
- Remote administration – SSH, Telnet  

## Application use of UDP

UDP is preferred when:

- Low latency is more important than perfect reliability  
- Occasional loss of individual packets is acceptable  
- Application layer can handle or ignore losses  

Typical examples:

- Real time voice and video – VoIP and many streaming protocols  
- Online gaming and sensor data streams  
- Simple request response exchanges – DNS, NTP  
- Protocols that include their own reliability – TFTP  

## Troubleshooting pointers

- Connection problems with TCP:
  - Check three way handshake with packet capture  
  - Verify correct ports are open on firewalls  
  - Confirm no port conflicts on the server  

- Performance problems with TCP:
  - Look for high loss leading to frequent retransmissions  
  - Consider window sizes and round trip time  

- UDP issues:
  - Check for packet loss or reordering in captures  
  - Verify that ACLs and firewalls permit the UDP ports in use  
  - Confirm that the application expects UDP and can tolerate loss  

Useful commands include:

- `netstat` or equivalent to view local ports and sessions  
- `show tcp brief` on Cisco devices  
- Packet capture tools to examine segments and datagrams  

## Quick review

- TCP and UDP operate at Layer 4 and use port numbers to identify application processes.  
- Port numbers range from 0 to 65535 and are divided into well known, registered, and ephemeral ranges.  
- TCP is connection oriented, reliable, and uses sequencing and flow control at the cost of additional overhead.  
- UDP is connectionless, has minimal overhead, and relies on applications to handle any required reliability.  
- TCP is used for applications that need accurate, complete delivery, while UDP is used where delay must stay low and some loss is acceptable.  
- Session multiplexing relies on the five tuple: source and destination addresses, ports, and transport protocol.
