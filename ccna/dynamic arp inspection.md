# Dynamic ARP Inspection

## Overview

We first covered Address Resolution Protocol (ARP) in chapter on Ethernet LAN switching, and it has come up several times throughout this book. ARP is an essential protocol in IP networks, serving as the bridge between Layer 2 and Layer 3 by mapping IP addresses to their corresponding MAC addresses. However, like many protocols, ARP is susceptible to exploitation that can compromise the security of a network. Dynamic ARP Inspection (DAI) is a security feature on Cisco switches that we can use to mitigate such threats. DAI is part of CCNA exam topic 5.7: Configure and verify Layer 2 security features. (These include DHCP Snooping, Dynamic ARP Inspection, and Port Security.) We have already covered Port Security and DHCP Snooping, so this is the final chapter addressing topic 5.7. As you read this chapter, you'll notice similarities between DAI and DHCP Snooping, both in functionality and Cisco IOS configuration. In fact, DAI relies on the DHCP Snooping binding table as one of its key components.

## ARP Fundamentals

### ARP Message Fields

- Although we have covered ARP before, understanding DAI requires deeper understanding of contents of ARP messages
- ARP messages include Sender MAC and Sender IP fields to indicate MAC and IP addresses of sender
- And Target MAC and Target IP fields to indicate target's addresses
- Target IP field of ARP request is particularly important because it's broadcast message
- Switch will flood message to all hosts in LAN
- So this field is used to indicate actual intended recipient of message
- ARP message is encapsulated directly in Ethernet frame—it does not include IP header
- Sender and target IP fields are part of ARP message itself, not part of IP header

### ARP Exchange Process

- In ARP exchange, both hosts learn each other's MAC address—that is ARP's purpose, after all
- PC1 broadcasts ARP request
- R1 uses information in Sender MAC and Sender IP fields of PC1's request to create ARP table entry
- Mapping PC1's IP address to its MAC address
- Then, R1 sends unicast ARP reply message to PC1
- After receiving it, PC1 uses information in Sender MAC and Sender IP fields to create entry for R1 in its own ARP table
- ARP process is complete, and both devices know each other's MAC address

## ARP Poisoning Attack

### ARP Vulnerability

- ARP's most significant vulnerability is how simple it is for attacker to overwrite legitimate ARP table entries with "poisoned" entries
- ARP poisoning attack
- After PC1 and R1 have learned each other's MAC address, attacker sends ARP replies to overwrite legitimate entries with its own MAC address
- As result, PC1 and R1 will send frames to attacker instead of each other
- Giving attacker access to their communications
- Regarding CIA triad, this affects confidentiality of communications between hosts
- ARP replies shown are gratuitous ARP (GARP) replies
- ARP replies that were not prompted by ARP requests
- We saw another example of GARP when covering First Hop Redundancy Protocols

### Existing Security Features

- Security features we have covered so far (Port Security and DHCP Snooping) don't protect against ARP poisoning attacks
- ARP poisoning is performed from single source MAC address
- So limiting number of MAC addresses on port with Port Security doesn't help
- And DHCP Snooping only filters DHCP messages—not ARP messages
- However, DHCP Snooping does produce table of hosts who have leased IP address using DHCP
- Mapping their IP addresses to their MAC addresses: DHCP Snooping binding table
- DAI uses this table as part of its inspection process

## DAI Configuration

### Enabling DAI

- To enable DAI, use `ip arp inspection vlan vlans` command in global config mode
- As with `ip dhcp snooping vlan` command, can enable DAI on multiple VLANs with single command
- Example: `ip arp inspection vlan 1-4094` for all VLANs
- Example: `ip arp inspection vlan 2-5,7,9,2028` for specific VLANs
- Use `show ip arp inspection` to view general information about DAI on switch
- Shows which VLANs DAI is enabled and operational on

### DAI and DHCP Snooping

- Rest of chapter will focus on DAI configuration, not DHCP Snooping
- But keep in mind that two features work together
- Although DAI can be used without DHCP Snooping, it is rare
- DAI relies on DHCP Snooping binding table for its inspection process

## Trusted and Untrusted Ports

### Trusted/Untrusted Concept

