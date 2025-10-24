# The Cisco IOS CLI

## Overview

The Cisco IOS CLI (Command-Line Interface) is the primary interface for configuring and managing Cisco network devices. Understanding how to navigate and use the CLI is essential for CCNA certification and network administration. The CLI provides a text-based interface for entering commands to configure routers, switches, and other Cisco devices.

## Shells: GUI and CLI

A shell is a computer program that allows a user to interact with the computer. It's the interface between the computer and the user, and it's called a shell because it's the outer layer of the operating system.

### GUI (Graphical User Interface)

A GUI allows a user to manipulate the computer via a graphical interface. Examples include:

- Windows desktop environment
- Smartphone interfaces
- Web browsers
- Cisco Wireless LAN Controller (WLC) GUI (the only GUI tested on CCNA)

### CLI (Command-Line Interface)

A CLI is a text-based interface that allows you to control and interact with a device by entering commands, which are lines of text. Examples include:

- Windows Command Prompt
- Linux terminal
- Cisco IOS CLI (primary focus for CCNA)

## Accessing the CLI of a Cisco Device

There are two main methods to access the CLI of a Cisco device:

### Console Port Connection

**Physical Connection:**

- Connect a PC/laptop to the console port of the device with a console cable
- Console ports are dedicated to configuring the device via CLI
- Cannot be used for network communication
- Requires physical proximity to the device

**Console Port Types:**

- **USB Mini-B**: Modern devices often include USB console ports
- **RJ45**: Traditional console port requiring rollover cable

**Rollover Cable Wiring:**

Rollover cables use a specific pin configuration:

- Pin 1 to pin 8
- Pin 2 to pin 7  
- Pin 3 to pin 6
- Pin 4 to pin 5
- Pin 5 to pin 4
- Pin 6 to pin 3
- Pin 7 to pin 2
- Pin 8 to pin 1

### Terminal Emulator Configuration

After physically connecting, use a terminal emulator application (such as PuTTY) with these settings:

**Required Settings:**

- **Speed**: 9600 bits per second
- **Data bits**: 8
- **Stop bits**: 1
- **Parity**: None
- **Flow control**: None

### Network-Based Access

**Remote Access Methods:**

- **Telnet**: Unencrypted remote access (covered in Volume 2)
- **SSH (Secure Shell)**: Encrypted remote access (covered in Volume 2)

## Navigating the Cisco IOS CLI

### System Configuration Dialog

When first accessing a new Cisco device, you'll see the system configuration dialog:

```text
--- System Configuration Dialog ---
Would you like to enter the initial configuration dialog? [yes/no]: no
```

**Recommendation**: Type `no` to skip the wizard and access the CLI directly.

### EXEC Modes

The Cisco IOS CLI uses a hierarchical command structure with different modes:

#### User EXEC Mode

**Characteristics:**

- Least-privileged mode
- Prompt format: `hostname>`
- Limited to viewing basic information
- Cannot make configuration changes or perform intrusive operations

**Example Commands:**

- `show clock` - View device time
- `show version` - View IOS version
- `ping` - Test connectivity

**Limitations:**

- Cannot use `reload` command
- Cannot access configuration mode
- Cannot view sensitive configuration details

#### Privileged EXEC Mode

**Characteristics:**

- Higher privilege level
- Prompt format: `hostname#`
- Access to all EXEC mode commands
- Can perform operational tasks

**Access Method:**

```text
Router> enable
Router#
```

**Available Commands:**

- All user EXEC commands
- `reload` - Restart device
- `show running-config` - View current configuration
- `copy` - Copy files
- `configure terminal` - Enter configuration mode

**Returning to User Mode:**

```text
Router# disable
Router>
```

### Global Configuration Mode

**Purpose:**

- Make configuration changes to the device
- Access other configuration modes
- Modify device settings

**Access Method:**

```text
Router# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#
```

**Prompt Format:** `hostname(config)#`

**Common Configuration Commands:**

- `hostname R1` - Change device hostname
- `enable password ccna` - Set enable password
- `enable secret cisco` - Set enable secret

**Exiting Configuration Mode:**

- `end` - Return directly to privileged EXEC mode
- `exit` - Return to previous mode
- `Ctrl-C` - Return to privileged EXEC mode
- `Ctrl-Z` - Return to privileged EXEC mode (executes current command first)

### The `do` Command

When in configuration mode, use `do` to execute EXEC mode commands:

```text
R1(config)# do show clock
*03:06:22.892 UTC Fri Feb 10 2023
```

**Note:** Regular `show` commands don't work in configuration mode without `do`.

## Keyboard Shortcuts and Navigation

### Cursor Movement and Editing

**Basic Navigation:**

- **Left Arrow** - Move cursor left
- **Right Arrow** - Move cursor right
- **Backspace** - Delete previous character
- **Ctrl-A** - Move cursor to beginning of line
- **Ctrl-E** - Move cursor to end of line
- **Ctrl-U** - Delete all characters to the left of cursor

### Command History

