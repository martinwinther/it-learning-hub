# Dynamic Host Configuration Protocol

## Overview

Dynamic Host Configuration Protocol (DHCP) automates the assignment of IP addresses, default gateways, and other network configuration information to hosts. A host is any device that sends and receives packets over a network—any device with an IP address. Manually configuring thousands of hosts in a large network is not feasible, and even in small networks, automating host configuration makes using the network much simpler for end users. DHCP uses a client-server model in which clients send requests to a DHCP server, which then leases an IP address to each client along with other settings such as the default gateway and DNS server addresses.

## Why DHCP is Needed

### Network Configuration Parameters

For a host to communicate over a network, it typically needs:

- **IP address**: Acts as host's identity on network, providing address to send and receive packets
- **Netmask**: Allows host to determine which IP addresses belong to its LAN and which do not
- **Default gateway**: Enables host to communicate with devices in different LANs
- **DNS server address**: Translates human-readable domain names into IP addresses

### Problems with Manual Configuration

- Not scalable: Manually configuring thousands of hosts is time consuming and error prone
- Typos are inevitable with manual configuration
- Not flexible: In dynamic environments where hosts frequently move between networks, manual configuration becomes impractical
- DHCP automates host configuration in way that is both accurate and scalable

## DHCP Fundamentals

### Client-Server Model

- DHCP uses client-server model
- Clients send requests to DHCP server
- Server leases IP address to each client
- Server provides other settings such as default gateway and DNS server
- DHCP is stateful: server keeps track of addresses it leases to clients
- Contrast to SLAAC (Stateless Address Autoconfiguration), which is stateless

### DHCP Ports

- DHCP servers source messages from and listen on UDP port 67
- DHCP clients source messages from and listen on UDP port 68
- Both use reserved ports (unlike most protocols where only server uses reserved port)
- DHCP based on older protocol called Bootstrap Protocol (BOOTP)
- BOOTP also used UDP ports 67 and 68
- Extended ACL keywords: bootps (UDP 67) and bootpc (UDP 68)

## DHCP Leasing Process (DORA)

### Four-Step Process

The DHCP leasing process consists of four steps, remembered as DORA:

1. **DISCOVER**: Client locates DHCP servers and announces it needs IP address
2. **OFFER**: Server offers client an IP address (and other settings)
3. **REQUEST**: Client accepts the offered IP address
4. **ACK (Acknowledgment)**: Server confirms and finalizes the lease

### DISCOVER Message

- Sent by client to locate any DHCP servers on LAN
- Client doesn't have IP address yet, so sources packet from 0.0.0.0
- Client doesn't know IP address of any DHCP servers, so sends to 255.255.255.255 (broadcast)
- When host first connects to switch port, takes 30 seconds for port to move through STP states
- PortFast can be configured to skip to forwarding state immediately

### OFFER Message

- Sent by DHCP server in response to DISCOVER
- Usually sent as unicast packet destined for IP address offered to client
- Some client devices unable to accept unicast packets until DHCP process complete
- Such clients indicate so in DISCOVER message, and server broadcasts OFFER instead
- If multiple DHCP servers in LAN, all will send OFFER messages
- Client typically accepts first OFFER it receives

### REQUEST Message

- Sent by client to accept offered IP address
- Again sourced from 0.0.0.0
- Client broadcasts this message to all hosts in LAN
- Reason: accommodate situations where multiple DHCP servers sent OFFERs
- If server sees another server's OFFER was accepted, it knows its own OFFER was not
- Server whose OFFER was not accepted will free up its offered IP address

### ACK Message

- Sent by server to confirm and finalize lease
- Can be unicast or broadcast, depending on client capabilities
- After receiving ACK, lease process is complete
- Client can start using assigned IP address and other parameters

### Lease Renewal

- DHCP leases are typically not permanent
- Lease time can vary from few hours (public Wi-Fi) to 24 hours or more (home networks)
- Client must renew lease to maintain network connectivity
- Client sends REQUEST message to server it is leasing address from
- Unlike REQUEST in DORA process, this is unicast message
- Client typically starts renewal process when 50% of lease time has expired
- Server responds with ACK message, effectively renewing lease

