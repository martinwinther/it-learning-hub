# Port Security

## Overview

Connections to an external network, such as the public internet, are obvious security concerns. However, internal network threats should not be overlooked. It could be a malware-infected device—an external threat from the internet that has taken hold in the internal network. Or it could be a malicious user; no one wants to view their own coworkers with suspicion, but ignoring such possibilities is asking for trouble. Given these concerns, securing the points where users connect to the network—switches—is paramount. Port Security is a feature of Cisco switches that adds a layer of security to a switch's MAC address-learning process. Specifically, Port Security allows you to set a limit on the number of unique MAC addresses that can be learned on each port, and it defines actions to be taken if that limit is exceeded.

## Port Security Fundamentals

### Default MAC Address Learning

- By default, number of MAC addresses that switch can learn on port is limited only by maximum size of switch's MAC address table
- Typically in range of few thousand to tens of thousands of MAC addresses
- However, this default behavior is vulnerability that can potentially be exploited

### DHCP Exhaustion Attack

- In DHCP exhaustion attack, attacker sends countless DHCP DISCOVER messages with spoofed MAC addresses
- To exhaust DHCP server's pool of available addresses
- Preventing legitimate user devices from getting IP addresses
- This is example of spoofing attack

### MAC Flooding Attack

- Another type of attack that involves spoofed MAC addresses is MAC flooding attack
- Which attempts to fill up switch's MAC address table with spoofed addresses
- With full MAC address table, switch is unable to learn legitimate MAC addresses of hosts in LAN
- To understand effect of this, recall how switch forwards and floods frames
- When switch receives unicast frame (frame destined for single host's MAC address), switch will look for matching entry in its MAC address table
- If it finds matching entry, it will forward frame out of port specified in entry
- However, if switch doesn't find matching entry, switch will flood frame out of all ports (in same VLAN) except port frame was received on
- If switch can't learn host's MAC address because switch's MAC address table is full, result is that switch will always flood frames that are destined for that host
- This allows attacker to receive copies of those frames
- With regard to CIA triad, this harms confidentiality of communications between hosts
- Although DHCP exhaustion and MAC flooding are separate attacks with different goals, MAC flooding is often side effect of DHCP exhaustion
- Thousands of spoofed DHCP DISCOVER messages can result in MAC flooding

### Port Security Protection

- Port Security can mitigate against both of these attack types
- By limiting number of MAC addresses switch can learn on port
- And taking action if that number is exceeded

## Basic Port Security Configuration

### Enabling Port Security

- Port Security, at its most basic, can be configured with single command in interface config mode: `switchport port-security`
- Once switch detects multiple unique MAC addresses on port, port transitions to error-disabled state
- This action effectively blocks all incoming and outgoing frames on that port

### Port Requirements

- If you try to enable Port Security on switch port with default settings, command will be rejected
- Switch won't allow Port Security on dynamic port (one that uses DTP—it hasn't been explicitly set to access or trunk mode)
- Must first configure port as access or trunk port
- Use `switchport mode access` to configure port as access port
- Then can enable Port Security with `switchport port-security`

### Verifying Port Security

- To confirm Port Security settings of port, use `show port-security interface interface` command
- Shows Port Security status, port status, violation mode, aging settings, maximum MAC addresses, total MAC addresses, and security violation count

### Default Settings

- By default, Port Security-enabled port can only receive frames from one unique MAC address
- Anything more will trigger violation
- Default action when violation occurs is to error-disable port
- MAC address learned on Port Security-enabled port is called secure MAC address

### Port Security Violation

- When switch receives frame with different MAC address on Port Security-enabled port, violation occurs
- Switch will display Syslog messages indicating that Port Security violation occurred
- Port status will change to Secure-shutdown, meaning it has been disabled by Port Security
- When port is disabled, all dynamically learned MAC addresses on port are forgotten
- Including secure MAC addresses
- However, output still shows MAC address that was most recently seen on that port
- This is MAC address that triggered Port Security violation
- Security Violation Count will increment each time port is disabled by Port Security

## Error-Disabled Ports

### Reenabling Ports

