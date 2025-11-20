# Trivial File Transfer Protocol and File Transfer Protocol

## Overview

A file serves as a digital container in a computer, designed to store a variety of data ranging from text and images to audio, video, and software applications. Files can be of any size, from a few bytes to hundreds of gigabytes or more. Transferring files from one computer to another has been one of the primary functions of networks since their beginning. Over time, this has led to the development of various protocols dedicated to facilitating file transfers over a network. Trivial File Transfer Protocol (TFTP) and File Transfer Protocol (FTP) are two such protocols that have been widely used for this purpose and still are. While TFTP is a simple protocol that is often used to transfer small files in a controlled environment, FTP offers a robust set of features for secure and versatile file transfers. TFTP and FTP can both be used to transfer any kind of file over a network, but one use case that is relevant for anyone working with Cisco routers and switches is transferring IOS files from a file server to upgrade the operating system of a device.

## Trivial File Transfer Protocol (TFTP)

### TFTP Overview

- Protocol used for transferring files over a network
- Uses client-server model, in which one device (i.e., PC) acts as client and another (i.e., file server) acts as server
- "Trivial" because it is relatively simple protocol with few features
- Client can transfer files to and from server, but that's about it
- TFTP doesn't use any kind of authentication
- TFTP server will respond to all client requests—no username/password needed
- TFTP communications are unencrypted, so all data is sent in plaintext
- For these reasons, would not be wise to use TFTP to send important files over public network like internet
- TFTP does not provide sufficient security
- To transfer files within controlled environment like LAN, TFTP is often selected for its simplicity and ease of use

### TFTP Ports

- TFTP servers listen for requests on UDP port 69
- Memorize that port for the exam
- Given characteristics of TCP and UDP, this may be unexpected
- When transferring files, you want to make sure entire file arrives intact, with all bytes in correct order
- TCP's reliability and sequencing features make it usual Layer 4 protocol of choice for transferring files
- However, UDP may be preferred when reliability is provided via other means
- This is case with TFTP

### TFTP Lock-Step Communication

- TFTP uses lock-step communication
- Client and server alternately send message and then wait for reply
- When TFTP server transfers file to client, it divides file into ordered blocks
- After sending one block, server won't send another block until it has received acknowledgment message from client
- Each block must be acknowledged
- Messages are retransmitted if needed
- After either device (client or server) sends message, it sets timer
- If timer expires, it retransmits its previous message
- Example: After client acknowledges block 1, it sets timer
- If server's block 2 is lost in transit, client's timer expires
- Client retransmits block 1's acknowledgment
- Upon receiving retransmitted acknowledgment for block 1, server understands that block 2 did not make it to client
- Server then retransmits block 2

### TFTP Transfer ID

- Although TFTP servers listen for requests on UDP port 69, that only applies to initial read or write request
- After receiving initial request, server allocates new port number in ephemeral range (49152-65535) to identify that specific session
- This port is called Transfer ID (TID)
- For remainder of communication between server and client, server will listen on and source messages from TID port, not port 69
- For CCNA exam, just remember that TFTP = UDP port 69

### TFTP Reliability

- Although TFTP uses UDP, which doesn't offer sequencing and reliability features, TFTP protocol itself uses lock-step communication to provide both sequencing and reliability
- Not as sophisticated as TCP's features, but sufficient to allow TFTP to use lightweight UDP as its Layer 4 protocol

### TFTP Read and Write Requests

- TFTP file transfer is initiated by client sending either read request or write request to TFTP server
- Purpose of read request is to request to download file from server
- Purpose of write request is to request to upload file to server
- For this chapter, focus on read requests, but keep in mind that TFTP supports both functions

## Cisco IOS File Systems

### File System Overview

- To transfer files to and from Cisco IOS devices, need basic understanding of Cisco IOS file system
- Hierarchical structure that IOS uses to store, manage, and organize various types of files
- Such as configuration files, IOS images, and log files
- Files can then be easily accessed and manipulated by both applications and users
- While commonly refer to "the IOS file system" in general sense, this term encompasses multiple file systems
- Designed to manage different physical storage locations
- Such as flash memory, NVRAM (non-volatile RAM), and even remote storage like TFTP or FTP servers
- Each of these storage options has its own unique file system
- Can view various file systems with `show file systems` command

### File System Types

- **Opaque**: Logical file systems used for internal functions
- **NVRAM**: Used for device's NVRAM (where startup-config file is saved)
- **Disk**: Physical storage devices (like flash memory)
- **Network**: Used to access external file systems over network (i.e., TFTP servers)

