# DHCP Snooping

## Overview

DHCP is almost ubiquitous in modern networks, allowing for the automatic configuration of IP addresses, netmasks, default gateways, DNS servers, and other configuration information on hosts. However, DHCP contains vulnerabilities that can be exploited if sufficient care is not taken. We looked at one example: DHCP exhaustion, which is a type of DoS attack that prevents legitimate user devices from leasing IP addresses from a DHCP server. DHCP Snooping is a security feature on Cisco switches that protects against DHCP-based attacks by inspecting DHCP messages as they are received by the switch. DHCP Snooping only filters DHCP messages—non-DHCP messages are unaffected by DHCP Snooping.

## DHCP-Based Attacks

### DHCP Poisoning Attack

- In DHCP poisoning attack, attacker configures rogue DHCP server (sometimes called spurious DHCP server) to lease IP addresses to clients
- Rogue server leases valid IP addresses, but point of attack is to tell clients to use rogue server as their default gateway
- Not LAN's legitimate router
- This allows rogue server to intercept clients' communications
- Gaining access to (and possibly altering) their contents before relaying them to router
- DHCP poisoning may remind you of similarly named attack: ARP poisoning
- Both attacks allow attacker's device to act as man-in-the-middle, secretly intercepting targets' communications

### DHCP Poisoning Operation

- DHCP clients tend to accept first OFFER message they receive in response to their DISCOVER
- So rogue server's goal is to respond before any legitimate DHCP servers
- If both rogue and legitimate DHCP servers are in same LAN, it's race to reply first
- But if legitimate DHCP server is in different LAN, introducing additional delay between client and server
- Rogue server's "poisoned" OFFER has good chance of reaching client first due to its lower latency

### Port Security Limitation

- Port Security, which we covered in previous chapter, doesn't mitigate against DHCP poisoning attacks
- Rogue server sends DHCP messages from single MAC address
- So limiting number of MAC addresses on port doesn't help
- To defend your network against DHCP poisoning attacks, should use DHCP Snooping

## DHCP Snooping Configuration

### Enabling DHCP Snooping

- DHCP Snooping works by examining and filtering DHCP messages received by switch
- That's important point: DHCP Snooping only filters DHCP messages
- Non-DHCP messages are unaffected by DHCP Snooping
- Enable DHCP Snooping with `ip dhcp snooping` in global config mode
- It also needs to be activated on each VLAN with `ip dhcp snooping vlan vlans`
- `ip dhcp snooping` enables DHCP Snooping, but it won't actually take effect until you use second command (`ip dhcp snooping vlan vlans`) to activate it on each VLAN in LAN
- To keep things simple, example network has single VLAN (VLAN 1)
- But in LAN with multiple VLANs, should enable it on each VLAN that has hosts using DHCP
- Can activate DHCP Snooping on multiple VLANs with single command by using commas and hyphens in vlans argument
- Example: `ip dhcp snooping vlan 1-4094` for all VLANs
- Example: `ip dhcp snooping vlan 1,3-5,7,9-11` for specific VLANs

### Verifying DHCP Snooping

- Use `show ip dhcp snooping` to verify DHCP Snooping settings
- Shows whether DHCP Snooping is enabled
- Which VLANs it is configured on
- Which VLANs it is operational on
- And other settings

## Trusted and Untrusted Ports

### Trusted/Untrusted Concept

- DHCP Snooping works by filtering DHCP messages
- However, it doesn't filter DHCP messages received on all ports
- It only filters those received on untrusted ports
- Messages received on trusted ports are not filtered
- Concept of trusted and untrusted ports is fundamental to how DHCP Snooping works
- DHCP Snooping filters DHCP messages received on untrusted ports based on set of rules
- All ports are untrusted by default
- All DHCP messages received on trusted ports, however, are allowed
- Need to manually specify each trusted port with `ip dhcp snooping trust`

### Port Configuration Guidelines