- This isn't first time we've seen error-disabled ports
- First time was in Spanning Tree Protocol (STP) when we covered BPDU Guard
- Feature that error-disables port if it receives STP Bridge Protocol Data Units (BPDUs)
- And in Power Policing, which disables port if PoE-powered device draws too much power
- Just like in those previous examples, can reenable error-disabled port by first disabling port with `shutdown` and then reenabling it with `no shutdown`
- However, if underlying issue causing error-disabled state is not addressed, port will be disabled again almost immediately
- Should always address underlying issue causing error-disabled state before reenabling port

### ErrDisable Recovery

- In addition to manually reenabling error-disabled ports, there is feature called ErrDisable Recovery that does it automatically
- ErrDisable Recovery is disabled by default, but can be enabled on per-cause (also called per-reason) basis
- Cause refers to event that caused port to be error-disabled (BPDU Guard, Power Policing, Port Security, etc.)
- Can use `show errdisable recovery` to verify status of ErrDisable Recovery
- ErrDisable Recovery works by automatically reenabling error-disabled port after preset duration
- Default timer is 300 seconds
- To enable ErrDisable Recovery for ports disabled by particular cause, use `errdisable recovery cause cause` command in global config mode
- Keywords for causes we have covered:
  - `bpduguard` (BPDU Guard)
  - `inline-power` (Power Policing)
  - `psecure-violation` (Port Security)
- ErrDisable Recovery is convenient feature for reenabling error-disabled ports
- But keep in mind that you still need to solve problem that caused port to be error-disabled in first place
- If not, port will be disabled again after recovering

## Configuring Maximum MAC Addresses

### Multiple MAC Address Scenarios

- By default, Port Security-enabled port can only receive frames from one unique MAC address
- However, there are some scenarios that require switch port to learn multiple MAC addresses on single port
- Example: port connected to another switch with its own connected hosts
- As those hosts communicate over network, switch will learn their MAC addresses on that port
- Port Security default of single MAC address isn't enough in this situation
- Another example: port connected to IP phone and PC, each with its own MAC address
- Switch needs to be able to receive frames from both devices
- So Port Security default of one MAC address doesn't work here either

### Configuring Maximum

- Use `switchport port-security maximum maximum` to increase maximum number of MAC addresses allowed on port before violation is triggered
- Example: `switchport port-security maximum 8` allows switch to learn up to eight unique MAC addresses on port
- Appropriate number depends on how many hosts are connected to other switch
- Example: `switchport port-security maximum 2` increases maximum number of MAC addresses to two
- For port connected to IP phone and PC
- Can use `show port-security` to view information about all Port Security-enabled ports
- Such as maximum number of MAC addresses allowed on each port

## Static Secure MAC Addresses

### Dynamic vs Static Secure MAC Addresses

- Examples we have looked at so far are dynamic secure MAC addresses
- Secure MAC addresses that are dynamically learned
- But Port Security allows you to control not only how many MAC addresses are allowed on port
- But also exactly which MAC addresses are allowed
- Can do this by manually configuring static secure MAC addresses

### Configuring Static Secure MAC Addresses

- Might want to configure static secure MAC addresses to control exactly which devices can connect to which ports
- Example: server connected to switch port, and no other devices are allowed to connect to that port
- Command to configure static secure MAC address is `switchport port-security mac-address mac-address`
- If you issue command as is, static secure MAC address will be configured in access VLAN of port
- However, to configure static secure MAC address in voice VLAN—MAC address of IP phone—add `vlan voice` keywords to end of command
- Dynamic and static secure MAC addresses both count toward maximum
- If maximum is two addresses, and you configure one static secure MAC address, that means that only one dynamic MAC address can be learned on port
- There can be mix of static and dynamic secure MAC addresses on same port

### Viewing Secure MAC Addresses

- Like any other MAC addresses learned by switch, secure MAC addresses appear in switch's MAC address table
- Can view with `show mac address-table`
- However, to view only secure MAC addresses, can add `secure` keyword
- Example: `show mac address-table secure`
- One confusing fact about secure MAC addresses in MAC address table: they are all listed as STATIC
- Regardless of whether they were dynamically learned or statically configured
- Instead, better option to view secure MAC addresses is `show port-security address`
- This command lists static secure MAC addresses as SecureConfigured and dynamic secure MAC addresses as SecureDynamic

