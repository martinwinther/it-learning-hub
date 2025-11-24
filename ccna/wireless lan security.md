
# Wireless LAN Security

## Overview

Wireless LANs use an unbounded medium, so signals are visible to any receiver in range. Security focuses on applying the CIA triad to 802.11, and on how WEP, WPA, WPA2, and WPA3 handle authentication, encryption, and integrity.

## CIA triad and wireless LANs

### CIA triad

- Confidentiality  
  Data and systems are accessible only to authorized entities.

- Integrity  
  Data and systems remain accurate and unaltered except by authorized entities.

- Availability  
  Data and systems stay reachable and usable when needed.

These goals apply to wireless LANs just as they do to wired networks, but the open RF medium changes how they are enforced.

### Confidentiality in wireless LANs

- Wired LANs rely partly on the fact that signals stay inside cables.
- Wireless LANs broadcast signals into the surrounding area.
- Any receiver within range can capture unprotected frames.
- Unencrypted wireless traffic exposes application data and security credentials.
- Protecting confidentiality on a WLAN requires strong encryption on the wireless link, not just on the internet edge.

### Encryption terminology

- Cleartext  
  Unencrypted information that will not be encrypted.

- Plaintext  
  Unencrypted information that will be fed into an encryption algorithm.

- Ciphertext  
  Encrypted form of the plaintext.

### Integrity protection

- Encryption alone does not guarantee integrity.
- An attacker can flip bits in ciphertext to produce predictable changes in plaintext (bit flipping).
- Integrity protection uses a checksum or message authentication code:
  - Sender calculates a checksum over the plaintext.
  - Checksum is appended, then the combined data is encrypted.
  - Receiver decrypts, recalculates the checksum, and compares values.
  - Mismatch indicates tampering, so the frame is discarded.

### Availability attacks

- Denial of service (DoS) attacks against wireless LANs are easy to launch.
- RF jamming uses a signal source to flood 802.11 frequency bands.
- Jamming prevents legitimate devices from sending or receiving frames.
- Mitigation depends on finding and removing the jamming source.
- Physical security and monitoring help reduce the risk but cannot eliminate it.

In exam scope, most focus is on confidentiality and integrity mechanisms, not on detailed DoS countermeasures.

## Wired Equivalent Privacy (WEP)

### WEP overview

- Original 802.11 security protocol.
- Intended to provide privacy equivalent to wired LANs.
- Offers:
  - Authentication
  - Encryption
  - Integrity protection
- Now considered insecure and obsolete, but useful historically.

### WEP authentication

WEP defines two authentication methods:

- Open System Authentication
- Shared Key Authentication

#### Open System Authentication

- Client sends an authentication request.
- AP replies with an authentication response.
- No credentials are checked.
- Only verifies that both devices speak 802.11.
- Provides no real security.

#### Shared Key Authentication

- Static WEP key is configured on AP and clients.
- Acts as a simple Wi‑Fi password.
- Authentication procedure:
  1. Client sends authentication request.
  2. AP replies with an unencrypted challenge phrase.
  3. Client encrypts the challenge phrase with the WEP key.
  4. Client returns the ciphertext challenge.
  5. AP decrypts the ciphertext with the same WEP key.
  6. AP compares decrypted text to the original challenge.
  7. Match means success, mismatch means failure.

After authentication succeeds, the client associates with the AP and can start data transfer.

### WEP key configuration

- WEP key lengths:
  - 40 bit
  - 104 bit
- A 24 bit initialization vector (IV) is generated for each frame.
- IV is combined with the WEP key as part of RC4 keying.
- New IV per frame adds some variability and was intended to make key recovery harder.

### WEP encryption and integrity

- Encryption algorithm: RC4 stream cipher.
- Same key material is used for both authentication and data encryption.
- Integrity mechanism:
  - 32 bit integrity check value (ICV) appended to plaintext before encryption.
  - Receiver decrypts and checks ICV to detect changes.

