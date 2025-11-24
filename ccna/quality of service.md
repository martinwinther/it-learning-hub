# Quality of Service

## Overview

Quality of Service (QoS) is a set of tools that control how traffic is treated during congestion. The goal is to protect delay and loss sensitive traffic such as voice and video when links fill up.

## IP telephony and voice VLANs

### IP telephony basics

- Traditional phones use the PSTN (POTS) on a separate network from data.
- IP phones (VoIP) connect to Ethernet switches and send voice as IP packets.
- Common reasons to use IP telephony:
  - Lower cost for calls
  - Easy integration with software (voicemail to email, softphones, etc.)

### Internal switch and shared ports

- IP phones include a small internal switch.
- A single wall port and switch port can serve both phone and PC.
- Typical wiring:
  - Wall jack ↔ IP phone
  - IP phone internal switch:
    - One port to PC
    - One port to access switch
    - One internal port for the phone itself

### Voice VLANs

- Phone and PC traffic should stay in separate VLANs and subnets.
- Data VLAN (access VLAN):
  - Used by the attached PC, frames are untagged.
- Voice VLAN:
  - Used by the phone, frames are tagged.
- Access port with voice VLAN carries two VLANs:
  - Untagged data VLAN
  - Tagged voice VLAN

Basic configuration:

```cisco
interface GigabitEthernet0/1
 switchport mode access
 switchport access vlan 10
 switchport voice vlan 20
```

- Verify with `show interfaces GigabitEthernet0/1 switchport`.

## Power over Ethernet

### PoE basics

- Power over Ethernet (PoE) provides power and data on the same UTP cable.
- Switch supplying power is Power Sourcing Equipment (PSE).
- IP phones and access points are Powered Devices (PDs).
- Benefits:
  - No separate power bricks and wall outlets
  - Flexible device placement

### PoE process

High level steps on a PoE enabled port:

1. Detection - low voltage test to see if the device supports PoE.
2. Classification - determine required power class.
3. Startup - apply correct voltage and power limit.
4. Normal operation - monitor current draw.

### PoE configuration and verification

- Default mode on many switches:

  ```cisco
  interface GigabitEthernet0/1
   power inline auto
  ```

- Key commands:
  - `show power inline` - overview of PoE usage and device classes.
  - `power inline static [max milliwatts]` - reserve power for a specific port.
  - `power inline never` - disable PoE on a port.

### Power policing

- `power inline police` protects the switch if a device draws too much power.
- If the draw exceeds the limit, the port is error disabled and a syslog is generated.
- Status can be checked with `show power inline police`.

## QoS fundamentals

### Why QoS is needed

- Bandwidth is limited, especially at WAN and internet edges.
- When packets arrive faster than a link can send them, they are queued.
- Without QoS, a single FIFO queue is used:
  - All packets treated the same.
  - Important flows can be delayed or dropped.

Voice and real time video are sensitive to:

- Delay (latency) - one way travel time.
- Jitter - variation in delay between packets.
- Loss - packets dropped due to congestion or errors.

Cisco voice guidelines:

- Delay: 150 ms or less one way.
- Jitter: 30 ms or less.
- Loss: 1 percent or less.

## Classification and marking

### Classification

- Classification groups packets into classes for different QoS treatment.
- Example classes:
  - Real time (voice and video)
  - Business critical
  - Default
  - Scavenger (low priority, drop first)
- Methods:
  - Access control lists (ACLs) matching L3/L4 fields
  - Network Based Application Recognition (NBAR) for deep inspection

### Marking

- After classification, packets are marked so downstream devices can recognize the class easily.
- Marking uses specific header fields:
  - DSCP in IP header
  - PCP (Class of Service) in 802.1Q tag
- Devices later in the path can make decisions based on these fields instead of repeating complex classification.

## PCP and DSCP

### PCP (CoS) marking

- Priority Code Point (PCP) is a 3 bit field in the 802.1Q tag.
- Often called Class of Service (CoS).
- Provides 8 values (0 to 7).
- Typical mapping:
  - Voice frames: PCP 5
  - Best effort: PCP 0
- Limitation:
  - 802.1Q tag is present only on trunk links and on the voice VLAN of access links.
  - PCP information is lost once the frame is forwarded without a tag.

### DSCP marking

- Differentiated Services Code Point (DSCP) is a 6 bit field in IPv4 and IPv6 headers.
- Part of the DiffServ byte (formerly ToS).
- Provides 64 values (0 to 63).
- DSCP stays with the packet end to end unless changed by a device.

Important standardized DSCP values:

- Default Forwarding (DF or CS0): 0
  - Best effort traffic.