- Ports that lead toward DHCP server should be trusted
- DHCP Snooping forwards DHCP messages received on those ports without any further inspection
- Ports that lead away from DHCP server—toward end hosts—should remain in default untrusted state
- When DHCP message is received on untrusted port, switch will inspect it and act as follows:
  - If it is DHCP server message (OFFER, ACK, or NAK), discard it
  - If it is DHCP client message (DISCOVER, REQUEST, DECLINE, or RELEASE), inspect it further to determine if it is legitimate
  - If client successfully leases IP address, create new entry in DHCP Snooping binding table

### Configuring Trusted Ports

- Use `ip dhcp snooping trust` in interface config mode to configure trusted port
- Can verify with `show ip dhcp snooping`
- Shows which interfaces are trusted and their rate limit settings

## DHCP Message Types

### Client Messages

- Should already be familiar with messages in DHCP DORA exchange: DISCOVER, OFFER, REQUEST, ACK
- However, there are some other DHCP message types that you should know
- When DHCP Snooping filters DHCP messages, it differentiates between messages sent by DHCP clients and those sent by DHCP servers
- Messages sent by DHCP clients include:
  - DISCOVER
  - REQUEST
  - DECLINE
  - RELEASE

### Server Messages

- Messages sent by DHCP servers include:
  - OFFER
  - ACK
  - NAK (negative ACK)

### Additional Message Types

- DECLINE: Used to tell server that leased IP address is already in use
- RELEASE: Used to tell server that client no longer needs its IP address
- NAK (negative ACK): Opposite of ACK; used to decline client's REQUEST
- You don't have to know details of these additional message types
- But should know which are sent by clients and which are sent by servers
- Other DHCP message types exist, but wouldn't expect to see them on CCNA exam

## DHCP Snooping Filtering

### Untrusted Port Filtering

- Untrusted ports only accept DHCP client messages
- However, they don't blindly accept all client messages
- They perform additional checks to verify that message is valid before accepting it
- Checks that switch performs depend on message type

### DISCOVER and REQUEST Messages

