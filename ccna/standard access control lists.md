# Standard Access Control Lists

## Overview

Access Control Lists (ACLs) are ordered lists of rules that filter packets as they enter or exit router interfaces. They function as packet filters, examining each packet and determining whether it should be allowed or blocked based on predefined rules. Standard ACLs filter packets based on a single parameter: the source IP address. ACLs are essential tools for implementing network security requirements and controlling access to network resources.

## How ACLs Work

### ACL Fundamentals

- ACLs function like if-then-else conditionals in programming
- Evaluate conditions and take actions based on results
- Each ACL consists of series of rules called Access Control Entries (ACEs)
- Each ACE specifies:
  - Matching condition (IP address or range of IP addresses)
  - Action (permit or deny)

### Packet Evaluation Process

- Router evaluates packets against ACL sequentially from top to bottom
- Once packet matches an ACE, router takes specified action (permit or deny)
- Router does not process remaining ACEs after match is found
- Order of ACEs is very important; it influences overall effect of ACL

### Permit and Deny Actions

- **Permit**: Packet is forwarded
- **Deny**: Packet is discarded
- Packets are evaluated against each ACE in order until match is found

### Implicit Deny

- At end of every ACL, there is hidden rule that denies all unmatched packets
- Called implicit deny
- Ensures secure stance: only traffic explicitly permitted by ACL is forwarded
- Everything else is automatically discarded
- If packet doesn't match any explicitly defined conditions, it is denied

### Shadowed Rules

- ACE that will never be acted upon because it is preceded by less specific rule
- Less specific rule covers the matching condition of the shadowed rule
- Example: If permit 192.168.0.0/16 comes before deny 192.168.1.0/24, the deny rule is shadowed
- Should not occur in properly configured ACL
- Always configure more specific rules first

## Applying ACLs to Interfaces

### ACL Application Requirement

- Creating ACL doesn't affect router behavior on its own
- ACL must be applied to one or more interfaces to take effect
- Can be applied in inbound direction, outbound direction, or both

### Inbound ACLs

- Evaluate packets as they enter the interface
- Every time router receives packet on interface, router evaluates packet against ACL
- If ACL permits packet, router continues to process packet
- If ACL denies packet, router discards it

### Outbound ACLs

- Evaluate packets as they exit the interface
- If router determines packet should be forwarded out of interface, router first evaluates packet against ACL
- If ACL permits packet, router forwards it
- If ACL denies packet, router discards it

### Interface Limitations

- Each interface can have maximum of one ACL applied in each direction
- One inbound ACL and one outbound ACL per interface

### Placement Guidelines

- Standard ACLs should usually be applied outbound on interface connected to destination LAN you want to protect
- This serves to filter packets destined for that LAN
- Applying ACL inbound can be useful to block unwanted traffic from entering router
- Ideal location and direction depend on desired result

## ACL Types

### Categorization Methods

ACLs can be categorized in two ways:

1. **Matching parameters**:
   - Standard ACLs: Match based on source IP address only
   - Extended ACLs: Match based on source/destination IP addresses, ports, protocols, and others

2. **Identification method**:
   - Numbered ACLs: Identified by number
   - Named ACLs: Identified by name

### Four ACL Types for CCNA

- Standard numbered ACL
- Standard named ACL
- Extended numbered ACL
- Extended named ACL

### Numbered ACL Ranges

- **Standard IP ACLs**: 1-99 and 1300-1999
- **Extended IP ACLs**: 100-199 and 2000-2699
- Original ranges (1-99, 100-199) were expanded to allow more ACLs
- Must pick ACL number from appropriate range

## Standard Numbered ACLs

### Configuration Method

- Configured entirely from global config mode
- Configure each ACE sequentially, from top to bottom
- Order in which you configure ACEs is very important
- Router processes ACEs in order they were configured

### Configuration Command

- Primary command: `access-list number {permit | deny} source-ip wildcard-mask`
- Number argument must be in correct range (1-99 or 1300-1999 for standard ACLs)
- Wildcard masks indicate bits that must match (0) and bits that don't have to match (1)
- Can think of wildcard masks as inverse netmasks

### Wildcard Mask Calculation

- Shortcut: subtract each octet of netmask from 255
- Example: /24 netmask (255.255.255.0) → wildcard mask 0.0.0.255
- First three octets: 255 - 255 = 0
- Final octet: 255 - 0 = 255

### Optional Remarks

- Configure descriptive remark with: `access-list number remark remark-text`
- Useful to clarify purpose of ACL
- Example: `access-list 1 remark Block Engineering`

### Verification Commands

- `show access-lists`: View all ACLs
- `show ip access-lists`: View only IP ACLs
- Output shows sequence numbers automatically assigned to each ACE

### Sequence Numbers

