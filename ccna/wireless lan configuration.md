# Wireless LAN Configuration

## Overview

Wireless LAN configuration on a Cisco wireless LAN controller (WLC) ties together switch VLANs, WLC interfaces, WLANs (SSIDs), and lightweight APs (LWAPs). For CCNA, focus on basic WLC wizard concepts, GUI configuration of WLANs with WPA2 PSK, and how APs discover and join a WLC.

## Network topology and terminology

### Topology summary

Example lab topology:

- One LWAP (AP1)
- One switch (SW1)
- One WLC (WLC1)

SW1 roles:

- Layer 2 switch for wired infrastructure
- Default gateway for all subnets (SVIs)
- DHCP server for APs and wireless clients
- NTP server for time synchronization

WLC1 ports are labeled P1, P2, and so on. These map to distribution system (DS) ports on the controller.

### WLAN and VLAN mapping

Lab design:

- Management VLAN (VLAN 10) for device management and CAPWAP tunnels
- Internal WLAN mapped to VLAN 100
- Guest WLAN mapped to VLAN 200

WLAN term usage:

- In some contexts, WLAN refers to the entire wireless deployment.
- In WLC configuration, a WLAN is a logical entity that maps an SSID to security and interface settings.
- Each SSID is treated as a separate WLAN in the WLC GUI.

## Switch configuration

### VLANs

SW1 creates three VLANs:

- VLAN 10: Management
- VLAN 100: Internal
- VLAN 200: Guest

These VLANs carry management, internal user, and guest traffic respectively.

### Access ports

For split MAC architecture:

- AP1 connects to SW1 on an access port in the management VLAN.
- A lab PC also connects to SW1 on an access port in the management VLAN to reach the WLC GUI.
- PortFast is enabled on access ports to move them quickly to forwarding state.

Example pattern:

```cisco
interface FastEthernet0/7
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast

interface FastEthernet0/8
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
```

### Trunk and LAG to the WLC

- WLC1 must carry multiple VLANs over its uplink.
- SW1 uses a static Link Aggregation Group (LAG) toward WLC1.
- The LAG operates as an 802.1Q trunk that allows VLANs 10, 100, and 200.

Key points:

- Cisco WLCs support static LAG only (mode on).
- WLCs do not run PAgP or LACP.

Example pattern on SW1:

```cisco
interface range FastEthernet0/1 - 2
 channel-group 1 mode on

interface Port-channel1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 10,100,200
```

### SVIs and routing

SW1 routes between VLANs using SVIs and `ip routing`:

- VLAN 10 SVI: 192.168.1.1/24 (management)
- VLAN 100 SVI: 10.0.0.1/24 (internal)
- VLAN 200 SVI: 10.1.0.1/24 (guest)

Example pattern:

```cisco
ip routing

interface vlan 10
 ip address 192.168.1.1 255.255.255.0
 no shutdown

interface vlan 100
 ip address 10.0.0.1 255.255.255.0
 no shutdown

interface vlan 200
 ip address 10.1.0.1 255.255.255.0
 no shutdown
```

### DHCP and NTP

SW1 provides:

- NTP service
- DHCP pools for management, internal, and guest networks

DHCP details:

- Management pool leases addresses to LWAPs and management devices.
- Internal and guest pools lease addresses to wireless clients.
- DHCP option 42 points clients to the NTP server (SW1).
- DHCP option 43 can tell LWAPs which WLC IP to use.

High level steps:

- Configure NTP service and set SW1 as its own time source or an NTP client of an upstream server.
- Define DHCP pools for each subnet.
- Add option 42 and option 43 where required.

## WLC initial configuration (wizard)

### Wizard overview

Before using the GUI, the WLC requires initial setup over the console. Cisco Wizard Configuration Tool collects:

- Hostname and admin credentials
- Link aggregation setting
- Management interface addressing
- Virtual gateway address
- Multicast address
- WLAN basics
- Country code
- 802.11 options
- NTP settings

Exam focus is on GUI WLAN configuration rather than wizard details, but the wizard concepts explain later settings.

### Link aggregation and management interface

Wizard items:

- System name: WLC hostname (for example, WLC1).
- Administrative user name and password: local admin account.
- Link aggregation: enables static LAG across all DS ports.
- Management interface:
  - IP address and mask
  - Default gateway (SW1 SVI in management VLAN)
  - VLAN ID (management VLAN)
  - DHCP server IP (SW1)

Management interface becomes the in band management endpoint for GUI and SSH.

### Virtual gateway and multicast address

Additional wizard addresses:

- Virtual Gateway IP Address
  - Used for client related functions such as DHCP relay.
  - Must be unique in the network.
  - Does not need to be reachable as a normal routed address.
  - Often taken from documentation ranges such as 192.0.2.0/24, 198.51.100.0/24, or 203.0.113.0/24.

- Multicast IP address
  - Used for WLC multicast toward clients.
  - Chosen from the administratively scoped multicast range (239.0.0.0/8).

### Country code and RF options

Wizard prompts:

- Country code
  - Must match the regulatory domain supported by the LWAP model.
  - Mismatched country and regulatory domain prevent APs from joining.

- 802.11b, 802.11a, 802.11g
  - Enable or disable the bands.
  - Default wizard choices usually enable them.

- Auto RF
  - Allows WLC to control LWAP transmit power and channel selection automatically.

### WLAN and DHCP behavior

Wizard also asks for:

- A first WLAN (often deleted later in lab setups).
- DHCP bridging mode versus proxy mode.
  - Bridging: WLC forwards DHCP messages transparently between 802.11 and Ethernet.
  - Proxy: WLC behaves as a DHCP relay agent.
- Whether to allow static IP addresses on wireless clients.

### NTP settings

Final wizard items:

- NTP server address (SW1 in the lab).
- Polling interval.
- Confirmation to save the configuration and reboot the WLC.

After the reboot, the WLC is ready for GUI access on the management interface IP address.

## WLC management access

### Management connection methods

Supported methods:

- CLI:
  - Console
  - Telnet
  - SSH

- GUI:
  - HTTP
  - HTTPS

Authentication sources:

- Local user database
- RADIUS server
- TACACS+ server
- Combinations in priority order

Example CCNA exam topic: management access connections and related protocols.

### GUI access and tabs

To reach the GUI:

- Ensure the PC has IP connectivity to the WLC management interface.
- Browse to the management IP (for example 192.168.1.100) using HTTPS.
- Log in with the admin credentials.

Main tabs used in CCNA scope:

- Monitor: status overview of WLC, APs, and clients.
- WLANs: WLAN creation and configuration, including SSID, security, and QoS.
- Controller: interfaces, ports, DHCP, NTP, global controller settings.
- Wireless: LWAP configuration and monitoring.
- Security: ACLs, management authentication, and AAA related settings.
- Management: management access protocols, SNMP, Syslog, and related options.

### Management protocol settings

From the Management tab:

- Enable or disable HTTP, HTTPS, Telnet, and SSH.
- Typical practice is to disable HTTP and use HTTPS plus SSH.

From the Security tab, Management User priority order defines:

- Which sources (local, RADIUS, TACACS+) are checked for management logins.
- In what order those sources are used.

## CPU ACL for management protection

### Purpose

CPU ACLs filter traffic destined for the WLC itself. Examples:

- HTTP, HTTPS, Telnet, SSH management sessions
- CAPWAP traffic from LWAPs

CPU ACLs are applied to the WLC CPU, not to specific physical interfaces.

### Creating a CPU ACL

Steps in the GUI:

- Security tab
- Access Control Lists menu
- Access Control Lists submenu
- Create a new ACL (for example MGMT)
- Add rules that permit management sources, such as 192.168.1.0/24
- Rely on the implicit deny at the end to block other sources

### Applying a CPU ACL

- Security tab
- Access Control Lists menu
- CPU Access Control Lists submenu
- Enable CPU ACL
- Select the ACL name
- Apply the configuration

Important reminder: rules must allow CAPWAP from legitimate LWAPs as well as management traffic. Otherwise valid APs cannot join.

## WLC ports and interfaces

### Ports and interfaces

On a WLC:

- Port: physical connector (for example RJ45) that cables plug into.
- Interface: logical construct similar to an SVI on a switch.

Ports connect to the distribution system. Interfaces handle management, CAPWAP, WLAN to VLAN mapping, and redundancy roles.

### Physical port types

Common physical port types:

- Console port
  - Serial port (RJ45 or USB) for direct CLI access.

- Service port
  - Dedicated out of band management port.
  - Connects to a switch access port (no VLAN tagging).

- Redundancy port
  - Connects two WLCs to form an active and standby pair.

- Distribution system (DS) ports
  - Standard network ports toward the LAN.
  - Can participate in LAG for bandwidth and redundancy.

Not all WLC models include every port type. In the lab example, WLC1 has a console port and several DS ports without separate service or redundancy ports.

### Logical interface types

Logical interfaces include:

- Management interface
  - Default in band management interface.
  - Maps to the management VLAN and uses DS ports.

- AP manager interface
  - Used for CAPWAP communication with LWAPs.
  - Management interface acts as AP manager by default.
  - Optional separate AP manager interface can isolate CAPWAP traffic.

- Redundancy management interface
  - Used to manage the standby WLC in a redundant pair.

- Service port interface
  - Logical interface linked to the service port.

- Virtual interface
  - Uses the Virtual Gateway IP configured in the wizard.
  - Supports DHCP relay and certain client related functions.

- Dynamic interfaces
  - Similar to SVIs on a switch.
  - Each dynamic interface maps a VLAN to a WLAN.

### Creating dynamic interfaces

To create dynamic interfaces for Internal and Guest WLANs:

- Controller tab
- Interfaces menu
- New interface (for example Internal, VLAN 100)
- Configure:
  - IP address and mask for the VLAN
  - Default gateway (SW1 SVI for that VLAN)
  - DHCP server (SW1 SVI)

