# Wireless LAN Fundamentals

## Overview

It's time to break our communications out of their wired constraints and explore a new medium for communication: air. Just as copper twisted-pair and glass fiber-optic cables provide a medium to transmit encoded messages using electricity and light, the air all around us (or, more precisely, the space around us that happens to be filled with air) provides an alternative medium to transmit messages using electromagnetic waves. In this chapter and the three that follow it, we will cover various aspects of wireless LANs as defined by IEEE 802.11—better known as Wi-Fi. This chapter starts by covering the foundational concepts of wireless LANs and how devices communicate with radio frequency waves.

## Wireless LAN Standards

### IEEE 802.11

- Wired LANs as defined by IEEE 802.3—better known as Ethernet—have been major focus of both volumes of this book up to this point
- And for good reason: Ethernet is dominant technology used in modern wired network connections and is key topic of CCNA exam
- Ethernet defines standards at Layers 1 and 2 of TCP/IP model: physical cables, methods of encoding data signals over these cables, Ethernet frame format, and various other functions
- Wireless LANs are defined by IEEE 802.11
- Like Ethernet, 802.11 defines standards at Layers 1 and 2 of TCP/IP model: precise frequencies that can be used for wireless LANs, how to encode data signals in electromagnetic waves over air, 802.11 frame format, etc.
- Wireless LAN is sometimes abbreviated as WLAN
- Wired and wireless both start with W, so that might seem confusing, but wired LAN is typically just called LAN
- Ethernet and 802.11 serve similar functions: how to send message to another device over particular physical medium
- Layers 3 and above operate identically, regardless of which Layer 1/2 protocols are used

### Wi-Fi Alliance

- Most people know 802.11 wireless LANs by name Wi-Fi
- However, Wi-Fi is not official name used by IEEE; it is trademark of Wi-Fi Alliance
- Organization that tests and certifies equipment for 802.11 standards compliance
- Organization whose products pass testing and certification process can mark their equipment as "Wi-Fi Certified"
- Goal of this process is to ensure interoperability between different vendors' devices
- Although device's lack of Wi-Fi certification doesn't necessarily mean that it is incompatible with other devices
- For sake of accuracy, will avoid name Wi-Fi unless specifically referring to Wi-Fi Alliance's certifications

## Bounded vs Unbounded Media

### Bounded Media

- Copper and fiber-optic Ethernet cables are bounded media
- Signals are confined to cables, providing controlled pathway for data transmission
- This physical boundary offers some advantages in terms of security (only device at other end of cable receives signal) and signal consistency (signal is less susceptible to interference)

### Unbounded Media

- In contrast, air used to transmit wireless signals is unbounded medium
- Unlike wired connections, wireless signals propagate freely in open space
- Radiating in all directions from source
- Unbounded nature of wireless communication introduces both opportunities and challenges
- On one hand, it allows for greater mobility and flexibility, as devices don't need to be physically connected with network cable
- However, it also brings various challenges

## Wireless Communication Challenges

### Signal Reception

- All devices within range of wireless device receive that device's signals
- In fact, wireless communication is sometimes likened to wired communication via Ethernet hub
- All devices connected to hub receive all frames from other devices connected to hub
- This means that data privacy within wireless LAN is greater concern than it is in wired LAN
- For this reason, communications are usually encrypted, even within LAN
- We'll cover more about wireless LAN security in chapter on wireless LAN security

### Half-Duplex Operation

- Another consequence of using unbounded medium is that devices must operate in half-duplex mode
- Only one device can transmit at time, or their signals will collide
- Wireless devices must contend for airtime—they compete for chance to transmit data over shared medium
- This half-duplex nature is significant factor in why wireless networks often do not match speeds of wired networks using switches (which operate in full-duplex mode)
- While wired devices connected to hub use Carrier-Sense Multiple Access with Collision Detection (CSMA/CD) to detect and recover from collisions
- Wireless devices use similar protocol called Carrier-Sense Multiple Access with Collision Avoidance (CSMA/CA)
- CSMA/CA process: after preparing frame for transmission, device will listen to see if channel is free
- If channel is busy, device will wait random (short) period of time before checking again
- Device will transmit frame only when it senses channel is free
- Although CSMA/CA attempts to avoid collisions, if two devices happen to transmit simultaneously, frames can still collide, resulting in incoherent signal
- In such case, devices will have to retransmit their frames

### Signal Interference

