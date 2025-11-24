# DHCP Snooping

## Overview

Dynamic Host Configuration Protocol (DHCP) automates IP address assignment for hosts. DHCP is widely used but has weaknesses that can be abused. DHCP snooping is a Layer 2 security feature on Cisco switches that inspects DHCP messages, blocks malicious ones, and builds a table of valid bindings. Only DHCP traffic is affected. Non-DHCP traffic is forwarded normally.

## DHCP-based attacks

### DHCP poisoning

- Attacker connects a rogue DHCP server to the LAN
- Rogue server hands out valid IP addresses but advertises itself as the default gateway
- Traffic from clients is then sent through the attacker
- Attacker can capture or modify traffic before forwarding it to the real router
- This is a man-in-the-middle attack and is similar in effect to ARP poisoning

### DHCP exhaustion (starvation)

- Attacker sends a large number of fake DHCP requests
- Each request uses a different client identifier (for example, different chaddr values)
- DHCP pool is exhausted and legitimate clients cannot obtain addresses
- Often used as a first step before other attacks

Port security cannot stop a rogue DHCP server because all server messages come from a single MAC address. DHCP snooping is the primary protection mechanism for these attacks on switches.

## Enabling DHCP snooping

### Global and VLAN configuration

DHCP snooping inspects DHCP messages as they enter the switch.

Commands:

- Enable globally:
  - `ip dhcp snooping`
- Enable per VLAN:
  - `ip dhcp snooping vlan <vlan-list>`

Notes:

- No effect until at least one VLAN is enabled
- `<vlan-list>` can be a list and ranges, for example `ip dhcp snooping vlan 1,10-20`
- Typical deployments enable DHCP snooping on every VLAN that uses DHCP

### Verification

Key command:

- `show ip dhcp snooping`
  - Global status
  - Enabled VLANs
  - Operational VLANs
  - Interface trust and rate-limit information

## Trusted and untrusted ports

### Concept

DHCP snooping behavior depends on whether an interface is trusted or untrusted.

- All interfaces are untrusted by default
- DHCP messages on untrusted interfaces are inspected and filtered
- DHCP messages on trusted interfaces are allowed without snooping checks

General guideline:

- Ports toward DHCP servers or DHCP relay devices: trusted
- Ports toward end hosts and access networks: untrusted

### Behavior on untrusted ports

On untrusted interfaces, a DHCP snooping switch:

- Drops all DHCP server messages received (OFFER, ACK, NAK)
- Allows only DHCP client messages that pass additional checks
- Populates and uses the DHCP snooping binding table

### Configuring trusted ports

Commands on interface:

- Trust an interface:
  - `ip dhcp snooping trust`
- Remove trust:
  - `no ip dhcp snooping trust`

Verification:

- `show ip dhcp snooping` lists trusted interfaces and rate settings

## DHCP message types

### Client messages

Messages treated as client messages:

- DISCOVER
- REQUEST
- DECLINE
- RELEASE

### Server messages

Messages treated as server messages:

- OFFER
- ACK
- NAK (negative ACK)

For DHCP snooping, it is important to distinguish which side sends which messages. Client messages are allowed on untrusted ports if they pass validation. Server messages are only expected on trusted ports.

## DHCP snooping validation checks

### DISCOVER and REQUEST

For DISCOVER and REQUEST messages on untrusted ports, the switch checks:

- Ethernet source MAC address
- DHCP chaddr (client hardware address field)

Rules:

- If source MAC and chaddr match, the message is allowed
- If they differ and no relay is involved, the message is dropped

Reason:

- Prevents a single host from sending many DISCOVER messages with different chaddr values
- Protects against DHCP exhaustion attacks that try to bypass port security

### RELEASE and DECLINE

RELEASE and DECLINE are sent by clients after obtaining an address.

- DECLINE: client reports that the offered address is already in use
- RELEASE: client informs the server that it no longer needs the address

For these messages on untrusted ports, the switch checks the DHCP snooping binding table:

- IP address must match a binding
- Message must arrive on the same interface and VLAN recorded in the binding

If the checks fail, the message is dropped.

## DHCP snooping binding table

### Purpose

