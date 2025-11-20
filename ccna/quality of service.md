# Quality of Service

## Overview

Network resources—bandwidth, in particular—are not unlimited. This means that networks can become congested, and bottlenecks can occur, negatively affecting network performance and the experience of the network's users. Some types of network communications are more sensitive to these problems. For example, users in a voice/video call, due to their real-time nature, are more likely to notice a network slowdown than users communicating via email. Quality of Service (QoS) is a set of technologies that enable the prioritization of more important traffic (and the de-prioritization of less important traffic) in times of network congestion. Before covering QoS itself, we will cover the topic of IP telephony, also called Voice over IP (VoIP)—telephones that communicate over a network using IP packets. Voice traffic is particularly sensitive to poor network performance and is usually prioritized in a QoS policy. We'll also cover Power over Ethernet (PoE), which is used to power IP phones (and other devices) over Ethernet cables.

## IP Telephony

### Traditional vs IP Telephony

- Traditional telephones connect to public switched telephone network (PSTN)
- Network separate from computer networks
- Also called plain old telephone service (POTS)
- IP phones, or VoIP phones, on other hand, connect to Ethernet switches and communicate by sending and receiving IP packets
- Many companies have migrated from POTS to IP telephony for variety of reasons
- Cost effectiveness and advanced features that IP telephony provides
- Examples: voicemail-to-email, integration with other business software, etc.

### IP Phone Internal Switch

- Migration to IP telephony created its own problems
- Each desk would now have two end-user devices (PC and IP phone)
- Doubling required number of Ethernet UTP cables that must be installed to each desk
- Doubling number of switch ports required
- As solution to this problem, IP phones have small, internal three-port switch
- Allowing IP phone and PC to connect to single switch port
- One port of mini-switch connects to PC, one to switch, and one to IP phone's internals

### Voice VLANs

- Although PC and IP phone can share single switch port, their traffic should be kept segmented
- Kept in separate subnets and separate VLANs
- One major reason for this is QoS: voice calls are very sensitive to lost and delayed packets
- Voice traffic should be prioritized over regular network traffic from PCs—also called data traffic
- By segmenting voice and data traffic into separate subnets and VLANs, can more easily identify and prioritize each traffic type in QoS policies
- This can be achieved using voice VLAN feature

### Access Ports with Voice VLANs

- When covering access and trunk ports, access ports belong to single VLAN
- Trunk ports can carry traffic from multiple VLANs, tagging frames with 802.1Q protocol
- Given that information, configuration shown—access ports carrying traffic in two VLANs—might seem incorrect
- However, this case is exception
- When access port is configured with voice VLAN, it carries traffic in two VLANs:
  - One for data VLAN (also called access VLAN), which is untagged
  - One for voice VLAN, which is tagged

### Voice VLAN Configuration

- Use `switchport mode access` to configure port as access port
- Use `switchport access vlan vlan-id` to configure data VLAN
- Use `switchport voice vlan vlan-id` to configure voice VLAN
- Can verify with `show interfaces interface switchport`
- Shows that port is considered access port despite carrying traffic in two VLANs
- Lists both data and voice VLANs

## Power over Ethernet (PoE)

### PoE Overview

- IP phones often take advantage of technology called Power over Ethernet (PoE)
- Allows phones to receive electrical power over same Ethernet UTP cables that they use to transmit data
- No need for separate power cables
- Provides reduced costs (fewer power cable runs required)
- Less desk and office clutter (fewer cables and adapters)
- Flexibility to place devices in locations without power outlet nearby

### PoE Power Transmission

- May wonder how electrical power and data can be transmitted over same cable
- Short answer: because of different frequency ranges used for power and data transmissions, they don't interfere with each other

### Power Sourcing Equipment and Powered Devices

- Switch is Power Sourcing Equipment (PSE)—device that supplies power using PoE
- IP phones are Powered Devices (PDs)
- Whereas switch and PCs receive electrical power from wall outlets, IP phones receive electrical power from switch using PoE

### PoE Process

A PSE must be cautious about sending electrical power over Ethernet cable. If PSE were to incorrectly send electrical power using PoE to device that is not designed to handle it, there is risk of damaging device. Similarly, if PSE were to send too much power to PD, that could damage PD. For that reason, PoE-enabled switch port doesn't immediately send electrical power when device is connected. Instead, it uses following process:

1. **Detection**: When device is connected, PSE performs initial check by applying low voltage to cable to detect if device can handle PoE
2. **Classification**: PSE assesses power needs of connected PD, and allocates required amount of power from its available supply
3. **Startup**: PSE supplies appropriate voltage to start up PD
4. **Normal operation**: PSE supplies power to PD and monitors electrical current to ensure safe and consistent delivery of power

### PoE Verification

- Use `show power inline` to confirm status of PDs
- Shows available power, used power, and remaining power
- Shows interface, admin state, operational state, power allocated, device type, class, and maximum power
- Class indicates power needs of connected device
- IP phones typically require less power and are often class 1 (4 watts) or class 2 (7 watts)
- Wireless access points are often class 3 (15.4 watts)

### PoE Configuration

- Can modify PoE settings of each switch port with `power inline` command in interface config mode
- Has various keywords
- By default, `power inline auto` command is applied
- With this command enabled, switch will automatically allocate power to port after detecting device that requires PoE connected to port
- However, power is allocated on first come, first served basis
- If there isn't enough power remaining in switch's total budget, it will not be able to supply power to device

### PoE Static Mode

- `power inline static [max milliwatts]` command can be used to preallocate power to port
- Reserving certain amount of power for port even when PD isn't connected
- If you don't specify value in command, maximum value is allocated
- When device is connected to port, switch still waits to detect PD, assess its power needs, and supply appropriate amount of power
- But amount of power specified in this command is always allocated for this port, even when it's not in use
- Should usually use default mode of `auto` since it allocates only as much power as needed to each device
- Doesn't require manual configuration
- However, `static` can be used if power budget is tight and you need to guarantee power to particular device
- Another option is `never`, which disables PoE on port

### PoE and Discovery Protocols

- Layer 2 discovery protocols CDP and LLDP can be used to facilitate PoE
- By allowing devices to communicate their PoE requirements
- These protocols help switches determine how much power connected device needs
- Like IP phone or wireless access point
- This negotiation process helps to prevent devices from drawing too much power
- While ensuring that each device is getting power it needs

### Power Policing

- If PD draws too much power from switch, it can damage switch
- One feature to protect against this is power policing (also called power classification override)
- Can enable this feature on switch port with `power inline police` command in interface config mode
- With power policing enabled, if PD draws too much power (more than cutoff power), switch will put port into error-disabled state
- Stopping data and power transmission on port
- And generate Syslog message
- To reenable error-disabled port, can use `shutdown` to administratively disable port and then `no shutdown` to reenable it
- Make sure to disconnect device that caused problem first!
- Use `show power inline police` to check status

## QoS Fundamentals

### Need for QoS

- Voice traffic from IP phones is particularly sensitive to network congestion
- If packets are getting delayed or dropped, user experience can be severely impacted
- Same applies to calls on Zoom and similar apps
- However, other types of traffic are less affected
- File downloads, for example, may take bit longer to complete when network is congested
- But overall user experience remains same
- Using QoS, can prioritize some types of traffic and de-prioritize others
- To maintain positive user experience when congestion occurs

### Bandwidth and Bottlenecks

- Bandwidth refers to link's capacity—how much data it can carry per second
- Different areas of network typically have different total bandwidths
- Which can lead to bottlenecks
- Whereas each end host typically has plenty of bandwidth over its connection to network (e.g., 1 Gbps link per host)
- Wide area network (WAN) and internet connections are common bottlenecks
- Significant reason for this is cost; connecting remote sites over service provider's network is expensive
- Fortunately, it's not necessary to have 1:1 ratio of bandwidth between end hosts and WAN
- End hosts aren't always communicating over WAN
- When they are, they usually aren't all communicating at their full capacity at same time
- However, during peak usage, congestion can occur
- Leading to some negative effects: delay, jitter, and loss

### Delay (Latency)

- Purpose of QoS is to minimize delay, jitter, and loss of important traffic during times of congestion
- Delay (or latency) is amount of time it takes packet to travel across network from its source to its destination
- Related term is round-trip time (RTT), which is two-way delay
- Amount of time it takes packet to reach its destination and for reply packet to be received by original sender
- Delay is usually measured in milliseconds
- Cisco recommends that delay should be 150 ms or less for voice traffic
- What happens if delay gets much higher than that?
- Think of phone call in which person you're talking to only hears what you say 2 seconds after fact
- Not smooth conversation