- First ACE given sequence number 10
- Default increment is 10 (10, 20, 30, etc.)
- Leaves room between ACEs to insert new ACEs if needed
- Only possible to insert new ACEs in named ACL config mode

### Applying Numbered ACLs

- Command: `ip access-group number {in | out}` in interface config mode
- Verify with: `show ip interface [interface]`
- Shows "Outgoing access list" or "Inbound access list" in output

## Standard Named ACLs

### Configuration Method

- First created in global config mode
- Each ACE configured in separate config mode (standard named ACL config mode)
- Enter config mode: `ip access-list standard name`
- Configure ACEs: `[seq-num] {permit | deny} source-ip wildcard-mask`

### Sequence Number Control

- Can optionally specify sequence number (seq-num) to control where ACE is inserted
- Default: ACEs start at sequence 10 and increment by 10
- Useful for inserting new ACEs between existing ones (e.g., at sequence 15)

### Matching Single IP Address

Three ways to match single IP address (work for both numbered and named ACLs):

1. `deny 8.8.8.8` (simplest)
2. `deny 8.8.8.8 0.0.0.0` (/32 wildcard mask)
3. `deny host 8.8.8.8` (explicit host keyword)

### Any Keyword

- `permit any` matches all IP addresses
- Equivalent to `permit 0.0.0.0 255.255.255.255`
- Can be used in both numbered and named ACLs

### Applying Named ACLs

- Identical to applying numbered ACLs
- Command: `ip access-group name {in | out}` in interface config mode
- Example: `ip access-group BLOCK_MARTHA_BOB in`

### Numbered ACLs in Named Mode

- Modern versions of Cisco IOS allow configuring numbered ACLs in named ACL config mode
- Specify number instead of name: `ip access-list standard 99`
- Provides benefits of named ACL mode (sequence numbers, easier editing)
- After configuration, appears in running config as if configured using traditional method

## Real-World Applications

- **Department access control**: Restrict access to specific servers or networks by department
- **Security policies**: Implement security requirements from security teams
- **Network segmentation**: Control communication between different network segments
- **Resource protection**: Protect sensitive servers from unauthorized access
- **Traffic filtering**: Block unwanted traffic from entering or exiting network segments
- **Compliance**: Meet regulatory requirements for network access control

## Troubleshooting Standard ACLs

### Common Issues

- **ACL not working**: Verify ACL is applied to correct interface in correct direction
- **Unexpected traffic blocked**: Check ACE order; more specific rules should come first
- **Shadowed rules**: Verify no less specific rules come before more specific ones
- **All traffic blocked**: Check for implicit deny; ensure permit statements exist
- **Wrong traffic permitted**: Verify wildcard masks are correct

### Troubleshooting Steps

1. Verify ACL configuration: `show access-lists [number | name]`
2. Check interface application: `show ip interface [interface]`
3. Verify ACE order: More specific rules should come first
4. Test connectivity: Ping or other tests to verify ACL behavior
5. Check for shadowed rules: Review ACE order carefully

### Verification Commands

- `show access-lists`: View all ACLs with sequence numbers
- `show ip access-lists`: View only IP ACLs
- `show ip interface [interface]`: View applied ACLs on interface
- `show running-config | include access-list`: View ACL configuration

## Best Practices

- Apply standard ACLs as close to destination as possible
- Configure more specific ACEs before less specific ones
- Use descriptive names for named ACLs
- Add remarks to document ACL purpose
- Test ACLs in lab before production deployment
- Document ACL requirements and configurations
- Review ACLs regularly for effectiveness
- Use named ACLs when editing is likely needed
- Verify ACL placement and direction carefully
- Consider implicit deny when designing ACLs

## Summary

- ACLs are ordered lists of rules that filter packets as they enter or exit router interfaces
- Each ACL consists of Access Control Entries (ACEs) specifying matching conditions and actions
- Packets evaluated sequentially from top to bottom; first match determines action
- Permit action forwards packet; deny action discards packet
- Implicit deny at end of every ACL denies all unmatched packets
- Shadowed rules are ACEs that will never be acted upon due to preceding less specific rules
- ACLs must be applied to interfaces in inbound or outbound direction to take effect
- Standard ACLs match packets based only on source IP address
- Numbered ACLs identified by number (standard: 1-99, 1300-1999)
- Named ACLs identified by name and configured in separate config mode
- Standard numbered ACLs configured with `access-list number {permit | deny} source-ip wildcard-mask`
- Standard named ACLs created with `ip access-list standard name`, then ACEs configured in that mode
- Wildcard masks indicate matching bits (0) and non-matching bits (1); inverse of netmasks
- Sequence numbers automatically assigned (10, 20, 30, etc.) with default increment of 10
- Apply ACLs with `ip access-group {number | name} {in | out}` in interface config mode
- Standard ACLs should be applied as close to destination as possible
- Use `show access-lists` and `show ip interface` to verify ACL configuration and application

