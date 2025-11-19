# Extended Access Control Lists

## Overview

Extended Access Control Lists provide more granular packet filtering than standard ACLs. While standard ACLs only match packets based on source IP address, extended ACLs can match packets based on protocol, source and destination IP addresses, and source and destination port numbers. This allows for precise control over which types of traffic are permitted and denied, making extended ACLs essential for implementing detailed security policies.

## Extended ACL Fundamentals

### Similarities to Standard ACLs

- ACEs processed in order from top to bottom
- Implicit deny discards all traffic not matched by explicitly configured ACEs
- Must be applied to interface in inbound and/or outbound direction to take effect
- Same basic evaluation process: first match determines action

### Extended ACL Matching Parameters

Extended ACLs can match packets based on:

- **Protocol**: TCP, UDP, ICMP, OSPF, IP (all IPv4), etc.
- **Source IP address**: Specific host, subnet, or any
- **Destination IP address**: Specific host, subnet, or any
- **Source port**: TCP/UDP port numbers (when protocol is TCP or UDP)
- **Destination port**: TCP/UDP port numbers (when protocol is TCP or UDP)

### Packet Matching Requirements

- Packet must match **all** specified parameters in ACE to be considered a match
- Partial matches don't count
- If ACE specifies protocol, source IP, source port, destination IP, and destination port, all five must match

## Extended ACL Configuration

### Numbered ACL Configuration

- Configure in global config mode
- Command syntax: `access-list number {permit | deny} protocol source destination`
- Extended numbered ACLs use ranges 100-199 or 2000-2699
- Configure each ACE sequentially from top to bottom

### Named ACL Configuration

- Create in global config mode: `ip access-list extended {name | number}`
- Configure ACEs in extended named ACL config mode
- Command syntax: `[seq-num] {permit | deny} protocol source destination`
- Modern IOS allows configuring numbered ACLs in named ACL config mode

### Protocol Argument

