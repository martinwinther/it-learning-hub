# Dynamic ARP Inspection

## Overview

Address Resolution Protocol (ARP) maps IPv4 addresses to MAC addresses on a local segment. ARP is simple and has no authentication, which makes it vulnerable to attacks. Dynamic ARP Inspection (DAI) is a Layer 2 security feature on Cisco switches that inspects ARP messages on untrusted ports and drops those that do not match trusted information. DAI is closely tied to DHCP snooping and is part of CCNA topic 5.7.

## ARP basics for DAI

### ARP fields

ARP messages contain these key fields:

- Sender MAC address
- Sender IP address
- Target MAC address
- Target IP address

ARP requests are broadcasts. The target IP in the request identifies the intended recipient. ARP is carried directly in Ethernet frames and does not use an IP header.

### ARP exchange summary

Typical ARP process between two devices:

- Host sends an ARP request as a broadcast for the target IP
- Target learns the sender mapping from the request
- Target replies with a unicast ARP reply
- Sender learns the target mapping from the reply
- Both devices now have IP to MAC mappings in their ARP tables

DAI focuses on validating the sender information in these ARP messages.

## ARP poisoning

### ARP poisoning attack

ARP poisoning overwrites legitimate ARP entries with attacker supplied entries.

Basic flow:

- Legitimate ARP exchange occurs between two devices
- Attacker sends forged ARP replies with its own MAC address and a victim IP address
- Victims update their ARP tables with the attacker MAC for the victim IP
- Traffic intended for the real device is sent to the attacker instead

This enables man in the middle attacks and breaks confidentiality. Gratuitous ARP (GARP) replies are often used for poisoning because they do not require a preceding request.

### Limits of other features

Existing features alone do not stop ARP poisoning:

- Port security
  - Limits number of MAC addresses on a port
  - ARP poisoning typically uses a single MAC address
- DHCP snooping
  - Inspects DHCP messages only
  - Does not inspect ARP traffic

DHCP snooping does build a binding table of valid IP to MAC to interface mappings. DAI uses that table as a trusted source.

## Enabling DAI

### Global and VLAN configuration

DAI operates per VLAN. It must be enabled globally and on selected VLANs.

Commands:

- Global enable:
  - `ip arp inspection vlan <vlan-list>`
- Examples:
  - `ip arp inspection vlan 1-4094`
  - `ip arp inspection vlan 2-5,7,9,2028`

Verification:

- `show ip arp inspection`
  - Shows enabled VLANs
  - Shows operational state
  - Lists validation settings

### Relationship with DHCP snooping

DAI commonly relies on the DHCP snooping binding table.

- DHCP snooping learns IP, MAC, VLAN, and interface for DHCP clients
- DAI compares ARP sender fields against this binding table
- DAI without DHCP snooping is possible but uncommon on access switches

DHCP snooping should normally be configured and stable before enabling DAI.

## Trusted and untrusted ports

### Trust model

DAI classifies switch ports as trusted or untrusted.

- Trusted ports
  - ARP messages received are forwarded without DAI inspection
- Untrusted ports
  - ARP messages are inspected
  - Messages that fail checks are dropped

Default state:

- All ports are untrusted by default when DAI is enabled

General guidelines:

- Access ports toward end hosts: untrusted
- Ports toward infrastructure devices such as routers and switches: trusted

These guidelines differ slightly from DHCP snooping, where trust is based on direction toward DHCP servers and relays.

### Configuring trusted ports

Interface configuration:

- Trust a port:
  - `ip arp inspection trust`
- Return to untrusted:
  - `no ip arp inspection trust`

Verification:

- `show ip arp inspection interfaces`
  - Lists trust state
  - Shows rate limiting values

Incorrect trust settings either expose the network to poisoning or block valid ARP traffic.

## DAI inspection process

### Basic inspection logic

On untrusted ports, DAI inspects ARP requests and replies.

For each ARP message:

- Read ARP sender MAC and sender IP
- Look for a match in the DHCP snooping binding table
- If a matching entry is found:
  - ARP message is forwarded
- If no match is found:
  - ARP message is dropped

Binding table fields used:

- MAC address
- IP address
- VLAN
- Interface

### Static IP addresses

Devices with statically configured IP addresses do not create DHCP snooping bindings. Their ARP messages will not match the binding table when received on untrusted ports.

Examples:

- Switch SVIs
- Routers with static addresses
- Servers with static IP configurations

For these devices, either:

- Trust the ports connected to them, or
- Use ARP ACLs to define static IP to MAC mappings

ARP ACLs are beyond CCNA scope. For exam purposes, remember that ports to infrastructure devices with static IPs should be trusted.

## Additional validation checks

### Validation options

DAI can perform optional checks beyond the binding table lookup. These are configured with:

- `ip arp inspection validate <options>`

Options:

- `src-mac`
  - Compares Ethernet source MAC and ARP sender MAC
  - Drops messages where they differ
- `dst-mac`
  - Compares Ethernet destination MAC and ARP target MAC in ARP replies
  - Drops messages where they differ
- `ip`
  - Checks ARP sender and target IP fields for invalid or unexpected addresses such as `0.0.0.0` or `255.255.255.255`

All validation options are disabled by default.

Example enabling all checks:

- `ip arp inspection validate src-mac dst-mac ip`

Verification:

- `show ip arp inspection`
  - Lists enabled validation checks

Enabling additional checks increases CPU work but provides stronger spoofing protection.

## DAI rate limiting

### Default rate limits

DAI can rate limit ARP messages per interface to protect the switch CPU.

Defaults:

- Untrusted ports
  - Limit of 15 packets per second
- Trusted ports
  - No default limit

### Configuring rate limits

Interface command:

- `ip arp inspection limit rate <rate> [burst interval <seconds>]`

Examples:

- `ip arp inspection limit rate 20`
- `ip arp inspection limit rate 40 burst interval 2`

Notes:

- `rate` is packets per second averaged over the burst interval
- Longer burst intervals allow short bursts without exceeding the configured average

### When rate is exceeded

If ARP traffic exceeds the configured limit on a port:

- The switch places the interface into an error disabled state
- Traffic on that interface stops

Recovery methods:

- Manual:
  - Shut and reopen the interface:
    - `shutdown`
    - `no shutdown`
- Automatic:
  - Enable errdisable recovery for ARP inspection:
    - `errdisable recovery cause arp-inspection`

For most access ports, the default 15 packets per second is adequate and does not need adjustment.

## Troubleshooting notes

- ARP messages blocked on access ports:
  - Check whether the port is trusted or untrusted
  - Confirm that the device has a binding in the DHCP snooping table
- Static devices failing ARP:
  - Ensure ports to routers or statically addressed servers are trusted
  - Consider ARP ACLs if trust is not appropriate
- Ports error disabled:
  - Check `show interfaces status` and `show logging` for ARP inspection messages
  - Verify rate limits with `show ip arp inspection interfaces`
- High CPU usage:
  - Review validation settings and traffic levels
  - Use `show processes cpu` to confirm load

## Quick review

- ARP provides IP to MAC mapping on local segments but is easy to spoof.
- DAI inspects ARP messages on untrusted ports and uses the DHCP snooping binding table to decide whether to forward or drop them.
- All ports are untrusted by default when DAI is enabled. Access ports stay untrusted, links to infrastructure devices are usually trusted.
- Ports connected to statically addressed devices must be trusted or covered by ARP ACLs.
- Additional validation options `src-mac`, `dst-mac`, and `ip` strengthen protection against spoofing.
- DAI includes per port rate limiting, with a default of 15 packets per second on untrusted ports and no limit on trusted ports.
- Exceeding the rate limit causes the port to enter an error disabled state and may require manual or configured automatic recovery.
