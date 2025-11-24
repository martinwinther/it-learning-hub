
# Wireless LAN Fundamentals

## Overview

Wireless LANs use the air as a medium instead of copper or fiber. IEEE 802.11 defines how to send frames over radio frequency (RF), while upper TCP/IP layers work the same as on Ethernet. Key ideas for CCNA are RF basics, frequency bands and channels, and how service sets (BSS, ESS, IBSS, MBSS) and AP roles fit together.

## Wireless LAN standards

### IEEE 802.11

- Ethernet (IEEE 802.3) defines wired LANs at Layers 1 and 2.
- Wireless LANs are defined by IEEE 802.11 at Layers 1 and 2.
- 802.11 specifies:
  - RF frequencies and channels
  - Modulation and encoding on the air
  - 802.11 frame formats and control mechanisms
- From Layer 3 and up, IP and higher protocols behave the same on wired and wireless links.

### Wi‑Fi Alliance

- Wi‑Fi Alliance is an industry group that certifies 802.11 products.
- Devices that pass interoperability tests can use the “Wi‑Fi Certified” mark.
- Wi‑Fi is a marketing term, not the IEEE standard name.
- Lack of certification does not always mean incompatibility, but certification targets multi vendor interoperability.

## Bounded vs unbounded media

### Bounded media

- Copper and fiber Ethernet links are bounded media.
- Signals stay inside the cable.
- Easier to control interference and to limit who can see the signal.

### Unbounded media

- Wireless LANs use unbounded media.
- RF signals radiate in all directions from the transmitter.
- Any device in range can receive frames on that channel.
- Brings mobility and flexibility but introduces security and reliability challenges.

## Wireless communication challenges

### Shared medium and privacy

- All clients in range hear all wireless frames on a channel.
- Privacy is a concern even inside a single WLAN.
- Encryption is normally used for traffic on the WLAN, not only across the internet.

### Half duplex and CSMA/CA

- Wireless is half duplex; only one device can send at a time on a channel.
- Devices contend for airtime using CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance):
  - Listen for a clear channel.
  - If busy, wait a random backoff period.
  - Transmit when the channel is idle.
- Collisions can still occur if two devices transmit at nearly the same time.
- Collisions and retransmissions reduce throughput and contribute to lower effective speed compared to switched full duplex Ethernet.

### Interference

- Interference sources:
  - Nearby WLANs on the same or overlapping channels.
  - Non‑802.11 devices in the same band (microwave ovens, cordless phones, Bluetooth devices).
- Interference causes:
  - More retransmissions.
  - Higher latency.
  - Lower throughput.
- Channel planning is critical in dense environments.

### Regulatory compliance

- RF use is controlled by national regulators (for example FCC in the United States).
- International bodies such as ITU coordinate spectrum use, but local rules still differ.
- Some channels and power levels may be legal in one country and prohibited in another.
- Wireless equipment is built for specific regulatory domains.

### Coverage and signal strength

- RF signals weaken with distance (free space path loss).
- Additional loss comes from walls, floors, and other obstacles.
- Rough coverage guidelines:
  - Indoors: around 30 to 45 meters.
  - Outdoors: often 90 meters or more.
- Actual range depends on:
  - Frequency band
  - Transmit power
  - Antenna design
  - Environment (walls, metal, glass, etc.)

## Electromagnetic wave behavior

### Key phenomena

Electromagnetic waves are affected by the media and objects they encounter:

- Absorption
- Reflection
- Refraction
- Diffraction
- Scattering

These effects shape WLAN coverage and performance.

### Absorption

- Wave energy converts to heat in the medium.
- Thick or dense walls cause strong attenuation.
- Water and concrete often absorb RF energy significantly.

### Reflection

- Wave bounces off surfaces instead of passing through.
- Metal surfaces reflect RF strongly.
- Causes multipath, where delayed reflections combine at the receiver.

### Refraction

- Wave bends when passing between media with different density.
- Changes speed and direction of propagation.
- Can slightly shift where strongest signals appear.

### Diffraction

- Wave bends around edges of obstacles.
- Enables communication without perfect line of sight.
- Common in urban and indoor environments.

### Scattering

- Wave hits irregular surfaces or particles and spreads in many directions.
- Caused by dust, moisture, foliage, or textured surfaces.
- Disperses energy and weakens the main signal path.

## Electromagnetic waves and RF basics

### Wave generation

- Wireless transmitter applies alternating current to an antenna.
- Antenna produces changing electric and magnetic fields.
- Fields radiate as electromagnetic waves.

### Amplitude

- Amplitude is the maximum field strength of the wave.
- Higher amplitude means stronger signal and more energy.
- If amplitude falls too low, the receiver cannot separate the signal from noise.

### Frequency and period

