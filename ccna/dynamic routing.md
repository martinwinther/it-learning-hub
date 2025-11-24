# Dynamic Routing

## Overview

Dynamic routing uses routing protocols so routers can learn and update routes automatically. This reduces manual configuration, improves adaptability to failures, and scales to larger topologies.

## Why use dynamic routing

### Adaptability

- Routers react to link and node failures
- Alternate paths are calculated automatically
- Convergence restores connectivity without manual changes

### Scalability

- Static routes do not scale in networks with many routers
- Dynamic protocols share routes and maintain the table for each router
- Administrative effort moves from per route to per protocol configuration

### Static and dynamic together

- Static routes give precise control where needed
- Dynamic routes handle most destinations
- Floating static routes provide controlled backup paths

## Routing protocol categories

### Interior Gateway Protocols (IGP)

- Used inside a single autonomous system (AS)
- Typical enterprise protocols
- Examples: RIP, EIGRP, OSPF, IS-IS

### Exterior Gateway Protocols (EGP)

- Used between autonomous systems
- Internet edge and inter provider routing
- BGP is the only widely used EGP

## Algorithm types

### Distance vector

- Routers advertise known networks and metrics to neighbors
- Each router knows next hop and metric, not a full map
- Sometimes called routing by rumor
- Examples: RIP, EIGRP (often called advanced distance vector)

#### RIP

- Simple industry standard distance vector protocol
- Metric: hop count
- Useful mainly in very small or lab networks

#### EIGRP

- Cisco developed advanced distance vector protocol
- Metric: composite value based on bandwidth and delay (default)
- Originally proprietary, later documented in RFC 7868
- Still most common on Cisco devices

### Link state

- Routers flood link state information to form a topology database
- Each router runs SPF to calculate best paths
- Requires more CPU and memory than distance vector
- Examples: OSPF, IS-IS

#### OSPF

- Industry standard link state protocol
- Major CCNA topic
- Metric: cost derived from bandwidth
- Supports areas to scale in larger networks

#### IS-IS

- Industry standard link state protocol
- Common in service provider cores
- Not a main focus on CCNA

### Path vector

- Used by BGP
- Decisions based on AS path and other attributes
- Works at AS to AS scale instead of individual router hops

## Route selection concepts

### Two meanings of route selection

- Which routes enter the routing table
- Which route is used to forward a specific packet

### Metrics

- Measure of route quality inside a single protocol
- Lower metric is preferred
- Examples:
  - RIP: hop count
  - EIGRP: composite metric based on bandwidth and delay
  - OSPF: cost calculated from link bandwidth
- Metrics from different protocols cannot be compared directly

### Administrative distance (AD)

- Preference between different route sources
- Lower AD is more trusted
- Typical default values:
  - Connected: 0
  - Static: 1
  - External BGP: 20
  - EIGRP: 90
  - OSPF: 110
  - IS-IS: 115
  - RIP: 120
  - Internal BGP: 200
  - Unusable: 255

### Equal Cost Multi Path (ECMP)

- Multiple routes to the same destination with equal metric and AD
- All are installed in the routing table
- Traffic is load balanced across them

### Floating static routes

- Static route configured with AD higher than the default 1
- Less preferred than dynamic routes
- Used as a backup that appears only when primary dynamic routes disappear
- Example:
  - `ip route 10.0.0.0 255.0.0.0 192.168.1.2 111`

### Route selection rules

- Routes to different prefixes all coexist
- For the same prefix and mask:
  - Compare AD if learned from different sources
  - Compare metric if learned from the same source
- Packet forwarding uses the most specific matching route (longest prefix match)

## The network command (OSPF focus)

### Purpose

The `network` command activates a routing process on interfaces and causes their prefixes to be advertised.

For OSPF it:

- Selects interfaces based on IP and wildcard mask
- Enables OSPF on those interfaces
- Advertises connected prefixes into OSPF

### OSPF network command syntax

- Enter router configuration mode:
  - `router ospf PROCESS-ID`
- Network statement:
  - `network IP-ADDRESS WILDCARD-MASK area AREA-ID`

Notes:

- Process ID is locally significant
- Multiple processes are possible but rare

### Wildcard masks

- Invert each octet of a netmask to get a wildcard mask
- Bit 0 in wildcard: bits must match
- Bit 1 in wildcard: bits do not need to match
- Example:
  - Netmask 255.255.255.0 → wildcard 0.0.0.255

### Matching interfaces

- OSPF checks each interface IP against the network plus wildcard
- Any interface that matches is enabled for OSPF in the given area
- IP and wildcard do not need to match the interface mask exactly

Recommended style for clarity:

- Use the exact interface IP with wildcard `0.0.0.0`

Example:

- Interface `10.0.0.1/24` in area 0:
  - `network 10.0.0.1 0.0.0.0 area 0`

## Quick review

- Dynamic routing relies on routing protocols instead of manual static routes.
- IGPs (RIP, EIGRP, OSPF, IS-IS) work within an AS; BGP works between ASes.
- Distance vector uses neighbor metrics, link state builds a full map, BGP uses path vector and AS paths.
- Metrics decide the best route inside one protocol; administrative distance decides between protocols.
- ECMP installs multiple equal cost routes and load balances traffic.
- Floating static routes use a higher AD to act as backups to dynamic routes.
- The OSPF `network` command activates OSPF on matching interfaces, using wildcard masks to select them.
