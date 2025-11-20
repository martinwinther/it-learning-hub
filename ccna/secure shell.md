# Secure Shell

## Overview

Secure Shell (SSH) allows you to securely connect to devices over an IP network such as the internet. SSH is an essential protocol for managing networks, allowing you to remotely configure and verify devices without being physically near them. While console port access requires physical proximity, SSH enables remote management from anywhere on the network. SSH encrypts communications between the client and server, providing security that protocols like Telnet lack. SSH is the standard method for remote device management in modern networks.

## Securing Console Access

### Physical Access Control

- Anyone with laptop and console cable can access device's CLI via console port
- Not acceptable from security standpoint
- Important step: physical access control—controlling who has physical access to device
- Example: keep device in locked cabinet
- Physical access control alone is not sufficient

### Console Line Security

- When connecting via console port, you connect to console line
- Line is logical pathway on Cisco device that allows connection to and management via CLI
- Console line used when connecting via console port
- Use `line con 0` in global config mode to configure console line
- Only one console line exists (line con 0); only one user can connect at once

### Line Password Authentication

- Simplest way to secure console line: configure password on it
- After user connects to console port, they must enter password to access CLI
- Use `password password` in line config mode to configure line password
- Use `login` command to require users to enter password
- Without `login` command, password doesn't take effect
- After entering password, user brought to user EXEC mode
- User can then use `enable` command to access privileged EXEC mode

### User Account Authentication

- Instead of line password, can configure user accounts
- Use `username username secret password` to create account
- Password saved as secure hash thanks to `secret` keyword
- Use `login local` in line config mode to require user account authentication
- More secure than simple line password
- Allows for more granular access control
- Allows tracking of each user's activity on device
- Can use `username username password password` but password saved in cleartext (not recommended)

### Login Commands

- `login` and `login local` cannot be configured at same time
- If `login` is set, users must authenticate with line password
- If `login local` is set, users must authenticate with user account
- User account authentication generally preferred over line password

### Privilege Levels

- Cisco IOS uses privilege levels to control user's access to CLI commands
- 16 privilege levels: 0 to 15
- Default: users connecting via console or VTY lines have privilege level 1 (user EXEC mode)
- After using `enable` command, user given privilege level 15 (privileged EXEC mode)
- Can specify user's default privilege level: `username username privilege level secret password`
- Example: `username jeremy privilege 15 secret ccna` grants privilege level 15 immediately
- Remaining privilege levels (2-14) not used by default but provide means of precise control

### Inactivity Timeout

- By default, users logged out after 10 minutes of inactivity
- Use `exec-timeout minutes` to modify this behavior
- `exec-timeout 0` disables the timer
- Can configure on console line and VTY lines

## Remote Access Overview

### Need for Remote Access

- Console port useful for initially configuring device
- Once device set up and connected to network, remote management is more convenient
- No need to be physically near device to access CLI
- Two main options: Telnet and SSH

### Client-Server Model

- Telnet and SSH both use client-server model
- User's computer is the client
- Device (router or switch) that accepts connection is the server
- Both client and server need IP addresses to communicate

### Management IP Addresses

- Any Layer 3 interface's IP address can be used to connect to and manage device
- Common to configure management IP address for specific purpose of remote management
- Router's management IP address usually configured on loopback interface
- Provides stable IP address not dependent on status of any particular physical port
- Switch's management IP address usually configured on SVI of management VLAN
- Management VLAN is VLAN dedicated to remote management of devices
- Management traffic should be kept isolated from other traffic for security

## Layer 2 Switch Management

### Switch Virtual Interfaces (SVIs)

- Routers and Layer 3 switches have multiple Layer 3 interfaces with IP addresses
- Layer 2 switches operate only at Layer 2, forwarding frames
- Layer 2 switches can't route packets but can send and receive packets
- To enable Layer 2 switch to send and receive packets, configure one or more SVIs
- SVIs are Layer 3 virtual interfaces that can send and receive packets
- SVIs provide Layer 3 interface (and IP address) necessary to remotely connect to Layer 2 switch

### SVI Configuration