- Specify keyword to match packets carrying specific protocol:
  - `icmp`: ICMP packets
  - `tcp`: TCP packets
  - `udp`: UDP packets
  - `ospf`: OSPF packets
  - `ip`: All IPv4 packets (use when protocol doesn't matter)

### Source and Destination Arguments

Options for source and destination IP addresses:

- `any`: Matches all possible IP addresses (equivalent to 0.0.0.0 255.255.255.255)
- `host ip-addr`: Matches only specified IP address (equivalent to ip-addr 0.0.0.0)
- `ip-addr wildcard-mask`: Matches specified range of IP addresses

### Matching Single IP Address in Extended ACLs

- Cannot simply specify IP address without keyword or wildcard mask (unlike standard ACLs)
- Must use: `host 8.8.8.8` or `8.8.8.8 0.0.0.0`
- Both methods are equivalent

## Port Number Matching

### When Port Numbers Apply

- Port numbers can only be specified when protocol is TCP or UDP
- Cannot specify ports for ICMP, OSPF, or IP protocols

### Port Number Syntax

- Command syntax: `{permit | deny} {tcp | udp} src-ip [operator src-port] dst-ip [operator dst-port]`
- Can specify source port, destination port, both, or neither
- If port not specified, all ports will match

### Port Operators

- `eq port`: Equal to port number
- `gt port`: Greater than port number (not including port)
- `lt port`: Less than port number (not including port)
- `neq port`: Not equal to port number (anything other than port)
- `range port1 port2`: From port1 to port2 (including both)

### Port Number Keywords

Some common protocols have keywords that can be used instead of port numbers:

- TCP 20 (FTP data) = `ftp-data`
- TCP 21 (FTP control) = `ftp`
- TCP 23 (Telnet) = `telnet`
- TCP/UDP 53 (DNS) = `domain`
- UDP 67 (DHCP server) = `bootps`
- UDP 68 (DHCP client) = `bootpc`
- UDP 69 (TFTP) = `tftp`
- TCP 80 (HTTP) = `www`
- TCP 443 (HTTPS) = no keyword (must use `eq 443`)

### Client-Server Port Usage

- When host uses protocol to access resources on server, it uses protocol's port number as **destination port**
- Source port is typically ephemeral port (49152-65535)
- To filter client-to-server traffic, match based on **destination port**, not source port
- Example: HTTP traffic from client to server uses destination port 80

## Extended ACL Placement

### Placement Guidelines

- **Standard ACLs**: Apply as close to destination as possible
- **Extended ACLs**: Apply as close to source as possible
- Extended ACLs provide more control over which packets are filtered
- Applying close to source prevents packets from traveling across network just to be discarded
- More efficient use of network resources

### Why Close to Source

- Extended ACLs can precisely identify which traffic to block
- Won't inadvertently block legitimate traffic from source
- Prevents unnecessary network traffic
- Reduces processing load on network devices

## Editing ACLs

### Deleting ACEs from Numbered ACLs

- **From global config mode**: Cannot delete individual ACEs
- Using `no access-list number ...` deletes entire ACL
- **From named ACL config mode**: Can delete individual ACEs
- Use `no sequence-number` to delete specific ACE
- Example: `no 30` deletes ACE with sequence number 30

### Inserting New ACEs

- Named ACL config mode allows inserting ACEs between existing ones
- Specify sequence number at beginning of command
- Example: `30 deny 192.168.4.0 0.0.0.255` inserts ACE at sequence 30
- Default sequence numbers (10, 20, 30, etc.) leave room for insertion

### Resequencing ACLs

- Command: `ip access-list resequence {name | number} starting-seq-num increment`
- Automatically adjusts sequence numbers of all ACEs
- `starting-seq-num`: New sequence number for first ACE
- `increment`: Increment for each subsequent ACE
- Example: `ip access-list resequence 2 10 10` sets first ACE to 10, second to 20, etc.
- Useful when sequence numbers become too close together

## Real-World Applications

- **Protocol-specific filtering**: Allow only specific protocols (e.g., HTTPS only)
- **Port-based access control**: Restrict access to specific services (e.g., block HTTP but allow HTTPS)
- **Granular security policies**: Implement detailed security requirements
- **Service filtering**: Control which services can be accessed from specific networks
- **ICMP control**: Allow ping from specific sources while blocking others
- **Application-layer filtering**: Control access to specific applications based on port numbers

## Troubleshooting Extended ACLs

### Common Issues

- **ACL too restrictive**: Check if all required traffic is explicitly permitted
- **Wrong ports matched**: Verify client uses destination port, not source port
- **Protocol mismatch**: Ensure protocol keyword matches actual traffic
- **ACE order**: More specific rules should come before less specific ones
- **Implicit deny**: Remember implicit deny blocks all unmatched traffic

### Troubleshooting Steps

1. Verify ACL configuration: `show access-lists [name | number]`
2. Check interface application: `show ip interface [interface]`
3. Verify protocol and port specifications are correct
4. Test connectivity with specific protocols and ports
5. Review ACE order for proper specificity
6. Check for shadowed rules

### Verification Commands

- `show access-lists`: View all ACLs with sequence numbers
- `show ip access-lists`: View only IP ACLs
- `show ip interface [interface]`: View applied ACLs on interface
- `show running-config | include access-list`: View ACL configuration

## Best Practices

- Apply extended ACLs as close to source as possible
- Configure more specific ACEs before less specific ones
- Use named ACLs when editing is likely needed
- Specify both source and destination when possible for precision
- Use port numbers to filter specific services
- Document ACL purpose and requirements
- Test ACLs in lab before production deployment
- Review ACLs regularly for effectiveness
- Use protocol keywords when available for readability
- Remember client-to-server traffic uses destination port
- Consider implicit deny when designing ACLs
- Use resequence command to maintain proper spacing between ACEs

## Summary

- Extended ACLs provide more granular filtering than standard ACLs
- Can match packets based on protocol, source/destination IP addresses, and source/destination ports
- Packet must match all specified parameters in ACE to be considered a match
- Extended numbered ACLs use ranges 100-199 or 2000-2699
- Configure with `access-list number {permit | deny} protocol source destination`
- Named ACLs created with `ip access-list extended {name | number}`
- Protocol argument can be icmp, tcp, udp, ospf, ip (all IPv4), etc.
- Source/destination can be any, host ip-addr, or ip-addr wildcard-mask
- Port numbers can only be specified for TCP and UDP protocols
- Port operators: eq, gt, lt, neq, range
- Some protocols have keywords (ftp, telnet, domain, tftp, www, etc.)
- Client-to-server traffic uses destination port (not source port)
- Extended ACLs should be applied as close to source as possible
- Can delete individual ACEs in named ACL config mode with `no sequence-number`
- Can insert new ACEs between existing ones by specifying sequence number
- Use `ip access-list resequence` to adjust sequence numbers automatically
- Always verify ACL configuration and application with show commands