- Frequency is how many cycles occur per second, measured in hertz (Hz).
- Common prefixes:
  - kHz: 1,000 Hz
  - MHz: 1,000,000 Hz
  - GHz: 1,000,000,000 Hz
  - THz: 1,000,000,000,000 Hz
- Period is the time for one full cycle.
- Frequency and period are inverses:
  - Example: 4 Hz frequency equals a 0.25 second period.

### Frequency characteristics

- Frequency position in the spectrum affects signal behavior:
  - Higher frequency:
    - Shorter range.
    - More easily absorbed by obstacles.
    - Supports higher theoretical data rates.
    - Often less crowded at first, but may fill over time.
  - Lower frequency:
    - Better obstacle penetration.
    - Larger coverage area.
    - Lower maximum data rates.
    - Often more crowded.

## Electromagnetic spectrum and RF bands

### Electromagnetic spectrum

- Full range of electromagnetic radiation:
  - Radio, microwaves, infrared, visible light, ultraviolet, X‑rays, gamma rays.
- RF portion used for radio communications is a subset of this spectrum.

### Radio frequency range

- RF range is roughly 20 kHz to 300 GHz.
- Many systems use RF, including broadcast radio, cellular, radar, and WLANs.
- WLAN focus is on the 2.4 GHz, 5 GHz, and 6 GHz bands.

## 2.4 GHz band

### Band characteristics

- Frequency range approximately 2.4 to 2.4835 GHz.
- Good wall penetration and longer range than 5 GHz and 6 GHz.
- Heavily used by:
  - 802.11b/g/n/ax radios
  - Bluetooth
  - Microwave ovens
  - Some cordless phones and other devices
- Often congested and prone to interference.

### Channels and overlap

- Band is divided into channels with 20 MHz width in typical WLAN designs.
- Channels overlap heavily.
- Non‑overlapping channel plans:
  - 1, 6, 11 (common in many regions)
  - 1, 5, 9, 13 (possible where channel 13 is allowed)
- Key exam idea:
  - 2.4 GHz uses overlapping channels.
  - Neighboring APs should use non‑overlapping channel sets.

## 5 GHz band

### Band characteristics

- Frequency range approximately 5.150 to 5.895 GHz (varies by country).
- Shorter range and less wall penetration than 2.4 GHz.
- Less interference from consumer devices in many environments.
- Better suited for higher throughput in dense deployments.

### Channels and widths

- 20 MHz channels do not overlap in this band.
- Channels can be bonded for higher throughput:
  - 40 MHz
  - 80 MHz
  - 160 MHz
- Wider channels reduce the total number of distinct channels available, so design must balance channel reuse and throughput.

## 6 GHz band

### Band characteristics

- Frequency range roughly 5.925 to 7.125 GHz.
- Newest band for 802.11 WLANs.
- Used by Wi‑Fi 6E and Wi‑Fi 7 equipment.
- Provides many more non‑overlapping channels than 5 GHz.
- Higher frequencies mean shorter range and more sensitivity to obstacles.

### Channels and adoption

- Standard channel width is 20 MHz.
- Channels can be bonded to 40, 80, 160, and 320 MHz widths.
- 320 MHz support appears in Wi‑Fi 7.
- Adoption is still growing but expected to relieve congestion in 2.4 and 5 GHz bands.

## IEEE 802.11 standards and Wi‑Fi generations

### Standards summary

| Standard  | Wi‑Fi name | Max rate (approx Mbps) | Bands (GHz) |
|-----------|------------|------------------------|------------|
| 802.11    | -          | 1–2                    | 2.4        |
| 802.11b   | -          | 1–11                   | 2.4        |
| 802.11a   | -          | 6–54                   | 5          |
| 802.11g   | -          | 6–54                   | 2.4        |
| 802.11n   | Wi‑Fi 4    | 72–600                 | 2.4 / 5    |
| 802.11ac  | Wi‑Fi 5    | 433–6933               | 5          |
| 802.11ax  | Wi‑Fi 6    | 574–9608               | 2.4 / 5    |
| 802.11ax  | Wi‑Fi 6E   | 574–9608               | 6          |
| 802.11be  | Wi‑Fi 7    | 1376–46120             | 2.4 / 5 / 6 |

Notes:

- Data rates are theoretical maxima under ideal conditions.
- Actual throughput is much lower due to overhead and environmental factors.

### Exam focus

Important mappings to remember:

- 2.4 GHz capable standards:
  - 802.11
  - 802.11b
  - 802.11g
  - 802.11n
  - 802.11ax (Wi‑Fi 6)
- 5 GHz capable standards:
  - 802.11a
  - 802.11n
  - 802.11ac
  - 802.11ax (Wi‑Fi 6)
  - 802.11be (Wi‑Fi 7)