- Use `interface vlan vlan-id` to create SVI
- Use `ip address ip-address netmask` to configure IP address
- Use `ip default-gateway ip-address` from global config mode to specify switch's default gateway
- Layer 2 switch doesn't route packets and doesn't need routing table
- Does need to know IP address of router it should send packets destined for remote hosts to
- Switch sends packets to other hosts in local network directly
- Switch sends packets to hosts in remote networks to default gateway

## Telnet

### Telnet Overview

- Telnet (teletype network) developed in 1969
- Allows remote connection to CLI of devices over network
- Telnet has largely been replaced by SSH
- Main reason: security—Telnet sends data in cleartext, not encrypted
- If password entered to log in, password sent across network as is
- Any attacker who gets copy of packet will know device's password
- Telnet still supported on most network devices but use cases are limited

### Telnet Configuration Requirements

- Configure enable secret to password-protect privileged EXEC mode
- Essential when configuring Telnet; if no enable secret, `enable` command won't work
- Configure user account: `username username secret password`
- Can configure either password-only authentication (`login`) or user account authentication (`login local`)
- User account authentication more secure

### Access Control Lists

- Optionally configure ACL to limit which hosts can access VTY lines
- Example: `access-list 1 permit 192.168.1.0 0.0.0.255`
- Apply ACL to VTY lines (not to interface)
- Good practice to limit which hosts can access VTY lines

### VTY Line Configuration

- Connecting via Telnet or SSH uses Virtual Teletype (VTY) lines
- Whereas there is only single console line, there are typically 16 VTY lines
- Access range with `line vty first-line last-line`
- In most cases, configure all VTY lines identically: `line vty 0 15`
- Up to 16 users can be connected to device's CLI at once via Telnet or SSH

### VTY Line Commands

- `login local`: Require authentication with one of accounts on local device
- `exec-timeout minutes`: Modify default inactivity timeout (default is 10 minutes)
- `transport input protocol`: Control which protocol(s) can be used to connect to VTY lines
  - `transport input telnet`: Allows only Telnet
  - `transport input ssh`: Allows only SSH
  - `transport input telnet ssh`: Allows both Telnet and SSH
  - `transport input all`: Allows connections with all supported protocols
  - `transport input none`: Allows no connections to VTY lines
- `access-class acl in`: Apply ACL to VTY lines to control which hosts can connect

### VTY Line Groups

- 16 VTY lines divided into two groups in configuration files
- `line vty 0 4` and `line vty 5 15`
- Division maintains backward compatibility with older devices that only supported five VTY lines

### Telnet Connection

- Telnet servers listen on TCP port 23
- Use `telnet ip-address` command from client to connect
- User must authenticate with configured credentials
- After authentication, user in user EXEC mode
- Can use `enable` command to access privileged EXEC mode

## Secure Shell (SSH)

### SSH Overview

- SSH serves similar purpose to Telnet
- Allows remote connection to CLI of network devices over network
- Major difference: SSH is secure—encrypts communications between client and server
- Even if attacker gains access to communications, messages are encrypted
- Messages appear as unintelligible mess to anyone but intended destination host
- SSH is standard method for remote device management

### SSH Configuration Steps

SSH configuration consists of two main steps:

1. Generating cryptographic RSA keys
2. Enabling SSH connections on VTY lines

### RSA Key Generation

- SSH requires pair of cryptographic keys to encrypt and decrypt messages
- Cryptographic key is piece of information used as input for cryptographic algorithms
- Specifically need RSA keys—cryptographic keys that use RSA algorithm
- Use `crypto key generate rsa` in global config mode to generate keys
- Device will name key pair using device's FQDN
- Must configure hostname and domain name first
- Or use `crypto key generate rsa label name` to manually specify name

### Domain Name Requirement

- Domain name needed because key pair needs name
- IOS uses device's FQDN to name keys
- May be required to configure non-default hostname as well
- Some devices show error if default hostname (Router) is used

### RSA Key Modulus Size

- When generating RSA keys, asked to specify size of key modulus
- Modulus determines strength of encryption—larger is more secure
- Modulus size usually referred to as key size or key length
- Cisco recommends modulus sizes of at least 2,048 bits
- In newer software versions, SSH can't be used with modulus sizes smaller than 2,048 bits
- Can specify modulus size in command: `crypto key generate rsa modulus size`

### SSH Version

