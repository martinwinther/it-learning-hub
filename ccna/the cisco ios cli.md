# The Cisco IOS CLI

## Overview

The Cisco IOS Command Line Interface (CLI) is the primary interface for configuring and operating Cisco routers and switches. Most CCNA configuration, verification, and troubleshooting tasks are performed from the CLI.

## Shell types

### GUI

- Graphical interface controlled with mouse and keyboard.
- Examples: desktop environments, smartphone interfaces, web GUIs.
- On CCNA, the main GUI reference is the Cisco Wireless LAN Controller (WLC) web interface.

### CLI

- Text based interface for entering commands.
- Examples: Windows Command Prompt, Linux terminal, Cisco IOS CLI.
- CCNA configuration work focuses on the Cisco IOS CLI.

## Accessing the Cisco IOS CLI

### Console access

- Direct, out of band access to the device.
- Requires physical connection to the console port.
- Does not use the network for communication.

Console port types:

- USB Mini-B on many modern devices.
- RJ45 console port on older and some current devices.

Rollover cable wiring pairs pins in reverse order:

- 1 ↔ 8, 2 ↔ 7, 3 ↔ 6, 4 ↔ 5.

Terminal emulator settings for console:

- Speed: 9600 bps
- Data bits: 8
- Stop bits: 1
- Parity: none
- Flow control: none

Common terminal emulators include PuTTY and similar tools.

### Network access

- In band access over the network.
- Requires a reachable management IP address on the device.
- Uses VTY lines for remote CLI sessions.

Main protocols:

- Telnet – clear text remote access (legacy, not secure).
- SSH – encrypted remote access (preferred for production).

## Initial dialog and CLI modes

### System Configuration Dialog

First time access often shows the System Configuration Dialog:

```text
--- System Configuration Dialog ---
Would you like to enter the initial configuration dialog? [yes/no]: no
```

For lab and exam work, answering `no` is standard to reach the CLI prompt.

### User EXEC mode

- Lowest privilege CLI mode.
- Prompt format: `hostname>`.
- Limited to basic monitoring commands.

Example commands:

- `show clock`
- `show version`
- `ping`

Commands that change configuration are not available in this mode.

### Privileged EXEC mode

- Also called enable mode.
- Prompt format: `hostname#`.
- Provides access to all EXEC level commands, including `show running-config` and `reload`.
- Entry from user EXEC:

  ```text
  Router> enable
  Router#
  ```

- Return to user EXEC:

  ```text
  Router# disable
  Router>
  ```

### Global configuration mode

- Used to change device configuration.
- Prompt format: `hostname(config)#`.
- Entry from privileged EXEC:

  ```text
  Router# configure terminal
  Enter configuration commands, one per line. End with CNTL/Z.
  Router(config)#
  ```

Examples of commands in global configuration:

- `hostname R1`
- `enable secret <password>`

Exiting configuration mode:

- `end` – return directly to privileged EXEC.
- `exit` – return to the previous mode.
- `Ctrl-Z` – return to privileged EXEC, executing the current command first.
- `Ctrl-C` – aborts the current command and returns to privileged EXEC.

### The `do` command

- Allows EXEC commands to run from configuration modes.
- Pattern:

  ```text
  R1(config)# do show clock
  ```

- Without `do`, `show` commands are not accepted in configuration modes.

## Keyboard shortcuts and history

### Line editing

- Left Arrow – move cursor left.
- Right Arrow – move cursor right.
- Backspace – delete character to the left.
- `Ctrl-A` – move to beginning of line.
- `Ctrl-E` – move to end of line.
- `Ctrl-U` – delete from cursor to line start.

### Command history

- Up Arrow – previous command.
- Down Arrow – next command.
- History size can be adjusted with line configuration commands but defaults are usually sufficient for CCNA work.

## Context-sensitive help and completion

### Question mark help

Types of help:

- At a new prompt, `?` lists available commands.
- After a command name, `?` lists available keywords:

  ```text
  R1> show ?
  ```

- After a partial word, `?` shows matching commands:

  ```text
  R1> e?
  enable  ethernet  exit
  ```

### Tab completion

- Type enough letters to uniquely identify a command.
- Press Tab to complete the command.
- If the partial string is ambiguous, IOS leaves the text unchanged.
- If the partial string is unique, IOS completes the command.

### Abbreviated commands

- Commands can be entered with the shortest unique abbreviation.
- Example:

  ```text
  R1> en
  R1#
  ```

- IOS rejects ambiguous abbreviations.

## IOS configuration files

Cisco IOS devices maintain two main configuration files.

### Running configuration

- Stored in RAM.
- Active configuration currently used by the device.
- Changes in configuration modes update the running configuration immediately.
- Lost when the device reloads or loses power.

Command to view:

```cisco
show running-config
```

### Startup configuration

- Stored in NVRAM.
- Loaded during boot to initialize the running configuration.
- Does not change until saved from running configuration.

Command to view:

```cisco
show startup-config
```

### Saving configuration

- Copies running configuration to startup configuration:

  ```cisco
  copy running-config startup-config
  ```

- Short forms such as `write memory` perform the same action on many platforms.

### Erasing configuration

- Erase startup configuration from NVRAM:

  ```cisco
  erase startup-config
  ```

- After erasing, reload the device to return to default:

  ```cisco
  reload
  ```

- On reload, the device starts without a saved configuration and may show the System Configuration Dialog again.

## Password protection

### Enable password

- Configured with:

  ```cisco
  enable password <password>
  ```

- Stored in cleartext by default.
- Can be obfuscated with `service password-encryption` (Type 7), which is reversible.
- Considered a legacy method for privileged access control.

### Enable secret

- Configured with:

  ```cisco
  enable secret <password>
  ```

- Stored as a nonreversible hash.
- Stronger protection than enable password.
- Supported hash types include MD5 and stronger algorithms such as scrypt, depending on IOS version.
- When both enable password and enable secret are configured, enable secret takes precedence.

## Quick review

- Cisco IOS CLI is the main interface for configuration and troubleshooting on CCNA devices.  
- Access is via console (out of band) or network (in band) using Telnet or SSH.  
- Key modes are user EXEC (`>`), privileged EXEC (`#`), and global configuration (`(config)#`).  
- `do` allows EXEC commands to be run while in configuration modes.  
- Keyboard shortcuts, command history, and context-sensitive help (`?`, Tab) improve efficiency.  
- Running configuration is in RAM, startup configuration is in NVRAM; use `copy running-config startup-config` to save changes.  
- Enable secret provides secure privileged access and is preferred over enable password.  
