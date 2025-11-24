
# Port Security

## Overview

Port Security is a Cisco switch feature that adds control to the normal MAC address learning process. It limits how many unique MAC addresses can be learned on an interface and defines what happens when that limit is exceeded. This helps protect against attacks that abuse MAC learning and DHCP behavior.

## Threats to MAC learning

### Default MAC address learning

- By default, a switch can learn many MAC addresses on a port, limited only by the size of the MAC address table
- Tables often support thousands of entries
- This default behavior can be abused to fill the table with bogus entries

### DHCP exhaustion attack

- Attacker sends many DHCP DISCOVER messages with spoofed MAC addresses
- DHCP pool is exhausted
- Legitimate clients fail to obtain addresses
- Large numbers of spoofed MACs can also pollute switch tables

### MAC flooding attack

- Attacker sends frames with many different spoofed source MAC addresses
- Goal is to fill the MAC address table
- When the table is full, the switch cannot learn new MAC addresses
- Frames destined to unknown unicast MAC addresses are flooded
- Flooding lets an attacker connected elsewhere on the VLAN receive copies of traffic
- This damages confidentiality and can be a side effect of DHCP exhaustion

## Port Security fundamentals

### Basic protection

- Port Security limits the number of MAC addresses a port can learn
- If the limit is exceeded, the port triggers a violation action
- MAC addresses learned on a Port Security enabled interface are called secure MAC addresses

### Port requirements

- Port Security does not work on dynamic switchports that use DTP
- Interface must be configured as access or trunk first

Example:

```cisco
interface GigabitEthernet0/1
 switchport mode access
 switchport port-security
```

### Default behavior

- Default maximum: 1 secure MAC address per port
- Default violation mode: shutdown (error disabled)
- When a violating frame arrives:
  - Syslog message is generated
  - Port status changes to secure-shutdown
  - Dynamically learned MAC addresses, including secure ones, are cleared from the table
  - The last seen MAC address is recorded as the violating address
  - Violation counter increments

### Verification

- `show port-security interface <interface>`
  - Status, violation mode, max and current MAC count, violation counter
- `show port-security`
  - Summary of Port Security enabled ports

## Error disabled ports and recovery

### Manual recovery

- Error disabled ports are administratively shut down by the switch
- Manual recovery:
  - `shutdown`
  - `no shutdown`
- Underlying cause must be fixed or the port will be disabled again

### ErrDisable Recovery

- Feature that can automatically reenable error disabled ports
- Disabled by default
- Enabled on a per cause basis

Key commands:

- `show errdisable recovery`
  - Lists causes and timers
- `errdisable recovery cause psecure-violation`
- `errdisable recovery cause bpduguard`
- `errdisable recovery cause inline-power`
- `errdisable recovery interval <seconds>`
  - Default is 300 seconds

ErrDisable Recovery is useful, but the original problem still needs to be solved or the port will cycle between up and error disabled.

## Configuring maximum MAC addresses

### Multi device ports

Some ports need more than one MAC address:

- Access port connected to an IP phone and a PC
- Access port connected to another switch that has its own hosts

Default maximum of 1 is not suitable for these cases.

### Maximum setting

- Command:

  ```cisco
  switchport port-security maximum <number>
  ```

- Example:

  ```cisco
  switchport port-security maximum 2
  ```

- Both static and dynamic secure MAC addresses count toward this limit

## Secure MAC address types

### Dynamic and static secure MAC addresses

- Dynamic secure MAC addresses
  - Learned automatically when traffic is seen
- Static secure MAC addresses
  - Configured manually on the interface

### Configuring static secure MAC addresses

- Basic command:

  ```cisco
  switchport port-security mac-address <mac-address>
  ```

- Applies to the access VLAN by default
- To specify a voice VLAN MAC address for the phone:

  ```cisco
  switchport port-security mac-address <mac-address> vlan voice
  ```

- Static and dynamic secure MAC addresses can be mixed on the same port

### Viewing secure MAC addresses

