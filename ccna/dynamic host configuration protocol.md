
# Dynamic Host Configuration Protocol

## Overview

Dynamic Host Configuration Protocol (DHCP) automates assignment of IP addresses and other network parameters to hosts. A DHCP server leases addresses to clients and provides settings such as default gateway and DNS servers. This removes the need for manual IP configuration and reduces errors.

## Why DHCP is used

### Required settings for IPv4 hosts

Typical IPv4 host parameters:

- IP address
- Netmask
- Default gateway
- DNS server address
- Optional: domain name, additional DNS servers

### Problems with manual configuration

- Time consuming and error prone, especially at scale
- Typos and duplicate addresses are common
- Difficult to change addressing schemes
- Not practical for mobile devices and dynamic environments

DHCP centralizes and automates host configuration in a consistent way.

## DHCP fundamentals

### Client server model

- DHCP uses a client server model
- Clients request configuration
- Server assigns an address and options
- Server keeps state about active leases
- Stateless alternatives exist, such as SLAAC for IPv6, but DHCP for IPv4 is stateful

### Ports and transport

- DHCP server
  - Sends from and listens on UDP port 67
- DHCP client
  - Sends from and listens on UDP port 68
- Both sides use well known ports
- DHCP evolved from BOOTP, which used the same ports
- Extended ACL keywords: `bootps` (UDP 67), `bootpc` (UDP 68)

## DHCP leasing process (DORA)

DHCP for IPv4 uses a four step process remembered as DORA.

### DISCOVER

- Client must locate a DHCP server on the local subnet
- Source IP: `0.0.0.0` (client has no address yet)
- Destination IP: `255.255.255.255` (broadcast)
- Sent as soon as the interface is up
- On switches without PortFast, STP delay can slow DHCP start

### OFFER

- DHCP server offers an address and options
- Often sent as unicast to the offered IP address
- Some clients cannot receive unicast before completing DHCP
  - These signal that requirement, and the server uses broadcast instead
- If multiple servers respond, each sends an OFFER
- Client typically accepts the first OFFER received

### REQUEST

- Client accepts one of the offers
- Source IP: `0.0.0.0`
- Destination IP: `255.255.255.255` (broadcast)
- Broadcast allows all servers to see which offer was accepted
- Servers that did not win free their offered address

### ACK

- Server confirms the lease
- May be unicast or broadcast, depending on client capabilities
- When ACK is received, the client starts using the address and other options

### Lease renewal

- Leases have a finite duration
- Length varies by environment
  - Public Wi Fi: shorter leases
  - Enterprise or home: often 24 hours or longer
- Renewal process:
  - Client sends a REQUEST to the original server before lease expiry
  - Typically at 50 percent of the lease time (T1)
  - Server replies with an ACK to extend the lease
- Renewal uses unicast between client and server when possible

## DHCP server configuration (Cisco IOS)

### Excluded addresses

- Prevent DHCP from leasing specific addresses
- Command:
  - `ip dhcp excluded-address low-ip high-ip`
- Common uses:
  - Reserve addresses for statically configured servers and network devices

### DHCP pool

- Create a pool:
  - `ip dhcp pool NAME`
- Configure pool parameters:
  - Network:
    - `network NETWORK {NETMASK | /PREFIX-LENGTH}`
    - Example: `network 10.0.0.0 255.255.255.0` or `network 10.0.0.0 /24`
  - Default gateway:
    - `default-router IP-ADDRESS`
  - DNS servers:
    - `dns-server IP1 [IP2 ... IP8]`
  - Domain name:
    - `domain-name DOMAIN`
  - Lease time:
    - `lease {days hours minutes | infinite}`

Notes:

- Router does not lease:
  - Network address
  - Directed broadcast address
  - Its own interface address
  - Any excluded addresses

### Verification and management

- Show active bindings:
  - `show ip dhcp binding`
- Remove bindings:
  - `clear ip dhcp binding *`
  - `clear ip dhcp binding IP-ADDRESS`
- Check DHCP pools:
  - `show ip dhcp pool`

## Address conflict detection

### Conflict detection

- DHCP server tries to avoid address duplication
- Before sending an OFFER:
  - Server pings the address it plans to lease
  - If no reply, address is assumed free
  - If a reply is received, address is marked as conflicting

- Conflicted addresses:
  - Stored in the conflict table
  - Not offered to clients

### Commands

- Show conflicts:
  - `show ip dhcp conflict`
- Clear conflicts:
  - `clear ip dhcp conflict IP-ADDRESS`
  - `clear ip dhcp conflict *`

## DHCP client on Cisco devices

### Router as DHCP client

- Many infrastructure interfaces use static addressing
- Exception: WAN or ISP facing interfaces often use DHCP
- Interface configuration:
  - `ip address dhcp`
- Router learns:
  - IP address
  - Netmask
  - Default gateway (via default route option)
- Verification:
  - `show ip interface INTERFACE`
  - `show ip route` (DHCP learned default route appears as a static route installed by DHCP)

## DHCP relay

### Purpose

- Centralized DHCP server supports multiple subnets
- DHCP messages are broadcasts that do not cross routers
- DHCP relay forwards client broadcasts as unicast to a remote server

### Configuration

- On the interface that receives client broadcasts:
  - `ip helper-address SERVER-IP`
- Router actions:
  - Receives client DISCOVER and REQUEST broadcasts
  - Forwards them as unicast packets to the configured server
  - Receives server OFFER and ACK
  - Forwards them back toward the client

- Helper address is not exclusive to DHCP
  - Also forwards some other UDP based services by default

### Verification

- `show ip interface INTERFACE`
- Confirms helper addresses and DHCP relay role

## Checking client settings

Exact commands depend on operating system, but basic checks are similar.

- Windows
  - `ipconfig`
  - `ipconfig /all`
- macOS
  - `ifconfig`
  - `netstat -rn`
- Linux
  - `ip addr`
  - `ip route`
  - On some systems: `ifconfig`, `route`

These commands show IP address, mask, gateway, DHCP status, and DNS information.

## Troubleshooting notes

- Client not receiving an address
  - Confirm DHCP server configuration and reachability
  - Check `show ip dhcp pool` and `show ip dhcp binding`
  - Confirm relay configuration with `show ip interface`
- Wrong address range
  - Review pool `network` and excluded addresses
  - Check for overlapping pools
- Address conflicts
  - Check `show ip dhcp conflict`
  - Look for statically assigned addresses inside DHCP ranges
- Lease not renewing
  - Verify server reachability
  - Confirm lease time is appropriate for the environment

## Quick review

- DHCP automates assignment of IPv4 addresses and options using a client server model.
- Servers use UDP 67, clients use UDP 68.
- DORA sequence:
  - DISCOVER: client broadcast from `0.0.0.0` to `255.255.255.255`
  - OFFER: server offers address and options
  - REQUEST: client accepts an offer
  - ACK: server confirms the lease
- Leases expire and must be renewed, usually starting at 50 percent of the lease time.
- On Cisco IOS, DHCP server setup uses:
  - `ip dhcp excluded-address`
  - `ip dhcp pool`
  - `network`, `default-router`, `dns-server`, `domain-name`, `lease`
- Address conflict detection pings candidate addresses and tracks conflicts with `show ip dhcp conflict`.
- A router can act as a DHCP client with `ip address dhcp` and as a DHCP relay with `ip helper-address`.
- Client OS tools such as `ipconfig`, `ifconfig`, and `ip addr` reveal DHCP learned settings for verification.

