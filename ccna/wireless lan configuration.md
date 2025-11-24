# Wireless LAN Configuration

## Overview

Over the past three chapters, we've covered the fundamentals of wireless LANs, starting with the basics of radio frequency (RF) communications and 802.11 standards, various wireless LAN architectures, and the many protocols used to secure communications over the airwaves. In this chapter, we'll bring it all together and see how to configure basic wireless LANs in the graphical user interface (GUI) of a Cisco wireless LAN controller (WLC). Wireless LAN configuration is the only CCNA exam topic that requires configuration via the GUI; you could be tested on your knowledge of the WLC GUI via any of the exam question formats (multiple choice, drag-and-drop, lab simulation). When configuring a WLC that potentially manages hundreds or even thousands of lightweight APs (LWAPs), the GUI is usually the tool of choice; it provides a more user-friendly experience, simplifying the configuration, monitoring, and troubleshooting of wireless LANs.

## Network Topology

### Topology Overview

- Simple network topology consisting of one LWAP (AP1), one switch (SW1), and one WLC (WLC1)
- SW1 functions as DHCP server, NTP server, and default gateway for all subnets
- Notice that WLC1's ports are labeled P1 and P2
- Cisco WLC ports are simply called Port 1, Port 2, Port 3, etc.
- To keep diagram as simple as possible, no external connections are shown
- In real network, SW1 would likely have connections to internet, corporate WAN, larger wired LAN, etc.

### WLAN Terminology

- Network consists of two WLANs, each mapped to VLAN on wired network
- There is also dedicated management VLAN that is used for remote management of network devices
- CAPWAP tunnels between AP1 and WLC1 use this VLAN
- Like term LAN, term WLAN can have different meanings depending on context
- Example: it can refer to entire wireless network with its various APs providing BSSs and ESSs for clients using different SSIDs
- In that sense, figure depicts single WLAN consisting of two BSSs, each with unique SSID
- However, WLAN can also refer to logical entity within wireless network—not wireless network as whole
- By this definition, each SSID is its own WLAN, and figure shows two WLANs: one identified by Internal SSID and one identified by Guest SSID
- We will use this latter definition in this chapter to remain consistent with wording of Cisco WLC GUI

## Switch Configuration

### VLAN Configuration

- SW1 fulfills some important roles in this LAN: it's wired infrastructure that AP1 connects to
- DHCP server that AP1 and its wireless clients will lease IP addresses from
- NTP server that enables devices in LAN to keep consistent time
- And default gateway for hosts in each subnet
- To configure SW1, start by creating three VLANs we need:
  - VLAN 10: Management
  - VLAN 100: Internal
  - VLAN 200: Guest

### Access Port Configuration

- Because this LAN uses split-MAC architecture, AP1 should connect to SW1 via access port (F0/8) in management VLAN
- Will also configure additional access port (F0/7) for PC
- This will allow PC to connect to WLC1's GUI over network when we configure WLANs later in this chapter
- To allow ports to immediately move to Spanning Tree Protocol (STP) forwarding state, will enable PortFast as well
- Configure F0/7 and F0/8 as access ports in management VLAN
- Enable PortFast

### Trunk and LAG Configuration

- In split-MAC architecture, WLC is responsible for translating between VLANs and WLANs (SSIDs)
- So it must connect to SW1 via trunk link to support multiple VLANs
- For redundancy and additional throughput capacity, it's common to connect WLC to network via Link Aggregation Group (LAG)
- Configure SW1 F0/1 and F0/2 as members of static LAG and configure it as trunk
- Cisco WLCs use industry-standard terminology LAG instead of EtherChannel—they're same thing
- Also, note that WLCs only support static LAGs (configured with mode on)
- They cannot use negotiation protocols PAgP or LACP
- Configure F0/1 and F0/2 as members of static LAG
- Configure LAG as trunk and allow only three VLANs used in LAN

### SVI Configuration

- To function as default gateway for hosts in each subnet, SW1 needs some switch virtual interfaces (SVIs)
- Routing also must be enabled to allow SW1 to route packets between subnets
- Enable routing on SW1 and configure SVI for each of VLANs we created previously:
  - Management VLAN's SVI: 192.168.1.1/24
  - Internal WLAN/VLAN's SVI: 10.0.0.1/24
  - Guest WLAN/VLAN's SVI: 10.1.0.1/24

### DHCP and NTP Configuration

- Finally, SW1 provides couple of services to network: NTP and DHCP
- Not only will wireless clients lease their IP addresses from SW1 but so will AP1
- LWAPs' IP addresses are usually not manually configured
- Configure SW1 as NTP server and create three DHCP pools:
  - Management pool (to lease IP addresses to LWAPs)
  - Internal and Guest pools (to lease IP addresses to wireless clients)