### Jitter

- Jitter is variation in delay in series of packets
- Some delay is inevitable; packets sometimes have to travel quite long way and through quite few intermediate devices to reach their destination
- However, delay should ideally remain fairly constant
- Too much jitter negatively affects user experience in real-time apps like voice and video calls
- Like delay, jitter is measured in milliseconds
- Cisco recommends that jitter should be 30 ms or less for voice traffic

### Loss

- Final concept is loss, which is percentage of packets lost over period of time
- Packets that didn't reach their destination
- Under normal circumstances, loss should be close to zero
- However, in times of congestion, some packets may have to be dropped
- Cisco recommends loss of 1% or less for voice calls
- TCP-based applications can deal with dropped packets through retransmissions
- On other hand, UDP-based VoIP protocols don't retransmit dropped packets
- This is intentional; waiting for packet to be retransmitted in voice call would only cause more delay and disrupt conversation
- However, if there are too many drops, users will experience familiar issue of call "breaking up"
- Resulting in choppy or interrupted audio

### IP SLA

- Cisco IOS devices include feature called IP Service-Level Agreement (IP SLA)
- Can be used to measure various aspects of network performance
- Including delay, RTT, jitter, and loss
- Service-level agreement is predefined set of performance metrics/standards that service is expected to meet
- Usually agreed upon between service provider and customer
- IP SLA helps verify these standards by using mechanisms such as ICMP echo requests (ping) to measure RTT and loss
- Can be used to measure effectiveness of QoS policies
- Although IP SLA was part of older CCNA exams, it was removed in current 200-301 version

## QoS Components

### QoS Big Picture

- When packets arrive faster than router can forward them out of particular interface, it queues packets waiting to be transmitted
- This is when QoS is needed
- By default, there is only single queue, and packets are forwarded in first in, first out (FIFO) manner
- Not prioritizing any packets over others
- However, QoS allows you to classify packets based on their type, queue them in separate queues, and use advanced scheduling methods
- Such as Class-Based Weighted Fair Queuing (CBWFQ), Priority Queuing (PQ), and Low Latency Queuing (LLQ)
- To determine order in which packets are transmitted

## Classification and Marking

### Classification vs Marking

- Classification and marking are two components of QoS that are often confused
- Classification is process of sorting messages into different classes based on kind of treatment you want to give them
- High priority, low priority, etc.
- Marking is process of setting value of certain header fields to make classification process simpler

### Classification

- Classification is essential for QoS
- To prioritize certain types of traffic, have to identify those types of traffic
- That is role of classification
- Device classifies packets into different classes
- Examples: Real-Time (voice and video), Business Critical (important business apps), Default, and Scavenger traffic (low priority)
- Scavenger traffic is low-priority, noncritical traffic that is left to "scavenge" for leftover bandwidth during network congestion
- These packets are first that should be dropped or delayed to prioritize more critical/delay-sensitive packets
- Example: social media browsing would likely be classified as scavenger traffic

### Classification Methods

- Packets can be classified in variety of ways
- For example, ACLs can be used
- Packets permitted by one ACL are assigned to one class
- Packets permitted by another ACL are assigned to another class
- However, ACLs have their limitations—matching based on information in Layer 3 and Layer 4 headers
- Sometimes, have to look deeper to determine exactly what kind of packets are being sent
- Network-Based Application Recognition (NBAR) makes this possible
- By performing deep packet inspection, examining actual contents of some of packets in particular exchange to accurately classify them

### Marking

- Complex classification using ACLs/NBAR can be demanding on device doing classification
- Also complex to configure on every device in network
- Ideally, packet should be classified with these methods early and then marked
- Using specific fields in IP/Ethernet headers
- To make classification process simpler for rest of packet's life
- After packet has been marked, instead of examining packet's source/destination IP addresses and port numbers with ACLs
- Or examining contents of packet's payload with NBAR
- Device can simply look at marking in DSCP or PCP fields to make classification decision
- This reduces burden on device itself, and on people who configure it

### Priority Code Point (PCP)