**History Navigation:**

- **Up Arrow** - Previous command
- **Down Arrow** - Next command

### Context-Sensitive Help

Cisco IOS provides extensive help features:

#### Question Mark (?) Usage

**1. List Available Commands:**

```text
R1> ?
Exec commands:
  <1-99>           Session number to resume
  access-enable    Create a temporary Access-List entry
  access-profile   Apply user-profile to interface
  clear            Reset functions
  connect          Open a terminal connection
```

**2. List Command Keywords:**

```text
R1> show ?
  aaa             Show AAA values
  arp             ARP table
  auto            Show Automation Template
  call-home       Show command for call home
  capability      Capability Information
```

**3. List Partial Command Completions:**

```text
R1> e?
enable  ethernet  exit
R1> en?
enable
```

#### Auto-Completion

**Tab Completion:**

- Type enough characters for unique identification
- Press Tab to complete the command
- Example: `en` + Tab = `enable`

**Direct Execution:**

- Type unique characters and press Enter
- Example: `en` + Enter = executes `enable`

**Examples:**

```text
R1> e<Tab>        # Reprints e (ambiguous)
R1> en<Tab>       # Completes to enable
R1> enable
R1#

R1> e             # Error: ambiguous command
% Ambiguous command: "e"
R1> en            # Executes enable command
R1#
```

## IOS Configuration Files

Cisco IOS devices use two configuration files stored in different memory types:

### Running-Config

**Characteristics:**

- Stored in RAM (Random Access Memory)
- Determines current device operations
- Changes take effect immediately
- Lost when device is powered off or restarted

**Viewing:**

```text
R1# show running-config
```

**Purpose:**

- Active configuration
- Immediate effect of changes
- Temporary storage

### Startup-Config

**Characteristics:**

- Stored in NVRAM (Non-Volatile RAM)
- Does not determine current operations
- Loaded during device boot
- Persists through power cycles

**Viewing:**

```text
R1# show startup-config
```

**Purpose:**

- Persistent configuration
- Loaded at boot time
- Survives power outages

### Configuration Management Commands

#### Saving Configuration

**Commands to save running-config to startup-config:**

- `write`
- `write memory`
- `copy running-config startup-config`

**Example:**

```text
R1# copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
```

#### Erasing Configuration

**Commands to erase startup-config:**

- `write erase`
- `erase nvram:`
- `erase startup-config`

**Factory Reset Process:**

1. Erase startup-config
2. Reload device
3. Device boots with factory-default configuration

**Example:**

```text
R1# write erase
Erasing the nvram filesystem will remove all configuration files! Continue? [confirm]
[OK]
R1# reload
Proceed with reload? [confirm]
```

## Password Protection

### Enable Password vs Enable Secret

#### Enable Password (Legacy)

**Configuration:**

```text
R1(config)# enable password ccna
```

**Characteristics:**

- Stored in cleartext by default
- Can be encrypted with `service password-encryption` (Type 7)
- Weak security (Type 7 easily reversible)
- Legacy feature, not recommended

**Security Issues:**

```text
R1# show running-config | include enable
enable password ccna
```

**Encryption Example:**

```text
R1(config)# service password-encryption
R1(config)# do show running-config | include enable
enable password 7 0307580507
```

#### Enable Secret (Recommended)

**Configuration:**

```text
R1(config)# enable secret cisco
```

**Characteristics:**

- Stored as a hash (one-way encryption)
- Much more secure than enable password
- Cannot be reversed
- Recommended for modern devices

**Example Output:**

```text
R1(config)# do show running-config | include enable
enable secret 9 $9$emuJQV5sVZCY8v$INbrp9XrtfWHieMubzYt7N640m4KXDIqKg/a6SHY9lU
enable password 7 0307580507
```

**Hashing Algorithms:**

- **Type 5 (MD5)**: Older devices, less secure
- **Type 9 (scrypt)**: Modern devices, more secure
- Algorithm depends on IOS version

**Priority:**

- If both enable password and enable secret are configured, only enable secret is used
- Enable password remains in config but is inactive

### Password Configuration Process

**Complete Example:**

```text
R1(config)# enable secret cisco
R1(config)# exit
R1# disable
R1> enable
Password: [cisco - hidden]
R1#
```

## Summary

Understanding the Cisco IOS CLI is fundamental to CCNA certification and network administration:

- **Shell Types**: GUI for graphical interfaces, CLI for text-based command entry
- **Access Methods**: Console port (physical) or network-based (Telnet/SSH)
- **Mode Hierarchy**: User EXEC → Privileged EXEC → Global Configuration
- **Help Features**: Context-sensitive help with `?` and auto-completion
- **Configuration Files**: Running-config (RAM) vs startup-config (NVRAM)
- **Password Security**: Enable secret (hash) preferred over enable password (cleartext)
- **Navigation**: Keyboard shortcuts and command history for efficiency

The CLI provides the foundation for configuring all Cisco network devices and protocols covered in the CCNA exam topics.
