# Domain Name System

## Overview

Domain Name System (DNS) is a protocol that resolves (translates) human-readable names like www.google.com into IP addresses that computers use to communicate. DNS is one of the foundational protocols of the internet and is essential for network operations. While humans prefer memorable names, computers use IP addresses, so DNS bridges this gap by providing name-to-IP-address translation. DNS enables users to access websites and network resources using easy-to-remember names instead of numeric IP addresses.

## Uniform Resource Locators (URLs)

### URL Structure

- URL (Uniform Resource Locator) is type of URI (Uniform Resource Identifier)
- URI identifies resource; URL identifies resource and how to locate it
- URL consists of multiple elements:
  - **Scheme**: Protocol used to access resource (https, http, ftp, etc.)
  - **Authority**: Name of server hosting resource (www.google.com)
  - **Path**: Specific resource on server (/maps)

### URL Example

- Example: `https://www.google.com/maps`
- Scheme: `https` (protocol)
- Authority: `www.google.com` (domain name of server)
- Path: `/maps` (specific web page)
- Browser uses HTTPS protocol to request /maps resource on www.google.com server
- DNS translates www.google.com domain name into IP address

### Default Behavior

- If scheme not specified, browser assumes default (usually HTTPS)
- If path not specified, browser shows default page (index.html, index.php, etc.)

## DNS Name Resolution Process

### DNS Cache

- Device first checks DNS cache for matching entry
- DNS cache temporarily stores previously resolved names and IP addresses
- If matching entry found, process complete; no need to query DNS server
- DNS cache exists at multiple levels:
  - Operating system maintains cache
  - Applications like web browsers maintain own cache
- View Windows DNS cache with `ipconfig /displaydns` command

### DNS Query Process

- If no matching entry in cache, device sends DNS query to DNS server
- DNS query asks server to resolve name to IP address
- DNS server replies with IP address or error message
- After successful resolution, device stores mapping in DNS cache
- Subsequent requests for same name use cached information

### DNS Port and Protocol

- DNS queries sent to port 53 on DNS server
- DNS can use both TCP and UDP as Layer 4 protocol
- UDP most common for standard DNS queries and responses
- TCP used in certain situations (e.g., when response exceeds certain size)
- DNS servers listen on port 53 for both TCP and UDP

### Hosts File

- Many devices have hosts file with IP address to hostname mappings
- Location varies by OS (Windows: C:\Windows\System32\drivers\etc\hosts)
- Device checks hosts file before sending DNS request
- Entirely separate from DNS resolution process
- Before DNS existed, devices relied on hosts file
- Lack of scalability led to creation of DNS
- Hosts file still present but use is limited

## DNS Hierarchy

### Hierarchical Structure

- DNS is hierarchical naming system organized in tree-like structure
- Domain is subtree of structure under administrative control
- At top is root domain, represented by single dot (.)
- Under root domain are various top-level domains (TLDs)
- Under each TLD are various second-level domains (SLDs)
- Under each SLD can be third-level domains, fourth-level domains, etc.
- Each domain is subdomain of domains above it in hierarchy

### Top-Level Domains

- Most common TLD is com
- Other TLDs: net, org, edu, gov, country codes, etc.
- Each TLD has various second-level domains under it
- Example: google is second-level domain under com TLD

### Fully Qualified Domain Names (FQDNs)

- Complete name of host on internet is FQDN
- Written with dot separating each part
- Example: `www.google.com.` (note final dot)
- Final dot represents root domain (often omitted)
- Domain name without final dot is partially qualified domain name (PQDN)
- FQDN specifies exact location in DNS hierarchy

### Partially Qualified Domain Names (PQDNs)

- PQDN is domain name that doesn't include all information about host's location
- Example: `www` is PQDN within domain `business.com`
- FQDN would be `www.business.com`
- PQDN identifies host within its domain but not globally

### Terminology