### Opaque File Systems

- Opaque file systems are logical file systems used for device's internal functions
- Example: system: is where device's running-config file is stored
- Configuration commands in this file determine how device actually functions
- Can view contents of file system with `dir` command
- Example: `dir system:` shows running-config file
- Previously used `show running-config` command to view this file
- This command is basically shortcut, providing simple method to view device's configuration
- Without needing to know actual location of file
- Alternatively, can use `more` command to view contents of file
- Specify `system:running-config` file path
- Output is same as `show running-config`

### NVRAM File System

- NVRAM file system type is only used for one file system: nvram:
- Although it stores other files, this file system is best known for storing startup-config file
- File that device loads when booting up
- Can use `dir nvram:` to confirm contents of file system
- Can use `more nvram:startup-config` to view startup-config file
- This is equivalent to using `show startup-config` command

### Disk File System

- Disk file system type is used for physical storage devices
- One example is flash:, which is default file system
- Primary location where operating system looks for files during various operations
- Unless another file system is specified
- This is location we'll copy files to with TFTP
- If USB flash drive is inserted, it typically uses Disk file system type as well

### Network File System

- Network file system type is used to access remote file systems over network
- Such as TFTP servers; tftp: file system is example
- Likewise, there is also ftp: file system
- When specifying network file system in command, also have to specify IP address of target host
- These file systems don't reside on local device

## Transferring Files with TFTP

### Copy Command

- To transfer files to and from TFTP server, use `copy source destination` command
- This creates copy of specified source file at specified destination
- Example: `copy tftp: flash:`
- Tells device that you would like to copy file from TFTP server to flash: file system

### TFTP Copy Process

- After issuing `copy tftp: flash:` command, shown series of prompts
- First prompt asks for IP address (or name, if DNS is available) of TFTP server
- Second prompt asks for source filename—name of file that you want to copy from TFTP server
- Final prompt is for destination filename—name that file will be saved as on local device
- By default, destination filename will be same as source filename (as indicated by value in square brackets)
- Simply pressing Enter at this prompt accepts default
- Can optionally specify different name, but IOS image names include information about image type and IOS version
- They're best left as is

### TFTP Copy Example

- Example: Copying IOS image from TFTP server to switch
- Specify TFTP server IP address: 192.168.1.224
- Specify source filename: c2960c405-universalk9-mz.152-7.E7.bin
- Accept default destination filename
- File is transferred to switch
- Can verify with `show flash:` command
- Shows new image in flash: file system

## File Transfer Protocol (FTP)

### FTP Overview

- Of two protocols covering in this chapter, FTP is older one, first standardized in 1971
- However, FTP is more robust, providing variety of features that TFTP does not
- FTP requires authentication with username/password, providing greater security than TFTP
- However, FTP does not encrypt data; files are transferred as plaintext
- For even more security, can use encrypted protocol like FTP Secure (FTPS)
- For purpose of CCNA exam, focus on FTP itself, not its related encrypted protocols

### Encrypted FTP Alternatives

- File Transfer Protocol Secure (FTPS) uses Transport Layer Security (TLS) to secure FTP communications between server and client
- SSH File Transfer Protocol (SFTP) is extension of SSH that enables it to perform encrypted file transfers
- Despite name, this protocol isn't actually related to FTP

### FTP Layer 4 Protocol

- Unlike TFTP, FTP uses TCP as its Layer 4 protocol
- Means that whereas TFTP exchange begins with client immediately sending request to server, FTP exchange must begin by establishing TCP connection
- TCP three-way handshake
- However, transferring files with FTP requires two TCP connections, not one

### FTP Control Connection

- Initial TCP connection establishment is standard TCP three-way handshake
- SYN (client to server), SYN-ACK (server to client), and ACK (client to server)
- Once three-way handshake is done, client and server have established FTP control connection
- Through this connection, server will first authenticate client by checking its username and password
- If authentication succeeds, client can then send FTP commands to server
- It is through these commands that client can tell server what it wants to do
- Unlike TFTP, in which client can only copy files to or from server, FTP has variety of commands
- Support functions like listing available files and directories, navigating through directories, renaming and deleting files, and various others
- Example: Client needs to download file from server
- Client will send RETR (retrieve) command to get copy of specific file
- This is equivalent to TFTP read request

### FTP Data Connection