- 6 GHz capable standards:
  - 802.11ax (Wi‑Fi 6E)
  - 802.11be (Wi‑Fi 7)

Also important:

- 2.4 GHz channels overlap, so non‑overlapping patterns such as 1‑6‑11 or 1‑5‑9‑13 are used.
- 5 GHz and 6 GHz offer many non‑overlapping channels with 20 MHz widths.

## Service sets and SSIDs

### Service set concept

- 802.11 service set is a group of devices that share a common SSID.
- SSID is the human readable name of the WLAN.
- BSSID is the MAC address identifier for a specific BSS.

Main service set types:

- Independent Basic Service Set (IBSS)
- Basic Service Set (BSS)
- Extended Service Set (ESS)
- Mesh Basic Service Set (MBSS)

## Independent Basic Service Set (IBSS)

- Peer to peer ad hoc network.
- Wireless devices communicate directly, with no AP.
- Useful for temporary or small setups.
- Poor scalability and limited control.
- Rare in enterprise environments.

## Basic Service Set (BSS)

### BSS and AP role

- One AP plus its associated clients form a BSS.
- AP coordinates access to the RF medium.
- AP bridges traffic between wireless clients and the distribution system.
- AP coverage area is called a basic service area (BSA) or cell.

### SSID and BSSID

- SSID identifies the network name.
- SSIDs do not need to be globally unique.
- BSSID uniquely identifies the BSS and is usually the AP radio MAC address.
- A single AP can host multiple BSSs by broadcasting multiple SSIDs, each with its own BSSID.
- All BSSs on a single radio share the same channel, so additional SSIDs do not solve channel congestion.

## Distribution system (DS)

- Wired infrastructure that connects APs and other network devices.
- Usually an Ethernet LAN with switches and routers.
- AP uses the DS to reach:
  - Other BSSs
  - Wired hosts
  - Remote sites
  - Internet

AP behavior:

- Translates 802.11 frames to Ethernet frames and back.
- Maps each SSID to a VLAN on the wired LAN.

## Extended Service Set (ESS)

### ESS overview

- Multiple APs and BSSs share the same SSID.
- BSSs are linked through the distribution system.
- Provides larger coverage area than a single AP.

### Roaming

- Clients move between AP cells inside the ESS.
- Each AP has its own BSSID.
- Cells typically overlap by around 10 to 15 percent for reliable roaming.
- Neighboring BSSs use non‑overlapping channels to reduce co‑channel interference.

## Mesh Basic Service Set (MBSS)

### MBSS overview

- Mesh of APs that connect wirelessly to provide backhaul.
- Used where Ethernet cabling to every AP is not practical.
- Two main AP roles:
  - Root access point (RAP): has a wired connection to the DS.
  - Mesh access point (MAP): has no wired connection and uses wireless backhaul.

### Radios and performance

- Two‑radio design is preferred:
  - One radio for client access BSS.
  - One radio for mesh backhaul.
- Single‑radio mesh APs share airtime between backhaul and clients and have lower throughput.

## Specialized AP operational modes

### Repeater mode

- AP receives frames from a main AP and retransmits them.
- Extends coverage into dead spots without extra cabling.
- Reduces throughput because every frame is transmitted twice on the same channel.

### Workgroup bridge (WGB)

- AP acts as a wireless client to an AP.
- Bridges one or more wired devices into the WLAN.
- Useful for devices that lack native wireless capability.
- Some platforms support a universal WGB mode that connects to non‑Cisco APs but may limit the number of wired clients.

### Outdoor bridge

- APs configured to link separate LANs over long distances.
- Often use directional antennas for focused signal paths.
- Deployed in point to point or point to multipoint topologies.
- Useful for inter‑building links where fiber or copper is not practical.

## Quick review

- 802.11 defines wireless LANs at Layers 1 and 2, using RF as an unbounded medium where all devices in range share the channel.  
- Wireless networks run half duplex and rely on CSMA/CA, so collisions, interference, and retransmissions reduce effective throughput.  
- RF signals are affected by absorption, reflection, refraction, diffraction, and scattering, which together shape coverage and reliability.  
- WLANs use the 2.4 GHz, 5 GHz, and 6 GHz bands; 2.4 GHz channels overlap and require 1‑6‑11 or similar patterns, while 5 GHz and 6 GHz offer many non‑overlapping channels.  
- Newer 802.11 standards (n, ac, ax, be) increase data rates and add support for multiple bands, with Wi‑Fi 6E and Wi‑Fi 7 using 6 GHz.  
- IBSS is ad hoc, BSS is one AP plus its clients, ESS is multiple APs with the same SSID linked by a distribution system, and MBSS uses mesh AP backhaul.  
- APs can also operate as repeaters, workgroup bridges, and outdoor bridges to extend coverage and connect wired segments over wireless links.  
