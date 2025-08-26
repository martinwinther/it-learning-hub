# Network Security Infrastructure

## Overview

Network security infrastructure provides the foundation for protecting organizational
networks and data. It encompasses physical security, network devices, security zones,
and access controls that work together to create a secure network environment.

## Data Center Protection

### Environmental Threats

Data centers should be carefully managed to protect the equipment that they contain.
This includes maintaining temperature and humidity levels using heating, ventilation,
and air conditioning (HVAC) systems and maintaining fire suppression controls.

### Temperature Control

- **Air Temperature**: Generates a lot of heat and needs to be cooled down
- **Optimal Range**: Should be between 64.4 and 80.6 degrees Fahrenheit as specified
  by the American Society of Heating, Refrigerating and Air Conditioning (ASHRAE)
- **HVAC Systems**: Heating, ventilation, and air conditioning (HVAC) helps with
  temperature control
- **Monitoring**: Continuous temperature monitoring and alerting

### Humidity Management

- **Condensation Risk**: Condensation forms if humidity is too high
- **Dew Point**: Should be between 41.9 and 50.0 degrees Fahrenheit
- **HVAC Control**: HVAC systems help maintain proper humidity levels
- **Monitoring**: Continuous humidity monitoring and control

### Fire Suppression

- **Fire Triangle**: Fire needs heat, oxygen, and fuel
- **Suppression Methods**: Fire fighting deprives one of these three elements
- **Water Systems**: Most commonly used, but water is damaging to electronics
- **Chemical Systems**: Chemicals can also be used, but dangerous with people in
  the room
- **Gas Systems**: Clean agent systems for sensitive equipment

### Power Considerations

- **Uninterruptible Power Supply (UPS)**: Backup power for critical systems
- **Generator Systems**: Long-term power backup
- **Power Monitoring**: Continuous power monitoring and alerting
- **Redundant Power**: Multiple power sources for critical equipment

## Network Security Zones

### Zone Architecture

A well-designed network uses firewalls to split the network into network security
zones: Internet, Intranet, and DMZ.

#### Internet Zone

- **Purpose**: Connects the organization to the Internet
- **Security Level**: Lowest trust level
- **Traffic**: All external internet traffic
- **Protection**: Strong filtering and monitoring

#### Intranet Zone

- **Purpose**: Hosts internal systems
- **Security Level**: Highest trust level
- **Traffic**: Internal organizational traffic
- **Protection**: Internal security controls

#### DMZ (Demilitarized Zone)

- **Purpose**: Hosts systems that can be accessed by the general public
- **Security Level**: Intermediate trust level
- **Services**: Web servers, email servers, public-facing applications
- **Protection**: Controlled access and monitoring

## Network Devices

### Routers and Switches

Routers and switches are the devices that form the backbone of the modern network.
Networked devices connect to a switch via a network cable or to a wireless access
point via a Wi-Fi connection. Switches connect to each other and to routers.
Routers send traffic between switches on the internal network and the Internet.

#### Switches

- **Function**: Switches connect devices to the network
- **Operation**: Layer 2 devices that forward traffic based on MAC addresses
- **Types**: Access switches, distribution switches, core switches
- **Security**: Port security, VLAN support, access control

#### Wireless Access Points (WAPs)

- **Function**: Connect devices to the network wirelessly
- **Standards**: Wi-Fi 6, Wi-Fi 5, Wi-Fi 4
- **Security**: WPA2/WPA3 encryption, authentication
- **Management**: Centralized wireless controller management

#### Routers

- **Function**: The central point for all network traffic
- **Operation**: Layer 3 devices that route traffic between networks
- **Routing**: Sends traffic around the network and to the Internet
- **Security**: Access control lists, routing security

### Network Device Security

- **Access Control**: Secure administrative access to network devices
- **Configuration Management**: Secure configuration and change management
- **Monitoring**: Continuous monitoring of network device activity
- **Updates**: Regular firmware and software updates

## Firewalls

### Firewall Overview

Firewalls are security devices that restrict the traffic that can enter and leave
a network. Border firewalls connect three zones. The Internet zone connects the
organization to the Internet. The intranet zone hosts internal systems. The DMZ
hosts systems that can be accessed by the general public.

### Firewall Types

