# Standard Access Control Lists

## Overview

Standard Access Control Lists (ACLs) are ordered lists of rules that filter IPv4 packets as they enter or leave router interfaces. Standard ACLs match on the source IP address only and apply a permit or deny action. They are a basic tool for enforcing simple security policies and controlling access between subnets.

## How standard ACLs work

### ACL fundamentals

- ACLs act like ordered if-then rules  
- Each rule is an Access Control Entry (ACE)  
- Each ACE contains:
  - Match condition (source IP address or range)  
  - Action (permit or deny)  

### Packet evaluation

- Router checks ACL from top to bottom  
- First matching ACE decides the action  
- Remaining ACEs are ignored once a match is found  
- Order of ACEs directly affects behavior  

### Permit, deny, and implicit deny

- `permit`  
  Matching packets are allowed through the interface

- `deny`  
  Matching packets are dropped and not forwarded

- Implicit deny  
  - Every ACL ends with an invisible `deny any`  
  - Packets that do not match any ACE are dropped  
  - At least one permit is required or all traffic will be blocked  

### Shadowed entries

- ACE that can never match because an earlier ACE already covers that traffic  
- Example:
  - `permit 192.168.0.0 0.0.255.255`
  - `deny   192.168.1.0 0.0.0.255`  (shadowed)  
- More specific ACEs should appear before less specific ACEs  

## Interface application

### Inbound vs outbound

- Inbound ACL  
  - Packets are checked as they enter an interface  
  - If permitted, normal routing continues  
  - If denied, packet is dropped immediately  

- Outbound ACL  
  - Packets are checked as they leave an interface  
  - Used after routing has chosen an exit interface  

### One ACL per direction

- Each interface supports:
  - One inbound ACL  
  - One outbound ACL  
- Standard ACL and extended ACL cannot both be applied in the same direction on the same interface  

### Placement guidelines

- Standard ACLs filter only by source address  
- Usual guideline:
  - Place standard ACLs **close to the destination** being protected  
- Outbound placement on the destination LAN interface is common  
- Inbound placement can be used when blocking traffic as it enters the router is preferred  

## ACL types and ranges

### Match scope

- Standard ACLs  
  - Match source IPv4 address only  

- Extended ACLs  
  - Match source and destination addresses, protocols, and ports  

### Identification

- Numbered ACLs  
  - Identified by a number  

- Named ACLs  
  - Identified by a name  

### Number ranges

- Standard IPv4 ACLs  
  - 1–99  
  - 1300–1999  

- Extended IPv4 ACLs  
  - 100–199  
  - 2000–2699  

## Standard numbered ACLs

### Configuration

- Configured in global configuration mode  
- ACEs are added in order from top to bottom

Basic command:

```cisco
access-list <number> {permit | deny} <source-ip> <wildcard-mask>
```

- `<number>` must be in the standard ACL range  
- Wildcard mask:
  - 0 bit = must match  
  - 1 bit = do not care  

### Wildcard masks

- Calculated as: `255 - subnet mask` for each octet  
- Examples:
  - /24 (255.255.255.0) → 0.0.0.255  
  - /16 (255.255.0.0)   → 0.0.255.255  

### Remarks

- Optional comment lines clarify ACL purpose:

  ```cisco
  access-list 1 remark Block Engineering to ServerA
  access-list 1 deny 192.168.10.0 0.0.0.255
  access-list 1 permit any
  ```

### Verification

- `show access-lists`  
  - Displays all ACLs and ACEs  

- `show ip access-lists`  
  - Displays IP ACLs only  

- Output includes automatic sequence numbers (10, 20, 30, and so on)  

### Applying numbered ACLs

- Applied under interface configuration:

  ```cisco
  interface GigabitEthernet0/0
   ip access-group 1 out
  ```

- `show ip interface <name>`  
  - Confirms ACLs applied inbound or outbound  

## Standard named ACLs

### Configuration mode

- Created in global configuration mode:

  ```cisco
  ip access-list standard BLOCK_USERS
  ```

- ACEs are added in ACL configuration mode:

  ```cisco
  ip access-list standard BLOCK_USERS
   10 deny 192.168.10.0 0.0.0.255
   20 permit any
  ```

- Sequence numbers control ACE order and make edits easier  

### Matching single addresses

Equivalent ways to match a single host:

- `deny 8.8.8.8`  
- `deny 8.8.8.8 0.0.0.0`  
- `deny host 8.8.8.8`  

### Matching any address

- `permit any`  
  - Matches all IPv4 addresses  
  - Equivalent to `permit 0.0.0.0 255.255.255.255`  

### Applying named ACLs

- Applied just like numbered ACLs, but with a name:

  ```cisco
  interface GigabitEthernet0/0
   ip access-group BLOCK_USERS in
  ```

### Numbered ACLs in named mode

- Some IOS versions allow:

  ```cisco
  ip access-list standard 10
  ```

- This configures ACL 10 using named ACL style with sequence numbers  
- Running configuration still shows ACL 10 as a numbered standard ACL  

## Troubleshooting standard ACLs

### Common issues

- ACL applied to wrong interface or wrong direction  
- ACE order causing unexpected matches  
- Wildcard masks not matching intended ranges  
- Missing permit statements leaving only the implicit deny  
- Shadowed ACEs that never match  

### Troubleshooting steps

1. Check ACL contents:

   ```cisco
   show access-lists <number-or-name>
   ```

2. Confirm interface application:

   ```cisco
   show ip interface <name>
   ```

3. Review ACE order, placing more specific entries first  
4. Correct wildcard masks where needed  
5. Test with pings or traceroute and monitor ACL counters  

## Quick review

- Standard ACLs match on source IPv4 address only.  
- ACLs are processed top to bottom and stop at the first match.  
- Every ACL ends with an implicit `deny any`, so at least one permit is required.  
- Standard ACLs are usually placed close to the destination they protect.  
- Numbered standard ACLs use ranges 1–99 and 1300–1999.  
- Named ACLs use `ip access-list standard <name>` and provide easier editing with sequence numbers.  
- ACLs are applied to interfaces with `ip access-group <number-or-name> in | out`.  
- Verification and troubleshooting rely on `show access-lists`, `show ip access-lists`, and `show ip interface`.  