- Two fields have been specifically defined for QoS marking
- Differentiated Services Code Point (DSCP) field of IPv4 and IPv6 headers
- Priority Code Point (PCP) field of 802.1Q tag in Ethernet header
- PCP field is also called Class of Service (CoS)
- Commonly confused with QoS as whole
- However, CoS only refers to this specific field in 802.1Q tag
- Three-bit PCP field can be used to mark 802.1Q-tagged Ethernet frames
- Allowing them to be easily classified based on value in this field
- PCP is three-bit field in 802.1Q tag of Ethernet header
- As three-bit field, PCP provides eight possible values (2^3 = 8)
- Example: standard PCP marking for voice traffic is 0b101 (0d5)
- Messages with this marking should be treated with high priority
- On other hand, default value is 0b000 (0d0), meaning "best effort"
- Regular traffic that should not be given special treatment

### PCP Limitations

- PCP field has one major limitation: it's part of 802.1Q tag
- Which is only present in frames traversing trunk links (or voice VLAN of access links)
- Frames sent between two routers, for example, don't include 802.1Q tags
- If user is having phone call on IP phone, phone can send its packets in 802.1Q-tagged frames marked with PCP value of 5
- This allows switch and router to recognize them as high priority
- However, 802.1Q tag is only present until packet reaches router
- When router forwards packets to another router, it forwards them in untagged frames
- For this reason, PCP's utility is limited
- Instead, most QoS policies make use of DSCP field in IP header

### Differentiated Services Code Point (DSCP)

- Both IPv4 and IPv6 headers contain 6-bit DSCP field
- In IPv4 header, it's part of byte called Differentiated Services (DiffServ)
- DiffServ byte was formerly known as Type of Service (ToS)
- In IPv6 header, this byte is called Traffic Class
- Its definition is same as in IPv4: DSCP (6 bits) and ECN (2 bits)
- In past, only 3 bits of this byte were used for QoS marking
- This 3-bit field was called IP Precedence (IPP)
- Old ToS byte defined 3-bit IPP field for QoS marking
- Current DiffServ byte defines 6-bit DSCP field for QoS marking

### Explicit Congestion Notification (ECN)

- 2-bit Explicit Congestion Notification (ECN) field's purpose is to notify packet's receiver of network congestion
- However, its practical adoption has been somewhat limited
- Not part of CCNA exam

### DSCP Advantages

- One major benefit of basing QoS policies on DSCP markings, rather than PCP markings, is that DSCP markings stay with packet end to end
- Once device marks packet's DSCP field, that marking will remain with packet until it reaches its destination
- Unless another device modifies marking
- As opposed to IPP and PCP, which are both 3 bits in size, DSCP is 6 bits
- Providing 64 (2^6) unique values
- You are free to use these 64 values as you like in your QoS policies
- Example: could mark voice traffic with highest value (63), scavenger traffic with lowest value (0), and everything else with value in between

### Standardized DSCP Markings

- However, it would not be ideal for every network to use totally different marking scheme
- This would overcomplicate things and create challenges in maintaining consistent QoS policies when different networks connect with each other
- To address this, standardized markings have been developed and are widely adopted in industry
- These standards provide common "language" for QoS across various devices and vendors

### Default Forwarding (DF)

- Default Forwarding (DF) is default marking used for best-effort traffic
- Uses binary value of 000000 in DSCP field (0 in decimal)

### Expedited Forwarding (EF)

- Expedited Forwarding (EF) is used for delay/jitter/loss-sensitive traffic
- Uses binary value of 101110 in DSCP field (46 in decimal)

### Class Selector (CS)

- Class Selector (CS) is standardized set of DSCP markings created to be backward compatible with older IPP system
- Both IPP and CS use only first three bits of ToS/DiffServ byte
- Providing eight possible values
- Three least-significant bits of DSCP field are set to 0
- Then, three most significant bits—same bits used by IPP—are used to create eight possible values
- CS marking system is particularly useful when dealing with legacy systems or environments where older IPP values are still in use
- Organizations that designed their QoS policies around IPP can simply translate those values to their equivalent CS values
- In other words, CS was designed as way to bridge gap between old IPP and new DSCP

### Assured Forwarding (AF)

- CS is useful for its backward compatibility with IPP, but it doesn't take advantage of greater number of possible values that DSCP offers
- Assured Forwarding (AF) defines 12 additional standardized marking values
- Four traffic classes, with three levels of drop precedence within each class
- Packet marked with higher drop precedence is more likely to be dropped during congestion
- Packets are assigned to one of four queues
- Within each queue, some packets are more likely to be dropped than others during congestion
- AF uses five most significant bits of DSCP field; least significant bit is set to 0
- Furthermore, 5 bits are divided into class value (3 bits) and drop precedence value (2 bits)
- Written as AFXY (X = class, Y = drop precedence)
- Although 3 bits allow for eight different values (0–7), AF only defines four traffic classes (1–4)
- Likewise, 2 bits allow for four different values (0–3), but AF only defines three drop precedence levels (1–3)