- Note that configure two DHCP options: option 42 and option 43
- In all three pools, configure option 42, which can be used to tell DHCP clients which NTP server they should use (SW1 itself, in this case)
- Option 43 can be used to tell LWAPs IP address of their WLC
- Makes SW1 NTP server
- Creates pool for Management VLAN and assigns its IP range
- Specifies SW1 as default gateway
- Tells DHCP clients to use SW1 as their NTP server
- Tells DHCP clients (AP1) to use WLC1 as their WLC
- Configures pool for Internal WLAN/VLAN
- Configures pool for Guest WLAN/VLAN

### Key Points

- Aside from DHCP options 42 and 43, we have covered all of these configurations in previous chapters
- Main point to take away is that WLC only supports static LAG; it can't use PAgP or LACP to negotiate

## WLC Initial Configuration

### Initial Setup Overview

- SW1 is configured and ready to go, but we aren't ready to start configuring WLANs in WLC1's GUI yet
- Need to do some initial configurations on WLC1 first
- To do so, connect PC to WLC1's console port and go through Cisco Wizard Configuration Tool—series of CLI prompts
- Exam topics are clear that you need to know how to configure WLANs in GUI, not how to set up WLC from scratch
- So you can expect any WLC configuration questions to start from already-setup WLC
- However, steps in this section cover some important concepts and are essential to get WLC up and running

### Wizard Configuration Steps

- First prompt asks if you would like to terminate autoinstall
- Feature that allows WLC to automatically download its configuration from server
- Press Enter to accept default choice of yes
- System Name: Configure WLC's hostname (e.g., WLC1)
- Enter Administrative User Name: Create admin username
- Enter Administrative Password: Create admin password
- Re-enter Administrative Password: Confirm password
- Enable Link Aggregation (LAG): Enable link aggregation on WLC1's ports

### Management Interface Configuration

- Next few prompts ask for information about management interface
- Virtual interface in WLC that is used to manage it
- This is interface will connect to later to access WLC1's GUI
- Final setting (DHCP Server IP Address) allows you to specify DHCP server to which WLC will forward wireless clients' DHCP messages (SW1 in this example)
- Management Interface IP Address: Configure management interface's IP address and netmask
- Management Interface Default Router: Specify SW1 as WLC1's default gateway
- Management Interface VLAN Identifier: Configure VLAN 10 as management VLAN
- Management Interface DHCP Server IP Address: Specify SW1 as DHCP server

### Additional Configuration Settings

- Next few prompts cover some settings whose details are beyond what you need to know for CCNA exam
- But you must enter them to complete initial configuration
- Virtual Gateway IP Address: Used in communications between WLC and wireless clients and is used for specific purposes like relaying DHCP messages. Should be unique in network but doesn't have to be reachable by any other devices. Cisco recommends using address in one of ranges reserved for documentation/examples (192.0.2.0/24, 198.51.100.0/24, or 203.0.113.0/24)
- Multicast IP Address: Used by WLC to send multicast messages to clients. Should be in multicast (class D) range of 224.0.0.0 to 239.255.255.255. Specifically, should be in private ("administratively scoped") multicast range: 239.0.0.0/8
- Mobility/RF Group Name: Actually two separate settings. First is WLC's mobility group, which is used to allow multiple WLCs to coordinate to support clients that roam between APs controlled by different WLCs. RF group is used to manage and coordinate RF settings like power levels and channel selections across multiple WLCs. These are usually same group, but you can change them individually from GUI later

### WLAN and DHCP Settings

- With those three prompts out of way, remaining ones are more familiar
- In next prompt, have to create WLAN, specifying its SSID
- Will delete this later and create Internal and Guest WLANs, so named it TEST
- Network Name (SSID): TEST
- Configure DHCP Bridging Mode: Following prompt determines how WLC will handle DHCP traffic from wireless clients. If you type yes to enable bridging mode, WLC will forward clients' DHCP messages as is, simply translating 802.11 frames to Ethernet frames without any further changes. If you accept default NO option (default option is indicated with uppercase letters), WLC will function in proxy mode—basically, it will function like DHCP relay agent. Press Enter to accept default
- Allow Static IP Addresses: Wizard then asks if you want to allow clients to use static (manually configured) IP addresses or not. If you select no, all clients will be required to lease IP address via DHCP. Press enter at this prompt to accept default YES

### RADIUS and Country Code