- Third challenge of wireless communications is signal interference
- Which can significantly impact network performance
- Example: wireless LANs from neighboring offices, homes, or apartments operating on same or overlapping frequency ranges can cause interference
- Interference can disrupt clarity and integrity of signal, leading to data transmission errors and reduced network performance in LAN
- Managing interference is critical aspect of wireless network design, requiring careful channel selection
- It's not only other 802.11 networks that can cause interference
- Other devices like microwave ovens, cordless phones, and Bluetooth devices operating in same frequency range can disrupt wireless LAN communications

### Regulatory Compliance

- Another challenge stems from complex landscape of national and international regulations
- Each country has its own regulatory body, such as US Federal Communications Commission (FCC)
- That governs use of radio frequencies and sets standards for wireless communication
- These regulations are necessary to manage electromagnetic spectrum and prevent interference between different types of services
- Such as cellular signals, satellite communications, and wireless LANs
- Although international bodies like International Telecommunications Union (ITU) work to coordinate allocation of radio frequency spectrum across countries to ensure consistent use
- There are still differences between countries, and adhering to these regulations is legal necessity
- For this reason, wireless networking equipment used in one country might be legally prohibited in another

### Signal Coverage Area

- Final challenge we'll consider is signal coverage area of wireless LAN
- Similar to how cable length must be considered in wired LANs, coverage area is essential consideration in wireless LANs
- As wireless signals propagate through space, they lose strength; this is called free-space path loss (FSPL)
- In addition to FSPL, signals can be influenced by variety of factors
- These include reflection off surfaces, diffraction around obstacles, scattering due to irregularities in medium, and others
- Real question here is "How far can wireless signal travel and maintain enough strength for receiver to effectively distinguish signal from background noise and decode information?"
- Indoors, this is typically up to 150 feet (46 meters)
- Outdoors, it can extend beyond 300 feet (91 meters)
- But these distances vary greatly depending on factors like signal's frequency, transmitter power, antenna type, and environmental conditions such as physical obstructions

## Electromagnetic Wave Phenomena

### Five Phenomena

- Electromagnetic waves that are used to encode wireless signals are influenced by media they pass through and objects they encounter
- In this section, we'll examine five phenomena that must be considered in wireless LAN design
- Phenomena affecting behavior of electromagnetic waves include absorption by medium, reflection off surfaces, refraction (bending) as waves pass through medium, diffraction around obstacles, and scattering from irregularities

### Absorption

- Absorption occurs when wave passes through medium and is converted into heat, weakening signal
- Example: wireless signal passing through wall can cause significant attenuation
- Particularly if wall is made of dense material
- This can prevent devices on other side of wall from receiving coherent signal

### Reflection

- Reflection happens when wave bounces off surface rather than passing through it
- This is same phenomenon as light reflecting off mirror
- Metal surfaces are common culprits, as they are highly reflective of radio waves
- Reflection is reason wireless reception is usually poor in elevators
- Signal bounces off metal, and very little penetrates into elevator

### Refraction

- Refraction occurs when wave passes from one medium to another one with different density
- Altering wave's speed and causing it to bend
- Common everyday occurrence of refraction is apparent shift in position of object in water when viewed from above
- This is due to light waves bending as they move from water to air

### Diffraction

- Diffraction is bending and spreading of waves around edges of obstacle, such as wall
- This enables wireless communication even when there isn't clear line of sight between transmitter and receiver
- In urban environments, diffraction often allows signals to reach street level and indoor areas that are not in direct view of cell tower or wireless access point

### Scattering

- Final phenomenon is scattering
- Which occurs when wave encounters surface or medium with irregularities that cause wave to spread out erratically
- Common causes of scattering are dust, smog, water vapor, and textured surfaces
- Scattering can cause signal attenuation as it disperses signal's energy in various directions

### Design Considerations

- When designing wireless LAN, it's essential to account for various wave behaviors that affect wireless signals
- Absorption by walls, reflection from surfaces, refraction through different media, diffraction around obstacles, and scattering due to irregularities all play role in shaping coverage and reliability of wireless network
- For CCNA exam, you are not expected to be able to design wireless LAN that accounts for these various factors
- However, you should have basic understanding of each

## Electromagnetic Waves

### Wave Generation

- To send wireless signal, device applies alternating electric current to antenna
- Which in turn produces fluctuating electromagnetic fields that radiate out as waves
- These are called electromagnetic waves
- Two key measurements of electromagnetic wave are its amplitude and frequency

### Amplitude

