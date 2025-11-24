# Domain Name System

## Overview

Domain Name System (DNS) maps human readable names like `www.google.com` to IP addresses. It is critical for web browsing, email, and most application traffic. Hosts prefer to use names, but IP packets need addresses, so DNS provides the translation.

## URLs

### URL structure

A URL (Uniform Resource Locator) is a type of URI that identifies a resource and how to reach it.

Basic parts:

- Scheme: protocol in use, for example `https`, `http`, `ftp`
- Authority: server name, for example `www.google.com`
- Path: specific resource, for example `/maps`

### URL example

For `https://www.google.com/maps`:

- Scheme: `https`
- Authority: `www.google.com`
- Path: `/maps`

The browser uses HTTPS to request `/maps` from `www.google.com`. DNS is used to translate `www.google.com` into an IP address.

### Default behavior

- If the scheme is omitted, browsers normally assume HTTPS
- If the path is omitted, the server returns a default page such as `index.html`

## Name resolution process

### Local cache and hosts file

Before sending a DNS query, a host checks local sources:

- Application cache, for example browser cache
- Operating system DNS cache
- Hosts file entries, for example on Windows `C:\Windows\System32\drivers\etc\hosts`

If a matching entry is found, no query is sent to a DNS server.

### Query to DNS server

If there is no match in local sources:

- The host sends a DNS query to the configured DNS server
- The server replies with an IP address or an error
- The result is stored in the local DNS cache with a time to live (TTL)

### Port and transport

- DNS servers listen on port 53
- UDP is used for most queries and responses
- TCP is used when responses are too large for UDP or for some special cases

## DNS hierarchy

### Structure

DNS uses a hierarchical, tree like naming structure:

- Root domain at the top, written as a single dot `.`
- Top level domains (TLDs) under the root, for example `com`, `net`, `org`, country codes
- Second level domains under each TLD, for example `google` under `com`
- Additional levels as needed, for example `www.google.com`

Each node in the tree is a domain and may contain subdomains.

### FQDN and PQDN

- Fully Qualified Domain Name (FQDN):
  - Full path from host to root
  - Often written with a trailing dot to show the root, for example `www.google.com.`
- Partially Qualified Domain Name (PQDN):
  - Does not include the full path
  - Interpreted relative to a default domain or search list

Example:

- Domain: `business.com`
- Host within the domain: `www`
- PQDN: `www`
- FQDN: `www.business.com`

### Common terms

- Domain name: a portion of the namespace such as `example.com`
- Hostname: the label for a specific device, for example `srv1`
- FQDN: `srv1.example.com`
- PQDN: `srv1` when used inside the `example.com` domain

## Query types and server roles

### Recursive and iterative queries

- Recursive query:
  - Sent by a client to a DNS server (recursive resolver)
  - Asks for a complete answer or an error
  - The client does not contact other servers directly
- Iterative query:
  - Sent by a resolver to other DNS servers
  - Can be answered with an address or with a referral to another server

### Server types

- Root server:
  - Knows the TLD servers
  - Does not hold all records
- TLD server:
  - Knows the authoritative servers for domains under a TLD, for example `com`
- Authoritative server:
  - Holds the records for a specific domain
  - Responds with final answers for that domain
- Recursive resolver:
  - Handles client queries
  - Performs iterative queries to other servers

### Example resolution flow

1. Client sends a recursive query for `www.example.com` to the recursive resolver
2. Resolver checks its cache
3. If not cached, resolver sends iterative query to a root server
4. Root server responds with a referral to the `com` TLD server
5. Resolver queries the `com` TLD server
6. TLD server responds with a referral to the authoritative server for `example.com`
7. Resolver queries the authoritative server
8. Authoritative server responds with an A or AAAA record
9. Resolver caches the reply and returns the IP address to the client

Caching at each step reduces future query traffic and speeds up resolution.

## Common record types

### Address records

- A record:
  - Maps a name to an IPv4 address
  - Example: `example.com` to `192.0.2.1`
- AAAA record:
  - Maps a name to an IPv6 address
  - Example: `example.com` to `2001:db8::1`

### Alias and mail records

- CNAME record:
  - Creates an alias from one name to another name
  - Example: `www.example.com` as an alias for `example.com`
- MX record:
  - Identifies mail servers for a domain
  - Can include preferences to rank multiple mail servers

### Name server and reverse records

- NS record:
  - Identifies the authoritative name servers for a domain
- PTR record:
  - Maps an IP address back to a name
  - Used for reverse DNS lookups

### SOA and TTL

- SOA record:
  - Start of Authority for a zone
  - Contains administrative data, including contact and serial number
- TTL:
  - Time to live in seconds
  - Specifies how long records can be cached before they must be refreshed
  - Low TTL gives faster propagation of changes but more query load

## DNS on Cisco IOS

### Client side DNS

- Enable DNS lookups:
  - `ip domain lookup` or `ip domain-lookup` (on by default)
- Configure DNS servers:
  - `ip name-server <ip-address>`
  - Up to six servers can be configured
- Configure default domain:
  - `ip domain name example.com`
  - Appended to hostnames if no domain is given

With these settings, commands can use names instead of IP addresses, for example:
  
- `ping www.example.com`
- `ntp server time1.google.com`

### Router as DNS server

- Enable DNS server feature:
  - `ip dns server`
- Configure upstream DNS servers:
  - `ip name-server <ip-address>`
- The router then:
  - Accepts queries from clients
  - Forwards queries to upstream servers
  - Caches responses

This provides basic caching DNS for a small network.

### Static name to address mappings

- Configure manual mappings:
  - `ip host SRV1 192.0.2.10`
  - `ip host FW1 198.51.100.2`
- These entries are stored locally on the router
- Helpful for internal devices that do not have public DNS entries

### Verification

- `show hosts`
  - Displays static and learned name to address mappings
  - Shows name servers in use and the default domain

## Troubleshooting notes

- If names do not resolve:
  - Check `ip name-server` configuration
  - Confirm reachability of DNS servers with `ping`
- If wrong IPs appear:
  - Check local and router caches
  - Consider TTL and recent changes
- If internal names fail:
  - Verify static `ip host` entries or internal DNS server records

## Quick review

- DNS maps names to IP addresses using a hierarchical structure and multiple server roles.
- URLs include scheme, authority, and path. DNS is used to resolve the authority part.
- Name resolution checks local caches and hosts files before sending queries.
- Port 53 is used for DNS over UDP and TCP.
- Recursive resolvers answer client queries by performing iterative queries to root, TLD, and authoritative servers.
- Key record types: A, AAAA, CNAME, MX, NS, PTR, SOA.
- TTL controls how long records are cached and affects propagation time for changes.
- On Cisco IOS, DNS client features use `ip domain lookup`, `ip name-server`, and `ip domain name`.
- Routers can act as simple caching DNS servers with `ip dns server` and static mappings via `ip host`.