- Next up is RADIUS server configuration, which is necessary if using WPA-Enterprise authentication with 802.1X/EAP
- CCNA exam topics state that you need to be able to configure PSK authentication (WPA-Personal), so type no here
- Configure a RADIUS Server now? \[YES\]\[no\]: no
- Wizard then prompts you for country code
- This is necessary because, as we covered in chapter on wireless LAN fundamentals, different countries have different laws governing use of RF frequency bands
- You might be tempted to enter country you live in, but if you bought secondhand hardware for home lab, need to make sure that country code you enter matches regulatory domain of APs you are using
- Regulatory domain is indicated in AP model's name, i.e., AIR-CAP3502I-E-K9
- If WLC's country code isn't in same regulatory domain as AP, WLC won't be able to manage AP
- Enter Country Code list (enter 'help' for list of countries) [US]: FR

### 802.11 Standards and Auto-RF

- Following series of prompts asks if you want to enable each of series of 802.11 standards
- Press Enter to accept default for each
- Enable 802.11b Network \[YES\]\[no\]:
- Enable 802.11a Network \[YES\]\[no\]:
- Enable 802.11g Network \[YES\]\[no\]:
- Enable Auto-RF \[YES\]\[no\]: Final Enable Auto-RF option allows WLC to automatically control each LWAP's transmit power and channel assignment—it's usually good idea to leave this on

### NTP Configuration

- We've reached final prompts!
- In following prompts, specify SW1 as WLC1's NTP server
- Configure its polling interval (how frequently WLC1 will query NTP server for time)
- And then save configuration, causing WLC1 to reboot
- Configure a NTP server now? \[YES\]\[no\]:
- Enter NTP server's IP address: 192.168.1.1
- Enter polling interval between 3600 and 604800 secs: 3600
- Configuration correct? If yes, system will save it and reset. \[yes\]\[NO\]: yes

## WLC Management Access

### Management Access Overview

- Connecting to WLC to manage and configure it is CCNA exam topic 2.8: Describe network device management access connections (Telnet, SSH, HTTP, HTTPS, console, TACACS+/RADIUS, and cloud managed)
- Now that WLC1's initial configuration is complete, can connect to it and configure some WLANs
- There are various ways to connect to and configure WLC
- In this section, we'll cover those different methods and also configure CPU ACL to restrict which devices can manage WLC

### Connection Methods

- Can configure Cisco WLC via either CLI or GUI using protocols you're already familiar with: Telnet, SSH, HTTP, HTTPS, or console connection
- WLC also has multiple methods of authenticating users who want to connect to it: its own local user database or RADIUS/TACACS+ AAA server
- WLC management connection methods
- CLI can be accessed via console port or network connection (Telnet/SSH)
- GUI can be accessed over network via HTTP/HTTPS
- WLC can authenticate users by checking its local user database or TACACS+/RADIUS server
- PC needs network access to WLC to connect via Telnet/SSH or HTTP/HTTPS
- Earlier in this chapter, configured SW1 F0/7 as access port in management VLAN
- Allowing PC to connect to network and access WLC1

### GUI Access