- Amplitude and frequency are two fundamental characteristics of electromagnetic waves
- Amplitude measures maximum strength of electric and magnetic fields of wave
- And is associated with how much energy wave carries
- Basically, higher amplitude means stronger signal
- If amplitude of signal is too low, receiver won't be able to distinguish coherent message from signal
- Waves with higher amplitude carry stronger signals, indicated by greater electric and magnetic field strengths
- Figure only shows electric field of each wave, but each has equivalent magnetic field (hence name electromagnetic wave) that oscillates perpendicular to electric field

### Frequency

- Frequency measures how quickly strength of wave's electric and magnetic fields oscillates
- And is measured in hertz (Hz)—number of oscillations per second
- Like bits and bytes, hertz are typically measured in thousands, millions, billions, and trillions (or even greater):
  - kHz (kilohertz): 1000 cycles per second
  - MHz (megahertz): 1,000,000 cycles per second
  - GHz (gigahertz): 1,000,000,000 cycles per second
  - THz (terahertz): 1,000,000,000,000 cycles per second
- Waves with higher frequency oscillate at greater rate
- Frequency is measured in hertz (Hz), which is number of oscillations per second
- Related concept is period, which is amount of time it takes for one full oscillation
- Example: wave with frequency of 4 Hz and, therefore, period of 0.25 seconds—each oscillation takes 0.25 seconds

### Frequency Characteristics

- In context of radio waves, frequency determines wave's position within electromagnetic spectrum
- And has major effect on how signal behaves as it propagates through air and other media
- In wireless LANs, higher frequencies can typically support higher data transfer rates and are less crowded with other wireless devices
- However, they are also more susceptible to absorption by obstacles
- On other hand, lower frequencies penetrate better through obstacles and can, therefore, cover larger distances
- However, lower frequencies typically support lower transfer rates and are more crowded with other wireless devices
- In next section, we'll examine concepts of electromagnetic spectrum, radio frequency's position in spectrum, and different bands and channels used by 802.11 wireless LANs

## Electromagnetic Spectrum and Radio Frequency

### Electromagnetic Spectrum

- Electromagnetic spectrum is entire range of electromagnetic radiation
- Such as AM and FM radio, ultraviolet light, X-rays, and gamma rays
- Electromagnetic spectrum and radio frequency's position within it
- Figure is designed to show general progression from lower to higher frequencies across electromagnetic spectrum
- Placement of each example doesn't represent its precise frequency value

### Radio Frequency

- Radio frequency (RF) is segment of electromagnetic spectrum generally defined as ranging from around 20 kHz to around 300 GHz
- RF is used for variety of purposes, from AM and FM radio to microwaves and radar
- However, most relevant to this chapter are 802.11 wireless LANs
- Three bands within RF range are used for wireless LANs: 2.4 GHz band, 5 GHz band, and newer 6 GHz band, introduced to wireless LANs in 2020

## 2.4 GHz Band

### 2.4 GHz Band Characteristics

- 2.4 GHz band spans from 2.4 to 2.495 GHz and is widely used for wireless communications due to its lower frequency
- Which enables better penetration through obstacles compared to 5 GHz and 6 GHz bands
- However, this band is also used for other technologies, such as Bluetooth, microwave ovens, cordless telephones, and many others
- This means that it can sometimes be crowded, leading to congestion and interference

### 2.4 GHz Channels