- **Packet Filtering**: Basic packet-level filtering
- **Stateful Inspection**: Tracks connection state
- **Application Layer**: Deep packet inspection
- **Next-Generation**: Advanced features like IPS, application control

### Firewall Deployment

- **Border Firewalls**: Protect network perimeter
- **Internal Firewalls**: Segment internal networks
- **Host-Based Firewalls**: Protect individual systems
- **Cloud Firewalls**: Protect cloud environments

### Firewall Configuration

- **Rule Sets**: Define allowed and denied traffic
- **Default Deny**: Deny all traffic by default, allow only necessary traffic
- **Logging**: Comprehensive logging of all traffic
- **Monitoring**: Continuous monitoring of firewall activity

## Network Segmentation

### VLANs (Virtual Local Area Networks)

VLANs enable you to group together related systems logically, regardless of where
they normally exist on the network. For example, you can group together two HR
users that are in separate buildings into the same VLANs.

#### VLAN Benefits

- **Logical Grouping**: Group systems by function, not location
- **Security**: Isolate different types of traffic
- **Performance**: Reduce broadcast traffic
- **Management**: Easier network management

#### VLAN Types

- **Data VLANs**: Regular user traffic
- **Voice VLANs**: Voice over IP traffic
- **Management VLANs**: Network management traffic
- **Guest VLANs**: Guest and visitor traffic

### Segmentation Implementation

Network segmentation separates systems into networks consisting of similar systems.

#### Segmentation Benefits

- **Security**: Isolate different security zones
- **Compliance**: Meet regulatory requirements
- **Performance**: Optimize network performance
- **Management**: Simplify network management

## Virtual Private Networks (VPNs)

### VPN Types

Two types of VPNs:

#### Site-to-Site VPN

- **Purpose**: Secure interconnection of remote networks
- **Use Case**: Connecting office branches
- **Configuration**: Permanent connection between sites
- **Security**: Encrypted tunnel between networks

#### Remote Access VPN

- **Purpose**: Allows a mobile worker to connect to the office network remotely
- **Use Case**: Telecommuting, business travel
- **Configuration**: On-demand connections
- **Security**: Encrypted tunnel from remote location

### VPN Technology

- **Virtual Tunnel**: Creates a virtual tunnel between two systems over the
  internet
- **Encryption**: Strong encryption for data protection
- **Authentication**: Secure authentication mechanisms
- **Protocols**: IPsec, SSL/TLS, OpenVPN

### VPN Endpoints

Requires VPN endpoint on the receiving network, such as:

- **Firewall**: Integrated VPN capabilities
- **Router**: Router-based VPN termination
- **Server**: Dedicated VPN server
- **VPN Concentrator**: Dedicated VPN concentrator

**Performance Consideration**: Using the router, firewall, or server can cause
performance issues with a lot of connections as it requires intensive encryption.

## Network Access Control (NAC)

### NAC Overview

Network access control (NAC) technology intercepts network traffic from devices
that connect to a wired or wireless network and verifies that the system and user
are authorized to connect to the network before allowing them to communicate with
other systems.

### NAC Components

Often uses 802.1x authentication with three components:

#### Supplicant

- **Definition**: The device that wants to connect
- **Function**: Provides authentication credentials
- **Examples**: Workstations, laptops, mobile devices
- **Software**: 802.1x supplicant software

#### Authenticator

- **Definition**: The switch or wireless controller the device connects to
- **Function**: Controls access to the network
- **Examples**: Network switches, wireless controllers
- **Operation**: Enforces access control based on authentication results

#### Authentication Server

- **Definition**: The backend authentication server
- **Function**: Verifies credentials and makes access decisions
- **Examples**: RADIUS servers, Active Directory
- **Protocol**: RADIUS (Remote Authentication Dial-In User Service)

### NAC Process

Here's how they work together:

1. **Connection Attempt**: A user with a NAC supplicant attempts to join the
   network by plugging into a network jack, connecting to a VPN, or connecting
   to a wireless network.

2. **Credential Provision**: The NAC supplicant provides the authenticator with
   the required authentication credentials.

3. **Credential Forwarding**: When the authenticator receives those credentials,
   it passes them along to the authentication server for verification. This
   happens over a RADIUS connection.

4. **Access Grant**: If the credentials are authentic, the authentication server
   sends the authenticator a RADIUS Access-Accept message and the authenticator
   allows the device to access the network.