### WEP vulnerabilities

- Static keys shared by all clients.
- Short IV and weak key mixing.
- Practical key recovery attacks have existed for many years.
- Open System and Shared Key authentication can both be exploited.
- WEP should not be used on modern WLANs.

## Wi‑Fi Protected Access (WPA)

### WPA overview

- Created by the Wi‑Fi Alliance as a replacement for WEP.
- WPA was an interim step, later followed by WPA2 and WPA3.
- Each WPA generation defines:
  - Personal mode (WPA‑Personal)
  - Enterprise mode (WPA‑Enterprise)
- WPA2 is still common, WPA3 is the current certification baseline.

### Personal vs Enterprise modes

- WPA‑Personal  
  - Uses a single pre‑shared key (PSK) for the entire WLAN.  
  - Typical choice in SOHO environments.

- WPA‑Enterprise  
  - Uses individual user or device credentials.  
  - Uses 802.1X and EAP with a RADIUS server.  
  - Typical choice in enterprise environments.

## WPA‑Personal (PSK)

### PSK and passphrase

- WPA‑Personal uses a 256 bit PSK as the base secret.
- Same PSK is configured on AP and all clients in the BSS.
- To simplify configuration:
  - Administrator enters an 8 to 63 character passphrase.
  - Device converts the passphrase into the 256 bit PSK.
- This is the familiar Wi‑Fi password in most home networks.

### Four way handshake

- Occurs after 802.11 Open System Authentication and association.
- Goals:
  - Prove that client and AP share the same PSK.
  - Derive unique encryption keys for that client.
- High level steps:
  - AP and client exchange nonces and derive a pairwise transient key (PTK).
  - Unique keys are derived per session and per client.
- Four way handshake is used in WPA and WPA2 and remains part of WPA3.

### PSK attack surface

- If an attacker captures a four way handshake, the captured data can be used in offline brute force attacks against the PSK.
- Strong, random passphrases reduce this risk but do not remove it completely.

## WPA3‑Personal (SAE)

### SAE overview

- WPA3‑Personal replaces legacy PSK exchange with Simultaneous Authentication of Equals (SAE).
- SAE runs before association and the four way handshake.
- Both sides prove knowledge of the password without exposing material that enables offline brute force attacks in a practical way.
- SAE still relies on a shared password but protects it more effectively on the air.

### SAE limitations and exam focus

- Password quality still matters. Social engineering or poor passphrase choices can still expose the WLAN.
- For CCNA:
  - WPA‑Personal uses a shared passphrase that produces a PSK.
  - WPA3‑Personal adds SAE to protect that PSK from offline brute force attacks.

## WPA‑Enterprise (802.1X and EAP)

### WPA‑Enterprise overview

- Replaces a shared PSK with per user or per device authentication.
- Uses 802.1X for port based access control and EAP for the authentication framework.
- Common in enterprise WLANs, often combined with directory services.

### 802.1X roles and protocol flow

Roles:

- Supplicant  
  Client device that requests access.

- Authenticator  
  Network device that controls access (AP or WLC).

- Authentication server (AS)  
  Verifies credentials, typically a RADIUS server.

Protocol flow:

- Supplicant and authenticator exchange EAP messages using EAP over LAN (EAPoL) on the WLAN.
- Authenticator forwards EAP payloads to the AS using RADIUS.
- AS validates credentials and returns an accept or reject.
- On success, the same four way handshake mechanism is used to derive encryption keys between client and AP.

### EAP methods

EAP defines a framework and supports multiple authentication methods:

- LEAP  
  Cisco proprietary method that uses username and password but relies on WEP. Considered insecure.

- EAP‑FAST  
  Uses a Protected Access Credential (PAC) to build a TLS tunnel, then exchanges user credentials inside that tunnel.

- PEAP  
  AS presents a certificate. A TLS tunnel is built, then user credentials are sent inside the tunnel.

- EAP‑TLS  
  Both client and AS use certificates for mutual authentication. Considered very secure but requires certificate deployment to all clients.