- 2.4 GHz band is divided into 14 individual channels
- Like band, channel is specific range of frequencies—can think of channel as smaller division of band
- For wireless communication to occur, both transmitting and receiving devices must be tuned to same channel
- Enabling them to "speak" and "listen" on same frequency range
- Each channel has defined center frequency and standard width of 20 MHz
- Although older standards use 22 MHz
- Wireless devices communicate using these channels, so careful channel selection is critical to minimize interference
- Channels in 2.4 GHz band (don't have to memorize center frequency values)
- Not all channels in 2.4 GHz band can be used in all countries
- Example: only channels 1 to 11 are commonly allowed in United States/Canada
- While most countries allow 1 to 13
- Channel 14 is allowed in Japan, but only when using older 802.11 standard

### Channel Overlap

- There is significant overlap between 2.4 GHz channels
- In wireless LAN that needs multiple APs for full coverage, it's important to use non-overlapping channels to avoid interference
- If adjacent access points use same channel, devices not only have to contend for airtime with other devices using same access point
- But with devices using neighboring access points too
- Channels 1, 6, and 11 are recommended, as highlighted in figure
- However, in countries that allow up to channel 13, layout using channels 1, 5, 9, and 13 is also possible
- Non-overlapping channel layout options in 2.4 GHz band
- Each hexagon represents wireless access point's coverage area
- Key takeaways for CCNA exam are that 2.4 GHz band uses overlapping channels
- And that you should use 1–6–11 layout to avoid interference (1–5–9–13 is also possible in most countries outside of U.S./Canada)

## 5 GHz Band

### 5 GHz Band Characteristics

- 5 GHz band, ranging from approximately 5.150 to 5.895 GHz (depending on country), is second frequency band widely used for wireless LANs
- Compared to 2.4 GHz band, 5 GHz is generally less crowded and not as prone to interference from common household devices
- However, signals in 5 GHz band don't penetrate walls and other barriers as well as 2.4 GHz band
- This can be both benefit and drawback
- On upside, it means that 5 GHz signals from neighboring rooms and buildings are less likely to cause interference
- On downside, this can limit coverage area of 5 GHz signals

### 5 GHz Channels

- Unlike 2.4 GHz band, channels in 5 GHz band are non-overlapping when using standard 20 MHz width
- Which simplifies channel selection process when setting up multiple wireless access points
- These channels can be combined to form wider channels of 40, 80, or 160 MHz
- Supporting higher data transfer rates (although resulting in fewer available channels)
- Channels in 5 GHz band
- Twenty MHz channels can be combined into wider channels of 40, 80, or 160 MHz to support greater data transfer rates
- Number written in each channel is channel number that identifies it
- Include them only for reference; you don't have to memorize them

## 6 GHz Band

### 6 GHz Band Characteristics

- 6 GHz band is newest addition to 802.11 wireless LAN frequency bands
- Ranging from 5.925 GHz to 7.125 GHz (notably, its low and high ends are both beyond 6 GHz range)
- This band provides even more non-overlapping channels than 5 GHz band
- Standard channel width is 20 GHz, but channels can be combined to form wider channels of 40, 80, 160, or even 320 MHz
- Enhancing data transfer rates
- Channels in 6 GHz band
- 20 MHz channels can be combined into wider channels of 40, 80, 160, or 320 MHz to support greater data transfer rates
- Note that there is some overlap between 320 MHz channels

### Adoption

- 6 GHz band was adopted in 2020 in 802.11ax standard, better known as Wi-Fi 6E
- And also new 802.11be (Wi-Fi 7) standard
- Due to its relatively recent adoption, 6 GHz band isn't as widely used as 2.4 and 5 GHz bands
- However, it's expected to alleviate congestion found in other bands and provide even greater data transfer rates

## IEEE 802.11 Standards

### Standards Overview

- Just as there are various 802.3 Ethernet standards designed to accommodate different network environments and objectives
- With new ones continually in development to meet evolving demands (such as higher speeds)
- Same can be said of 802.11 family of standards
- Major generations of 802.11 wireless LAN standards, starting from original 802.11 standard, which was released in 1997

### Standards Table

- 802.11 standard: Wi-Fi generation: -, Maximum rate (Mbps): 1–2, RF band (GHz): 2.4
- 802.11b: Wi-Fi generation: -, Maximum rate (Mbps): 1–11, RF band (GHz): 2.4
- 802.11a: Wi-Fi generation: -, Maximum rate (Mbps): 6–54, RF band (GHz): 5
- 802.11g: Wi-Fi generation: -, Maximum rate (Mbps): 6–54, RF band (GHz): 2.4
- 802.11n: Wi-Fi generation: Wi-Fi 4, Maximum rate (Mbps): 72–600, RF band (GHz): 2.4/5
- 802.11ac: Wi-Fi generation: Wi-Fi 5, Maximum rate (Mbps): 433–6933, RF band (GHz): 5
- 802.11ax: Wi-Fi generation: Wi-Fi 6, Maximum rate (Mbps): 574–9608, RF band (GHz): 2.4/5
- 802.11ax: Wi-Fi generation: Wi-Fi 6E, Maximum rate (Mbps): 574–9608, RF band (GHz): 6
- 802.11be: Wi-Fi generation: Wi-Fi 7, Maximum rate (Mbps): 1376–46120, RF band (GHz): 2.4/5/6

### Wi-Fi Generations

- Starting from 802.11n standard, each new generation has been marketed as Wi-Fi X, with 802.11n as Wi-Fi 4
- Although not official names, 802.11, 802.11b, 802.11a, and 802.11g are sometimes retroactively called Wi-Fi 0, 1, 2, and 3, respectively
- Maximum transfer rates listed are theoretical maximums under ideal conditions
- And don't necessarily reflect performance that can actually be achieved
- Due to complexities of wireless communications and various external factors that can have effect
- In real-world applications, actual transfer rates will be lower

### Exam Focus

- For CCNA exam, particularly recommend memorizing which standards use which RF bands
- For most CCNA exam domains, you don't have to memorize IEEE standard names, but this is exception
- Example: CCNA exam questions that require you to select multiple answers will state so explicitly (select two, select three, etc.)
- To correctly answer question, need to know two things: which frequency band requires careful channel selection to avoid interference and which 802.11 standards use that band
- 2.4 GHz band consists of channels with significant overlap, so 1-6-11 or 1-5-9-13 channel patterns should be used to avoid interference among neighboring APs
- Of four options in question, two standards that use 2.4 GHz band are 802.11b and 802.11g

## Service Sets

### Service Set Overview

- Now that we've covered basics of electromagnetic waves, RF frequency bands, and 802.11 standards
- Let's consider how wireless devices can use these tools to communicate
- In 802.11 standards, service set is group of devices that operate on same wireless LAN
- Sharing same service set identifier (SSID)—human-readable label that identifies service set
- There are four main types of service sets:
  - Independent basic service set (IBSS)—peer-to-peer network where devices communicate directly (without access point)
  - Basic service set (BSS)—devices connect through single access point, forming basic building block of wireless LAN
  - Extended service set (ESS)—multiple linked BSSs, providing seamless connectivity across broader area
  - Mesh basic service set (MBSS)—network of interconnected APs providing flexible coverage

## Independent Basic Service Set (IBSS)

### IBSS Overview

- Independent basic service set (IBSS), also called ad hoc wireless network
- Consists of wireless devices (laptops, smartphones, etc.) communicating directly with each other
- Simple IBSS with SSID of "Jeremy's IBSS" that consists of smartphone and two laptops
- Devices can communicate directly with each other and share resources

### IBSS Use Cases

- IBSS is useful for quick, temporary communication setups
- Example: IBSS can be used for file sharing or gaming (although LAN parties are largely thing of past)
- However, IBSS doesn't scale beyond few devices
- In most wireless LANs, will want to employ some network infrastructure: wireless access points

## Basic Service Set (BSS)

### BSS Overview

- Basic service set (BSS) forms fundamental building block of 802.11 wireless LAN
- In BSS, wireless clients connect to wireless access point (abbreviated as WAP or AP)
- Which coordinates communication between devices and serves as gateway to other network resources
- Such as wired LAN or internet
- Client is any device that connects to wireless LAN via AP
- 802.11 standards use term station to refer to any wireless-capable device (including clients and APs)
- But it's more technical term that isn't common in everyday usage
- Cisco products call them clients, so that's term I'd expect on exam questions

### BSS Operation

- BSS consisting of AP and three clients, all communicating using channel 1 of 2.4 GHz band
- Clients connected to AP1 cannot send frames directly to each other (even if they are in range of each other's signals)
- They must send their frames to AP1, which will relay frames to their destination
- SSID of BSS, Jeremy's Wi-Fi, is human-readable name that serves as network's identifier for users
- SSIDs do not need to be unique
- Instead, basic service set identifier (BSSID) serves to uniquely identify BSS
- While multiple BSSs may use same SSID to create extended service set (ESS) for wider coverage
- Each BSS will have unique BSSID; we'll cover ESSs in next section
- BSSID is MAC address of AP's radio
- MAC addresses are uniquely assigned to device by manufacturer; no two devices will have same MAC

### Multiple BSSs on Single AP

- Single AP is capable of providing more than one BSS
- Example: enterprise may create BSS for staff and BSS for guests, applying different security policies to each
- However, all of AP's BSSs must use same channel—channel its radio is tuned to
- For this reason, creating multiple BSSs won't help to alleviate congested wireless LAN
- All of AP's clients, regardless of BSS, share same channel
- AP providing two BSSs for clients
- Both use same channel
- Each BSS requires unique BSSID
- Hosts can only communicate within their BSS
- Note that, despite both BSSs sharing same radio, each has unique BSSID
- This is usually accomplished by incrementing radio's MAC address by 1 for each new BSS

## Distribution System

### Distribution System Overview

- Most wireless LANs aren't standalone networks
- Rather, wireless LANs are way for wireless clients to connect to wired network infrastructure
- Enabling wireless clients to communicate with hosts in other BSSs, hosts in wired LAN, in remote sites via WAN, over internet, etc.
- 802.11 calls wired network infrastructure distribution system (DS)
- Although previous diagrams omitted DS, wireless LAN without DS is rare
- Without DS, AP's wireless clients can only communicate among themselves; they have no gateway to other networks

### AP as Bridge

- In addition to its wireless radio, each AP has Ethernet port through which it can connect to DS (usually via switch)
- AP serves as bridge connecting two mediums: it translates 802.11 frames from wireless clients to Ethernet frames to be sent over wired LAN, and vice versa
- DS connects each BSS to rest of network, enabling wireless clients to communicate with hosts outside of their BSSs
- AP maps each wireless SSID to VLAN on wired Ethernet network

## Extended Service Set (ESS)

### ESS Overview

- In SOHO network, single AP (typically component of wireless router) is usually sufficient
- However, in most enterprise sites (i.e., office), range of single AP isn't enough to provide signal coverage for entire site
- To expand wireless LAN beyond range of single AP, we use extended service set (ESS)
- ESS links multiple BSSs through DS
- Each BSS in ESS is identified by its own BSSID (MAC address of AP)
- But all operate using same SSID
- ESS consisting of three BSSs
- Each BSS shares same SSID, but has unique BSSID
- Client can roam seamlessly between BSSs

### Roaming

- To user, ESS appears as single wireless network
- Using figure's example, once user connects to Jeremy's Wi-Fi, they can move freely throughout office space without needing to manually reconnect to network
- As user moves away from current AP and its signal weakens, client device will automatically decide to switch to new AP with stronger signal
- Joining its BSS instead of previous one
- This process of passing between BSSs in ESS is called roaming

## Mesh Basic Service Set (MBSS)

### MBSS Overview

- In most cases, each AP has its own wired connection to DS
- But in environments where it is impractical or too costly to run Ethernet cable to each AP
- Mesh basic service set (MBSS) provides flexible solution
- MBSS connects multiple APs wirelessly, forming mesh of APs that can relay data between wireless clients and DS
- Without each AP requiring wired connection to DS
- MBSS is mesh of wireless connections between two types of APs, RAPs and MAPs
- That allows them to relay data to and from wireless clients

### Root and Mesh Access Points

- In MBSS, AP connected to DS is root access point (RAP)
- And AP not connected to DS is mesh access point (MAP)
- Ideally, each AP in MBSS should have two radios tuned to two different channels
- One dedicated to providing BSS to serve wireless clients
- And one dedicated to relaying frames between wireless clients and DS over mesh
- Single-radio AP can participate in MBSS but with greatly reduced performance
- Its single radio has to perform both jobs

## Specialized AP Operational Modes

### Repeater Mode

- APs can operate in various specialized roles outside of simply providing BSS for wireless clients
- AP participating in MBSS is example; in addition to providing BSS for wireless clients, AP forms mesh with other APs to relay frames between them
- In this section, we'll look at three more specialized AP operational modes: repeater, workgroup bridge, and outdoor bridge
- Repeater is AP used to extend range of wireless network
- AP configured as repeater takes signal from main AP and retransmits it to areas outside of main AP's cell range
- This mode is particularly useful in large homes or offices where coverage of single AP might not be sufficient
- AP2, in repeater mode, extends AP1's cell by repeating (retransmitting) wireless signals it receives
- Repeater APs might remind you of MBSS
- While both repeater APs and APs in MBSS extend wireless coverage, they serve different network topologies and function differently
- Repeater AP is typically standalone device that extends range of single AP without need for additional configuration or infrastructure
- In contrast, mesh AP is part of larger mesh network where each AP intelligently routes traffic through best path within web of interconnected APs
- Repeater AP can significantly reduce performance of wireless LAN
- By retransmitting main AP's signal, repeater occupies additional airtime for each packet
- Reducing network's overall data throughput—rate at which data can be transferred over network

### Workgroup Bridge Mode

- Not all devices have wireless capabilities
- If such device needs to connect to network, but running cable to nearest switch is not feasible
- AP operating as workgroup bridge (WGB) can be used to connect wired device to wireless LAN
- Wired device connects to WGB via Ethernet cable
- And WGB functions as client of main AP on behalf of wired device
- Effectively allowing it to participate in wireless LAN despite having no wireless capabilities
- AP2, in WGB mode, functions as client of AP1 to provide network access to PC1
- Which does not have wireless capabilities
- WGB can support multiple wired devices—not just one
- However, if main AP (AP1 in figure) is not Cisco AP, WGB will have to operate in Universal WGB (uWGB) mode
- Which only supports single wired device

### Outdoor Bridge Mode

- Laying cabling between buildings across campus or city can be quite expensive
- Alternative is to connect remote sites wirelessly with APs operating as outdoor bridges
- Outdoor bridges connect separate LANs over long distances
- And are ideal for campus or metropolitan settings, connecting buildings without need for physical cabling
- Point-to-point outdoor bridge setup connecting two sites
- However, point-to-multipoint setup, in which multiple sites connect to central site, is also possible
- APs functioning as outdoor bridges can connect LANs wirelessly over long distances
- Outdoor bridges can be established over many kilometers
- However, maximum distance varies greatly depending on hardware and various external conditions
- Example: clear line of sight between two APs is essential

## Real-World Applications

- **Enterprise wireless networks**: Providing wireless connectivity in office environments
- **SOHO networks**: Home and small office wireless networks
- **Public Wi-Fi**: Wireless access in cafes, airports, hotels
- **Mesh networks**: Extending coverage in challenging environments
- **Outdoor connectivity**: Connecting remote buildings wirelessly

## Troubleshooting

### Common Issues

- **Poor signal strength**: Check for obstacles, interference, and distance
- **Connection problems**: Verify SSID, security settings, and channel configuration
- **Interference**: Check for overlapping channels and competing devices
- **Coverage gaps**: Verify AP placement and signal strength

### Troubleshooting Steps

1. Verify AP configuration: Check SSID, channel, and security settings
2. Test signal strength: Use wireless analyzer tools
3. Check for interference: Identify competing devices and channels
4. Verify client configuration: Check SSID and security credentials
5. Test connectivity: Verify client can associate and communicate

## Best Practices

- Use non-overlapping channels (1-6-11 or 1-5-9-13 in 2.4 GHz band)
- Avoid interference from other devices
- Plan for coverage area and signal strength
- Consider environmental factors (walls, obstacles, etc.)
- Use appropriate frequency band for environment
- Implement proper security measures
- Monitor and manage RF environment
- Document wireless network design

## Summary

- Wireless LANs (sometimes abbreviated as WLANs) are defined by IEEE 802.11 family of standards
- It defines standards at Layers 1 and 2 of TCP/IP model
- Copper and fiber-optic cables are bounded media; signals are confined to cables, providing controlled pathway for data transmission
- Air used to transmit wireless signals is unbounded medium; signals propagate freely in open space, radiating in all directions from source
- All devices in range of wireless device can receive its signals, making security major concern
- Wireless devices must contend for airtime
- If two devices transmit at same time, collision occurs
- Wireless devices use Carrier-Sense Multiple Access with Collision Avoidance (CSMA/CA) to avoid collisions
- Wireless signals are vulnerable to interference, for example, from neighboring wireless LANs, microwave ovens, cordless phones, and Bluetooth devices
- Complexity of national and international regulations means that same devices can't always be used in different countries
- Coverage area is essential consideration in wireless LANs
- As wireless signals propagate through space, they lose strength; this is called free-space path loss (FSPL)
- Devices will be unable to receive signal if it is too weak
- Electromagnetic waves are influenced by media they pass through and objects they encounter
- Absorption occurs when wave passes through medium and is converted into heat, resulting in signal attenuation (weakening)
- Reflection happens when wave bounces off surface
- Refraction occurs when wave passes from one medium to another with different density, altering wave's speed and causing it to bend
- Diffraction is bending and spreading of waves around edges of obstacle
- Scattering occurs when wave encounters surface or medium with irregularities that causes wave to spread out erratically
- To send wireless signal, device applies alternating electric current to antenna, which in turn produces fluctuating electromagnetic fields that radiate out as waves; these are called electromagnetic waves
- Amplitude is maximum strength of electric and magnetic fields of wave and is associated with how much energy wave carries; higher amplitude means stronger signal
- Frequency measures how often strength of wave's electric and magnetic fields oscillates and is measured in hertz (Hz)—oscillations per second
- 1 kHz (kilohertz) = 1000 Hz, 1 MHz (megahertz) = 1,000,000 Hz, 1 GHz (gigahertz) = 1,000,000,000 Hz, 1 THz (terahertz) = 1,000,000,000,000 Hz
- Period is amount of time it takes for one full oscillation
- If frequency is 4 Hz (four oscillations per second), period is 0.25 seconds
- In wireless LANs, higher frequencies can typically support higher data transfer rates and are less crowded with other wireless devices, but are more susceptible to absorption by obstacles (i.e. walls)
- Lower frequencies typically support lower data transfer rates and are more crowded, but penetrate better through obstacles
- Electromagnetic spectrum is entire range of electromagnetic radiation
- Radio frequency (RF) is segment of electromagnetic spectrum defined as ranging from around 20 kHz to around 300 GHz
- Wireless LANs use three RF bands: 2.4 GHz band, 5 GHz band, and 6 GHz band
- 2.4 GHz band spans from 2.4 to 2.4835 GHz and is divided into 14 channels with standard width of 20 MHz
- Not all channels can be used in all countries
- There is significant overlap among 2.4 GHz channels, so adjacent APs should use non-overlapping channels (1–6–11 or 1–5–9–13) to avoid interference
- 5 GHz band ranges from approximately 5.150 to 5.895 GHz (depending on country)
- Channels in this band are non-overlapping when using standard 20 MHz width, simplifying channel selection process
- Channels can be combined to form wider channels of 40, 80, or 160 MHz, supporting higher data transfer rates (although resulting in fewer channels)
- 6 GHz band is newest addition to 802.11 frequency bands, ranging from 5.925 GHz to 7.125 GHz, providing even more non-overlapping channels
- Standard channel width is 20 MHz, but channels can be combined to form wider 40, 80, 160, or 320 MHz channels
- New 802.11 standards are constantly in development to meet evolving demands
- Major generations of 802.11 standards and RF bands they use are 802.11 (2.4 GHz), 802.11b (2.4 GHz), 802.11a (5 GHz), 802.11g (2.4 GHz), 802.11n (Wi-Fi 4, 2.4/5 GHz), 802.11ac (Wi-Fi 5, 5 GHz), 802.11ax (Wi-Fi 6, 2.4/5 GHz and Wi-Fi 6E, 6 GHz), and 802.11be (Wi-Fi 7, 2.4/5/6 GHz)
- Service set is group of devices that operate on same wireless LAN and share same service set identifier (SSID)—human-readable label for service set
- Independent basic service set (IBSS), also called ad hoc wireless network, consists of wireless clients communicating directly with each other
- IBSS is useful for quick, temporary setups, but doesn't scale beyond few clients
- Wireless client is any device that connects to wireless LAN
- In basic service set (BSS), clients connect to wireless access point (WAP or AP), which coordinates communication between wireless clients and serves as gateway to other network resources, such as wired LAN or internet
- Clients in BSS must communicate via AP, not directly with each other
- AP's coverage area is called basic service area (BSA) or cell
- BSS's SSID does not have to be unique
- Instead, basic service set identifier (BSSID) serves to uniquely identify BSS
- BSSID is usually MAC address of AP's radio
- Single AP can provide more than one BSS
- However, if AP only has single radio, all BSSs must share same channel
- Most wireless LANs serve as way for wireless clients to connect to wired network infrastructure (Ethernet LAN)
- 802.11 calls wired network infrastructure distribution system (DS)
- AP maps each wireless SSID to VLAN on wired Ethernet LAN, serving as bridge connecting two mediums
- Extended service set (ESS) links multiple BSSs through DS, expanding coverage area
- Each BSS shares SSID, but has unique BSSID
- In ESS, each AP's cell should overlap by about 10%–15% to allow clients to seamlessly roam among BSSs without losing connectivity
- Neighboring BSSs should use non-overlapping channels
- Mesh basic service set (MBSS) connects multiple APs wirelessly, forming mesh of APs that can relay data between wireless clients and DS without each AP requiring wired connection to DS
- In MBSS, AP connected to DS is root access point (RAP), and AP not connected to DS is mesh access point (MAP)
- Repeater is AP used to extend range of wireless network
- AP configured as repeater takes signal from main AP and retransmits it to areas outside of main AP's coverage area
- AP functioning as workgroup bridge (WGB) allows wired device without wireless capabilities to communicate over wireless LAN
- Wired device connects to WGB via Ethernet cable, and WGB functions as client of main AP on behalf of wired device
- APs operating as outdoor bridges can be used to connect geographically separated LANs wirelessly without need for physical cabling
- Outdoor bridges use directional antennas to focus wireless signal, allowing signal's strength to be maintained over longer distances than normally possible
