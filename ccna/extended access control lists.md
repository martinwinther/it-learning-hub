# Extended Access Control Lists

## Overview

Extended Access Control Lists (ACLs) match on more fields than standard ACLs. They can filter traffic based on protocol, source and destination IP addresses, and source and destination port numbers. This allows precise control over which traffic is permitted or denied.

## Fundamentals

### Similarities with standard ACLs

- Access control entries (ACEs) are processed from top to bottom
- The first matching ACE decides the action
- An implicit deny exists at the end of every ACL
- ACLs have no effect until applied to an interface in a direction

### Matching fields

Extended ACLs can match on:

- Protocol
- Source IP address
- Destination IP address
- Source port (TCP or UDP)
- Destination port (TCP or UDP)

A packet must match every field in an ACE to be considered a match.

## Configuration

### Numbered extended ACLs

- Created in global configuration mode
- Number ranges:
  - 100 to 199
  - 2000 to 2699
- Basic syntax:

  ```text
  access-list <number> {permit | deny} <protocol> <source> <destination> [port-options]
  ```

- ACEs are entered in the order they should be evaluated

### Named extended ACLs

- Created with:

  ```text
  ip access-list extended <name-or-number>
  ```

- Within ACL configuration mode, use:

  ```text
  [sequence] {permit | deny} <protocol> <source> <destination> [port-options]
  ```

- Sequence numbers control ACE order and allow later insertion or deletion
- Modern IOS allows numbered ACLs to be edited in named ACL mode

### Protocol field

Common protocol keywords:

- `ip` for all IPv4 traffic
- `tcp` for TCP
- `udp` for UDP
- `icmp` for ICMP
- `ospf` for OSPF

Using `ip` ignores port numbers and matches all IPv4 packets between the specified source and destination.

### Address field

Source and destination address options:

- `any` matches any address  
  Equivalent to `0.0.0.0 255.255.255.255`
- `host A.B.C.D` matches a single IP address  
  Equivalent to `A.B.C.D 0.0.0.0`
- `A.B.C.D W.X.Y.Z` matches a range with a wildcard mask

In extended ACLs, a single IP address must be written as `host A.B.C.D` or `A.B.C.D 0.0.0.0`. Just writing the IP without a keyword is not allowed.

## Port matching

### When ports apply

- Port numbers are used only with TCP or UDP
- Ports cannot be specified with `icmp`, `ospf`, or `ip`

Basic format:

```text
{permit | deny} {tcp | udp} <src-ip> [src-operator src-port] <dst-ip> [dst-operator dst-port]
```

If ports are omitted, all ports match.

### Port operators

Operators are placed before the port value:

- `eq` port equal to the given port
- `gt` port greater than the given port
- `lt` port less than the given port
- `neq` port not equal to the given port
- `range` port between two values, including both

Example:

```text
permit tcp any any eq 443
deny udp any any range 1 1023
```

### Port keywords

Some common services have keywords instead of numbers:

- `ftp-data` for TCP 20
- `ftp` for TCP 21
- `telnet` for TCP 23
- `domain` for TCP or UDP 53
- `bootps` for UDP 67 (DHCP server)
- `bootpc` for UDP 68 (DHCP client)
- `tftp` for UDP 69
- `www` for TCP 80

There is no keyword for HTTPS, so port 443 uses `eq 443`.

### Client and server ports

- Server applications listen on well known ports
- Clients use ephemeral source ports in a high range
- Initial client to server traffic has:
  - Source port: high ephemeral port
  - Destination port: server well known port

For most ACLs that control access to services, matching on the destination port is enough.

## Placement

### Placement guidelines

- Extended ACLs should be placed as close to the source as practical
- Standard ACLs are usually placed closer to the destination
- Placing extended ACLs near the source:
  - Stops unwanted traffic early
  - Saves bandwidth and processing on downstream devices

When designing ACLs, consider both the direction and the interface to avoid blocking legitimate traffic.

## Editing and resequencing

### Numbered ACL limitations

- Numbered ACLs created with `access-list` cannot remove single ACEs from global configuration mode
- `no access-list <number>` deletes the entire ACL

### Named ACL advantages

- Allows individual ACE deletion:

  ```text
  no <sequence-number>
  ```

- Allows inserting ACEs by picking sequence numbers between existing entries
- Example:

  ```text
  10 permit tcp any host 192.0.2.10 eq 22
  20 deny   ip any any
  ```

### Resequencing

- Command:

  ```text
  ip access-list resequence <name-or-number> <start> <increment>
  ```

- Renumbers all ACEs in the ACL
- Helpful when sequence numbers are too close together to allow new entries

## Troubleshooting and verification

### Common issues

- ACL too restrictive, missing required permits
- Ports or protocols do not match the actual traffic
- ACE order causes specific entries to be shadowed by earlier ones
- ACL applied in the wrong direction or on the wrong interface
- Implicit deny at the end blocking traffic that was never explicitly permitted

### Useful commands

- `show access-lists`
- `show ip access-lists`
- `show ip interface <interface>`
- `show running-config | include access-list`

These commands show ACE order, match counters, and where ACLs are applied.

## Quick review

- Extended ACLs match on protocol, addresses, and ports for more precise filtering than standard ACLs.
- Numbered extended ACLs use ranges 100 to 199 and 2000 to 2699.
- Named ACLs provide better editing options with sequence numbers, deletion, insertion, and resequencing.
- Port matching is valid only for TCP and UDP and uses operators such as `eq`, `gt`, `lt`, `neq`, and `range`.
- Common service ports have keywords such as `ftp`, `telnet`, `domain`, `tftp`, and `www`.
- Extended ACLs are usually placed close to the source network to drop unwanted traffic early.
- Troubleshooting focuses on ACE order, correct protocol and port usage, and confirming where the ACL is applied.