- Switch using DAI inspects and filters ARP messages it receives
- Much like DHCP Snooping, DAI operates using concept of trusted and untrusted ports
- On DAI-enabled switch, all ARP messages received on trusted ports are permitted
- While ARP messages received on untrusted ports are inspected to determine whether they should be forwarded or discarded

### Port Configuration Guidelines

- When DAI is enabled, all ports are untrusted by default
- This means that DAI will inspect ARP messages received on all ports
- When configuring DAI, ports connected to end hosts should remain in default untrusted state
- Ports connected to network infrastructure devices, such as routers and other switches, should be trusted
- These guidelines are slightly different from those for DHCP Snooping
- Leading to some ports being untrusted by DHCP Snooping but trusted by DAI
- We'll look at rationale behind this discrepancy in next section when we look at how DAI inspects and filters ARP messages
- Guidelines for DHCP Snooping are to make ports that lead toward DHCP server trusted
- And leave ports that lead toward end hosts in untrusted state (default)

### Configuring Trusted Ports

- To make port trusted, use `ip arp inspection trust` command in interface config mode
- Can verify with `show ip arp inspection interfaces`
- Shows trust state and rate limit of each port
- As with DHCP Snooping, trusting correct ports is critical
- Trusting ports that should remain untrusted exposes network to potential threats (like ARP poisoning)
- On other hand, failing to trust ports that should be trusted can disrupt network communications by blocking valid ARP requests

## DAI Inspection Process

### Inspection Overview

- DAI-enabled switch inspects ARP messages as they are received on untrusted ports
- This includes both ARP requests and ARP replies
- It then makes filtering decision: should I forward or discard this message?
- It does this by examining Sender MAC and Sender IP fields of ARP message
- And comparing them to DHCP Snooping binding table:
  - If there is matching entry, message is forwarded
  - Without matching entry, message is discarded

### DHCP Snooping Binding Table

- DHCP Snooping binding table includes information like client's MAC address, leased IP address, VLAN, and interface
- When DAI inspects ARP message, it looks for matching entry in this table
- If Sender MAC and Sender IP in ARP message match entry in binding table, message is forwarded
- If no matching entry is found, message is discarded

### Manually Configured IP Addresses

- With this table, let's consider why some ports should be trusted by DAI (despite being untrusted by DHCP Snooping)
- Example: switch uses R1 as its default gateway and has IP address on its VLAN 1 SVI
- Switch sends ARP request to learn MAC address of R1
- But another switch blocks it—it doesn't have matching entry in its DHCP Snooping binding table!
- Because switch's VLAN 1 SVI has manually configured IP address
- Switch had no opportunity to create DHCP Snooping binding table entry for it
- Same problem would occur for any device with manually configured IP address
- Ports connected to such devices should be trusted

### ARP ACLs

- In addition to DHCP Snooping binding table, there is second source that DAI-enabled switch can check when deciding to forward or discard ARP message: ARP ACLs
- ARP ACLs can be used to manually configure IP-MAC mappings for devices that don't use DHCP
- Allowing their ARP messages to pass through untrusted ports without being discarded by DAI
- ARP ACLs are beyond scope of CCNA exam
- So this chapter focuses on DAI using DHCP Snooping binding table
- Even though ARP ACLs are option, general recommendation is still to trust ports connected to infrastructure devices

## Additional Validation Checks

### Validation Overview

- By default, DAI checks that ARP message's Sender MAC and Sender IP fields have matching entry in DHCP Snooping binding table (or ARP ACLs)
- However, attacker can easily spoof these addresses
- To prevent various kinds of spoofing attacks, can enable additional checks with `ip arp inspection validate` command
- There are three keywords that can be used at end of this command

### Source MAC Validation

- `src-mac`: Switch verifies that Ethernet Source MAC and ARP Sender MAC of requests and responses match
- If they don't match, message is dropped

### Destination MAC Validation

- `dst-mac`: Switch verifies that Ethernet Destination MAC and ARP Target MAC of ARP responses match
- If they don't match, message is dropped

### IP Address Validation

- `ip`: Switch will check for invalid/unexpected IP addresses in ARP Sender IP or Target IP
- Such as 0.0.0.0 or 255.255.255.255
- These should normally not appear in ARP messages
- So their presence would indicate some kind of spoofing