### AF Marking Calculation

- Simple shortcut to calculate decimal DSCP value of particular AF marking
- Multiply class value by 8 and drop precedence value by 2 and then add them together
- Example: AF42
  - Class is 4: 4 × 8 = 32
  - Drop precedence is 2: 2 × 2 = 4
  - Add them together: 32 + 4 = 36
- One counterintuitive thing is that higher value doesn't necessarily mean better
- Example: AF41 (decimal 34) and AF43 (decimal 38) are both in highest-priority class
- But AF41 has lower drop precedence than AF43

### RFC 4594 Recommendations

- RFC 4594 provides standardized marking recommendations for various kinds of traffic
- Examples:
  - Network Control: CS6 (48) - OSPF, EIGRP, BGP messages
  - Telephony: EF (46) - Voice call traffic
  - Real-Time Interactive: AF4x (34, 36, 38) - Interactive gaming
  - Multimedia Streaming: AF3x (26, 28, 30) - Streaming video/audio
  - Low-Latency Data: AF2x (18, 20, 22) - Client–server interactions
  - Standard: DF (CS0) (0) - Default (best effort)
  - Low-Priority data: CS1 (8) - Scavenger traffic, guest Wi-Fi
- RFC 4594 includes several more recommendations than those shown
- Depending on needs of network, differentiating between so many traffic types may be unnecessary
- RFC recommends thinking of them as toolkit; some tools are necessary for some jobs but unnecessary for others
- For CCNA exam, recommend knowing DF's role as default best-effort marking, EF's role in marking delay/jitter/loss-sensitive traffic, CS's use for backward compatibility with IPP, and AF's class/drop precedence system

### Trust Boundaries

- Trust boundary is logical division in network
- Markings from devices on one side of boundary are trusted to be accurate
- Markings from devices on other side are not trusted
- If device trusts marking, device will forward packet without modifying marking
- However, if device doesn't trust marking, device will re-mark packet according to configured policy
- Typically, markings from IP phones are trusted
- But markings from PCs are not
- IP phones mark their packets—usually EF for packets that contain actual audio data
- To simplify things for switch, it is standard practice to trust phone's markings
- However, markings from PCs are different story
- Tech-savvy user (who is aware of QoS concepts) could configure their PC to mark its packets with EF as well
- Resulting in PC's traffic receiving preferential treatment over that of other PCs
- To protect against such situation, should ensure that PCs are on "untrusted" side of trust boundary
- If packet from PC is marked, IP phone or switch should re-mark it to appropriate value (according to configured policy)

## Queuing and Scheduling

### Queuing Overview

- In times of congestion, interface may not be able to transmit packets fast enough to keep up with rate at which packets are assigned to be transmitted out of interface
- What happens to excess packets that cannot immediately be transmitted?
- Answer is queuing; device will store excess packets in one or more queues as they wait their turn to be transmitted

### FIFO Queuing

- Without QoS, each interface uses single egress queue
- Device will transmit packets in queue in first in, first out (FIFO) manner
- In order that they enter queue
- This is called scheduling—process of determining order in which queued packets are actually transmitted
- FIFO is fine for simple networks without lot of traffic
- But to prioritize particular kinds of traffic—goal of QoS—different technique is needed

### Queuing vs Scheduling

- Queuing is process of storing packets in queues while they wait to be transmitted
- Scheduling is process of deciding in which order queued packets will be transmitted
- Remember this distinction!

### Priority Queuing (PQ)

- Priority Queuing (PQ) supports up to four separate queues that are ranked by priority
- Packets in lower-priority queue will only be transmitted if higher-priority queues are all empty
- When PQ scheduler decides which queue to service next, it scans queues in order from highest to lowest priority
- It makes this decision one packet at a time, scanning queues in order each time
- Depending on amount of traffic in higher-priority queues, this could mean that lowest-priority queue is serviced very infrequently
- This is called queue starvation
- For that reason, PQ is rarely used anymore
- It's better than simple FIFO, but there are even better options available on modern devices