## Violation Modes

### Three Violation Modes

- By default, Port Security-enabled port will be error-disabled if violation occurs
- This is because of default violation mode: shutdown
- However, there are two other violation modes that can be configured on per-port basis: restrict mode and protect mode

### Shutdown Mode

- With default shutdown violation mode enabled, switch error-disables port if violation occurs
- Effectively shutting down port
- In some cases, this reaction might be bit extreme
- Entire port becomes nonoperational
- Example: if port connects to server providing essential service, disabling entire port might not be ideal choice
- Despite it being most secure option

### Restrict Mode

- Restrict violation mode is less extreme
- Instead of error-disabling port, it only discards frames that violate MAC address limit
- Port remains up
- If port's maximum is one MAC address, frames from its learned secure MAC address are allowed
- But frames from other MAC addresses are discarded (but port is not error-disabled)
- Restrict mode increments violation counter for each violating frame
- Furthermore, restrict mode generates Syslog/SNMP messages
- Whereas protect silently discards violating frames without incrementing counter or generating any messages

### Protect Mode

- Third mode, protect, operates similarly to restrict mode
- Port with protect mode enabled will not be error-disabled if violation occurs
- Port will only discard violating frames
- Difference between these two modes is that protect mode silently discards violating frames
- But restrict mode increments violation counter for each violating frame
- And also generates Syslog messages and SNMP Traps/Informs to notify you of violation
- Shutdown mode also increments violation counter and generates notification messages
- But only when first violating frame is received
- After port has been error-disabled, all frames are simply ignored

### Configuring Violation Modes

- Use `switchport port-security violation mode` to configure each port's violation mode
- Protect mode is generally not recommended
- If Port Security violation occurs, it's better to receive notification (i.e., SNMP Trap) so you can take any necessary action
- Such as disconnecting device that triggered violation
- Choice between shutdown mode and restrict mode depends on how drastic action you want switch to take when violation occurs
- Shutdown mode is more secure because it prevents all traffic from being sent or received by port if violation occurs
- But restrict mode is less disruptive to legitimate network traffic

## Secure MAC Address Aging

### Default Aging Behavior

- We covered topic of MAC aging in chapter on Ethernet LAN switching
- To recap, dynamic MAC addresses are automatically removed (or "aged out") from MAC address table using 5-minute timer
- This timer resets whenever frame from corresponding MAC address is received
- But if frame from that MAC address isn't received for 5 minutes (allowing timer to count down to 0), entry is aged out of table
- This ensures that switch's MAC address table remains up to date and doesn't fill up with stale entries for devices that are no longer connected to LAN
- However, dynamic secure MAC addresses behave differently
- Unlike their regular counterparts, they don't age out by default
- By default, secure MAC address remains in table indefinitely as long as port it was learned on stays up
- Once port has learned its maximum number of secure MAC addresses, no more MAC addresses will be allowed on that port

### Configuring Aging Time

- Can change this behavior by enabling secure MAC address aging on per-port basis
- With `switchport port-security aging time minutes` command
- Example: `switchport port-security aging time 5` configures aging time of 5 minutes on port
- With this configuration, secure MAC addresses learned on port will be removed from table after 5 minutes
- Making port available for learning new secure MAC address
- This means that port isn't indefinitely "locked" to specific MAC address
- Creating balance between maintaining network security and allowing for dynamic changes in network environment

### Aging Types

- Even with aging enabled, aging behavior of secure MAC addresses is still different from that of regular MAC addresses
- Those learned on ports without Port Security
- That's because of default aging type, which determines how secure MAC addresses age out
- Default aging type is absolute
- This means that after secure MAC address is learned, aging timer starts
- And MAC address will be removed after timer expires, even if switch continues receiving frames from same MAC address
- In other words, timer doesn't reset upon receiving new frames from same MAC address
- However, can switch to different aging type—inactivity—to change this behavior on per-port basis
- Use `switchport port-security aging type inactivity` to enable inactivity aging type
- In inactivity mode, aging timer will reset if frame from secure MAC address is received
- Similar to regular dynamic MAC addresses
- Absolute aging type forces switch to regularly relearn its secure MAC addresses
- Inactivity aging type, on other hand, allows switch to keep secure MAC addresses in its MAC address table as long as it regularly receives frames from those addresses

