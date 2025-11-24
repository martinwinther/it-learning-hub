# Routing Fundamentals

## Overview

Routing is the process of forwarding IP packets between networks. In practice this has two parts:

- Building and maintaining the routing table
- Using the routing table to forward packets

These notes focus on end host behavior, basic router forwarding, static routes, default routes, and key verification commands.

## How end hosts send packets

### Local vs remote destinations

Before a router ever sees a packet, the sending host decides whether the destination is local or remote.

- Local destination  
  Destination IP is in the same subnet as the source. Frames are sent directly to the destination host.

- Remote destination  
  Destination IP is in a different subnet. Frames are sent to the default gateway.

### Default gateway

- IPv4 default gateway is the router interface address in the local subnet.
- Can be configured manually or learned via DHCP.
- Traffic for remote subnets is sent to this address at Layer 2.

### Encapsulation steps on the host

For each packet:

1. Build the IPv4 packet with source and destination IP.
2. Decide local or remote based on IP and mask.
3. If local, resolve the destination MAC with ARP.
4. If remote, resolve the default gateway MAC with ARP.
5. Encapsulate the IP packet in an Ethernet frame and send it.

## Router packet processing

### Basic forwarding logic

When a router receives a frame destined to its MAC address:

1. Remove the Layer 2 header to expose the IP packet.
2. Check the destination IP address.
3. If the destination IP matches a local interface, process the packet locally.
4. If the destination IP is not local, look for a route in the routing table.
5. If a matching route is found, forward according to that route.
6. If no route is found, drop the packet.

### Next hop and exit interface

Each route tells the router how to forward a packet:

- Next hop IP address to send packets toward
- Exit interface to use on the router

The router then:

- Resolves the next hop IP to a MAC address on the exit interface
- Encapsulates the packet in a new frame
- Sends the frame out the exit interface

## The routing table

### Purpose

The routing table is a list of known networks and how to reach them. Each entry includes:

- Destination network and mask (or prefix length)
- Next hop or outgoing interface
- Administrative distance and metric
- Route source (connected, static, dynamic protocol)

### Connected routes (C)

- Added automatically when an interface has an IP address and is up
- Represent directly attached networks
- No manual configuration required

### Local routes (L)

- One per interface IP address
- Host route using a /32 prefix
- Represent the exact address on the router itself

### Static routes (S)

- Manually configured by an administrator
- Default administrative distance 1
- Metric is usually 0 for static routes

### Viewing the routing table

Common commands:

- `show ip route`  
  Full IPv4 routing table.

- `show ip route connected`  
  Only connected routes.

- `show ip route static`  
  Only static routes.

- `show ip route 192.0.2.0`  
  Detailed view of matching routes for a specific network.

Output also shows the gateway of last resort if a default route is present.

## Static route configuration

### Static route types

Static routes can be configured three ways.

#### Next hop routes

- Form:

  ```cisco
  ip route 192.168.3.0 255.255.255.0 192.168.12.2
  ```

- Uses only a next hop IP
- Router must perform a recursive lookup to find the exit interface

#### Exit interface routes

- Form:

  ```cisco
  ip route 192.168.3.0 255.255.255.0 GigabitEthernet0/0
  ```

- Uses only an exit interface
- Common on point to point links
- Router forwards directly without recursive lookup

#### Fully specified routes

- Form:

  ```cisco
  ip route 192.168.3.0 255.255.255.0 GigabitEthernet0/0 192.168.12.2
  ```

- Includes both exit interface and next hop
- Gives clear forwarding behavior and avoids ambiguity on multipoint links
- Often recommended as a best practice

### Administrative distance and metric

- Administrative distance (AD)  
  - Trust level of a route source  
  - Lower is preferred  
  - Static routes default to AD 1

- Metric  
  - Cost within a route source  
  - Used when multiple routes have the same AD  
  - For static routes the metric is normally 0 and path choice is based on prefix length and AD

## Default routes

### Definition

A default route is the route with the least specific prefix:

- Destination: `0.0.0.0`
- Mask: `0.0.0.0`
- Prefix length: `/0`

It matches all possible IPv4 addresses and is used only when no more specific route exists.

### Configuration examples

Using next hop:

```cisco
ip route 0.0.0.0 0.0.0.0 192.0.2.1
```

Using exit interface:

```cisco
ip route 0.0.0.0 0.0.0.0 GigabitEthernet0/0
```

In edge routers, the default route usually points toward an upstream provider or firewall.

### Gateway of last resort

- The chosen default route is shown as the gateway of last resort in `show ip route` output
- If no default route exists, packets with unknown destinations are dropped

## Router forwarding decisions

### Route selection logic

When a router performs a routing table lookup for a destination address:

1. Find all routes whose prefix matches the destination.
2. Choose routes with the longest prefix length (most specific match).
3. If several routes tie on prefix length, choose the one with lowest administrative distance.
4. If several routes tie on prefix length and AD, use the lowest metric.
5. If several equal cost routes remain, install multiple routes and perform equal cost load balancing.

### Local vs remote forwarding

- For destinations in directly connected subnets, the router forwards without using another router as next hop
- For remote subnets, the router sends packets to the next hop that leads toward the destination

## Troubleshooting routing

### Common problems

- No route to destination  
  - No matching route in the table  
  - Symptoms: pings fail, `show ip route` shows no relevant entry  
  - Fix: add static routes or configure dynamic routing

- Wrong next hop  
  - Static route points to an unreachable or incorrect address  
  - Symptoms: packets leave but never reach the target, multiple hops show in `traceroute` before loss  
  - Fix: verify connectivity to the next hop and correct the route

- Asymmetric or looping paths  
  - Misconfigured routes on multiple routers  
  - Symptoms: high latency, repeated hops, or TTL exceeded messages  
  - Fix: review routing tables end to end

### Useful verification commands

- `show ip interface brief`  
  - Confirms interface addresses and status

- `show ip route`  
  - Confirms presence and type of routes

- `ping <ip>`  
  - Basic reachability test

- `traceroute <ip>`  
  - Shows the path taken by packets

### Selected debug commands

Debug commands are powerful and should be used with care, especially on production devices.

- `debug ip routing`  
  - Shows routing table changes

- `debug ip packet`  
  - Shows packet level forwarding decisions  
  - Usually combined with filters to limit output

## Quick review

- Routing has two parts: building the routing table and forwarding packets based on that table.  
- End hosts send local traffic directly and remote traffic to the default gateway.  
- Routers remove the Layer 2 frame, check destination IPs, look up routes, and forward packets using next hops and exit interfaces.  
- Connected and local routes are created automatically, static routes are configured manually.  
- Default routes use `0.0.0.0/0` to match all destinations when no more specific route exists.  
- Route selection uses longest prefix match, then administrative distance, then metric.  
- Core verification uses `show ip interface brief`, `show ip route`, `ping`, and `traceroute`, with debug commands used carefully when deeper analysis is required.