### Configuring Validation

- By default, all of these optional checks are disabled
- But can choose to enable one, two, or all three of them
- Example: `ip arp inspection validate src-mac dst-mac ip` enables all three
- Can verify with `show ip arp inspection`
- Shows which validation checks are enabled
- One potential concern when enabling these additional checks is that they increase load on switch's CPU
- While this is generally not concern with modern hardware, it's good practice to monitor CPU usage
- Especially in older or resource-constrained environments
- Use `show processes cpu` command to check CPU load

## DAI Rate Limiting

### Rate Limiting Overview

- Like DHCP Snooping, DAI can be demanding on switch's CPU
- Switch is very efficient at forwarding frames without taxing its CPU
- However, when it has to stop and inspect ARP message with DAI, CPU gets involved
- This means that attacker can potentially overwhelm switch with ARP messages
- Resulting in denial of service
- To mitigate against such threats, DAI can limit rate at which port can receive ARP messages
- Whereas DHCP Snooping rate limiting is disabled on all ports by default
- DAI has default rate-limiting settings:
  - Untrusted ports: Rate limit of 15 packets per second (pps)
  - Trusted ports: No rate limit

### Configuring Rate Limiting

- Can modify rate limit on per-port basis with `ip arp inspection limit rate rate [burst interval seconds]`
- Specifying burst interval is optional—default is 1
- But it lets you specify over how many seconds packet rate is measured
- Example: `ip arp inspection limit rate 20` (twenty packets per second, equivalent to burst interval 1)
- Example: `ip arp inspection limit rate 40 burst interval 2` (forty packets every 2 seconds)
- Twenty packets per second and 40 packets every 2 seconds are same average rate
- But latter allows for larger bursts of traffic (as long as average rate doesn't surpass 40 packets every 2 seconds)

### Rate Limit Exceeded

- What happens if rate limit is exceeded?
- Switch will error-disable port
- To demonstrate, if rate limit is set to 1 pps and exceeded, switch will error-disable port
- Can reenable port disabled by DAI rate limiting in two ways:
  - **Manual**: Issue `shutdown` and `no shutdown` on error-disabled port
  - **Automatic**: Enable ErrDisable Recovery for ports disabled by DAI rate limiting with `errdisable recovery cause arp-inspection`

### Rate Limiting Best Practices

- Because DAI rate limiting is enabled on untrusted ports by default, you probably won't have to make any changes
- Fifteen packets per second is more than enough for most end hosts
- But low enough to prevent DoS attacks from trying to overwhelm switch's CPU

## Real-World Applications

- **Network security**: Protect against ARP poisoning attacks
- **Man-in-the-middle prevention**: Prevent attackers from intercepting communications
- **Access control**: Ensure only legitimate devices can communicate
- **Network monitoring**: Track ARP activity and detect anomalies
- **Compliance**: Meet security requirements for network access

## Troubleshooting

### Common Issues

- **ARP messages blocked**: Check trusted/untrusted port configuration
- **Legitimate devices cannot communicate**: Verify devices with static IPs have trusted ports or ARP ACLs
- **Rate limiting issues**: Check rate limits are not too restrictive
- **CPU utilization**: Monitor CPU usage when validation checks are enabled

### Troubleshooting Steps

1. Verify DAI status: `show ip arp inspection`
2. Check VLAN configuration: Verify DAI is enabled on correct VLANs
3. Verify trusted ports: Use `show ip arp inspection interfaces` to check which ports are trusted
4. Review binding table: Use `show ip dhcp snooping binding` to view DHCP bindings
5. Check validation: Verify validation checks are configured appropriately
6. Monitor rate limits: Check rate limit settings on ports
7. Test ARP process: Verify devices can successfully resolve MAC addresses

## Best Practices

- Enable DAI on all switches in network
- Activate DAI on all VLANs that need protection
- Trust ports connected to infrastructure devices (routers, switches)
- Keep ports connected to end hosts in untrusted state
- Enable DHCP Snooping before enabling DAI (DAI relies on DHCP Snooping binding table)
- Configure appropriate validation checks (src-mac, dst-mac, ip)
- Monitor CPU usage when validation checks are enabled
- Use default rate limits unless specific requirements dictate otherwise
- Document which ports should be trusted
- Test DAI configuration in lab before production deployment
- Combine with Port Security and DHCP Snooping for comprehensive Layer 2 security

## Summary

- Dynamic ARP Inspection (DAI) is security feature on Cisco switches that protects against ARP-based attacks by inspecting and filtering ARP messages
- ARP messages include Sender MAC and Sender IP fields to indicate MAC and IP addresses of sender
- And Target MAC and Target IP fields to indicate target's (destination's) addresses
- ARP's most significant vulnerability is how simple it is for attacker to overwrite legitimate ARP table entries by sending gratuitous ARP messages—ARP poisoning
- By telling devices in LAN to send their frames to attacker, attacker gains access to their communications
- Port Security doesn't protect against ARP poisoning because ARP poisoning is performed from single source MAC address
- DHCP Snooping doesn't protect against ARP poisoning because it only filters DHCP messages
- DHCP Snooping produces table of hosts who have leased IP address using DHCP, mapping their IP addresses to their MAC addresses: DHCP Snooping binding table
- DAI uses DHCP Snooping binding table in its inspection and filtering process
- Use `ip arp inspection vlan vlans` in global config mode to enable DAI
- Use `show ip arp inspection` to view general information about DAI on switch
- DAI uses concepts of trusted and untrusted ports
- All ARP messages received on trusted ports are permitted
- While ARP messages received on untrusted ports are inspected to determine whether they should be forwarded or discarded
- All ports on DAI-enabled switch are untrusted by default
- Ports connected to end hosts should remain untrusted
- Ports connected to network infrastructure devices, such as routers and other switches, should be trusted
- Use `ip arp inspection trust` in interface config mode to trust port
- Use `show ip arp inspection interfaces` to view DAI trust state and rate limit of each port
- DAI inspects ARP messages received on untrusted ports by examining Sender MAC and Sender IP fields
- And looking for matching entry in DHCP Snooping binding table
- If there is matching entry, message is forwarded
- Without matching entry, message is discarded
- If device has manually configured IP address (not learned via DHCP), device won't have matching entry in switches' DHCP Snooping binding tables
- Leading to device's ARP messages being discarded if received on untrusted port
- For this reason, ports connected to devices with manually configured IP addresses should be trusted
- In addition to DHCP Snooping binding table, can use ARP ACLs to manually configure IP–MAC mappings for devices that don't use DHCP
- Allowing their ARP messages to pass through untrusted ports without being discarded by DAI
- In addition to checking ARP message's Sender MAC and Sender IP fields for matching entry in DHCP Snooping binding table, DAI can optionally check other parameters
- Can configure it with `ip arp inspection validate` command
- Three keywords that can be used with `ip arp inspection validate` are:
  - `src-mac`: Checks that Ethernet Source MAC and ARP Sender MAC of ARP requests and responses match
  - `dst-mac`: Checks that Ethernet Destination MAC and ARP Target MAC of ARP responses match
  - `ip`: Ensures that invalid/unexpected IP addresses (i.e., 0.0.0.0 or 255.255.255.255) are not present in ARP Sender IP or Target IP fields
- Three optional checks are all disabled by default, but can enable one, two, or all three of them
- DAI inspection can be demanding on switch's CPU
- This means that attacker can potentially overwhelm switch with ARP messages, resulting in denial of service
- To mitigate against such threats, DAI can limit rate at which port can receive ARP messages
- By default, untrusted ports have rate limit of 15 packets per second
- And trusted ports have no rate limit
- Use `ip arp inspection limit rate rate [burst interval seconds]` to modify rate limit on per-port basis
- Optional burst interval lets you specify over how many seconds packet rate is measured (i.e., 40 packets every 2 seconds)
- If port's rate limit is exceeded, switch will error-disable port
- Can reenable port disabled by DAI rate limiting in two ways:
  - Manual: Issue `shutdown` and `no shutdown` on error-disabled port
  - Automatic: Enable ErrDisable Recovery for ports disabled by DAI rate limiting with `errdisable recovery cause arp-inspection`