- **Domain name**: Region of administrative control (example.com) or particular node (srv1.example.com)
- **Hostname**: Identifier for specific device (srv1 or srv1.example.com)
- **FQDN**: Complete name specifying exact location in DNS hierarchy
- **PQDN**: Partial name that doesn't include all hierarchy information

## DNS Lookup Types

### Recursive Queries

- Client sends recursive query to DNS server
- Recursive query asks for definite answer: IP address or error message
- DNS server responsible for resolving recursive queries is recursive resolver
- Recursive resolver performs iterative queries to find answer
- Client doesn't perform iterative queries itself

### Iterative Queries

- Recursive resolver sends iterative queries to other DNS servers
- Iterative query can be answered with:
  - IP address, or
  - Referral to another DNS server
- Server says "I don't know, but try this other server"
- Process continues until authoritative server is reached

### Name Resolution Example

1. Client sends recursive query to recursive resolver (e.g., 8.8.8.8)
2. Recursive resolver checks cache; if not found, starts iterative process
3. Recursive resolver queries root DNS server (iterative query)
4. Root server refers to TLD server (e.g., com TLD server)
5. Recursive resolver queries TLD server (iterative query)
6. TLD server refers to authoritative DNS server for domain
7. Recursive resolver queries authoritative server (iterative query)
8. Authoritative server responds with IP address
9. Recursive resolver replies to client's recursive query with IP address
10. Client uses IP address to communicate with destination

### DNS Server Types

- **Root DNS server**: DNS server at top of DNS hierarchy
- **TLD server**: DNS server responsible for specific top-level domain
- **Authoritative DNS server**: Server holding definitive set of records for specific domain
- **Recursive resolver**: DNS server that resolves clients' recursive queries by performing iterative queries

### Caching

- Caching used at every step of name resolution process
- Reduces number of DNS queries needed
- If recursive resolver has cached entry, it replies immediately
- Caching improves performance and reduces DNS server load

## DNS Record Types

### A Records

- Map domain name to IPv4 address
- Example: example.com -> 192.0.2.1
- Most common type of DNS record
- Used for standard IPv4 name resolution

### AAAA Records

- Map domain name to IPv6 address
- Example: example.com -> 2001:db8::1
- Called quad-A records (IPv6 addresses are quadruple length of IPv4)
- Used for IPv6 name resolution

### CNAME Records

- Create alias for domain name
- Map one domain name to another domain name
- Example: www.example.com -> example.com
- Common use: map www.example.com to example.com
- No A record exists for aliased name; points to canonical name

### MX Records

- Specify domain's mail servers
- Example: example.com -> mail1.example.com
- Used for email delivery
- Multiple MX records can specify multiple mail servers with priorities

### NS Records

- Specify domain's authoritative DNS servers
- Example: example.com -> ns1.example.com
- Identifies which DNS servers are authoritative for domain
- Used to delegate DNS authority

### PTR Records

- Map IP address to domain name (reverse DNS lookup)
- Example: 192.0.2.1 -> example.com
- Unique: maps IP to name instead of name to IP
- Used for reverse DNS lookups

### SOA Records

- Start of Authority record
- Stores administrative information about domain
- Includes: contact information, serial number, refresh intervals, etc.
- Contact information format: admin.example.com (first dot replaced with @ for email)

### DNS Propagation

- DNS propagation delay: time for DNS record changes to be reflected across internet
- Generally takes few minutes to 48-72 hours
- Time to Live (TTL) value determines how long records are cached
- Lower TTL means more frequent refreshes
- Reduce TTL values before making changes to minimize propagation delay

## DNS on Cisco IOS

### DNS Client Configuration

- Enable DNS queries: `ip domain lookup` (enabled by default)
- Can also use: `ip domain-lookup`
- Disable with: `no ip domain lookup`
- Configure DNS server: `ip name-server ip-address`
- Can specify multiple DNS servers (up to six)
- Either single command: `ip name-server 8.8.8.8 1.1.1.1`
- Or separate commands for each server
- Router queries servers in order if first fails