- Management connection and authentication methods shown apply not only to Cisco WLCs, but to other network devices as well
- Example: in addition to familiar CLI, Catalyst switches (Cisco's line of enterprise-grade switches) have GUI called Web User Interface (WebUI) that you can use for configuration and management
- However, there's reason CCNA doesn't test you on how to configure routers and switches using GUI: it is quite limited compared to CLI and is rarely used
- Instead, CLI is usually tool of choice when configuring routers and switches
- While GUI configuration for devices like routers and switches is less common, opposite is true of WLC management
- To connect to WLC1's GUI, open web browser, and type IP address of WLC's management interface (192.168.1.100) in address bar
- After logging in with admin username/password, you'll be greeted with screen like that shown
- Cisco WLC GUI
- Image of WLC is displayed, showing active and inactive ports
- WLC settings are organized into various tabs at top

### GUI Tabs

- This first screen is Monitor tab, which shows overview of system's status (such as active and inactive ports)
- WLC's settings are organized into various tabs at top of screen, and we will use six of them:
  - Monitor: Provides overview of system status and client/AP statistics
  - WLANs: Manages individual WLAN settings including SSID configuration, security, QoS, and advanced WLAN features
  - Controller: Configures global settings for WLC itself, like network interfaces, IP addresses, NTP, etc.
  - Wireless: Settings related to LWAPs managed by WLC
  - Security: Security settings like ACLs and authentication methods
  - Management: WLC management settings like management connections (Telnet, SSH, HTTP, HTTPS, console), SNMP, and Syslog

### Management Tab Configuration

- To configure and verify WLC's management settings, first click Management tab at top of screen
- From Management tab, can see which kinds of connections are allowed by default
- By default, HTTP, HTTPS, and SSH connections are allowed—Telnet connections aren't
- Can change these settings from HTTP-HTTPS and Telnet-SSH menus on left
- Example: might want to disable HTTP connections because HTTP isn't secure protocol; it doesn't encrypt messages
- Management tab
- HTTP, HTTPS, and SSH connections are allowed by default, but Telnet connections aren't
- Can change these settings from HTTP-HTTPS and Telnet-SSH menus on left

### Authentication Methods

- WLC can authenticate users using its local user database (i.e., admin account created during initial configuration)
- RADIUS server, or TACACS+ server (or some combination of those three)
- To check default settings, click Security tab, expand Priority Order dropdown menu, and then select Management User
- Default management user authentication methods
- WLC will authenticate users by checking its local user database and, if that fails, by contacting its configured RADIUS server(s)
- When user tries to log in, WLC will check user's credentials against local user database
- If no matching credentials are found, it will check any configured RADIUS servers
- If both methods fail, user won't be able to log in
- Can change which authentication methods are used, and in which order, from this screen

### CPU ACL Configuration

- In addition to Management User menu, Security tab includes various other security-related menus
- Notably, if using WPA-Enterprise authentication, can configure relevant RADIUS settings from AAA dropdown menu
- Will stick to CCNA exam topics, so won't look at AAA menu
- But let's look at Access Control Lists dropdown menu to secure access to WLC with CPU ACL
- When covering Telnet and SSH, looked at how to configure ACL and apply it to VTY lines of router or switch to limit which hosts can connect to and configure device
- Can do same thing on WLC with CPU ACL
- ACL that filters traffic destined for WLC itself, such as HTTP/HTTPS/Telnet/SSH management connections
- There are two steps to configuring CPU ACL: create ACL, and then apply it as CPU ACL

### Creating ACL

- Creating new ACL
- From Security tab, expand Access Control Lists dropdown menu, and click Access Control Lists
- Click New… to create ACL (will be prompted for ACL's name)
- And then click ACL's name (MGMT) to edit it and configure some rules
- Clicking newly created ACL's name brings you to Edit page
- From which can create new rule by clicking Add New Rule at top right
- When covering ACLs, used term access control entry (ACE) for each of entries in ACL
- WLC GUI uses term rule
- Can specify rule's parameters
- To secure management access to WLC, create rule permitting only IP addresses in Management subnet (192.168.1.0/24)
- To finish configuring rule, click Apply

### Applying CPU ACL

- Like routers and switches, WLC's ACLs have "implicit deny" rule at end
- Any packets not explicitly permitted by ACL (packets not sourced from Management subnet) will be denied
- So there's no need to configure any further rules
- One rule configured permits Management subnet, and implicit deny blocks all other traffic
- Have now created ACL—all that's left is to apply it
- To do so, click CPU Access Control Lists under same Access Control Lists dropdown menu
- Check Enable CPU ACL box, select ACL's name, and click Apply
- In addition to filtering HTTP/HTTPS/Telnet/SSH management traffic to WLC, CPU ACL also filters CAPWAP traffic from LWAPs to WLC
- When configuring CPU ACL, make sure you don't deny CAPWAP traffic from legitimate LWAPs!

## WLC Ports and Interfaces

### Ports vs Interfaces

- Now that we've connected to WLC1's GUI and secured it with CPU ACL
- Are almost ready to configure Internal and Guest WLANs—but not quite
- Each WLAN needs interface on WLC that serves to connect WLAN to VLAN on wired network
- In this section, we'll examine different port and interface types on WLC
- And then configure dynamic interfaces to map WLANs to VLANs
- In chapter on router and switch interfaces, said that terms port and interface are often used interchangeably
- This is generally true, but in context of Cisco WLCs, they are strictly different
- WLC port is physical port—typically RJ45 port—that cables connect to
- WLC interface is logical entity in WLC, like SVI on switch
- WLC ports and interfaces
- Ports are physical connectors that connect to other devices
- And interfaces are logical entities in WLC

### Physical Port Types

- Console port: Standard console port like on router or switch (RJ45 or USB)
- Service port: Dedicated management port. Can be used for out-of-band (OOB) management—connecting to and managing WLC via dedicated connection that is separate from DS ports. Service port doesn't support VLAN tagging; it must connect to access port on switch
- Redundancy port: Used to connect two WLCs together to form redundant pair
- Distribution system port: Standard network ports that connect to distribution system (DS). DS ports can form LAG for increased bandwidth and redundancy. WLC1's LAG connection to SW1 in our example uses DS ports (Port 1 and Port 2)
- Note that not all WLC models have all of these port types
- WLC model used for this chapter only has one console port and four DS ports—no service or redundancy ports
- In section on initial setup, connected PC directly to WLC1's console port to perform initial configuration
- WLC1's two connections to SW1, which form LAG, are DS ports
- If enable link aggregation (as we did in WLC1's initial configuration), all of WLC's DS ports will be included in LAG
- However, don't need to use all of ports; as long as there is at least one functioning physical port in LAG, it will be operational

### Logical Interface Types

- Whereas ports are physical, interfaces are logical entities
- Cisco WLCs have variety of interface types, each used for specific purposes: connecting to and managing WLC, mapping WLANs to VLANs, communicating between WLC and its APs, etc.
- Different interface types are as follows:
  - Management interface: Default interface for in-band management; maps to management VLAN (VLAN 10 in this chapter's network) and sends and receives traffic via same DS ports as other network traffic
  - AP-manager interface: Interface that WLC uses to communicate with LWAPs via CAPWAP tunnels. Management interface acts as AP-manager interface by default, but can optionally configure separate AP-manager interface to separate CAPWAP traffic from other management traffic (SSH, etc)
  - Redundancy management interface: When two WLCs are connected by their redundancy ports, one WLC is "active" and other is "standby." This interface can be used to connect to and manage standby WLC
  - Service-port interface: Interface corresponds to physical service port and is used for OOB management
  - Virtual interface: Virtual Gateway IP Address configured during WLC1's initial configuration is applied to this interface. Used for specific purposes like relaying client DHCP messages
  - Dynamic interface: Dynamic interface is similar to SVI on switch. Each dynamic interface is mapped to VLAN and corresponding WLAN. Example: traffic from Internal WLAN will be sent to wired network from WLC's Internal dynamic interface, tagged in appropriate VLAN

### Creating Dynamic Interfaces

- Each WLAN must be mapped to corresponding dynamic interface
- In this section, we'll create two dynamic interfaces we need: one for Internal WLAN and one for Guest WLAN
- Creating new dynamic interface
- From Controller tab, click Interfaces menu, and then click New… to create new interface
- Will only look at Interfaces menu, but Controller tab includes various other settings related to WLC itself: IP addresses, Ports, DHCP and NTP settings, etc.
- First screen prompts for interface name and VLAN ID
- Although not necessary, recommend keeping interface, VLAN, and WLAN naming consistent for simplicity's sake
- Named this interface Internal and assigned it to VLAN 100
- To move to next screen, click Apply
- Next screen, can configure interface's IP address, netmask, and gateway
- Address of router (or multilayer switch, in this case) that can be used to reach external destinations
- After that, can specify DHCP server that WLC should forward client DHCP messages to
- In this case, gateway and DHCP server are both SW1's VLAN 100 SVI
- After creating dynamic interface for Internal WLAN, can repeat same process for Guest WLAN's dynamic interface
- When done, will see both interfaces displayed alongside Management and Virtual interfaces in Interfaces menu's list

## WLAN Configuration

### Creating WLANs

- Now that have created two dynamic interfaces, can create our two WLANs
- When performing WLC1's initial configuration, wizard prompted us to create WLAN—named it TEST
- Instead of editing that WLAN, will delete it and start from clean slate
- Deleting TEST WLAN (created during initial configuration) and creating new WLAN
- From WLANs tab, select TEST WLAN, select Remove Selected from dropdown menu, and click Go
- Then, to create new WLAN, select Create New, and click Go once again

### WLAN Identifiers

- Next page asks for three different identifiers for WLAN: Profile Name, SSID, and ID
- SSID is name of WLAN as seen by clients
- Profile Name and ID aren't seen by clients; they are used only by WLC
- Profile Name can be any descriptive name—kept it same as SSID
- Finally, ID is unique numeric identifier
- After configuring these three settings, click Apply to move to next screen
- Configuring Profile Name, SSID, and ID of WLAN

### General Tab Configuration

- Next page shows series of tabs allowing you to configure various aspects of WLAN
- Starting with General tab
- There are two main things to point out here
- First, make sure to check Status box to enable WLAN; if don't do this, WLAN will be disabled and clients won't be able to connect to it
- Second, make sure to select appropriate interface
- This is Internal WLAN, so selected Internal dynamic interface that we created earlier
- General tab on WLANs page
- Make sure to enable WLAN, and select appropriate interface

### Security Tab Configuration

- Let's configure Internal WLAN's security settings next
- Security tab has its own series of tabs, starting with Layer 2
- This is where configure settings like WPA authentication and encryption
- These are considered Layer 2 security settings because they control client's access to LAN before client has its own IP address and is able to participate in Layer 3 communication
- WLAN Layer 2 security settings
- For CCNA, must configure WPA2 with PSK authentication
- CCNA exam topic 5.10 says that must be able to configure WPA2 PSK authentication, so that's what we'll do
- From top dropdown menu, select WPA + WPA2
- Also highlighted Protected Management Frame (PMF); as stated in chapter on wireless LAN security, PMF is mandatory in WPA3 but can optionally be enabled in WPA2 to secure management frames
- Will leave it disabled since it's optional
- Under WPA + WPA2 Parameters, make sure that WPA2 Policy and AES Encryption are checked
- Original WPA is no longer considered secure, and neither is TKIP; leave them disabled
- Finally, under Authentication Key Management, notice that 802.1X is enabled by default
- CCNA exam topics list specifies PSK authentication, so change 802.1X to PSK
- Enabling PSK authentication
- PSK can be configured as 8- to 63-character ASCII passphrase or 64-character hexadecimal string
- As covered in chapter on wireless LAN security, PSK is 256 bits in length
- Can configure it as string of 64 hexadecimal characters, but it's much easier to configure 8- to 63-character ASCII passphrase
- Wi-Fi password that users will use to authenticate
- WLC will convert passphrase into 256-bit PSK for you

### Layer 3 Security

- From Layer 3 tab, can configure additional security measures that take place after client has connected to network and received IP address
- Hence name Layer 3
- Select Web Policy to view options
- Layer 3 security measures take effect after client has completed any Layer 2 security measures and has IP address
- Authentication: After client receives IP address and tries to access web page, user will have to enter username and password to authenticate
- Passthrough: User can access network after accepting certain terms and conditions or viewing mandatory message. No actual authentication is performed (although email address might be required)
- Conditional Web Redirect: User will be redirected to specific web page only under certain conditions (i.e., their password has expired or they need to pay bill to continue using network)
- Splash Page Web Redirect: Client is shown particular web page upon connecting to network
- Although don't have to know details of these Layer 3 security measures, recommend being able to differentiate between Layer 2 (WPA with PSK or 802.1X) and Layer 3 (web policies like passthrough or redirects) security measures

### QoS Configuration

- Next tab on WLANs page after Security is QoS
- Wireless QoS is its own can of worms that don't have to open for CCNA
- However, should know four QoS levels supported by Cisco WLC
- Four QoS levels: Platinum, Gold, Silver, and Bronze
- Dropdown menu gives brief description of each
- For Internal WLAN that we are configuring, default Silver level is appropriate
- For Guest WLAN, Bronze is appropriate; this gives guest user traffic lower priority than internal user traffic
- Platinum: Used for voice (VoIP) traffic, which is sensitive to delay/loss/jitter
- Gold: Used for video traffic
- Silver: Described as "best effort"; this is default setting and should be used for standard user data traffic
- Bronze: This is lowest level of service. Should be used for guest services or other low-priority traffic

### Advanced Tab Configuration

- After QoS, will skip Policy-Mapping and move on to final tab: Advanced
- Many different settings can be enabled here
- Let's highlight few of them:
  - Client Load Balancing: If client tries to associate with busy LWAP (with lots of clients) and another less-busy LWAP is in range, WLC's response will encourage client to seek less-busy LWAP
  - Client Band Select: If client supports both 2.4 GHz band and 5 GHz band, LWAPs will delay responses to probes in 2.4 GHz band, encouraging client to use 5 GHz band, which is usually less crowded with devices
- Advanced tab allows you to enable features like Client Load Balancing and Client Band Select
- However, there's more to advanced tab
- Scrolls down bit to where can enable familiar feature: FlexConnect
- As covered in chapter on wireless LAN architectures, FlexConnect can be enabled per WLAN
- FlexConnect Local Switching means that LWAP can switch client traffic between wired and wireless networks on its own
- No need to tunnel it to WLC
- FlexConnect Local Auth allows LWAP to authenticate clients on its own, instead of relying on WLC
- FlexConnect features can be enabled on per-WLAN basis from Advanced tab
- As can see, there are plenty of other features in Advanced tab
- But recommend knowing few that we covered
- Once all configurations are complete, click Apply button at top right

### WLAN Summary

- We've walked through how to configure Internal WLAN; process to configure Guest WLAN is same
- WLANs tab with Internal and Guest WLANs, both of which use WPA2 with PSK authentication

## AP Discovery and Management

### AP Discovery Process

- With Internal and Guest WLANs configured, let's see what happens when connect LWAP (AP1) to network
- After connecting AP1 to SW1, waited for few minutes for it to boot up
- Result: in Wireless tab of WLC1's GUI, AP1 is listed
- Without any manual configuration of AP1, it joined with and is now managed by WLC1
- AP1 (with its default hostname) automatically joined with and is managed by WLC1 without any manual configuration

### Discovery Methods

- After AP boots up and gets IP address, it begins WLC discovery process
- In which it attempts to discover any available WLCs
- It uses various methods to do this:
  - Sending broadcast discovery messages to LAN
  - Contacting any WLCs it had previously joined
  - Contacting any WLCs it learned about via manual configuration (in AP's CLI)
  - Contacting any WLCs it learned about via DHCP option 43
  - Using DNS to attempt to resolve CISCO-CAPWAP-CONTROLLER.local-domain and contacting any WLCs if resolution succeeds
- After using these methods to discover WLCs, AP will then decide to join one
- Logic it uses to select WLC isn't important for CCNA
- In our network, there is one WLC (WLC1), and it is located in same LAN as AP1
- This means that WLC1 receives AP1's broadcast discovery messages
- Furthermore, also configured DHCP option 43 in SW1's DHCP pool
- So AP1 also learns WLC1's IP address when it leases IP address from SW1

### AP Configuration

- Let's change AP's name from default name to AP1
- To modify AP's settings, click AP name to see screen shown
- In addition to being able to change AP's name, this is where can change AP's operational mode
- Should recognize these modes from chapter on wireless LAN architectures: local, FlexConnect, monitor, etc.
- AP configuration screen
- From here, can change AP's name, configuration mode, and various other settings
- After joining with WLC1, AP1 receives its configuration information from WLC1
- Including two WLANs we configured, which bands and channels it should use, its transmit power, etc.
- AP1 and WLC1 are now ready to accept clients!

### Client List

- WLC1's client list after connecting client to each of WLANs
- Can view client list by returning to MONITOR tab and clicking on Clients menu on left
- WLC1's client list, with one client connected to each WLAN
- As probably noticed when looking through these screenshots of GUI, there are countless tabs, menus, and settings that can configure from GUI
- Most of which we skipped over
- Settings we covered are essentials that should know for CCNA
- Recommend spending some time in GUI familiarizing yourself with them

## Real-World Applications

- **Enterprise wireless deployment**: Configuring WLCs to manage large-scale wireless networks
- **Multi-VLAN wireless networks**: Mapping WLANs to different VLANs for network segmentation
- **Guest network access**: Providing secure guest access with appropriate QoS and security policies
- **Centralized management**: Managing hundreds of APs from single WLC
- **Network security**: Implementing CPU ACLs and proper authentication methods

## Troubleshooting

### Common Issues

- **AP not joining WLC**: Verify CAPWAP connectivity, DHCP option 43, and discovery methods
- **Client connectivity problems**: Check WLAN configuration, security settings, and interface mapping
- **DHCP issues**: Verify DHCP server configuration and WLC proxy mode settings
- **Management access**: Check CPU ACL and management interface configuration

### Troubleshooting Steps

1. Verify WLC connectivity: Check management interface and network connectivity
2. Check AP discovery: Verify DHCP option 43 and discovery methods
3. Review WLAN configuration: Check SSID, security, and interface mapping
4. Test client connectivity: Verify client can associate and authenticate
5. Check DHCP: Verify DHCP server and WLC proxy mode configuration

## Best Practices

- Use static LAG for WLC connections (WLCs don't support PAgP or LACP)
- Configure DHCP option 43 for AP discovery
- Use separate management VLAN for network devices
- Enable CPU ACLs to secure management access
- Configure appropriate QoS levels for different WLANs
- Use WPA2 or WPA3 for security
- Document WLC and WLAN configurations
- Test client connectivity after configuration

## Summary

- WLC usually connects to network via Link Aggregation Group (LAG)—industry-standard term for EtherChannel
- Cisco WLCs only support static LAGs; they cannot use negotiation protocols PAgP or LACP
- DHCP option 42 can be used to tell DHCP clients which NTP server they should use
- DHCP option 43 can be used to tell LWAPs IP address of their WLC
- Before can create WLANs via WLC GUI, need to perform some initial configurations
- Can do so with Cisco Wizard Configuration Tool in CLI by connecting to WLC's console port
- Initial configuration includes settings like management interface; this is interface can connect to in order to access WLC's GUI
- Virtual Gateway IP Address is used in communications between WLC and wireless clients, such as when relaying DHCP messages
- Should be unique on network but doesn't have to be reachable by other devices
- Multicast IP Address is used by WLC to send multicast messages to clients
- Mobility/RF Group Name configures mobility group, which is used to allow multiple WLCs to coordinate to support roaming clients
- And RF group, which is used to manage and coordinate RF settings across multiple WLCs
- If enable DHCP bridging mode, WLC will forward clients' DHCP messages as is, simply translating 802.11 frames to Ethernet frames
- If disable bridging mode, WLC will function in proxy mode, like DHCP relay agent
- WLC's country code must match regulatory domain of LWAPs it manages
- There are various methods to connect to and manage WLC
- Can access CLI via console port or over network via Telnet/SSH
- Can access GUI over network via HTTP/HTTPS
- WLC can authenticate users with its own local user database or by using RADIUS/TACACS+ AAA server
- To connect to WLC's GUI, open web browser, and type IP address of its management interface in address bar
- From Management tab, can view and modify which kinds of management connections are allowed
- By default, HTTP, HTTPS, and SSH connections are allowed, but Telnet connections aren't
- To view and modify WLC's management user authentication methods and their order, go to Security tab, open Priority Order dropdown menu, and access Management User menu
- Can configure CPU ACL in Security tab to filter traffic to and from WLC itself, such as management and CAPWAP traffic
- To configure CPU ACL, expand Access Control Lists dropdown menu, create ACL in Access Controls Lists menu, and apply it in CPU Access Control Lists menu
- WLC port is physical port, and WLC interface is logical entity in WLC
- Console port is standard console port like on router or switch
- Service port is dedicated out-of-band (OOB) management port
- It doesn't support VLAN tagging, so it must connect to access port on switch
- Redundancy port is used to connect two WLCs to form redundant pair
- Distribution system (DS) ports are standard network ports that connect to distribution system
- If enable link aggregation, all of WLC's DS ports will be included in LAG by default
- As long as there is at least one functioning physical port in LAG, it will be operational
- Management interface is default interface for in-band management
- It maps to management VLAN and sends and receives traffic via DS ports
- AP-manager interface is used by WLC to communicate with LWAPs via CAPWAP
- By default, management interface functions as AP-manager interface, but can configure separate AP-manager interface
- Redundancy management interface is used to connect to and manage standby WLC in redundant pair
- Service-port interface corresponds to physical service port
- Virtual interface is used for specific purposes like DHCP relay; Virtual Gateway IP Address is applied to this interface
- Dynamic interface is similar to SVI on switch
- Each dynamic interface is mapped to VLAN and corresponding WLAN
- Before creating WLANs, must create dynamic interface for each WLAN
- Can create dynamic interfaces from Interfaces menu of Controller tab
- Can create WLANs from WLANs tab
- Each WLAN has three identifiers: SSID is name as seen by clients
- Profile Name can be any descriptive name (or same as SSID), and ID is unique numeric identifier
- When creating WLAN, Security tab allows you to configure settings like WPA authentication/encryption, which are Layer 2 security settings
- Can configure PSK as 64 hexadecimal characters or 8- to 63-bit ASCII passphrase
- Layer 3 tab allows you to configure web policy security features that require clients to perform additional actions/authentication before accessing network
- Such as Authentication, Passthrough, Conditional Web Redirect, and Splash Page Web Redirect
- QoS tab allows you to specify WLAN's QoS level
- Levels are Platinum (voice), Gold (video), Silver (best effort, default), and Bronze (background)
- Advanced tab allows you to configure various optional features
- Client Load Balancing encourages clients to associate with less busy LWAPs
- Client Band Select encourages clients to use 5 GHz band instead of 2.4 Ghz band
- FlexConnect can be enabled from Advanced tab
- FlexConnect Local Switching means LWAP can switch client traffic between wired and wireless networks on its own—no need to tunnel it to WLC
- FlexConnect Local Auth allows LWAP to authenticate clients on its own
- Can view LWAPs that WLC controls from Wireless tab
- After AP boots up and gets IP address, it brings WLC discovery process, in which it attempts to discover WLCs before joining with one
- Discovery methods include broadcast discovery messages, previously joined WLCs, manual configuration, DHCP option 43, and DNS
- Can configure AP's operational mode (local, FlexConnect, monitor, etc.) by clicking on AP name in Wireless tab
- Can view list of wireless clients from Clients menu in Monitor tab