- After creating RSA keys, `show ip ssh` should show SSH is enabled
- Two major versions of SSH: SSHv1 and SSHv2
- Version 1.99 is enabled on Cisco devices by default
- Version 1.99 means device accepts both SSHv1 and SSHv2 connections
- SSHv2 offers security and performance advantages over SSHv1
- Best practice: allow only SSHv2

### SSH Configuration

- After creating RSA keys, SSH configuration nearly identical to Telnet configuration
- Use `ip ssh version 2` in global config mode to limit SSH connections to SSHv2 only
- Device's RSA key pair's modulus size must be at least 768 bits to support SSHv2
- Configure VTY lines with `login local`, `exec-timeout`, `transport input ssh`, `access-class`
- Best practice: use `transport input ssh` to allow only SSH connections
- Telnet is not secure and should not be used

### SSH Connection

- SSH servers listen on TCP port 22
- Use `ssh -l username ip-address` to connect to device with SSH
- `-l` means "login name"—username you want to log in with
- Command works in most systems: Windows, macOS, Linux, Cisco IOS
- Alternative: `ssh username@ip-address` (works in most OSs but not Cisco IOS)
- After authentication, user in user EXEC mode
- Can use `enable` command to access privileged EXEC mode

## Real-World Applications

- **Remote network management**: Access device CLI from anywhere on network
- **Multi-site networks**: Manage devices across geographically distributed networks
- **Troubleshooting**: Quickly access devices to diagnose and fix issues
- **Configuration management**: Remotely configure devices without physical access
- **Network monitoring**: Remotely verify device status and configurations
- **Security**: Encrypted communications prevent password and configuration exposure

## Troubleshooting

### Common Issues

- **Cannot connect**: Verify SSH is enabled and VTY lines configured correctly
- **Authentication fails**: Check username and password are correct
- **Enable command doesn't work**: Verify enable secret is configured
- **Connection refused**: Check ACL on VTY lines allows your source IP
- **SSH not available**: Verify RSA keys are generated and SSH version is configured

### Troubleshooting Steps

1. Verify SSH status: `show ip ssh`
2. Check VTY line configuration: `show running-config | section line vty`
3. Verify RSA keys: `show crypto key mypubkey rsa`
4. Check ACL: Verify access-class configuration on VTY lines
5. Test connectivity: Ping device from client
6. Verify port: Ensure TCP port 22 is not blocked

## Best Practices

- Always use SSH instead of Telnet for remote access
- Configure SSHv2 only (disable SSHv1)
- Use user account authentication instead of line passwords
- Configure ACLs on VTY lines to limit access
- Use management VLAN for switch management
- Use loopback interfaces for router management IP addresses
- Set appropriate inactivity timeout values
- Generate RSA keys with at least 2,048-bit modulus
- Disable Telnet completely in production networks
- Document SSH access credentials securely
- Regularly review and update VTY line ACLs
- Monitor SSH connection attempts for security

## Summary

- Physical access control essential but not sufficient; configure security settings on console port
- Use `line con 0` to configure console line (only one console line exists)
- Use `password password` and `login` for line password authentication
- Use `username username secret password` and `login local` for user account authentication
- User account authentication preferred over line password
- Use `exec-timeout minutes` to modify inactivity timeout (default 10 minutes)
- Two main options for remote access: Telnet and SSH
- Telnet sends data in cleartext; SSH encrypts communications
- Layer 2 switches can use SVIs to send and receive packets for remote management
- Configure SVI with `interface vlan vlan-id` and `ip address`
- Configure default gateway with `ip default-gateway ip-address` for Layer 2 switches
- Telnet servers listen on TCP port 23
- VTY lines used for Telnet and SSH connections (typically 16 lines: 0-15)
- Use `transport input protocol` to control which protocols can connect to VTY lines
- Use `access-class acl in` to apply ACL to VTY lines
- SSH requires RSA keys: use `crypto key generate rsa` (requires hostname and domain name)
- RSA key modulus size should be at least 2,048 bits
- Use `ip ssh version 2` to limit SSH to SSHv2 only
- SSH servers listen on TCP port 22
- Use `ssh -l username ip-address` to connect with SSH
- Always use SSH instead of Telnet in production networks