### Using DNS in Other Configurations

- Can use domain names instead of IP addresses in other commands
- Example: `ntp server time1.google.com` instead of IP address
- Router resolves domain name to IP address using configured DNS server

### DNS Server Configuration

- Configure router as DNS server: `ip dns server`
- Router responds to clients' DNS queries
- Router queries other DNS servers (configured with `ip name-server`) to resolve queries
- Router caches responses for commonly accessed websites
- Performance benefit: router can respond to multiple clients' queries for same name using cache
- Router forwards clients' DNS queries to configured DNS servers
- Both client-to-router and router-to-server queries are recursive queries

### Manual Name-to-IP Mappings

- Configure default domain name: `ip domain name name`
- Can also use: `ip domain-name name`
- Router appends default domain name to queries that specify only hostname
- Configure manual mappings: `ip host name ip-address`
- Useful for hosts in internal network
- Allows hosts to communicate using hostnames instead of IP addresses

### DNS Verification

- View all name-to-IP mappings: `show hosts`
- Shows both manually configured mappings and dynamically learned mappings
- Manually configured: marked as permanent (perm)
- Dynamically learned: marked as temporary (temp)
- Shows default domain name and name servers

## Real-World Applications

- **Web browsing**: Translate website names to IP addresses
- **Email**: Resolve mail server domain names
- **Network services**: Access services using memorable names
- **Internal networks**: Use hostnames for internal resources
- **Load balancing**: Multiple A records for same domain name
- **Service discovery**: Find services by name instead of IP
- **Security**: Reverse DNS lookups for authentication
- **Network management**: Use names instead of IP addresses in configurations

## Troubleshooting

### Common Issues

- **Name not resolving**: Verify DNS server is configured and reachable
- **Wrong IP address**: Check DNS cache; may need to flush cache
- **Slow resolution**: Check DNS server response times
- **Internal names not working**: Verify manual mappings or internal DNS server

### Troubleshooting Steps

1. Verify DNS server configuration: `show hosts`
2. Test DNS resolution: Ping domain name
3. Check DNS server reachability: Ping DNS server IP address
4. Verify manual mappings: `show hosts` for permanent entries
5. Check default domain: Verify `ip domain name` configuration
6. Flush DNS cache: May need to clear cache on client device

## Best Practices

- Configure multiple DNS servers for redundancy
- Use reliable DNS servers (e.g., 8.8.8.8, 1.1.1.1)
- Configure internal DNS server for internal network resources
- Use manual mappings for critical internal hosts
- Configure default domain name for convenience
- Monitor DNS resolution performance
- Document DNS server addresses and configurations
- Use DNS caching to improve performance
- Consider security implications of DNS queries

## Summary

- DNS resolves (translates) names like www.google.com to IP addresses
- URL consists of scheme (protocol), authority (domain name), and path (resource)
- Device checks DNS cache first; if not found, sends DNS query to DNS server
- DNS queries sent to port 53; can use TCP or UDP (UDP most common)
- Device checks hosts file before sending DNS request
- DNS is hierarchical naming system with root domain, TLDs, SLDs, and subdomains
- FQDN specifies exact location in DNS hierarchy; PQDN is partial name
- Recursive queries ask for definite answer; iterative queries can return referrals
- Root server refers to TLD server; TLD server refers to authoritative server
- Authoritative server holds definitive records for domain
- Recursive resolver performs iterative queries to resolve client's recursive query
- Caching used at every step to reduce DNS queries
- DNS record types: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), NS (name server), PTR (reverse), SOA (authority)
- Enable DNS on Cisco IOS with `ip domain lookup` (enabled by default)
- Configure DNS server with `ip name-server ip-address`
- Configure router as DNS server with `ip dns server`
- Configure default domain with `ip domain name name`
- Configure manual mappings with `ip host name ip-address`
- View mappings with `show hosts` command
- DNS propagation delay can take minutes to days depending on TTL values

