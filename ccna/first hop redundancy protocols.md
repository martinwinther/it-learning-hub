# First Hop Redundancy Protocols

## Overview

First hop redundancy protocols (FHRPs) allow multiple routers to work together to provide a redundant default gateway for hosts in a LAN, minimizing downtime in the event of hardware failures. The default gateway is the first hop in a packet's path to its destination, hence the name. FHRPs eliminate single points of failure for default gateway connectivity, ensuring network reliability and resilience.

## The Problem FHRPs Solve

### Default Gateway Dependency

- End hosts rely on default gateway to reach external destinations
- Default gateway is either manually configured or learned via DHCP
- Hosts use ARP to learn MAC address of default gateway
- If default gateway fails, hosts lose connectivity to external networks

### Redundancy Without FHRP

- Multiple routers may exist but cannot coordinate without FHRP
- Hosts continue using failed router's IP address as default gateway
- Manual reconfiguration of each host is not acceptable in modern networks
- Network must recover automatically with minimal downtime

### FHRP Solution

- Multiple routers share a virtual IP (VIP) address
- VIP is configured as default gateway for hosts in the LAN
- Routers coordinate to provide redundant default gateway
- Failover is transparent to end hosts

## How FHRPs Work

### Virtual IP Address (VIP)

- Shared IP address used by multiple routers in an FHRP group
- Configured as default gateway for hosts in the LAN
- Only one router (active) responds to ARP requests for VIP at a time
- If active router fails, standby router takes over and responds to ARP requests

### Virtual MAC Address

- Shared MAC address used by routers in FHRP group
- Active router replies to ARP requests with virtual MAC address (not its own interface MAC)
- Hosts create ARP table entry mapping VIP to virtual MAC
- Switches learn virtual MAC address on port leading toward active router

### FHRP Groups

- Set of routers configured to use an FHRP is called a group
- Single router can be part of multiple FHRP groups
- Each subnet can have its own FHRP group and VIP
- Useful when LAN has multiple subnets

### Hello Messages

- Routers communicate via multicast hello messages
- Sent at regular intervals
- Used for establishing and maintaining FHRP neighbor relationships
- If router stops receiving hellos from neighbor, assumes neighbor has failed
- Similar mechanism to OSPF neighbor relationships

### Active and Standby Routers

- **Active router**: Serves as default gateway, responds to ARP requests for VIP
- **Standby router**: Ready to take over if active router fails
- Note: Terminology varies by FHRP (HSRP uses active/standby, VRRP uses master/backup)

### Failover Process

- When active router fails, standby router takes over active role
- Process is called failover
- New active router sends gratuitous ARP (GARP) messages
- GARP messages update switches' MAC address tables
- End hosts are unaware of failover (VIP and virtual MAC remain same)

### Gratuitous ARP (GARP)

- ARP replies that were not prompted by ARP requests
- Sent to broadcast MAC address (ffff.ffff.ffff)
- Source MAC address is virtual MAC address
- Causes switches to flood messages and update MAC address tables
- Allows switches to learn virtual MAC on port leading toward new active router

### Preemption

- Feature that allows higher-priority router to take over active role
- Even if another router is currently active
- Behavior varies by FHRP (enabled by default in VRRP, disabled in HSRP)
- Same term used in OSPF DR/BDR elections

## FHRP Types

Cisco routers support three different FHRPs:

### Hot Standby Router Protocol (HSRP)

- Cisco-proprietary FHRP
- Only runs on Cisco routers
- Uses active/standby terminology
- Preemption disabled by default
- Two versions: HSRPv1 and HSRPv2

#### HSRP Versions

**HSRPv1:**
- Hello messages sent to multicast IP 224.0.0.2 (all routers)
- Virtual MAC format: 0000.0c07.acXX (XX is group number)
- Supports 256 groups (0-255)
- IPv4 only

**HSRPv2:**
- Hello messages sent to multicast IP 224.0.0.102 (reserved for HSRPv2 and GLBP)
- Virtual MAC format: 0000.0c9f.fXXX (XXX is group number)
- Supports 4,096 groups (0-4,095)
- Supports IPv6 (in addition to IPv4)

#### HSRP Load Balancing

- Load balancing achieved per subnet
- Configure one router as active in some subnets, standby in others
- Other router configured opposite
- Avoids congestion on single link

### Virtual Router Redundancy Protocol (VRRP)

- Industry-standard FHRP (IETF standard)
- Can be implemented on any vendor's routers
- Uses master/backup terminology (instead of active/standby)
- Preemption enabled by default
- Multicast IP: 224.0.0.18 (reserved for VRRP)
- Virtual MAC format: 0000.5e00.01XX (XX is group number)
- Supports per-subnet load balancing (like HSRP)

### Gateway Load Balancing Protocol (GLBP)

- Cisco-proprietary FHRP
- Unique feature: enables load balancing within single subnet
- Load balancing done on per-host basis
- Elects Active Virtual Gateway (AVG)
- AVG assigns up to four Active Virtual Forwarders (AVFs)
- AVG itself can be an AVF
- Multicast IP: 224.0.0.102 (same as HSRPv2)
- Virtual MAC format: 0007.b400.XXYY (XX is group number, YY is AVF number)
- AVG preemption disabled by default; AVF preemption enabled by default

#### GLBP Load Balancing