- Actual data exchange does not take place over FTP control connection
- Instead, second TCP connection is established
- Second three-way handshake establishes FTP data connection
- It is over this connection that server transfers file to client
- One advantage of having separate control and data connections is that FTP can support multiple data transfers simultaneously
- With single control connection, client can establish multiple data connections with server

### FTP Ports

- TCP port 20 is reserved for FTP data connections
- Modern FTP servers often use ephemeral port instead
- Port that will be used for data connection is conveyed through control connection
- For CCNA exam, memorize these ports: FTP control = TCP 21, FTP data = TCP 20

### FTP Active and Passive Mode

- Although FTP client initiates control connection (by sending first TCP SYN to port 21 on FTP server), data connection can be initiated by either client or server
- In original FTP standard, it was server that initiated data connection
- This is called active mode (server is "active" one)
- However, active mode caused problems as firewalls and Network Address Translation (NAT) became common
- They could block incoming data connection from server to client
- This led to development of passive mode, in which client initiates data connection (server is "passive")
- Solving problems with active mode
- Cisco IOS device will use passive mode by default when acting as FTP client
- It does this by sending PASV command to server

## Transferring Files with FTP

### FTP Authentication

- Transferring files with FTP is largely same as with TFTP but with addition of username/password authentication
- FTP requires username/password authentication, so first have to configure FTP username and password on device
- Use `ip ftp username username` and `ip ftp password password` commands
- Of course, these must match user account on FTP server
- Credentials specified in these commands are device's default FTP credentials
- Credentials that will be used if none are specified in command

### FTP Copy Command

- To transfer file with FTP, can use same command as with TFTP: `copy source destination`
- Using `ftp:` instead of `tftp:` for source argument
- Example: `copy ftp: flash:`
- Can specify credentials in command: `copy ftp://username:password@server-ip flash:`
- Example: `copy ftp://jeremy:password123@192.168.1.224 flash:`
- After file transfer is complete, can use `show flash:` to confirm that new IOS image is in device's flash drive

## Upgrading Cisco IOS

### Reasons to Upgrade

After transferring new IOS image to device, configuring device to use that new image requires just one configuration command, followed by system reboot. Regardless of whether you use TFTP, FTP, or another method to transfer new image to device, upgrade process is identical. However, before doing that, let's pause to consider purpose of upgrading to new version of IOS in first place. Here are few reasons:

- **Security**: New releases often include fixes for security vulnerabilities that have been discovered in previous releases. By keeping devices up to date, can protect network from known security threats.
- **Bug fixes**: New releases often include bug fixes for issues such as memory leaks, crashes, and performance problems that can negatively affect network.
- **New features and functionality**: New releases often include new features and functionality not present in previous versions, offering more configuration options and networking solutions.
- **Cisco support**: Cisco routinely ends support for older versions, making it challenging to get technical assistance for any issues that may occur.

### Security Importance

- Security is undoubtedly most important reason to upgrade to new version of Cisco IOS
- If particular version has known security vulnerabilities, running it is risk
- Example: Version of IOS currently running on switch may have 48 security advisories associated with it, 4 of which are marked as "critical"
- This would not be acceptable in enterprise network
- To check current version of IOS running on device, use `show version` command
- To check latest and recommended versions of IOS available for particular device, go to software.cisco.com
- Cisco account is required
- From there, will also be able to find links to release notes, security advisories, etc.

### Boot System Configuration

- To make device boot with different image, use `boot system image-path` command in global config mode
- Example: `boot system flash:/c2960c405-universalk9-mz.152-7.E7.bin`
- Can confirm before and after with `show boot` command
- Lists various boot settings
- Command indicates that device will load new image next time it boots

### Reloading Device

- After configuring boot system, just have to save configuration (very important!) and reboot device with `reload` command
- If connected to device remotely via Telnet or SSH, will lose connectivity while device reboots
- Won't be able to see CLI
- However, if connected via console port, device will display its boot sequence in real time
- Will be able to observe device as it goes through its POST (Power-On Self-Test), loads specified IOS image, and finally brings you back to CLI once it has successfully rebooted
- This can be particularly useful for troubleshooting issues or verifying that device is booting correctly
- After upgrade is complete, can use `show version` command once again to verify that device is using new image

### Deleting Old Images

- After upgrade is complete, can delete old IOS image with `delete` command
- Example: `delete flash:/c2960c405-universalk9-mz.150-2.SE5.bin`
- However, it's important to verify that device is functioning properly and there are no network issues before doing so
- If any issues arise, may have to "roll back" to previous IOS version