5. **Access Denial**: If the credentials don't verify correctly, the
   authentication server sends a RADIUS Access-Reject message and the user is
   often prompted to try again.

### Advanced NAC Features

#### Role-Based Access Control (RBAC)

- **Function**: After the user is verified, it also decides where to place the
  user on the network based on their identity
- **Implementation**: Assign users to VLANs based on role
- **Benefits**: Network access based on job function
- **Management**: Centralized role management

#### Posture Checking

- **Definition**: Also known as endpoint compliance checking
- **Function**: Verifies that the connecting device adheres to the
  organization's security policy before granting access
- **Checks**:
  - Does the device have antivirus?
  - Does the antivirus have current signatures?
  - Does it have a firewall?
  - Does it have security patches?

**Quarantine**: If it fails, it might be put in a quarantine VLAN where access
is limited to internal resources but may have internet access.

## Internet of Things (IoT)

### IoT Security Challenges

- **Update Difficulties**: Difficult for the consumer to update
- **Network Access**: Connects to the same network as the user's other devices
- **Cloud Connectivity**: Connects back to cloud services
- **Limited Security**: Often lacks basic security features

### IoT Network Segmentation

Place them within a secure network environment that is designed to protect smart
devices from attack. Use network segmentation. Same concept as DMZ.

#### IoT Security Measures

- **Network Isolation**: Separate IoT devices from critical systems
- **Access Control**: Restrict IoT device access to necessary services
- **Monitoring**: Monitor IoT device network activity
- **Updates**: Regular firmware updates when available

#### IoT Security Best Practices

- **Change Defaults**: Change default passwords and settings
- **Network Segmentation**: Isolate IoT devices on separate networks
- **Access Control**: Limit IoT device access to necessary services
- **Monitoring**: Monitor IoT device behavior and network activity
- **Updates**: Keep IoT devices updated when possible

## Network Security Monitoring

### Monitoring Tools

- **Network Monitoring**: Monitor network traffic and performance
- **Security Monitoring**: Monitor for security threats and incidents
- **Log Analysis**: Analyze network and security logs
- **Alerting**: Automated alerting for security events

### Security Information and Event Management (SIEM)

- **Centralized Logging**: Collect logs from all network devices
- **Correlation**: Correlate events across multiple sources
- **Alerting**: Generate alerts for security incidents
- **Reporting**: Generate security reports and dashboards

## Real-World Applications

### Enterprise Networks

- **Comprehensive Security**: Multi-layered security controls
- **Network Segmentation**: Logical separation of systems
- **Access Control**: Strong authentication and authorization
- **Monitoring**: Continuous security monitoring

### Small Business Networks

- **Basic Security**: Essential security controls
- **Simplified Management**: Easy-to-manage security solutions
- **Cost-Effective**: Affordable security options
- **Scalable**: Solutions that can grow with the business

### Cloud Networks

- **Cloud-Native Security**: Security designed for cloud environments
- **API Security**: Protection for cloud APIs
- **Identity Management**: Cloud-based identity and access management
- **Compliance**: Cloud security compliance frameworks

## Best Practices

### For Network Administrators

- **Documentation**: Maintain comprehensive network documentation
- **Change Management**: Follow change management procedures
- **Monitoring**: Continuous monitoring of network security
- **Updates**: Regular updates of network devices and security tools
- **Training**: Regular training on network security

### For Organizations

- **Security Policies**: Develop comprehensive network security policies
- **Risk Assessment**: Regular assessment of network security risks
- **Incident Response**: Establish network security incident response
  procedures
- **Compliance**: Ensure compliance with relevant regulations
- **Training**: Regular security awareness training

## Summary

Effective network security infrastructure requires:

- **Physical Security**: Proper data center protection and environmental
  controls
- **Network Design**: Well-designed network architecture with security zones
- **Device Security**: Secure configuration and management of network devices
- **Access Control**: Strong network access controls and authentication
- **Monitoring**: Continuous monitoring and security oversight

Key success factors:

- **Defense in Depth**: Multiple layers of security controls
- **Regular Updates**: Keep systems and security measures current
- **User Awareness**: Educate users on network security
- **Incident Response**: Ability to respond quickly to security incidents
- **Continuous Improvement**: Regular assessment and improvement of security
  measures

Understanding network security infrastructure is essential for cybersecurity
professionals and helps organizations build secure, reliable network environments.