- Expedited Forwarding (EF): 46
  - Delay and loss sensitive traffic such as voice.
- Class Selector (CSx):
  - Backward compatible with older IP precedence values.
  - Uses the upper three bits, lower three bits set to 0.
- Assured Forwarding (AFxy):
  - Four classes (1 to 4) and three drop precedence levels (1 to 3).
  - AF uses the pattern AFXY, where X is class and Y is drop precedence.

AF decimal calculation shortcut:

- AFxy = (x × 8) + (y × 2)
- Example: AF42
  - Class 4: 4 × 8 = 32
  - Drop precedence 2: 2 × 2 = 4
  - DSCP = 36

### Trust boundaries

- Trust boundary marks where markings are accepted as valid.
- Typical rules:
  - Trust DSCP/PCP from IP phones.
  - Do not trust markings from PCs.
- Devices at the boundary:
  - Preserve trusted markings.
  - Re mark or clear markings from untrusted devices according to policy.

## Queuing and scheduling

### Queuing vs scheduling

- Queuing:
  - Storing packets in one or more queues while waiting to send them.
- Scheduling:
  - Deciding the order in which packets leave the queues.

### FIFO

- Single queue per interface.
- First in, first out behavior.
- No differentiation between traffic types.

### Priority Queuing

- Up to four queues with priority levels.
- Higher priority queues are always emptied before lower ones.
- Risk of starvation for low priority queues.
- Rarely used alone in modern designs.

### Class Based Weighted Fair Queuing

- Class Based Weighted Fair Queuing (CBWFQ) uses round robin scheduling with weights.
- Each class is guaranteed a minimum share of bandwidth during congestion.
- Avoids starvation but can still introduce delay for real time traffic.

### Low Latency Queuing

- Low Latency Queuing (LLQ) combines CBWFQ with one strict priority queue.
- Real time traffic (voice, some video) goes to the priority queue.
- Scheduler always services the priority queue first, then rotates through other queues with CBWFQ.
- Priority queue gets a bandwidth limit to prevent starvation of other traffic.
- Excess traffic above the limit is policed or re marked into other queues.

## Policing and shaping

### Concepts

- Both techniques define a rate and act on traffic above that rate.
- Often configured per class, sometimes per interface.

### Policing

- Immediate enforcement.
- Traffic above the configured rate is dropped or optionally re marked to a lower class.
- Used for functions such as:
  - Limiting LLQ traffic
  - Enforcing contracted rates at a service provider edge

### Shaping

- Buffers traffic above the configured rate and sends it later.
- Smooths bursts so that downstream devices see a more consistent rate.
- Typical use case:
  - Customer router shapes to the contracted WAN rate to avoid drops at the provider edge.

## Congestion avoidance

### Tail drop

- When a queue is full, new packets are dropped from the tail of the queue.
- Tail drop can cause many TCP flows to detect loss at the same time.
- Each flow reduces its TCP window sharply, then slowly increases it again.
- Many flows doing this together is called TCP global synchronization and wastes bandwidth.

### RED and WRED

- Random Early Detection (RED) starts dropping packets randomly before the queue is full.
- Weighted RED (WRED) does the same but considers markings such as DSCP:
  - Higher drop precedence packets are dropped more aggressively.
- Goal is to signal congestion early and avoid full queues and global synchronization.
- RED and WRED are not used for very loss sensitive traffic such as voice.

## Per hop behavior

- Per hop behavior (PHB) describes how each device treats traffic based on its markings.
- QoS is configured per device:
  - One router trusting EF does not mean every device does.
- End to end QoS requires:
  - Consistent markings
  - Consistent class definitions
  - Matching queuing, scheduling, and policing rules along the path

## Quick review

- QoS protects important traffic such as voice and video when links are congested.  
- IP phones use internal switches, voice VLANs, and often PoE from access switches.  
- Classification assigns packets to classes; marking writes those decisions into PCP or DSCP fields.  
- PCP is a 3 bit field in 802.1Q tags and is only present on tagged Ethernet frames.  
- DSCP is a 6 bit field in IP headers and stays with the packet from source to destination.  
- Standard DSCP values include DF (0) for best effort, EF (46) for voice, CSx for precedence style classes, and AFxy for assured forwarding with drop precedence.  
- Trust boundaries define which markings are accepted (for example, trust phones but not PCs).  
- LLQ provides a strict priority queue for real time traffic combined with CBWFQ for other classes.  
- Policing drops or re marks traffic above a rate; shaping buffers excess traffic to smooth the rate.  
- RED and WRED perform early drops to avoid full queues and TCP global synchronization.  
- Per hop behavior means each device must be configured to honor markings for end to end QoS to work.