### Upgrade Best Practices

- Back up your configuration before upgrading. This will allow you to restore it if something goes wrong.
- Read release notes for new IOS version carefully and ensure you understand changes.
- Test new IOS version in lab before deploying it in live network to identify any potential problems.
- Have plan in place for rolling back to previous IOS version if necessary.

## Real-World Applications

- **IOS upgrades**: Transfer new IOS images to network devices for upgrades
- **Configuration backups**: Back up configuration files to central file server
- **Firmware updates**: Update firmware on network devices
- **File distribution**: Distribute files to multiple devices from central server
- **Network management**: Centralize file management for easier administration
- **Disaster recovery**: Store IOS images and configurations for disaster recovery

## Troubleshooting

### Common Issues

- **TFTP transfer fails**: Verify TFTP server is running and reachable
- **FTP authentication fails**: Verify username and password are correct
- **File not found**: Verify filename is correct and file exists on server
- **Insufficient space**: Check available space in flash: file system
- **Transfer timeout**: Check network connectivity and server response times

### Troubleshooting Steps

1. Verify file system: `show file systems` and `show flash:`
2. Test connectivity: Ping TFTP/FTP server from device
3. Verify file exists: Check server has file with correct name
4. Check available space: Verify flash: has enough space for file
5. Verify credentials: For FTP, check username and password are correct
6. Check ports: Ensure UDP 69 (TFTP) or TCP 21/20 (FTP) are not blocked

## Best Practices

- Use TFTP only in controlled environments like LANs
- Use FTP with authentication for better security
- Consider FTPS or SFTP for encrypted file transfers in production
- Always back up configuration before upgrading IOS
- Test new IOS versions in lab before production deployment
- Read release notes and security advisories before upgrading
- Verify file integrity after transfer
- Keep multiple IOS versions available for rollback
- Document upgrade procedures
- Monitor device after upgrade for issues

## Summary

- File is digital container for data such as text, images, audio, video, and software
- Transferring files between computers is one of primary functions of networks
- TFTP is relatively simple protocol allowing client to transfer files to and from server without additional features
- TFTP doesn't use authentication and encryption, so recommended that you only use it to transfer files within controlled environment like LAN
- TFTP file transfer is initiated by client sending read request (download) or write request (upload) to server
- TFTP servers listen for requests on UDP port 69
- TFTP uses lock-step communication in which client and server alternately send message and wait for reply
- Files are divided into ordered blocks, and each block must be acknowledged before next one is sent
- If device doesn't receive reply after certain period, it will retransmit message
- Cisco IOS uses variety of file systems to store, manage, and organize files
- Opaque file system type indicates logical file systems used for internal functions (e.g., system: stores running-config)
- Disk type is used for physical storage devices, like flash: file system (default file system)
- Network type is used to access external file systems over network (e.g., tftp: and ftp:)
- NVRAM type is used for device's NVRAM, where startup-config is stored
- Use `dir` command to view contents of particular file system; `show flash:` also works for flash:
- Use `more` command to view contents of particular file
- To transfer files to and from TFTP server, use `copy source destination` command
- Can specify full file path: `copy tftp://server-ip/src-filename flash:/dst-filename`
- FTP serves same purpose as TFTP but is more robust, providing variety of features
- FTP requires username/password authentication but does not encrypt data
- Protocols like FTPS and SFTP can be used for encrypted file transfers
- FTP uses TCP as its Layer 4 protocol
- FTP exchanges require two TCP connections: control connection (TCP 21) and data connection (TCP 20)
- FTP control connection is used for authentication and sending FTP commands
- FTP data connection is used for actual file exchange
- Transferring files from FTP server requires username and password
- Use `ip ftp username` and `ip ftp password` to configure default FTP credentials
- Can specify credentials in command: `copy ftp://username:password@server-ip flash:`
- Upgrade process is identical regardless of transfer method (TFTP, FTP, etc.)
- Reasons to upgrade: security, bug fixes, new features, Cisco support
- Security is most important reason to upgrade
- Use `show version` to confirm current version of IOS
- Use `show boot` to view device's boot settings
- Use `boot system image-path` to specify IOS image device should load next time it boots
- Remember to save configuration before rebooting
- Use `reload` to reboot device
- If connected remotely, will lose connectivity during reboot
- If connected via console, can observe boot sequence in real time