## DHCP Server Configuration

### Excluded Addresses

- Use `ip dhcp excluded-address low-ip high-ip` to specify range of IP addresses that will not be leased
- Common to reserve some IP addresses for hosts with statically assigned addresses
- Example: server's IP address should be manually configured rather than leased via DHCP
- No need to exclude network address, broadcast address, or router's own address
- Router knows not to lease these addresses to clients

### DHCP Pool Configuration

- Create DHCP pool with `ip dhcp pool name`
- Command brings you to DHCP config mode
- Configure range of IP addresses and other parameters to be leased to clients

### Network Address Range

- Use `network network-address {netmask | /prefix-length}` to configure range of IP addresses
- Can specify netmask (255.255.255.0) or prefix length (/24)
- Example: `network 10.0.0.0 /24` or `network 10.0.0.0 255.255.255.0`
- Router won't lease network address, broadcast address, router's own address, or excluded addresses

### Default Gateway

- Use `default-router ip-address` to specify default gateway clients should use
- More common term is default gateway, but command uses default-router
- Example: `default-router 10.0.0.1` (router's own IP address)

### DNS Server

- Use `dns-server ip-address` to specify DNS server(s) clients should send DNS queries to
- Can specify up to eight DNS servers with space between each
- Example: `dns-server 10.0.0.1 8.8.8.8`

### Domain Name

- Use `domain-name domain-name` to tell clients their domain name
- Example: PC1 will know its full domain name is pc1.jeremysitlab.com
- Makes it easier for computers in same domain to communicate using hostnames
- User can ping pc2 instead of pc2.jeremysitlab.com

### Lease Duration

- Use `lease {days hours minutes | infinite}` to specify duration of leases
- Default is 24 hours
- Example: `lease 0 5 30` specifies lease time of 5 hours and 30 minutes
- Might want to reduce for networks with lots of clients coming and going
- Ensures addresses remain available for new clients

### Verification

- Use `show ip dhcp binding` to see active DHCP leases
- Shows IP address, client ID/hardware address, lease expiration, and type
- Client ID typically includes prefix 01 (Ethernet) plus MAC address
- Use `clear ip dhcp binding {* | ip-address}` to clear bindings
- `*` clears all bindings; `ip-address` clears specific binding

## Address Conflict Detection

### Conflict Detection Process

- Before leasing IP address, server should check that address is unique
- Cisco IOS DHCP servers send pings to detect address conflicts
- After server receives DISCOVER message, it decides which address to lease
- Before sending OFFER message, server pings the IP address it intends to lease
- If no reply, address is unique
- If reply received, address is not unique; another host is already using it

### Conflict Resolution

- Address is marked as conflict and removed from DHCP pool
- Server will select different IP address to lease to client
- Use `show ip dhcp conflict` to view address conflicts
- Won't assign conflicted address to any clients until conflict is resolved
- After resolving conflict, must clear it from conflict table
- Use `clear ip dhcp conflict ip-address` to clear specific conflict
- Use `clear ip dhcp conflict *` to clear all conflicts

## DHCP Client Configuration

### Router as DHCP Client

- Network infrastructure devices typically use static IP addresses
- Common exception: router's ISP-connected interface can use DHCP
- Allows router to learn IP address from ISP and automatically install default route
- Use `ip address dhcp` on appropriate interface to configure router as DHCP client
- Router learns both IP address and default route via DHCP
- Verify with `show ip interface interface` and `show ip route`
- DHCP-learned routes use code S (static) in routing table

## DHCP Relay

### Purpose of DHCP Relay

- In larger networks, centralized DHCP server is used instead of each router
- Centralized approach simplifies management and maintains consistent policies
- Problem: DHCP relies on broadcast messages, which only remain within local subnet
- Routers don't forward broadcast messages to other networks
- Solution: DHCP relay agent forwards DHCP clients' broadcast messages as unicast to remote DHCP server

### DHCP Relay Configuration

- Use `ip helper-address server-ip` on interface connected to clients
- Command must be configured on interface that will receive clients' broadcast messages
- Router acts as middleman between DHCP client and remote DHCP server
- Router receives client's broadcast DISCOVER and REQUEST messages
- Router forwards them as unicast packets to DHCP server
- Router receives server's OFFER and ACK messages and forwards them to client
- Verify with `show ip interface interface-name`
- Helper address concept not exclusive to DHCP; other protocols can use helper address

## Verifying IP Settings on Client OS

### Windows

- Use `ipconfig` to view basic IP settings (domain name, IP address/netmask, default gateway)
- Use `ipconfig /all` to view more detailed information
  - Shows physical address (MAC address)
  - Shows DHCP enabled status
  - Shows lease obtained and lease expires times
  - Shows DHCP server and DNS server addresses
- Use `netstat -rn` to view routing table
- `-r` shows routing table; `-n` displays numerical addresses

### macOS

- Use `ifconfig` to view IP settings (similar to Windows ipconfig)
- Shows MAC address, IP address, netmask, and broadcast address
- Use `netstat -rn` to view routing table (same command as Windows)
- Output format slightly different from Windows

### Linux

- Linux is family of OSs based on Linux kernel; each is called Linux distribution
- Some distributions support net-tools by default:
  - `ifconfig`: View interface information
  - `route`: View routing table
- Other distributions use iproute2:
  - `ip addr`: Equivalent to ifconfig
  - `ip route`: Equivalent to route

## Real-World Applications

- **Home networks**: Routers typically preconfigured as DHCP servers
- **Enterprise networks**: Centralized DHCP servers for consistent management
- **Public Wi-Fi**: Short lease times to ensure addresses available for new clients
- **ISP connections**: Routers learn IP addresses and default routes from ISP via DHCP
- **Dynamic environments**: Automatically configure devices that move between networks
- **Large networks**: DHCP relay enables centralized DHCP server management

## Troubleshooting

### Common Issues

- **Client not receiving IP address**: Verify DHCP server is configured and reachable
- **Wrong IP address assigned**: Check DHCP pool configuration and excluded addresses
- **Address conflicts**: Check for manually configured addresses in DHCP pool range
- **Lease not renewing**: Verify server is reachable and lease time is appropriate

### Troubleshooting Steps

1. Verify DHCP server configuration: `show ip dhcp pool`
2. Check active leases: `show ip dhcp binding`
3. Check for conflicts: `show ip dhcp conflict`
4. Verify helper address: `show ip interface` (for relay configuration)
5. Test client connectivity: Ping DHCP server from client
6. Check client IP settings: Use OS-specific commands (ipconfig, ifconfig, ip addr)

## Best Practices

- Use centralized DHCP server in larger networks
- Reserve IP addresses for servers and network devices (excluded addresses)
- Configure appropriate lease times for network type
- Use DHCP relay for centralized management
- Monitor DHCP bindings regularly
- Document DHCP server addresses and configurations
- Use helper addresses on correct interfaces (connected to clients)
- Configure multiple DNS servers for redundancy
- Set appropriate domain names for internal networks
- Clear conflicts promptly after resolution

## Summary

- DHCP automates assignment of IP addresses, default gateways, and other network configuration
- DHCP uses client-server model; servers listen on UDP 67, clients on UDP 68
- DORA process: DISCOVER (client locates servers), OFFER (server offers address), REQUEST (client accepts), ACK (server confirms)
- DISCOVER and REQUEST sourced from 0.0.0.0 and broadcast to 255.255.255.255
- OFFER and ACK can be unicast or broadcast depending on client capabilities
- Leases are not permanent; clients renew when 50% of lease time expires
- Configure DHCP server with `ip dhcp pool name`, then `network`, `default-router`, `dns-server`, etc.
- Use `ip dhcp excluded-address` to reserve addresses for static configuration
- Use `show ip dhcp binding` to view active leases
- Servers detect address conflicts by pinging addresses before offering them
- Use `ip address dhcp` to configure router interface as DHCP client
- Use `ip helper-address server-ip` to configure router as DHCP relay agent
- Verify IP settings on Windows with `ipconfig` and `ipconfig /all`
- Verify IP settings on macOS with `ifconfig`
- Verify IP settings on Linux with `ifconfig`/`route` (net-tools) or `ip addr`/`ip route` (iproute2)