CCNA requires familiarity with the concepts and roles, not deep detail on each method.

### WPA‑Enterprise exam focus

- 802.1X controls access to the wireless LAN.
- EAPoL carries EAP between supplicant and authenticator.
- RADIUS carries EAP between authenticator and authentication server.
- Four way handshake still generates data encryption keys after successful authentication.

## Encryption and integrity protocols

### TKIP (WPA)

- Temporal Key Integrity Protocol (TKIP) was introduced as a WEP enhancement.
- Goal was to improve security without replacing existing WEP hardware.
- Included in the original WPA certification.
- Improvements over WEP:
  - Per packet key mixing creates a unique key for each frame.
  - Stronger integrity checksum called message integrity check (MIC).
  - Sequence numbers reduce replay attacks.
- Uses RC4 for encryption, so it is now considered legacy.

### CCMP (WPA2)

- Counter Mode with Cipher Block Chaining Message Authentication Code Protocol (CCMP).
- Introduced in 802.11i and used in WPA2.
- Uses AES instead of RC4.
- Encryption:
  - AES in counter mode for confidentiality.
- Integrity:
  - Cipher Block Chaining Message Authentication Code (CBC‑MAC).
- Much stronger than TKIP and still widely used.

### GCMP (WPA3)

- Galois/Counter Mode Protocol (GCMP) is used by WPA3.
- Designed to provide strong security with better performance for high data rates.
- Encryption:
  - AES in counter mode, with 128 or 256 bit keys.
- Integrity:
  - Galois Message Authentication Code (GMAC).
- Considered stronger and more efficient than CCMP.

## WPA security protocols summary

### Generations and protocols

| Protocol | Release year | Personal authentication      | Enterprise authentication | Encryption          | Integrity  |
|----------|--------------|-----------------------------|---------------------------|---------------------|------------|
| WEP      | 1997         | Open System, Shared Key     | N/A                       | RC4                 | ICV        |
| WPA      | 2003         | PSK                         | 802.1X / EAP              | RC4 (TKIP)          | MIC (TKIP) |
| WPA2     | 2004         | PSK                         | 802.1X / EAP              | AES (CCMP)          | CBC‑MAC    |
| WPA3     | 2018         | SAE                         | 802.1X / EAP              | AES (GCMP)          | GMAC       |

Notes for exam prep:

- WPA2 can optionally support TKIP for backward compatibility, but CCMP is the primary method.
- WPA3 supports CCMP as well, but GCMP is the flagship protocol for new deployments.

## WPA3 additional security benefits

### Protected Management Frames (PMF)

- PMF protects 802.11 management frames.
- Ensures authenticity and integrity for frames such as authentication and association messages.
- Reduces the impact of spoofing and some disconnection attacks.
- PMF was optional in WPA2 and is mandatory in WPA3.

### Forward secrecy

- Forward secrecy (or perfect forward secrecy) ensures that compromise of a long term key does not expose past encrypted sessions.
- Each session uses unique ephemeral keys.
- Even if an attacker obtains the PSK later, captured historical traffic remains protected.

## Quick review

- Wireless LANs share a broadcast RF medium, so confidentiality and integrity require strong link layer protection.  
- WEP provides basic authentication, encryption, and integrity but is broken and should not be used.  
- WPA‑Personal uses a shared passphrase that produces a PSK, combined with a four way handshake to confirm the PSK and derive per client keys.  
- WPA3‑Personal adds SAE to protect against practical offline brute force attacks on the PSK.  
- WPA‑Enterprise uses 802.1X with EAP and RADIUS to authenticate individual users or devices, followed by the same four way handshake.  
- TKIP was an interim improvement that still uses RC4. CCMP (AES) in WPA2 and GCMP (AES) in WPA3 provide modern encryption and integrity.  
- WPA3 also introduces mandatory PMF and stronger forward secrecy, improving protection for management frames and past encrypted traffic.  