- `show mac address-table secure`
  - Shows secure entries in the MAC address table
  - Secure entries are listed as STATIC regardless of how they were learned
- `show port-security address`
  - Distinguishes SecureConfigured (static) and SecureDynamic (dynamic) addresses

## Violation modes

### Three modes

- shutdown (default)
- restrict
- protect

Configured per interface:

```cisco
switchport port-security violation {shutdown | restrict | protect}
```

### Shutdown mode

- Default mode
- First violating frame triggers:
  - Syslog message
  - Violation counter increment
  - Port moved to error disabled state
- All traffic on that port stops until recovery

### Restrict mode

- Violation frames are dropped
- Port remains up
- Violation counter increments for each violating frame
- Syslog and SNMP notifications are generated
- Non violating traffic on the port continues

### Protect mode

- Violation frames are dropped
- Port remains up
- No violation counter increments
- No Syslog or SNMP messages
- Considered less useful because violations become invisible

## Secure MAC address aging

### Default aging behavior

- Regular dynamic MAC addresses age out after an idle timeout (default 5 minutes)
- Secure MAC addresses do not age out by default
- With Port Security enabled, once the maximum is reached, no new secure MAC addresses are learned while the port stays up

### Enabling aging

- Command:

  ```cisco
  switchport port-security aging time <minutes>
  ```

- Example:

  ```cisco
  switchport port-security aging time 5
  ```

- After the configured time, secure MAC addresses are removed and the port can learn new ones

### Aging types

- absolute (default)
  - Timer starts when a secure MAC is learned
  - Entry ages out after the timer expires, even if frames from that MAC continue
- inactivity
  - Timer resets each time a frame from that MAC address is received
  - Similar to regular dynamic MAC behavior

- Command:

  ```cisco
  switchport port-security aging type {absolute | inactivity}
  ```

### Static secure MAC aging

- Static MAC addresses do not age out by default
- Static secure MACs behave the same way
- Aging for static secure MAC addresses can be enabled:

  ```cisco
  switchport port-security aging static
  ```

- Rarely used in practice, because static secure MAC addresses are usually meant to be permanent

## Sticky secure MAC addresses

### Concept

- Sticky secure MAC addresses are a hybrid of dynamic and static
- Learned dynamically
- Automatically written into the running configuration
- Survive interface down events

### Configuration

- Enable sticky learning:

  ```cisco
  switchport port-security mac-address sticky
  ```

- Current and future dynamically learned secure addresses on the port become sticky entries
- Sticky secure MAC addresses do not age out
- If sticky learning is disabled on a port, sticky entries revert to dynamic secure MAC addresses

## Troubleshooting Port Security

### Common issues

- Port is error disabled
  - Result of a Port Security violation
  - Check cause and MAC address that triggered it
- Legitimate devices blocked
  - Maximum MAC count too low for the number of devices on the port
- Secure MAC addresses not behaving as expected
  - Aging time or type not configured as intended
  - Sticky not enabled where persistence is required

### Troubleshooting steps

1. Check Port Security status on the interface:

   ```cisco
   show port-security interface <interface>
   ```

2. Review violation count and last source MAC.
3. Confirm maximum MAC address setting and violation mode.
4. List secure MAC addresses with:

   ```cisco
   show port-security address
   ```

5. Test connectivity from expected devices after making adjustments.

## Quick review

- Port Security limits the number of MAC addresses learned on a switchport and defines actions when that limit is exceeded.  
- Default maximum is one secure MAC and default violation mode is shutdown, which error disables the port.  
- ErrDisable Recovery can automatically reenable ports, but the original problem must be corrected.  
- Maximum MAC limits must match the number of devices on the port, such as phones plus PCs or downstream switches.  
- Secure MAC addresses can be dynamic, static, or sticky, and all count toward the maximum.  
- Violation modes shutdown, restrict, and protect differ in how they block traffic and how much visibility they provide.  
- Secure MAC address aging can be configured with absolute or inactivity timers and can optionally apply to static entries.  
- Sticky MAC learning provides an easy way to persist dynamically learned secure MAC addresses across interface down events.