### Static Secure MAC Address Aging

- As mentioned in previous note, static MAC addresses, which are manually configured (with `mac address-table static` command), do not age out
- Just as they are manually configured, they must be manually removed
- Same is true of static secure MAC addresses by default
- However, this behavior can be changed on per-port basis
- With `switchport port-security aging static` command in interface config mode
- Enabling static secure MAC address aging is rare
- Generally, if you manually configure static secure MAC address, you don't want it to be automatically removed
- However, static aging could be used to configure static secure MAC address for limited time without needing to manually remove address afterward
- Aging type has major effect on how this works: do you want static address to be removed after certain period of time or only after device stops communicating?

## Sticky Secure MAC Addresses

### Sticky MAC Address Overview

- Sticky secure MAC addresses offer middle ground between dynamic and static secure MAC addresses
- They are dynamically learned but are automatically inserted into running-config
- And retained even if port goes down
- Sticky secure MAC addresses can be useful in situations where you want to combine flexibility of dynamic secure MAC addresses with persistence of static secure MAC addresses
- Example: perhaps security policy states that only intended devices can access certain ports
- Should not be able to disconnect one device from port and connect with another
- Sticky MAC address learning can facilitate that without requiring manual configuration of each MAC address on each port
- Automating process and reducing administrative overhead

### Configuring Sticky MAC Addresses

- To enable sticky secure MAC address learning, use `switchport port-security mac-address sticky` command in interface config mode
- This command turns all current and future dynamically learned secure MAC addresses on port into sticky addresses
- Automatically adding them to running-config
- Sticky secure MAC addresses cannot be aged out
- If you disable sticky learning on port, all sticky addresses on port will be converted back to dynamic addresses

### Secure MAC Address Persistence

- When port that has learned dynamic secure MAC addresses goes down, those addresses are forgotten
- When port comes back up, it is free to learn new dynamic secure MAC address (or addresses, depending on limit)
- Static and sticky secure MAC addresses, on other hand, are retained in running-config
- Persisting even when their associated port goes down

## Real-World Applications

- **Network security**: Protect against MAC flooding and DHCP exhaustion attacks
- **Access control**: Control which devices can connect to specific switch ports
- **Device management**: Ensure only authorized devices can access network
- **Server protection**: Protect server ports from unauthorized device connections
- **IP phone deployment**: Allow IP phones and PCs to share single port while maintaining security

## Troubleshooting

### Common Issues

- **Port error-disabled**: Check for Port Security violations and address underlying issue
- **Legitimate devices blocked**: Verify maximum MAC address count is appropriate for port
- **Sticky addresses not persisting**: Verify sticky learning is enabled and configuration is saved
- **Aging not working**: Check aging time and aging type configuration

### Troubleshooting Steps

1. Verify Port Security status: `show port-security interface interface`
2. Check violation count: Review security violation count and last source address
3. Verify maximum addresses: Ensure maximum is appropriate for port's use case
4. Check violation mode: Verify violation mode is appropriate for network requirements
5. Review secure MAC addresses: Use `show port-security address` to view all secure MAC addresses
6. Test connectivity: Verify legitimate devices can connect after addressing issues

## Best Practices

- Configure Port Security on all access ports
- Set appropriate maximum MAC address count for each port's use case
- Use static secure MAC addresses for critical devices like servers
- Use sticky MAC addresses for user ports to automate configuration
- Configure appropriate violation mode (shutdown for high security, restrict for flexibility)
- Enable aging on ports where device changes are expected
- Use inactivity aging type for ports with active devices
- Monitor Port Security violations regularly
- Document Port Security configuration for each port
- Test Port Security configuration in lab before production deployment

## Summary