The DHCP snooping binding table is a database of valid DHCP-learned bindings. It is built by observing successful DHCP exchanges between clients and servers.

Information stored per entry:

- Client MAC address
- IP address
- VLAN
- Interface
- Lease information

### Binding table verification

Command:

- `show ip dhcp snooping binding`

Binding entries are used later for:

- Validating RELEASE and DECLINE messages
- Use by other features such as Dynamic ARP Inspection (DAI) and IP Source Guard

## Option 82 and DHCP snooping

### DHCP options

DHCP supports many optional fields called options. Examples:

- Option 3: default gateway
- Option 6: DNS servers
- Option 50: requested IP address

Option 82 is the relay agent information option. It carries information about where the request entered the network, which can help servers make allocation decisions.

### Default option 82 behavior with snooping

When DHCP snooping is enabled on a switch:

- The switch inserts option 82 into client messages received on untrusted ports
- The switch drops DHCP messages received on untrusted ports if they already contain option 82

This default behavior assumes the switch is acting as a DHCP relay agent. On a pure Layer 2 access switch, this can cause problems.

Typical symptom:

- Clients fail to obtain leases
- DHCP snooping binding table remains empty
- Debug messages or logs point to option 82 drops

### Disabling option 82 insertion

On access switches that are not acting as DHCP relay agents, disable option 82 insertion:

- Global command:
  - `no ip dhcp snooping information option`

Important points:

- Configure this on all switches in the path between clients and the DHCP server
- With insertion disabled, relay agents (routers or multilayer switches) can still add option 82 if required

For CCNA, remember that option 82 can break DHCP when snooping is enabled and that disabling insertion often fixes this in simple topologies.

## DHCP snooping rate limiting

### Rate limiting purpose

Inspecting DHCP messages consumes CPU resources. A flood of DHCP traffic can be used as a denial-of-service attack against the switch. DHCP snooping rate limiting reduces this risk.

### Rate limiting configuration

Interface command:

- `ip dhcp snooping limit rate <pps>`

Where:

- `<pps>` is the maximum DHCP packets per second allowed on that interface

Guidelines:

- Lower rates on access ports with a single client
- Higher rates on uplinks carrying many clients
- Cisco commonly recommends no more than 100 pps on untrusted access ports as a starting point

### Exceeding the limit

If an interface receives DHCP messages faster than the configured limit:

- The port is placed into an error-disabled state
- Traffic on that interface stops until it is recovered

Recovery options:

- Manual:
  - `shutdown`
  - `no shutdown`
- Automatic (global):
  - `errdisable recovery cause dhcp-rate-limit`
  - Adjust recovery interval as needed

## Configuration summary

Typical configuration steps on access switches:

1. Enable DHCP snooping globally:
   - `ip dhcp snooping`
2. Enable DHCP snooping on relevant VLANs:
   - `ip dhcp snooping vlan <vlan-list>`
3. Trust interfaces toward legitimate DHCP servers or relay devices:
   - `interface <name>`
   - `ip dhcp snooping trust`
4. Disable option 82 insertion on switches that are not acting as DHCP relay agents:
   - `no ip dhcp snooping information option`
5. Configure rate limiting on untrusted ports (optional but recommended):
   - `ip dhcp snooping limit rate <pps>`

## Quick review

- DHCP snooping is a switch feature that inspects DHCP messages and blocks those from untrusted sources.
- Only DHCP messages are filtered; other traffic is forwarded as usual.
- Interfaces are untrusted by default; ports toward DHCP servers or relays should be set as trusted.
- Client messages (DISCOVER, REQUEST, DECLINE, RELEASE) are allowed on untrusted ports only after validation.
- Server messages (OFFER, ACK, NAK) are allowed only on trusted ports.
- The switch builds a DHCP snooping binding table with MAC, IP, VLAN, and interface information.
- Source MAC and chaddr are compared for DISCOVER and REQUEST messages to prevent exhaustion attacks.
- RELEASE and DECLINE messages are checked against the binding table before being accepted.
- Option 82 insertion is enabled by default when snooping is on and can prevent clients from obtaining addresses if not configured correctly.
- Rate limiting protects the switch CPU from DHCP floods by error-disabling ports that exceed a configured packets-per-second threshold.
