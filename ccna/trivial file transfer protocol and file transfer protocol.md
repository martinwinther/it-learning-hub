```markdown
# Trivial File Transfer Protocol and File Transfer Protocol

## Overview

Trivial File Transfer Protocol (TFTP) and File Transfer Protocol (FTP) provide simple ways to move files between devices. On Cisco IOS routers and switches they are commonly used to copy IOS images and configuration files to and from external servers. TFTP focuses on simplicity and runs over UDP. FTP offers more features and runs over TCP.

## Trivial File Transfer Protocol (TFTP)

### TFTP characteristics

- Client server protocol for file transfers
- Very small feature set
- No usernames or passwords
- All data sent in clear text
- Usually used only inside trusted networks

TFTP is often chosen for tasks such as copying IOS images on a lab network where simplicity is more important than security.

### Ports and transfer IDs

- TFTP servers listen for initial requests on UDP port 69
- After a read or write request arrives, the server allocates an ephemeral UDP port
- This port is the Transfer ID (TID) for that session
- All further messages for that transfer use the TID, not port 69

For CCNA, remember that TFTP uses UDP port 69.

### Lock step operation and reliability

TFTP uses its own reliability on top of UDP.

- Files are divided into numbered blocks
- Each block must be acknowledged before the next block is sent
- Sender starts a timer when a block or acknowledgment is sent
- If the timer expires before a reply arrives, the last message is retransmitted

This lock step behavior provides sequencing and basic reliability without using TCP.

### Read and write requests

- Read Request (RRQ)  
  Client requests to download a file from the server.

- Write Request (WRQ)  
  Client requests to upload a file to the server.

Both operations use the same basic lock step block and acknowledgment process.

## Cisco IOS file systems

### File system overview

Cisco IOS organizes storage into file systems. Examples include:

- `system:` for internal logical files
- `nvram:` for startup configuration
- `flash:` for IOS images and other files
- `tftp:` and `ftp:` for remote network file systems

The list of file systems appears in:

```cisco
show file systems
```

### File system types

- Opaque  
  Logical file systems used for internal functions. Example: `system:` holds `running-config`.

- NVRAM  
  Nonvolatile memory that stores `startup-config` and related files. Example: `nvram:`.

- Disk  
  Physical storage devices such as internal flash or USB. Example: `flash:`.

- Network  
  Remote file systems reached over the network. Examples: `tftp:` and `ftp:`.

### Viewing and reading files

- List the contents of a file system:

  ```cisco
  dir flash:
  dir nvram:
  dir system:
  ```

- View configuration files:

  ```cisco
  show running-config
  show startup-config
  ```

- Equivalent file based views:

  ```cisco
  more system:running-config
  more nvram:startup-config
  ```

## Transferring files with TFTP

### Copy command pattern

IOS uses a common copy pattern:

```cisco
copy source destination
```

Example for copying from a TFTP server to flash:

```cisco
copy tftp: flash:
```

Typical prompt sequence:

- IP address or name of TFTP server
- Source filename on the server
- Destination filename on the device

If the destination filename is left as the default, IOS stores the file under the same name.

### TFTP IOS image example

Example: copying an IOS image from a TFTP server to a switch:

```cisco
copy tftp: flash:
Address or name of remote host []? 192.168.1.224
Source filename []? c2960c405-universalk9-mz.152-7.E7.bin
Destination filename [c2960c405-universalk9-mz.152-7.E7.bin]? 
```

After the transfer completes, verify the file:

```cisco
show flash:
```

The new image should appear in the `flash:` file system.

## File Transfer Protocol (FTP)

### FTP characteristics

- Older protocol than TFTP, but more capable
- Requires username and password for access
- Uses clear text for credentials and data
- Supports directory listings, renaming, and file deletion
- Often replaced by secure variants in production networks

Secure alternatives:

- FTPS: FTP protected with TLS
- SFTP: file transfer over SSH (not the same protocol as FTP)

CCNA notes focus on basic FTP, not the encrypted variants.

### Control and data connections

FTP uses TCP as its transport protocol and separates control from data.

- Control connection:
  - Uses TCP port 21 on the server
  - Carries login and FTP commands (such as LIST and RETR)
- Data connection:
  - Carries file contents
  - Originally used TCP port 20 on the server
  - Modern implementations often use an ephemeral port for data

Two FTP modes control who starts the data connection:

- Active mode  
  Server initiates the data connection toward the client.

- Passive mode  
  Client initiates the data connection to a port advertised by the server.  
  Passive mode works better with firewalls and NAT. Cisco IOS acts as a passive FTP client by default.

For CCNA, remember that FTP uses TCP port 21 for control and port 20 for traditional data connections.

## Transferring files with FTP

### FTP credentials

IOS devices store default FTP credentials with:

```cisco
ip ftp username <name>
ip ftp password <password>
```

These values should match a user account on the FTP server.

### FTP copy command

The same copy pattern is used:

```cisco
copy ftp: flash:
```

Credentials can be placed directly in the URL:

```cisco
copy ftp://user:password@192.168.1.224/c2960c405-universalk9-mz.152-7.E7.bin flash:
```

After the transfer completes, confirm the file:

```cisco
show flash:
```

## Upgrading Cisco IOS

### Reasons to upgrade

Common reasons for upgrading IOS:

- Security fixes for known vulnerabilities
- Bug fixes for stability and performance
- New features and capabilities
- Continued vendor support

Current IOS version on a device:

```cisco
show version
```

Recommended versions and security advisories are listed on Cisco software download pages.

### Selecting the boot image

To boot from a specific image in flash, configure a boot statement:

```cisco
boot system flash:/c2960c405-universalk9-mz.152-7.E7.bin
```

Verify boot settings:

```cisco
show boot
```

Save configuration before reloading:

```cisco
copy running-config startup-config
```

### Reloading and cleanup

Reload the device:

```cisco
reload
```

After the device returns to the CLI, verify the new version:

```cisco
show version
```

Once the new image is stable in production, old images in flash can be removed with the `delete` command to free space.

## Quick review

- TFTP is a simple file transfer protocol that uses UDP and listens on port 69.  
- TFTP servers allocate a Transfer ID in the ephemeral port range for each session and use lock step block acknowledgments for reliability.  
- Cisco IOS file systems include `system:`, `nvram:`, `flash:`, and network file systems such as `tftp:` and `ftp:`.  
- The `copy source destination` command copies files between local file systems and TFTP or FTP servers.  
- FTP uses TCP with separate control (port 21) and data connections and supports directory and file management commands.  
- IOS can act as an FTP client using stored credentials or URLs with embedded username and password.  
- IOS upgrades involve copying a new image, pointing the boot system to that image, saving the configuration, reloading, verifying the version, and optionally deleting old images.  
```
