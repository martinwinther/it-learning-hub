# Network Devices

## Computer networks

A computer network is a telecommunications system that allows nodes to share resources.

### Key components

- **Node**  
  Any device that connects to a network.  
  Examples: PCs, laptops, phones, tablets, printers, IP cameras, IoT devices.

- **Resource**  
  Anything that can be used or accessed over the network.  
  Examples: web pages, file shares, databases, printers, cloud applications.

Networks exist so nodes can communicate and share resources efficiently.

## Clients and servers

Clients and servers describe roles, not specific hardware types.

- **Client**  
  Requests information or a service.

- **Server**  
  Provides information or a service.

The same device can act as both client and server at different times.

Examples:

- TV streaming a movie from a video platform  
- Phone using a social media app that talks to backend servers  
- PC opening files from a file server

## Switches

Switches operate at Layer 2 (data link layer) and provide local connectivity inside a LAN.

### Switch functions

- Connect end devices within a LAN
- Forward frames based on destination MAC address
- Build a MAC address table by learning source MAC addresses
- Keep each port in its own collision domain

Devices usually do not interact with the switch itself. The switch forwards traffic between devices in the same VLAN.

### Scope

- Switches forward traffic only within a broadcast domain
- They do not route between IP subnets
- Multilayer switches add Layer 3 capabilities but still include Layer 2 switching

## Routers

Routers operate at Layer 3 (network layer) and connect different networks.

### Router functions

- Route packets between IP subnets
- Connect LANs to WANs and the internet
- Use a routing table to choose the next hop
- Act as default gateways for end hosts

A router receives packets from one interface, looks up the destination network, and forwards them out another interface.

### Where routers are used

- At the edge of a campus or branch site
- Between office networks and service provider networks
- In SOHO environments, combined with switch and wireless access point roles

## Wireless routers and access points

### Wireless routers

A typical home or small office wireless router includes several functions in one device:

- Router between LAN and internet
- Small Ethernet switch
- Wireless access point
- Basic firewall features

This single device often provides all routing, switching, and Wi‑Fi for a SOHO network.

### Wireless access points

- Provide Wi‑Fi connectivity for wireless clients
- Bridge wireless traffic into a wired LAN
- Often connect to access layer switches in campus designs

## Firewalls

Firewalls enforce security policy by inspecting traffic and allowing or blocking it based on rules.

### Host based firewalls

- Software on an individual host
- Protects only the device where it runs
- Examines traffic entering or leaving that host
- Examples: built in OS firewalls

### Network firewalls

- Dedicated device placed at the edge or between network segments
- Inspects traffic passing through the firewall
- Enforces policies for many hosts at once
- Often combines stateful inspection, NAT, VPN, and other features

## Quick review

- Networks connect nodes so they can share resources.  
- Clients request services; servers provide them. The same device can be both.  
- Switches operate at Layer 2 and forward frames within a LAN based on MAC addresses.  
- Routers operate at Layer 3 and forward packets between networks using IP addresses and routing tables.  
- Wireless routers in SOHO networks combine router, switch, access point, and basic firewall functions.  
- Firewalls, host based or network based, enforce security policy by filtering traffic.