### Class-Based Weighted Fair Queuing (CBWFQ)

- Class-Based Weighted Fair Queuing (CBWFQ) uses round-robin scheduling
- It services each queue in cyclical order
- For example, if there are four queues: 1, 2, 3, 4, 1, 2, 3, 4, 1, etc.
- However, simple round-robin scheduling treats all queues equally
- Which doesn't fulfill goal of prioritizing certain types of traffic
- Instead, CBWFQ uses weighted round-robin
- Which allows you to specify guaranteed minimum amount of bandwidth for each queue
- In times of congestion, scheduler will ensure that each queue receives at least specified amount of bandwidth
- CBWFQ avoids problem of queue starvation by guaranteeing minimum amount of bandwidth to each queue
- However, its round-robin scheduler is problem for delay-sensitive traffic
- Even if delay-sensitive traffic is given sufficient bandwidth, packets may have to wait to be transmitted as scheduler services other queues
- Next queuing/scheduling method addresses this concern

### Low Latency Queuing (LLQ)

- Low Latency Queuing (LLQ) combines strengths of PQ and CBWFQ
- In fact, another name for it is PQCBWFQ (not very elegant name—let's stick with LLQ)
- To put it simply, LLQ is CBWFQ with priority queue
- Delay-sensitive traffic should be assigned to priority queue
- If packets are waiting in priority queue, scheduler will always service them first
- If priority queue is empty, scheduler will serve other queues using CBWFQ logic
- Notice that bandwidth is applied to priority queue
- In priority queue's case, this isn't minimum guaranteed bandwidth—it's maximum
- Because priority queue is always serviced before other queues, there is risk of queue starvation occurring if lots of packets are assigned to priority queue
- By limiting amount of traffic that is allowed to enter priority queue (e.g., 30% of interface's bandwidth), can avoid queue starvation
- What happens if more than configured percentage of bandwidth consists of packets assigned to priority queue?
- In that case, excess packets will either be dropped or re-marked and assigned to lower queue
- This is example of policing, which we will cover next

## Policing and Shaping

### Rate-Limiting Techniques

- Policing and shaping are two rate-limiting techniques
- They limit rate at which interface sends or receives traffic
- Both techniques work by defining rate limit (e.g., 300 Mbps) and then taking action on traffic that exceeds configured limit

### Policing

- Policing drops traffic that exceeds rate limit
- Instead of dropping packets that exceed rate limit, policing also provides option to re-mark them
- Causing packets to be classified differently
- Example: LLQ uses policing to limit rate at which packets enter priority queue
- Excess packets are either dropped or re-marked and assigned to different queue, depending on configuration

### Shaping

- Shaping buffers traffic that exceeds rate limit to smooth out flow of data
- Instead of dropping packets, shaping queues them in separate shaping queue
- Transmits them at rate that conforms with configured limit

### Policing and Shaping Configuration

- Policing and shaping can be configured on per-class basis
- So packets in each class (and, therefore, each queue) are policed/shaped separately
- They can also be configured on per-interface basis
- Applying to all packets transmitted or received by interface

### Common Use Case

- ISP's customer has paid for 300 Mbps connection
- So ISP router polices traffic received from customer to rate limit of 300 Mbps
- Both routers are connected by GigabitEthernet interfaces
- But because ISP router polices incoming traffic, customer router shouldn't send packets out of interface at full capacity
- That would result in dropped packets
- To ensure that packets don't get dropped by ISP's router, customer uses shaping to control rate at which packets are sent to ISP

## Congestion Avoidance

### Tail Drop

- QoS techniques covered so far are all designed to help devices in network deal with congestion
- Minimizing its impact on types of traffic that are particularly sensitive to delay, jitter, and loss
- However, interfaces' queues aren't infinite
- If congestion reaches certain point and queues start to overflow, packet loss is inevitable
- When packet is assigned to enter queue but can't because queue is full, packet will be dropped
- This is called tail drop

### TCP Global Synchronization

- Packet loss on its own isn't such bad thing
- Protocols that use TCP as their Layer 4 protocol can recover from dropped messages using retransmissions
- However, tail drop in particular can lead to (and result from) undesirable phenomenon called TCP global synchronization
- To understand TCP global synchronization, let's review TCP window size mechanism
- In TCP exchange between hosts, each host specifies window size
- In effect, this tells other host how much data to send before waiting for acknowledgment
- This mechanism allows receiver to control how quickly sender sends data
- To ensure that receiver isn't overwhelmed
- Window size is not static
- Each time receiver receives data, it will specify larger window size in acknowledgment message it sends in reply
- However, when segment is lost (e.g., as result of tail drop), receiver will immediately reduce window to much smaller size
- Receiver will then gradually increase window size again, and process will repeat
- Purpose is to find optimal transmission rate that doesn't result in packet loss
- And to dynamically adapt to network congestion
- Global synchronization occurs when many hosts simultaneously reduce and then increase their window sizes in response to packet loss
- This is often result of tail drop
- Although packet loss on its own doesn't have such negative effects, effect is greater when it happens to many hosts at once
- Leading to vicious cycle: network congestion leads to tail drop, which leads to global TCP window size decrease
- All hosts who experience packet loss will immediately reduce their window sizes
- This leads to network underutilization; all hosts are using very small window sizes, leading to slow transmission rates
- This leads to global TCP window size increase, which again leads to network congestion
- And vicious cycle repeats
- This isn't efficient use of network bandwidth

### Random Early Detection (RED)

- Instead of waiting for queues to fill up, resulting in tail drop and TCP global synchronization, better tactic is to start dropping some packets before tail drop happens
- That way, instead of all receivers reducing their TCP window sizes simultaneously, only those few hosts that have experienced packet loss will
- That's what Random Early Detection (RED) and Weighted Random Early Detection (WRED) do
- RED drops percentage of packets once queue starts filling up beyond certain point
- Hosts that experience dropped packets will reduce their window sizes
- And that will hopefully reduce overall traffic rate and size of queue

### Weighted Random Early Detection (WRED)

- WRED functions in same manner as RED but allows for more control over which packets are dropped
- For example, think back to AF markings covered earlier
- Some AF markings are designated as having high drop precedence, and some are designated as having low drop precedence
- This is one situation in which those drop precedences can be implemented
- Main advantage of using RED and WRED over simple tail drop is that they provide more proactive approach to managing congestion
- By dropping some packets before queue is full, RED and WRED aim to prevent queue from becoming full in first place
- And avoid TCP global synchronization
- RED and WRED should not be used for traffic types that are sensitive to packet loss

## Per-Hop Behavior (PHB)

### PHB Overview

- Exam topic 4.7 specifies per-hop behavior (PHB) of QoS
- PHB describes how each device handles QoS individually
- All of QoS concepts covered in this chapter, from classifying packets to scheduling them for transmission, apply on per-device basis
- In other words, just because one router is configured to prioritize EF-marked packets, it doesn't automatically mean that other devices in network will
- Each device needs to be explicitly configured to treat these markings according to your QoS policy
- EF marking (or any other marking) is meaningless unless you tell each device how to treat packets with that specific marking

### End-to-End QoS

- When implementing QoS, policy must be consistently applied across all devices in network path for it to be effective from end to end
- Details of designing and implementing QoS policies, including how to configure QoS on Cisco devices, are beyond scope of CCNA exam
- However, it's important to understand per-hop behavior of QoS

## Real-World Applications

- **Voice over IP**: Prioritize voice traffic to ensure quality phone calls
- **Video conferencing**: Ensure smooth video calls and meetings
- **Business applications**: Prioritize critical business applications over recreational traffic
- **Network management**: Ensure management traffic gets through during congestion
- **Service provider networks**: Meet SLA requirements for customers
- **Enterprise networks**: Ensure important traffic gets priority during peak usage

## Troubleshooting

### Common Issues

- **Voice quality poor**: Verify voice traffic is being classified and marked correctly
- **QoS not working**: Verify QoS is configured on all devices in path
- **Queue starvation**: Check queuing configuration and bandwidth allocations
- **Traffic not prioritized**: Verify markings are correct and devices trust/respect them

### Troubleshooting Steps

1. Verify classification: Check packets are being classified into correct classes
2. Check markings: Verify DSCP/PCP values are set correctly
3. Verify queuing: Check queuing configuration on interfaces
4. Monitor statistics: Use QoS statistics commands to monitor performance
5. Test traffic: Send test traffic and verify it's being treated correctly
6. Check trust boundaries: Verify trust boundaries are configured correctly

## Best Practices

- Classify and mark packets early in network (at access layer)
- Use standardized markings (DF, EF, CS, AF) for consistency
- Trust markings from IP phones but not from PCs
- Use LLQ for delay-sensitive traffic like voice
- Configure appropriate bandwidth guarantees for each traffic class
- Use policing to prevent queue starvation in priority queues
- Use shaping to smooth traffic to service provider limits
- Avoid using RED/WRED for loss-sensitive traffic
- Apply QoS consistently across all devices in network path
- Monitor QoS performance regularly
- Test QoS policies in lab before production deployment

## Summary

- Quality of Service (QoS) is set of technologies that enable prioritization and de-prioritization of certain types of traffic in times of network congestion
- QoS is often used to prioritize sensitive traffic like voice traffic from IP phones
- IP phones, also called Voice over IP (VoIP) phones, connect to Ethernet switches and communicate by sending and receiving IP packets
- IP phones have internal three-port switch that allows IP phone and PC to share single switch port
- Access ports can be configured with voice VLAN to carry traffic in two VLANs: data/access VLAN (untagged) and voice VLAN (tagged)
- Use `switchport voice vlan vlan-id` to configure access port's voice VLAN
- Power over Ethernet (PoE) is often used to power IP phones and other smaller devices over same Ethernet cable
- Switch is PoE Power Sourcing Equipment (PSE); IP phones are Powered Devices (PDs)
- PSE waits to detect PoE-enabled device, assess its power needs, and then supply electrical power
- Use `show power inline` to confirm status of PDs
- Use `power inline [auto | static [max milliwatts]]` to control port's PoE settings
- Power policing can be used to error-disable switch port if connected device draws too much power
- Bandwidth refers to link's capacity; not all areas of network have identical bandwidth, which can lead to bottlenecks
- Purpose of QoS is to minimize delay, jitter, and loss during network congestion
- Delay is amount of time it takes packet to travel from source to destination (one way)
- Cisco recommends delay should be 150 ms or less for voice traffic
- Jitter is variation in delay in series of packets
- Cisco recommends jitter should be 30 ms or less for voice traffic
- Loss is percentage of packets lost over period of time
- Cisco recommends loss should be 1% or less for voice traffic
- When packets arrive faster than router can forward them, it queues packets waiting to be transmitted
- By default, there is single queue, and packets are forwarded in FIFO manner
- Classification is process of sorting messages into different classes
- Packets can be classified using ACLs or Network-Based Application Recognition (NBAR)
- Marking is process of setting value of certain header fields (PCP/CoS, DSCP) to make classification simpler
- Priority Code Point (PCP) field, also called Class of Service (CoS), is 3-bit field in 802.1Q tag
- PCP is only included in 802.1Q-tagged frames and does not stay with packet for entire life
- Differentiated Services Code Point (DSCP) is 6-bit field in IP header providing 64 possible values
- Default Forwarding (DF) uses value 0 and is recommended for best-effort traffic
- Expedited Forwarding (EF) uses value 46 and is recommended for delay/jitter/loss-sensitive traffic
- Class Selector (CS) is standardized set of DSCP markings backward compatible with IPP
- Assured Forwarding (AF) defines 12 marking values: four traffic classes with three drop precedence levels
- To calculate AF decimal value: multiply class by 8 and drop precedence by 2, then add
- Trust boundary is logical division where markings from one side are trusted and from other side are not
- Typically, markings from IP phones are trusted, but markings from PCs are not
- Queuing is process of storing packets in queues; scheduling is process of deciding transmission order
- Priority Queuing (PQ) uses up to four queues ranked by priority; lower-priority queues can suffer from queue starvation
- Class-Based Weighted Fair Queuing (CBWFQ) uses weighted round-robin scheduling with guaranteed minimum bandwidth
- Low Latency Queuing (LLQ) combines CBWFQ with priority queue; delay-sensitive traffic is always serviced first
- Policing drops traffic that exceeds rate limit; shaping buffers excess traffic to smooth flow
- Tail drop occurs when queues fill up and cannot contain more packets
- Tail drop can lead to TCP global synchronization, causing inefficient use of bandwidth
- Random Early Detection (RED) and Weighted Random Early Detection (WRED) drop packets before queues fill up
- Per-hop behavior (PHB) describes how each device handles QoS individually
- QoS policy must be consistently applied across all devices in network path for end-to-end effectiveness