- Single VIP but multiple virtual MAC addresses (one per AVF)
- AVG replies to ARP requests with virtual MAC of AVFs in round-robin manner
- Half of hosts use one AVF, other half use another AVF
- Achieves load balancing within single subnet

## FHRP Comparison

| Characteristic | HSRP | VRRP | GLBP |
|----------------|------|------|------|
| Terminology | Active/Standby | Master/Backup | AVG/AVF |
| Multicast IP (v2) | 224.0.0.102 | 224.0.0.18 | 224.0.0.102 |
| Virtual MAC Format (v2) | 0000.0c9f.fXXX | 0000.5e00.01XX | 0007.b400.XXYY |
| Cisco Proprietary? | Yes | No | Yes |
| Load Balancing | Per subnet | Per subnet | Per host |
| Preemption (default) | Disabled | Enabled | AVG: Disabled, AVF: Enabled |

## HSRP Configuration

### Basic Configuration

Each router in HSRP group needs:

1. Unique IP address on interface (for router-to-router communication)
2. HSRP version configuration
3. VIP configuration
4. Optional: Priority and preemption configuration

### Configuration Commands

```cisco
interface GigabitEthernet0/0
 ip address 10.0.0.2 255.255.255.0
 standby version 2                    ! Enable HSRPv2
 standby 1 ip 10.0.0.1               ! Configure VIP for group 1
 standby 1 priority 105              ! Set priority (default 100)
 standby 1 preempt                   ! Enable preemption
 no shutdown
```

### Active Router Selection

HSRP active router is determined by:

1. Highest priority (default 100)
2. Highest IP address (if priorities tied)

### Configuration Notes

- Group number and VIP must match on both routers
- HSRPv1 and HSRPv2 are not compatible
- Preemption only needs to be configured on router that should retake active role
- Priority configuration only needed if you want specific router to be active

## Verification Commands

### HSRP Status

- `show standby brief`: View brief HSRP status for all groups
- `show standby`: View detailed HSRP information

### Command Output Interpretation

- **State**: Active or Standby
- **Active**: IP address of current active router (local if this router is active)
- **Standby**: IP address of current standby router (local if this router is standby)
- **Virtual IP**: The VIP address
- **Priority**: Router's priority value
- **P**: Indicates preemption is configured

## Real-World Applications

- **Enterprise LANs**: Provide redundant default gateway for critical network segments
- **Data centers**: Ensure high availability for server connectivity
- **Branch offices**: Redundant connectivity to headquarters
- **Multi-vendor environments**: Use VRRP when mixing Cisco and non-Cisco routers
- **High-availability requirements**: Minimize downtime for business-critical applications
- **Load balancing**: Distribute traffic across multiple routers (HSRP/VRRP per subnet, GLBP per host)

## Troubleshooting FHRPs

### Common Issues

- **Failover not occurring**: Check hello messages are being received, verify priority configuration
- **Both routers think they're active**: Check group number and VIP match on both routers
- **Hosts can't reach external networks**: Verify VIP is configured as default gateway on hosts
- **Slow failover**: Check hello and hold timers
- **Preemption not working**: Verify preemption is enabled on higher-priority router

### Troubleshooting Steps

1. Verify HSRP is configured on both routers: `show standby brief`
2. Check that group number and VIP match
3. Verify interface status: `show ip interface brief`
4. Check hello messages: Verify routers can communicate
5. Verify priority and preemption settings
6. Test failover by shutting down active router interface

## Best Practices

- Use HSRPv2 for modern networks (supports IPv6 and more groups)
- Configure preemption on routers that should be active when operational
- Set appropriate priorities to ensure desired router becomes active
- Use GLBP when load balancing within single subnet is needed
- Use VRRP in multi-vendor environments
- Configure consistent group numbers and VIPs across routers
- Monitor HSRP status regularly
- Document which router should be active for each group
- Test failover scenarios in lab before production deployment

## Summary

- FHRPs allow multiple routers to provide redundant default gateway for hosts
- Routers share virtual IP (VIP) and virtual MAC address
- Active router serves as default gateway; standby router ready to take over
- Routers communicate via multicast hello messages
- Failover is transparent to end hosts (VIP and virtual MAC remain same)
- New active router sends GARP messages to update switch MAC tables
- Preemption allows higher-priority router to take over active role
- Three FHRPs: HSRP (Cisco-proprietary), VRRP (industry-standard), GLBP (Cisco-proprietary)
- HSRP uses active/standby terminology; preemption disabled by default
- HSRPv1: multicast 224.0.0.2, MAC 0000.0c07.acXX, 256 groups, IPv4 only
- HSRPv2: multicast 224.0.0.102, MAC 0000.0c9f.fXXX, 4,096 groups, IPv4 and IPv6
- VRRP uses master/backup terminology; preemption enabled by default
- VRRP: multicast 224.0.0.18, MAC 0000.5e00.01XX, industry-standard
- GLBP enables per-host load balancing within single subnet
- GLBP: multicast 224.0.0.102, MAC 0007.b400.XXYY, AVG assigns AVFs
- HSRP load balancing achieved per subnet by configuring different active routers
- Each router needs unique IP address even when sharing VIP
- Configure HSRP with: `standby version 2`, `standby group ip vip`, `standby group priority`, `standby group preempt`
- Active router determined by highest priority, then highest IP address
- Use `show standby brief` and `show standby` to verify HSRP operation