- Port Security adds layer of security to switch's MAC address-learning process by setting limit on number of unique MAC addresses that can be learned on each port and defining action to be taken if that limit is exceeded
- By default, number of MAC addresses that can be learned on port is limited only by maximum size of switch's MAC address table
- This default behavior makes switch vulnerable to attacks such as DHCP exhaustion or MAC flooding
- Which attempts to fill up target switch's MAC address table with spoofed MAC addresses
- If switch's MAC address table is full, it can't learn any more MAC addresses
- If it can't learn host's MAC address, switch will flood frames destined for that host
- Port Security can be enabled on port with `switchport port-security`
- Port Security cannot be enabled on dynamic port—port that uses DTP
- Port must be configured in access or trunk mode
- Use `show port-security interface interface` to confirm Port Security settings of port
- MAC address learned on Port Security-enabled port is called secure MAC address
- By default, Port Security-enabled port can only learn one MAC address
- If frame from another MAC address is received on port, Port Security violation occurs
- Default action when violation occurs is to error-disable port
- When port goes down, all dynamically learned MAC addresses on port are forgotten (cleared from MAC address table), including secure MAC addresses
- Error-disabled port can be manually reenabled with `shutdown` followed by `no shutdown`
- Can use ErrDisable Recovery to automatically reenable error-disabled ports
- Use `show errdisable recovery` to check status of ErrDisable Recovery
- ErrDisable Recovery automatically reenables error-disabled port after preset duration; default timer is 300 seconds
- ErrDisable Recovery is disabled by default, but can be enabled on per-cause basis with `errdisable recovery cause cause` in global config mode
- Can modify ErrDisable Recovery timer with `errdisable recovery interval seconds` in global config mode
- Use `switchport port-security maximum maximum` to increase maximum number of MAC addresses allowed on port before violation is triggered
- Use `show port-security` to view information about all Port Security-enabled ports
- Dynamically learned secure MAC addresses are dynamic secure MAC addresses
- Statically configured secure MAC addresses are static secure MAC addresses
- Use `switchport port-security mac-address mac-address` to configure static secure MAC address on port
- Add `vlan voice` keywords if necessary to specify that MAC address is in port's voice VLAN
- There can be mix of static and dynamic secure MAC addresses on port
- Use `show mac address-table secure` to view secure MAC addresses in MAC address table
- Secure MAC addresses have STATIC type
- Can also use `show port-security address` to view secure MAC addresses
- There are three Port Security violation modes that determine how port reacts to Port Security violation: shutdown, restrict, and protect
- Use `switchport port-security violation mode` to configure each port's violation mode
- Default violation mode is shutdown, which error-disables port
- Restrict violation mode doesn't error-disable port if violation occurs; it only discards frames that violate MAC address limit
- Protect violation mode operates similarly to restrict mode
- It only discards violating frames; it doesn't error-disable port if violation occurs
- Difference between restrict and protect modes is that restrict increments violation counter for each violating frame
- Furthermore, restrict mode generates Syslog/SNMP messages, whereas protect silently discards violating frames without incrementing counter or generating any messages
- Secure MAC addresses have aging time of 0 by default, meaning they don't age out
- Use `switchport port-security aging time minutes` to configure aging time of secure MAC addresses
- Default secure MAC address aging type is absolute
- This means that after secure MAC address is learned, aging timer starts, and MAC address will be removed after timer expires, even if switch continues receiving frames
- Second aging type is inactivity
- With this mode configured, aging timer will be refreshed each time switch receives frame from corresponding MAC address
- This is similar to behavior of regular dynamic MAC addresses
- Use `switchport port-security aging type type` to modify aging type on per-port basis
- Regular static MAC addresses do not age out of MAC address table; they must be manually removed
- Same is true of secure static MAC addresses by default
- Aging of secure static MAC addresses can be enabled on per-port basis with `switchport port-security aging static`
- Sticky secure MAC addresses offer middle ground between dynamic and static secure MAC addresses
- They are dynamically learned but are automatically inserted into running-config and retained even if port goes down
- Sticky secure MAC addresses cannot be aged out
- Use `switchport port-security mac-address sticky` to enable sticky address learning on per-port basis
- If you enable it, all current and future dynamically learned secure MAC addresses on port will become sticky
- If you disable sticky learning on port, all sticky addresses on port will be converted back to dynamic addresses