Repeat for the guest VLAN (for example Guest, VLAN 200). After creation, the Interfaces list shows Management, Virtual, and the new dynamic interfaces.

## WLAN configuration

### Creating WLANs

Steps for Internal and Guest WLANs:

- WLANs tab
- Remove the initial wizard created WLAN (for example TEST)
- Create new WLAN entries for Internal and Guest

Each WLAN requires:

- Profile Name
- SSID
- Numeric ID

SSID is visible to clients. Profile Name and ID are internal to the WLC. Keeping all three consistent with VLAN and interface names can make troubleshooting easier.

### General tab

Key items on the General tab:

- Status: WLAN must be enabled for clients to associate.
- Interface: select the correct dynamic interface (for example Internal or Guest).

### Layer 2 security (WPA2 PSK)

On the Security tab, Layer 2 section:

- Select WPA + WPA2 from the Layer 2 security dropdown.
- Under WPA + WPA2 Parameters:
  - Enable WPA2 Policy.
  - Enable AES Encryption.
  - Leave WPA and TKIP disabled.

Under Authentication Key Management:

- Select PSK (pre shared key) for CCNA scope.
- Configure a passphrase of 8 to 63 ASCII characters.
- The WLC derives the 256 bit PSK from the passphrase.

Protected Management Frames (PMF) is optional in WPA2 and mandatory in WPA3. In many basic labs PMF remains disabled.

### Layer 3 web policies

Layer 3 tab settings apply after the client has obtained an IP address. Examples:

- Authentication
  - User must provide credentials on a web page before gaining access.

- Passthrough
  - User proceeds after accepting terms or viewing a message.

- Conditional Web Redirect
  - Redirection only under specific conditions (for example password expired or payment due).

- Splash Page Web Redirect
  - User is directed to a specific splash page after joining.

CCNA scope emphasizes understanding that Layer 2 security controls association and initial access, while Layer 3 web policies operate after IP connectivity exists.

### QoS levels

WLAN QoS profiles on Cisco WLC:

- Platinum
  - Voice traffic that is sensitive to delay, loss, and jitter.

- Gold
  - Video traffic.

- Silver
  - Best effort. Default profile for standard user data.

- Bronze
  - Lowest priority. Common for guest traffic.

Internal WLAN traffic often uses Silver, while guest WLAN traffic often uses Bronze.

### Advanced settings and FlexConnect

Advanced tab examples:

- Client Load Balancing
  - Encourages clients to join less busy APs when possible.

- Client Band Select
  - Encourages dual band clients to prefer 5 GHz over 2.4 GHz.

- FlexConnect options (per WLAN)
  - FlexConnect Local Switching
    - LWAP forwards client traffic directly between wireless and wired networks without tunneling all traffic to the WLC.
  - FlexConnect Local Auth
    - LWAP can authenticate clients locally.

FlexConnect features are useful for remote sites with WAN links to a WLC in a central location.

## AP discovery and management

### AP discovery process

After booting and obtaining an IP address, an LWAP discovers WLCs using several methods:

- Broadcast discovery messages on the local LAN
- Previously joined WLCs stored in AP settings
- Manually configured WLC addresses in the AP CLI
- DHCP option 43 (provides WLC IP address)
- DNS name such as `CISCO-CAPWAP-CONTROLLER.local-domain`

The AP builds a list of candidate WLCs and then selects one to join. Exact selection rules are outside CCNA scope.

### AP join and configuration

In the Wireless tab:

- APs that have successfully joined the WLC appear with their hostnames.
- Clicking an AP name opens its configuration.
- From this screen, operational modes can be changed (Local, FlexConnect, Monitor, and others).

After joining, the AP receives:

- WLAN definitions and mappings
- Channel and power settings
- Other RF and policy settings from the WLC

### Client list

In the Monitor tab:

- Clients menu lists currently associated wireless clients.
- Entries show which WLAN each client uses and basic status information.

This provides a quick way to confirm that WLANs, interfaces, DHCP, and AP association are working as expected.

## Quick review

- Switch SW1 provides VLANs, SVIs, routing, DHCP, and NTP for the wireless lab topology.  
- WLC1 uses static LAG toward SW1 and maps VLANs to WLANs through dynamic interfaces.  
- Initial WLC configuration uses a console based wizard to set hostname, management interface, virtual gateway, country code, and basic WLAN settings.  
- Management access to the WLC can use console, Telnet, SSH, HTTP, or HTTPS and can authenticate against local users or AAA servers.  
- CPU ACLs limit which sources can manage the WLC and must allow CAPWAP traffic from valid APs.  
- WLC ports are physical, while interfaces are logical; dynamic interfaces map VLANs to WLANs.  
- WLAN configuration in the GUI requires a Profile Name, SSID, ID, Layer 2 security, optional Layer 3 web policies, QoS level, and any advanced options like FlexConnect.  
- APs discover WLCs using broadcast, DHCP option 43, DNS, and stored information, then join and download configuration, allowing clients to connect to Internal and Guest WLANs.  