- For messages involved in DORA process—DISCOVER and REQUEST
- Switch checks that Ethernet source MAC address and DHCP chaddr match
- If addresses in two fields match, switch permits message
- If two addresses don't match, switch discards message
- chaddr field (written in lowercase to align with RFC 2131, which defines DHCP) represents client's hardware address
- Typically MAC address in modern networks (where Ethernet dominates)
- You might wonder, why have this field when client's MAC address is already present in Ethernet frame's source MAC address field?
- There are multiple reasons, but primary one is to support situations where DHCP client and server are in separate LANs (and DHCP relay agent is used)
- In such situations, by time client's DHCP message reaches server, source MAC address of Ethernet frame won't be client's MAC address
- Instead, it will be MAC address of last router that forwarded message to server
- chaddr field ensures that client's MAC address is still conveyed to server in such scenarios
- These two fields should match when client's message reaches switch
- They should only differ if message is forwarded by DHCP relay agent
- However, attacker might repeatedly send spoofed DHCP DISCOVER messages from single source MAC address (to bypass Port Security's MAC address limit)
- Each with unique address in chaddr field to perform DHCP exhaustion attack
- Verifying that these fields match protects against such attack

### RELEASE and DECLINE Messages

- Second category of DHCP client messages, RELEASE and DECLINE, are sent after client has leased IP address
- DECLINE is used if after receiving final ACK from server, client detects that IP address is already in use by another device
- RELEASE is used any time client decides it no longer needs its leased IP address
- For example, if it disconnects from network
- However, these messages can be exploited by attacker
- Example: attacker could send RELEASE message to tell server to release particular client's IP address
- And then attacker could attempt to lease that address for itself
- To verify that RELEASE and DECLINE messages are legitimate, switch will verify message by checking DHCP Snooping binding table

## DHCP Snooping Binding Table

### Binding Table Overview

- As DHCP Snooping-enabled switch observes DHCP exchanges between clients and servers, it builds table of clients that have successfully leased IP address
- That table is called DHCP Snooping binding table
- Can view it with `show ip dhcp snooping binding`

### Binding Table Contents

- DHCP Snooping binding table includes information like:
  - Client's MAC address
  - Leased IP address and duration of lease
  - VLAN
  - Interface (or port—terms are interchangeable) client is connected to
- When inspecting RELEASE or DECLINE message received on untrusted port, switch ensures that IP address of message and port it was received on match entry in binding table

## Option 82

### Option 82 Overview

- If you're following along in lab and have correctly enabled DHCP Snooping, activated it on necessary VLANs, and trusted appropriate ports
- You might be confused as to why hosts are unable to lease IP addresses via DHCP
- And why switches have empty DHCP Snooping binding tables
- Reason is option 82

### DHCP Options

- DHCP defines various optional fields, called options, that can be included in its messages
- One of those is DHCP relay agent information option, usually called by its number, option 82
- DHCP relay agent can insert this option when forwarding DHCP client messages to remote DHCP server
- Providing additional information to server that can inform IP allocation decision
- Details of option 82 are beyond scope of CCNA exam
- But option 82 is relevant to DHCP Snooping because of some default settings on Cisco routers and switches related to option 82

### Default Option 82 Behavior

- When DHCP Snooping is enabled, switch will automatically insert option 82 into DHCP client messages received on untrusted ports
- This behavior of inserting option 82 is useful if switch is multilayer switch acting as DHCP relay agent
- Forwarding client messages to remote DHCP server
- Default settings are configured with this common scenario in mind
- However, if switch is functioning as regular Layer 2 switch (not DHCP relay agent), this default setting can cause headaches
- This is because of another default setting: Option 82 on untrusted port is not allowed
- These two default settings mean that:
  - Switch adds option 82 to DHCP messages received on untrusted ports
  - Switch doesn't accept DHCP messages that already have option 82 on untrusted ports
- This might seem contradictory, but there's reason: DHCP client has no valid reason to add option 82 to its own messages
- If switch receives DHCP message that already contains option 82 on untrusted port, it's likely that rogue DHCP server or misconfigured client is at play
- For this reason, switch doesn't accept such messages

### Disabling Option 82 Insertion

- To disable option 82 insertion, use `no ip dhcp snooping information option` command in global config mode
- With this command configured, switch will no longer insert option 82 into clients' DHCP messages
- However, in example network, it's not enough to disable option 82 insertion on one switch alone
- Other switches having received DHCP client message on untrusted port will add option 82 themselves before forwarding message
- Cisco router acting as DHCP server or relay agent will drop such messages too
- So make sure to disable option 82 insertion on all switches
- With option 82 insertion disabled on all switches, client's DISCOVER message will reach DHCP server as is
- And client will be able to lease IP address
- If DHCP server were DHCP relay agent, it could then insert option 82 before forwarding DISCOVER to remote DHCP server
- Providing server with additional context about request
- This extra context can help server make informed IP allocation decision
- As far as CCNA exam is concerned, just know that you should disable option 82 insertion
- Unless switch itself is multilayer switch acting as DHCP relay agent
- This is often-forgotten step in configuring DHCP Snooping that can lead to frustration
- Don't forget!

### Other DHCP Options

- DHCP options enable client, server, and sometimes relay agents to exchange additional information that can support DHCP process and extend its functionality
- There are about 100 standard DHCP options defined in various RFCs, although not all are widely used
- In addition to option 82, here are few examples:
  - **Option 3 (Router)**: Very common option. Used by server to tell client which router to use as its default gateway
  - **Option 6 (DNS Server)**: Another very common option. Tells client which DNS server(s) to use for name resolution
  - **Option 50 (Requested IP Address)**: Client can include this option if it wants to request specific IP address from server (although server is not obligated to fulfill this request). Example: Windows PC will typically include this option to request same IP address it had previously (i.e., before it was last shut down)
- DHCP options are generally not something you need to know for CCNA exam
- Option 82 is relevant only due to its effect when DHCP Snooping is enabled

## DHCP Snooping Rate Limiting

### Rate Limiting Overview

- One more optional (but valuable) aspect of DHCP Snooping you can configure is rate limiting
- Limiting rate at which DHCP Snooping-enabled switch accepts DHCP messages
- Combination of Port Security and DHCP Snooping is able to thwart most DHCP-related attacks like DHCP starvation
- However, inspecting DHCP messages with DHCP Snooping can be demanding of switch's CPU
- This leads to another possible attack: overwhelming switch's CPU with countless DHCP messages
- Potentially leading to denial of service
- DHCP Snooping rate limiting can mitigate against such attack

### Configuring Rate Limiting

- Can enable DHCP Snooping rate limiting on per-port basis with `ip dhcp snooping limit rate rate`
- Rate argument is configured in packets per second (pps)
- Cisco recommends rate limit of no more than 100 pps on untrusted ports
- But appropriate rate varies greatly, depending on port
- Example: port connected to single PC should receive much less DHCP traffic than port connected to another switch with 40 of its own connected end hosts
- In real network, it's best to find balance between protecting against attacks and not blocking legitimate traffic

### Rate Limit Exceeded

- What happens if port receives DHCP messages at faster rate than its configured limit?
- Switch will error-disable port to prevent any further messages
- As with previous examples of error-disabled ports (BPDU Guard, power policing, and port security), there are two ways to reenable port that was disabled by DHCP Snooping rate limiting:
  - **Manual**: Issue `shutdown` and `no shutdown` on error-disabled port
  - **Automatic**: Configure `errdisable recovery cause dhcp-rate-limit` to enable ErrDisable Recovery for ports disabled by DHCP Snooping rate limiting

### Rate Limiting Best Practices

- Although rate limiting is optional and disabled by default, it's good idea to configure reasonable rate limits on untrusted ports as extra layer of protection against threats
- Make sure to test rate limits in controlled environment (lab) before rolling them out in live network!

## DHCP Snooping Configuration Summary

### Configuration Steps

1. Enable DHCP Snooping: `ip dhcp snooping`
2. Activate DHCP Snooping on each VLAN: `ip dhcp snooping vlan vlans`
3. Trust appropriate ports: `ip dhcp snooping trust`
4. Disable option 82 insertion: `no ip dhcp snooping information option`
5. (Optional) Configure rate limiting: `ip dhcp snooping limit rate rate`

## Real-World Applications

- **Network security**: Protect against DHCP poisoning and exhaustion attacks
- **Access control**: Ensure only legitimate DHCP servers can provide IP addresses
- **Man-in-the-middle prevention**: Prevent attackers from intercepting client communications
- **Network monitoring**: Track which devices have leased IP addresses
- **Compliance**: Meet security requirements for network access

## Troubleshooting

### Common Issues

- **Hosts cannot lease IP addresses**: Verify option 82 insertion is disabled on all switches
- **DHCP messages blocked**: Check trusted/untrusted port configuration
- **Binding table empty**: Verify DHCP Snooping is enabled and operational on correct VLANs
- **Rate limiting issues**: Check rate limits are not too restrictive

### Troubleshooting Steps

1. Verify DHCP Snooping status: `show ip dhcp snooping`
2. Check VLAN configuration: Verify DHCP Snooping is enabled on correct VLANs
3. Verify trusted ports: Use `show ip dhcp snooping` to check which ports are trusted
4. Check option 82: Verify option 82 insertion is disabled if not using DHCP relay
5. Review binding table: Use `show ip dhcp snooping binding` to view leased addresses
6. Test DHCP process: Verify clients can successfully lease IP addresses

## Best Practices

- Enable DHCP Snooping on all switches in network
- Activate DHCP Snooping on all VLANs that use DHCP
- Trust only ports that lead toward legitimate DHCP servers
- Keep all other ports in untrusted state
- Disable option 82 insertion unless switch is acting as DHCP relay agent
- Configure appropriate rate limits on untrusted ports
- Monitor DHCP Snooping binding table regularly
- Document which ports should be trusted
- Test DHCP Snooping configuration in lab before production deployment
- Combine with Port Security for comprehensive Layer 2 security

## Summary

- DHCP Snooping is security feature on switches that protects against DHCP-based attacks by inspecting DHCP messages as they are received
- In DHCP poisoning attack, attacker configures rogue DHCP server to lease IP addresses to clients
- Rogue server tells clients to use itself as their default gateway, resulting in man-in-the-middle attack
- Port Security doesn't mitigate against DHCP poisoning because rogue server sends DHCP messages from single MAC address
- DHCP Snooping only filters DHCP messages—non-DHCP messages are unaffected
- Enable DHCP Snooping with `ip dhcp snooping` in global config mode
- It also needs to be activated on each VLAN with `ip dhcp snooping vlan vlans`
- Use `show ip dhcp snooping` to verify DHCP Snooping settings
- DHCP Snooping only filters DHCP messages received on untrusted ports
- All ports are untrusted by default
- It doesn't filter messages received on trusted ports
- DHCP Snooping differentiates between messages sent by DHCP clients and those sent by DHCP servers
- Messages sent by clients include DISCOVER, REQUEST, DECLINE, and RELEASE
- Messages sent by servers include OFFER, ACK, and NAK
- Ports that lead toward DHCP server should be trusted
- Ports that lead away from DHCP server (toward end hosts) should remain in default untrusted state
- Use `ip dhcp snooping trust` in interface config mode to configure trusted port
- When DHCP message is received on untrusted port, switch will inspect it and act as follows:
  - If it is DHCP server message, discard it
  - If it is DHCP client message, inspect it further depending on type
  - If client successfully leases IP address, create new entry in DHCP Snooping binding table
- If message is DISCOVER or REQUEST message, switch will check that Ethernet source MAC address and DHCP chaddr (client hardware address) match
- If they match, it accepts message. If not, it discards message
- Source MAC address/chaddr check protects against DHCP exhaustion attacks
- If message is RELEASE or DECLINE message, switch will check DHCP Snooping binding table to verify message
- As DHCP Snooping-enabled switch observes exchanges between clients and servers, it builds table of clients that have successfully leased IP address: DHCP Snooping binding table
- View DHCP Snooping binding table with `show ip dhcp snooping binding`
- When RELEASE or DECLINE message is received on untrusted port, switch ensures that IP address of message and port it was received on match entry in binding table
- DHCP defines various optional fields, called options
- DHCP options are beyond scope of CCNA exam, except for option 82, which can impede DHCP process when DHCP Snooping is enabled
- Option 82 is DHCP relay information option
- DHCP relay agent can insert option 82 when forwarding DHCP client messages to remote DHCP server
- By default, DHCP Snooping-enabled switch will automatically insert option 82 into DHCP client messages received on untrusted ports
- By default, DHCP Snooping-enabled switch will discard DHCP messages with option 82 that are received on untrusted port
- Cisco router acting as DHCP server or relay agent will drop such messages too
- To prevent DHCP Snooping-enabled switch from adding option 82 to client messages, use `no ip dhcp snooping information option` in global config mode
- Can optionally configure rate limiting on per-port basis to limit rate at which port can receive DHCP messages
- Use `ip dhcp snooping limit rate rate` to configure rate limiting
- Rate argument is configured in packets per second (pps)
- Rate limiting can be configured on both untrusted and trusted ports, although it is rarely enabled on trusted ports
- If port receives DHCP messages at faster rate than its configured limit, switch will error-disable port
- Use `shutdown` and `no shutdown` to manually reenable error-disabled port
- Or `errdisable recovery cause dhcp-rate-limit` to enable ErrDisable Recovery for ports disabled by DHCP Snooping rate limiting

