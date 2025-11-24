# Secure Shell

## Overview

Secure Shell (SSH) provides encrypted remote access to the CLI of routers and switches over an IP network. SSH replaces Telnet in modern networks because it protects credentials and configuration data from eavesdropping. Console access is still used for initial setup and recovery, but routine management is normally done with SSH.

## Securing console access

### Physical access control

- Console access requires physical connection to the console port.
- Anyone with a laptop and console cable can reach the CLI if the device is not physically secured.
- Devices should be in locked rooms or racks.
- Physical security is necessary but not sufficient; logical protections on the console line are still required.

### Console line basics

- The console port maps to line `con 0`.
- Only one console line exists, so only one active console session is possible.
- Configuration is done under line configuration mode:

  ```cisco
  line console 0
  ```

### Console authentication

Two common options for console authentication:

- Line password

  ```cisco
  line console 0
   password <console_password>
   login
  ```

  - Users enter a single password to access user EXEC mode.

- Local user accounts

  ```cisco
  username admin secret <strong_password>
  !
  line console 0
   login local
  ```

  - Each user has a separate username and password.
  - Provides better accountability and security than a shared line password.

`login` and `login local` are mutually exclusive on a line.

### Privilege levels and inactivity timeout

- Default privilege level after login is 1 (user EXEC).
- `enable` elevates to privilege level 15 (privileged EXEC) when an enable password or secret is configured:

  ```cisco
  enable secret <strong_password>
  ```

- Intermediate privilege levels (2 to 14) exist but are not commonly used in basic CCNA configurations.
- Inactivity timer on the console line:

  ```cisco
  line console 0
   exec-timeout 10
  ```

  - Value is in minutes.
  - `exec-timeout 0` disables automatic logout.

## Remote access and management addresses

### Need for remote access

- Console access is practical for initial setup or when remote access fails.
- Daily management is easier through remote access protocols.
- Telnet and SSH use VTY lines for remote CLI sessions.

### Client server model

- Remote access protocols use a client server model.
- The administrator's workstation runs the client.
- The network device (router or switch) runs the server.
- Both endpoints require IP connectivity.

### Management IP addresses

- Any Layer 3 interface on a router can serve as a management address.
- Loopback interfaces are often used on routers for a stable management IP:

  ```cisco
  interface Loopback0
   ip address 192.0.2.1 255.255.255.255
  ```

- On Layer 2 switches, management is provided by a Switch Virtual Interface (SVI) in a management VLAN:

  ```cisco
  interface vlan 10
   ip address 192.168.10.2 255.255.255.0
  !
  ip default-gateway 192.168.10.1
  ```

- Management traffic is often placed in a dedicated VLAN to separate it from user data.

## Telnet

### Telnet overview

- Telnet provides remote CLI access over TCP port 23.
- All data is sent in clear text, including usernames and passwords.
- Telnet is still available on many devices but is not considered secure for production use.

### Basic Telnet configuration

Minimum pattern:

```cisco
enable secret <strong_password>
username admin secret <strong_password>
!
line vty 0 15
 login local
 transport input telnet
```

- Local username database is used for authentication.
- `line vty 0 15` configures all 16 VTY lines on typical platforms.

ACLs can restrict which hosts can reach the VTY lines:

```cisco
ip access-list standard MGMT-ACCESS
 permit 192.0.2.0 0.0.0.255
!
line vty 0 15
 access-class MGMT-ACCESS in
```

Telnet is mainly relevant as a comparison point for SSH.

## Secure Shell (SSH)

### SSH overview

- SSH serves the same purpose as Telnet but encrypts the session.
- SSH servers listen on TCP port 22.
- SSH is the recommended and expected method for remote device management.

### SSH prerequisites

SSH on Cisco IOS requires:

- A hostname.
- A domain name.
- An RSA key pair.

Example:

```cisco
hostname R1
ip domain-name example.com
crypto key generate rsa modulus 2048
```

- Modulus size controls key strength; 2048 bits is a common baseline.
- Some platforms require a nondefault hostname before key generation.

### Enabling SSH version 2

- Restrict to SSHv2:

  ```cisco
  ip ssh version 2
  ```

- Typical VTY configuration:

  ```cisco
  username admin secret <strong_password>
  !
  line vty 0 15
   login local
   transport input ssh
   exec-timeout 10
   access-class MGMT-ACCESS in
  ```

- `transport input ssh` disables Telnet on the VTY lines.
- `exec-timeout` controls idle disconnect behavior.

### Verifying SSH

Useful commands:

- `show ip ssh`  
  - Confirms SSH status and version.

- `show crypto key mypubkey rsa`  
  - Displays RSA keys.

- `show running-config | section line vty`  
  - Checks VTY settings.

### Making an SSH connection

- SSH client examples:

  ```bash
  ssh -l admin 192.0.2.1
  ssh admin@192.0.2.1
  ```

- After authentication, the session starts in user EXEC mode.
- `enable` is then used to enter privileged EXEC mode.

## Troubleshooting SSH

### Common issues

- Cannot connect at all
  - RSA keys not generated.
  - SSH disabled or misconfigured.
  - Access list blocking management traffic.

- Authentication failures
  - Incorrect username or password.
  - Local user account not configured.
  - `login local` missing on VTY lines.

- Enable password issues
  - `enable secret` not configured.
  - Wrong password entered at enable prompt.

### Troubleshooting steps

1. Confirm IP reachability with `ping`.
2. Verify management IP and default gateway on the device.
3. Check SSH configuration:

   ```cisco
   show ip ssh
   show running-config | section line vty
   show crypto key mypubkey rsa
   ```

4. Validate ACLs applied to VTY lines or inbound interfaces.
5. Check for log messages related to SSH with `show logging`.

## Quick review

- Console access remains important for initial setup and recovery but must be protected with passwords and timeouts.  
- Local user accounts with `login local` provide stronger authentication than a single line password.  
- Remote access uses VTY lines; Telnet is available but sends clear text and is not suitable for secure environments.  
- SSH provides encrypted CLI access on TCP port 22 and is the standard for remote management.  
- SSH on Cisco IOS requires hostname, domain name, and RSA keys, typically generated with `crypto key generate rsa modulus 2048`.  
- `ip ssh version 2` and `transport input ssh` restrict remote access to SSHv2 only.  
- Management IP addresses are usually provided by router loopbacks or switch SVIs in a dedicated management VLAN.  
- Core verification and troubleshooting use `show ip ssh`, RSA key checks, VTY configuration checks, ACL verification, and `ping` for basic connectivity.  
