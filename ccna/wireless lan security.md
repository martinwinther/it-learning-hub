# Wireless LAN Security

## Overview

Imagine that you are in a room full of people. You have to communicate a private message to your friend on the other side of the room, but all you can do is shout at the top of your lungs. Basically, that's how communication in a wireless LAN works. Security is a major concern in all networks, but the unbounded nature of the medium means that securing communications in wireless LANs is even more critical. In this chapter, we will take a high-level overview of wireless LAN security concerns and solutions, covering CCNA exam topic 5.9: Describe wireless security protocols (WPA, WPA2, and WPA3). WPA stands for Wi-Fi Protected Access—a set of security certification programs developed by the Wi-Fi Alliance. To earn "Wi-Fi Certified" status, devices must comply with WPA's standards. We will first examine the various elements of wireless LAN security and then see how they all fit together in WPA, WPA2, and WPA3.

## CIA Triad and Wireless LANs

### CIA Triad Application

- Although wireless LANs introduce unique challenges, fundamental security concepts we covered in chapter on security concepts still apply
- In this section, we'll consider how CIA triad applies to wireless LANs
- And examine security measures implemented in original 802.11 standard (before creation of WPA)
- Confidentiality: Data and systems should only be accessible by authorized entities
- Integrity: Data and systems should be trustworthy. For example, data should not be altered during storage or transmission except by authorized entities
- Availability: Data and systems should be accessible and usable by authorized entities when required

### Confidentiality in Wireless LANs

- Confidentiality in wired LAN is largely ensured by physical characteristics of medium: signals are contained within cables
- Reducing (although not eliminating) risk of unauthorized access to communications
- Confidentiality is primarily concern when communicating over public networks like internet
- However, wireless signals can be picked up by any receiver within range of transmitter
- Making it essential to protect information as it travels through air, even within private LAN
- Unencrypted communications in wireless LAN are not secure, as wireless signals can be picked up by nearby devices
- Allowing malicious users to gain access to confidential information
- To maintain confidentiality of communications in wireless LAN, encryption of wireless signals is essential
- Encrypting message converts it into unintelligible string of text that can only be restored by intended recipient
- Later in this chapter, we will take look at some encryption methods used in wireless LANs

### Encryption Terminology

- Unencrypted information (that will not be encrypted) is called cleartext
- Unencrypted information that will be encrypted (but has not yet been fed into encryption algorithm) is plaintext
- And encrypted information is called ciphertext

### Integrity Protection

- Even if message is encrypted, preventing attacker from reading its contents, that is no guarantee that data will not be altered by malicious user
- Bit-flipping attack is attack in which attacker flips bits (between 0 and 1) in ciphertext to create predictable changes in plaintext
- Even without decrypting ciphertext
- To protect integrity of message before sending it over air, sender uses mathematical function to generate checksum
- Small block of data derived from original message
- This checksum is appended to end of plaintext message before encrypting and sending it
- Appending checksum to end of message before encrypting and sending it helps to protect integrity of wireless communications
- Upon receiving encrypted message, receiver decrypts it and then calculates its own checksum from decrypted message
- If newly calculated checksum matches one sent with message, receiver can conclude that message hasn't been altered
- If they don't match, receiver discards message

### Availability Attacks

- Attacks against availability of wireless LAN—denial of service (DoS) attacks—are quite simple to carry out by any malicious user with proper tools
- Example: in RF jamming attack, attacker uses signal generator to flood 802.11 frequency bands
- Preventing legitimate devices from communicating
- RF jamming attack doesn't require sophisticated hacking skills or deep knowledge of network
- Making it easy choice for malicious user looking to disrupt network
- Furthermore, preventing such attacks can be challenging
- Only solution to RF jamming attack is to locate and disable/remove device that is performing attack
- And only preventative measure is physical security—ensuring that only authorized users have access to physical premises
- Due to simplicity of wireless DoS attacks, we won't address them any further in this chapter
- Instead, we'll focus on protecting confidentiality and integrity of wireless communications

## Wired Equivalent Privacy (WEP)

### WEP Overview

- Original 802.11 standard defined security protocol called Wired Equivalent Privacy (WEP)
- As name suggests, WEP promised to provide privacy to wireless communications equivalent to that of wired communications
- Unfortunately, it failed to live up to that promise; various vulnerabilities were soon identified
- And WEP is now obsolete—it is legacy protocol
- However, studying basics of WEP is crucial for understanding evolution of wireless security protocols

### WEP Authentication

- Definitions given for confidentiality, integrity, and availability all mention "authorized entities"
- Data should only be accessible to and modified by authorized entities and should remain available to those entities
- To authorize entity (user or device), must verify that entity's identity
- As we covered in chapter on security concepts, verification process is called authentication
- WEP defined two methods of authentication: Open System Authentication and Shared Key Authentication

### Open System Authentication

- We already saw example of Open System Authentication in chapter on wireless LAN architectures when covering association process
- Client device sends authentication request, and AP sends authentication response
- No credentials are exchanged; AP simply approves all authentication requests unless there's problem with request itself (i.e., invalid formatting)
- No questions asked!
- This verifies that client and AP are both valid 802.11 devices
- But I think it goes without saying that this is not secure authentication method

### Shared Key Authentication

- Shared Key Authentication involves configuration of static WEP key on AP and each client
- Basically, this is Wi-Fi password
- To verify that client has correct WEP key, following process is used:
  1. Client sends authentication request
  2. AP sends authentication response with unencrypted challenge phrase
  3. Client uses WEP key to encrypt challenge phrase
  4. Client sends ciphertext challenge phrase back to AP
  5. AP uses WEP key to decrypt challenge phrase
  6. AP compares original challenge phrase to one it just decrypted
  7. If decrypted text matches original phrase, AP sends back response indicating successful authentication (or unsuccessful, if text doesn't match)
- WEP Shared Key Authentication involves exchanging challenge phrase and encrypting/decrypting it with shared WEP key
- Diagrams in this chapter omit probe request/probe response exchange (or beacon messages when using passive discovery) that we covered in previous chapter
- But keep in mind that this exchange occurs before any authentication/association processes
- Client must discover AP before it can authenticate

### WEP Key Configuration

- Static WEP key can be either 40 bits or 104 bits in length
- Furthermore, device generates random 24-bit number called initialization vector (IV) that is combined with WEP key
- New IV is generated for each packet; this adds some randomness to encryption process
- Making it harder for attacker to figure out encryption key
- As we covered in previous chapter, after client successfully authenticates (via Open System or Shared Key Authentication)
- It can send association request to associate with AP and start communicating

### WEP Encryption

- In addition to authentication, WEP provides confidentiality via encryption
- Same WEP key used in Shared Key Authentication can be used to encrypt data messages to and from wireless clients
- Encryption algorithm used by WEP is Rivest Cipher 4 (RC4)
- RC4 is no longer considered secure, so newer security standards use different algorithms

### WEP Integrity

- WEP also ensures integrity of communications as described previously
- Appending 32-bit checksum called integrity check value (ICV)
- This is appended to each plaintext message before it is encrypted
- Allowing receiver to verify that message was not tampered with

### WEP Vulnerabilities

- Although WEP seems to have all bases covered when it comes to wireless security—authentication, confidentiality (encryption), and integrity
- It is no longer considered secure
- Cryptography, and security in general, is never-ending arms race
- And attackers have known how to exploit WEP for over two decades
- As threats evolve and become more sophisticated, so must security protocols

## Wi-Fi Protected Access (WPA)

### WPA Overview

- After WEP's vulnerabilities were discovered, Wi-Fi Alliance developed Wi-Fi Protected Access (WPA) certification as interim enhancement
- Until IEEE could develop more permanent solution (802.11i standard, which was adopted by WPA2)
- WPA (and its more recent versions WPA2 and WPA3) defines two main authentication methods:
  - WPA-Personal: Pre-shared key (PSK) is used for authentication. This is similar to WEP Shared Key Authentication but more secure. Most recent WPA3 certification enhances this with Simultaneous Authentication of Equals (SAE)
  - WPA-Enterprise: Designed to provide more robust authentication in enterprise LANs, WPA-Enterprise uses 802.1X and EAP, replacing PSK with individual user or device credentials

## WPA-Personal Authentication

### PSK Overview

- WPA-Personal authentication, typically used in SOHO networks, involves configuring pre-shared key (PSK)
- Static 256-bit string used to generate secure encryption keys
- Same PSK must be configured on all members of BSS—AP and its clients
- And is used similarly to key in WEP Shared Key Authentication

### Passphrase Configuration

- 256-bit PSK, which is 64 hexadecimal characters, would be difficult for most users to remember (or enter without typos)
- To simplify things, can configure 8- to 63-character passphrase
- What most people call "Wi-Fi password," which is then automatically converted into 256-bit PSK

### Four-Way Handshake

- WPA-Personal authentication with PSK
- After client associates with AP, four-way handshake is used to confirm that both have same PSK and to generate unique encryption keys
- Interestingly, this authentication occurs after client has already associated with AP
- Beginning with Open System Authentication as we covered earlier; true authentication occurs after association
- After 802.11 Open System Authentication and association, four-way handshake is used for two main purposes
- To confirm that both client and AP have same PSK
- And to generate unique encryption keys that will be used to encrypt and decrypt data sent to and from client
- This method of authentication is used in WPA and WPA2 and provides much greater security than WEP Shared Key authentication
- However, there are still vulnerabilities
- Example: if attacker manages to capture four-way handshake, those messages contain enough information for attacker to attempt brute-force attack to learn PSK

## WPA3-Personal Authentication

### SAE Overview

- To protect against vulnerabilities of WPA/WPA2's PSK authentication, WPA3 adopts new authentication method called simultaneous authentication of equals (SAE)
- Which is carried out before 802.11 association (which is then followed by four-way handshake)
- Note that SAE still uses PSK, but SAE authentication process allows client and AP to verify that they have matching PSKs without rendering PSK vulnerable to brute-force attacks
- While any password-based system can theoretically be brute-forced with enough time and computational power
- Design and implementation of SAE in WPA3 make it practically infeasible
- WPA3-Personal authentication using SAE
- SAE authentication allows client and AP to confirm they have same PSK and derive key used in four-way handshake
- In four-way handshake, they generate encryption keys used to encrypt/decrypt data messages

### SAE Limitations

- Although SAE makes WPA3-Personal more secure than WPA/WPA2 by protecting against brute-force attacks
- It still relies on PSK
- PSK, or passphrase from which it is derived, could be compromised through social engineering attack
- Granting attacker access to LAN
- Outside of SOHO networks, it's best to opt for more secure option: WPA-Enterprise

### Exam Focus

- For CCNA exam, know that WPA-Personal authentication involves configuring shared passphrase (which generates PSK)
- And that WPA3 uses SAE to protect PSK against brute-force attacks

## WPA-Enterprise Authentication

### WPA-Enterprise Overview

- Instead of using PSK that is shared among all devices in LAN
- WPA-Enterprise authentication mode verifies each individual user's or device's credentials through IEEE 802.1X standard
- Which uses Extensible Authentication Protocol (EAP) framework
- We briefly covered 802.1X and EAP in chapter on security concepts in context of port-based network access control (PNAC) for wired hosts connected to switch ports
- WPA-Enterprise uses same concept, but instead of controlling access to individual switch ports
- It controls access to wireless LAN

### 802.1X Process

- To authenticate with WPA-Enterprise, client first uses Open System Authentication and then associates with AP
- At this point, even though client is associated with AP, it cannot communicate over network
- It must authenticate with 802.1X/EAP
- EAP defines various authentication methods and message formats
- However, EAP itself doesn't define how those messages should be transported over network; that's 802.1X's role
- 802.1X defines how to encapsulate EAP messages over Ethernet or 802.11 LANs, called EAP over LANs (EAPoL)
- 802.1X/EAP protocol stack—set of protocols it uses to enable authentication via EAP
- 802.1X defines EAPoL, which allows EAP messages to be transported over Ethernet or 802.11 LANs

### EAPoL Operation

- EAPoL is designed to transport EAP messages within LAN between 802.1X supplicant (client device) and authenticator (AP)
- For review, here are three devices' roles in 802.1X:
  - Supplicant: Client device that wants to connect to network
  - Authenticator: Network device that client connects to (AP)
  - Authentication server (AS): Server that verifies supplicant's credentials (usually RADIUS server)
- To relay supplicant's EAP messages to AS, authenticator uses RADIUS
- EAPoL is used to transport EAP messages between supplicant and authenticator, and RADIUS between authenticator and AS
- EAPoL carries EAP messages between supplicant and authenticator
- And RADIUS carries EAP messages between authenticator and AS

### EAP Methods

- EAP isn't single authentication method
- As name suggests, EAP is extensible, acting as framework that defines various authentication methods called EAP methods
- CCNA exam doesn't expect you to know these EAP methods in detail, but here are few examples:
  - LEAP (Lightweight EAP): Developed by Cisco to address WEP's vulnerabilities. Client authenticates with username/password combination, and then supplicant and AS exchange challenge phrases, providing mutual authentication. LEAP uses WEP encryption and is no longer considered secure
  - EAP-FAST (EAP-Flexible Authentication via Secure Tunneling): Developed by Cisco to replace LEAP. It establishes Transport Layer Security (TLS) tunnel using Protected Access Credential (PAC)—shared secret—to authenticate supplicant and AS. Within this tunnel, user credentials are exchanged for authentication
  - PEAP (Protected EAP): AS has digital certificate that supplicant uses to authenticate AS and establish TLS tunnel. In tunnel, user credentials are provided for authentication
  - EAP-TLS (EAP-Transport Layer Security): AS and supplicant each have digital certificate that they use to authenticate each other. EAP-TLS is considered most secure, but managing certificates on all client devices can be burdensome

### Four-Way Handshake in WPA-Enterprise

- Regardless of which EAP method is used, same four-way handshake that we outlined in WPA-Personal section is always used after authentication to generate encryption keys used to encrypt/decrypt data messages
- This handshake is done between supplicant and authenticator (client and AP/WLC)

### Exam Focus

- For CCNA exam, should understand basics of 802.1X (supplicant, authenticator, AS), EAP, and RADIUS
- EAPoL carries EAP messages between supplicant and authenticator
- And RADIUS carries EAP messages between authenticator and AS

## Encryption and Integrity Protocols

### Protocol Evolution

- WEP defined confidentiality (encryption) and integrity measures that promised to offer privacy equivalent to that of wired LANs
- As we already covered, that turned out not to be case; WEP has various vulnerabilities and should not be used anymore
- In this section, we'll examine encryption and integrity protocols that replaced WEP and were adopted by Wi-Fi Alliance's WPA, WPA2, and WPA3 certifications

## Temporal Key Integrity Protocol (TKIP)

### TKIP Overview

- After WEP's vulnerabilities were discovered, more secure solution was urgently needed
- However, there was major problem: existing hardware was built to use WEP
- To address this issue before new protocols and hardware were developed
- Temporal Key Integrity Protocol (TKIP) was created as enhancement to WEP
- TKIP was included in Wi-Fi Alliance's first WPA certification

### TKIP Improvements

- WEP's fundamental flaw was fact that it used static encryption keys
- All clients used same encryption key, and it remained unchanged unless admin manually configured new passphrase
- TKIP solved this by using process called per-packet key mixing
- Generating unique encryption key for each packet
- This makes it much more difficult for attacker to decipher PSK through brute-force attack
- TKIP also added few more security improvements, such as following:
  - TKIP's data integrity checksum, called message integrity check (MIC), is stronger than WEP's ICV
  - TKIP adds sequence number to each frame to mitigate against replay attacks

### Replay Attacks

- Replay attack is when attacker captures valid messages and retransmits them later
- Example: attacker can gain unauthorized access to system by replaying user's valid authentication messages

## Counter Mode with Cipher Block Chaining Message Authentication Code Protocol (CCMP)

### CCMP Overview

- Although TKIP served as stopgap to protect against WEP's vulnerabilities
- IEEE 802.11i standard, which formed basis of WPA2, brought in more advanced security protocols that are still in use in many wireless LANs today
- 802.11i/WPA2 uses Counter Mode with Cipher Block Chaining Message Authentication Code Protocol (CCMP) to provide message encryption and integrity
- That's quite long name—let's examine it

### CCMP Encryption

- Whereas WEP and TKIP use RC4 encryption algorithm, CCMP uses Advanced Encryption Standard (AES)
- More robust algorithm that provides much more secure encryption
- Specifically, CCMP uses AES counter mode encryption, hence "Counter Mode" in CCMP's name
- Details of counter mode aren't necessary for CCNA exam
- But in essence, it involves encrypting counter value that increments for each block of encrypted data
- Ensuring that each block of data is encrypted with unique key

## Galois/Counter Mode Protocol (GCMP)

### GCMP Overview

- Latest security certification from Wi-Fi Alliance is WPA3
- And it uses Galois/Counter Mode Protocol (GCMP) for data encryption and integrity
- GCMP can be considered improved version of CCMP
- Offering improved security as well as greater efficiency
- This efficiency is necessary for encryption to keep up with faster data rates of latest 802.11 standards

### GCMP Characteristics

- Like CCMP, GCMP uses AES counter mode encryption
- However, it supports greater AES key lengths (128 or 256 bits) than CCMP (128 bits)
- Providing stronger encryption
- For its data integrity checksum, GCMP uses Galois Message Authentication Code (GMAC)
- Once again, this provides more secure data integrity than protocols used in earlier standards

## WPA Security Protocols Summary

### Protocol Comparison

- We've covered lot of different protocols for providing authentication, encryption, and integrity to wireless LANs
- Referencing WPA generation that supports each
- WPA security protocols summary, including WEP for reference as well
- CCNA exam topic 5.9 states that you must be able to "describe wireless security protocols (WPA, WPA2, and WPA3)"
- In this section, we'll summarize which standards are supported by which WPA certifications; make sure you know them!

### WPA Protocols Table

- WEP: Release Year: 1997, Authentication (WPA-Personal): Open System, Shared key, Authentication (WPA-Enterprise): N/A, Encryption: RC4, Integrity: ICV
- WPA: Release Year: 2003, Authentication (WPA-Personal): PSK, Authentication (WPA-Enterprise): 802.1X/EAP, Encryption: RC4 (TKIP), Integrity: MIC (TKIP)
- WPA2: Release Year: 2004, Authentication (WPA-Personal): PSK, Authentication (WPA-Enterprise): 802.1X/EAP, Encryption: AES (CCMP), Integrity: CBC-MAC (CCMP)
- WPA3: Release Year: 2018, Authentication (WPA-Personal): SAE, Authentication (WPA-Enterprise): 802.1X/EAP, Encryption: AES (GCMP), Integrity: GMAC (GCMP)

### Protocol Details

- It's worth noting that table isn't complete; it only lists strongest encryption protocol supported by each WPA certification
- Example: WPA2 includes optional support for TKIP to accommodate older client devices that don't support CCMP
- Similarly, WPA3 doesn't just support GCMP; it supports CCMP as well
- However, for CCNA exam, recommend learning protocols as listed in table
- Further details can be left for future studies

## WPA3 Additional Security Benefits

### Protected Management Frames (PMF)

- As of 2020, device must support WPA3 to earn "Wi-Fi Certified" status
- WPA2 is still commonly used in enterprise and SOHO wireless LANs
- But move to WPA3 is underway, and WPA3 support is now commonplace for new hardware
- In addition to superior protocols we already covered, WPA3 has some other security benefits:
  - Protected Management Frames (PMF): PMF ensures authenticity and integrity of 802.11 management frames (i.e., authentication and association messages), preventing certain types of spoofing attacks. PMF was supported in WPA2 but is mandatory in WPA3

### Forward Secrecy (FS)

- Forward Secrecy (FS), also known as Perfect Forward Secrecy (PFS)
- Ensures that security of encrypted data remains intact even if PSK is compromised in future
- Compromised PSK cannot be used to decrypt past communications
- This is because encryption keys used for each session are unique and not solely derived from PSK

## Real-World Applications

- **Enterprise security**: WPA-Enterprise with 802.1X/EAP for robust authentication
- **SOHO networks**: WPA-Personal with PSK for simple password-based authentication
- **High-security environments**: WPA3 with SAE and GCMP for enhanced security
- **Legacy device support**: WPA2 with optional TKIP for older devices
- **Network access control**: 802.1X for per-user authentication

## Troubleshooting

### Common Issues

- **Authentication failures**: Verify PSK/passphrase or 802.1X credentials
- **Encryption mismatches**: Check WPA version and encryption settings
- **Client connectivity**: Verify security settings match between AP and client
- **RADIUS issues**: Check RADIUS server connectivity and configuration

### Troubleshooting Steps

1. Verify security settings: Check WPA version, authentication method, and encryption
2. Test authentication: Verify PSK or 802.1X credentials
3. Check encryption: Verify encryption algorithm matches between AP and client
4. Review RADIUS configuration: Check server connectivity and EAP method
5. Test client connectivity: Verify client can authenticate and communicate

## Best Practices

- Use WPA3 when possible for enhanced security
- Use WPA-Enterprise for enterprise networks
- Use strong passphrases for WPA-Personal
- Enable PMF when supported
- Keep firmware updated for latest security features
- Monitor for rogue devices
- Implement proper access control
- Document security policies

## Summary

- Although wireless LANs introduce unique challenges, fundamental security concepts like CIA triad still apply
- Confidentiality in wired LAN is largely ensured by medium: signals are contained within cables
- However, wireless signals can be picked up by any receiver within range of transmitter, making encryption essential
- Unencrypted information (that will not be encrypted) is called cleartext
- Unencrypted information that will be encrypted (but has not yet been fed into encryption algorithm) is plaintext
- And encrypted information is called ciphertext
- To protect integrity of message before sending it over air, sender uses mathematical function to generate checksum
- Small block of data derived from original message, allowing receiver to check whether it was altered
- Attacks against availability of wireless LAN are simple to carry out by any malicious user with proper tools
- Example is RF jamming attack, in which attacker uses signal generator to flood 802.11 frequency bands
- Only solution to RF jamming attack is to locate and disable/remove source of attack
- And only preventative measure is physical security
- Original 802.11 standard defined security protocol called Wired Equivalent Privacy (WEP)
- WEP is now obsolete; it is no longer secure
- WEP defined two methods of authentication: Open System and Shared Key
- In WEP Open System Authentication, client device sends authentication request, and AP sends authentication response; no questions asked
- WEP Shared Key Authentication involves configuration of static WEP key on AP and each client—Wi-Fi password
- To verify that each client has correct WEP key, AP sends unencrypted challenge phrase that client encrypts with WEP key and sends back to AP
- AP then decrypts challenge phrase and ensures it matches original
- In addition to authentication, WEP provides confidentiality with encryption
- Same WEP key used in Shared Key Authentication can be used to encrypt messages to and from wireless clients
- Encryption algorithm is Rivest Cipher 4 (RC4)
- WEP ensures integrity of communications using checksum called integrity check value (ICV)
- After WEP's vulnerabilities were discovered, Wi-Fi Alliance developed Wi-Fi Protected Access (WPA) certification as interim enhancement until IEEE could develop more permanent solution (802.11i, which was adopted by WPA2)
- WPA, WPA2, and WPA3 define two main authentication methods: WPA-Personal (primarily for SOHO networks) and WPA-Enterprise (for larger businesses)
- WPA-Personal involves configuring pre-shared key (PSK)—static 256-bit string that is used to generate secure encryption keys
- Same PSK must be configured on AP and its clients
- To simplify experience, can configure 8- to 63-character passphrase—what most people call "Wi-Fi password"—which is then automatically converted into 256-bit PSK
- WPA-Personal authentication involves client and AP performing four-way handshake to verify PSK and generate encryption keys
- This occurs after client has performed Open System Authentication and is associated with AP
- WPA/WPA2's PSK authentication is vulnerable to brute-force attacks if attacker captures four-way handshake
- To protect against this, WPA3 adopts new method called simultaneous authentication of equals (SAE)
- SAE is carried out before 802.11 association, which is then followed by same four-way handshake
- It still uses PSK, but in way that protects against brute-force attacks
- WPA3 with SAE still relies on PSK—single passphrase that can be compromised through social engineering attack
- Outside of SOHO networks, it's best to opt for more secure option: WPA-Enterprise
- WPA-Enterprise authenticates each individual user's or device's credentials through 802.1X and EAP
- Client first uses Open System Authentication and associates with AP and then authenticates with 802.1X/EAP
- 802.1X defines port-based network access control (PNAC), controlling whether host is allowed to communicate via switch port (or wireless LAN, in this case)
- EAP defines various authentication methods (EAP methods) and message formats
- And 802.1X defines how to encapsulate EAP messages over Ethernet or 802.11 LANS, called EAP over LANs (EAPoL)
- 802.1X defines three device roles: supplicant (device that wants to connect to network), authenticator (network devices that client connects to), and authentication server/AS (server that verifies supplicant's credentials)
- EAPoL transports EAP messages within LAN between supplicant (client device) and authenticator (AP or WLC in split-MAC architecture)
- RADIUS is typically used to transport EAP messages between authenticator and AS, which is usually RADIUS server
- EAP isn't single authentication method; it is extensible and defines various EAP methods
- Some examples are LEAP (Lightweight EAP), EAP-FAST (EAP-Flexible Authentication via Secure Tunneling), PEAP (Protected EAP), and EAP-TLS (EAP-Transport Layer Security)
- Regardless of which EAP method is used, same four-way handshake is always used after authentication to generate encryption keys
- After WEP's vulnerabilities were discovered, Temporal Key Integrity Protocol (TKIP) was created as enhancement that worked on hardware developed for WEP
- TKIP was included in Wi-Fi Alliance's first WPA certification
- TKIP uses per-packet key mixing to generate unique encryption key for each packet, making PSK less vulnerable to brute-force attacks
- TKIP's data integrity checksum, called message integrity check (MIC), is stronger than WEP's ICV
- TKIP adds sequence number to each frame to mitigate against replay attacks
- IEEE 802.11i, which formed basis of WPA2, brought in more advanced security protocols that are still in use in many wireless LANs
- WPA2 uses Counter Mode with Cipher Block Chaining Message Authentication Code Protocol (CCMP) to provide data encryption and integrity
- CCMP uses Advanced Encryption Standard (AES) in counter mode as its encryption algorithm, which is stronger than WEP/TKIP's RC4 algorithm
- CCMP uses Cipher Block Chaining Message Authentication Code (CBC-MAC) to provide more robust data integrity checksum than TKIP's MIC
- WPA3 uses Galois/Counter Mode Protocol (GCMP) for data encryption and integrity
- GCMP is more secure and more efficient than CCMP, which is necessary for encryption to keep up with faster data rates of latest 802.11 standards
- Like CCMP, GCMP uses AES counter mode encryption, although it supports greater key lengths (128 bits or 256 bits) than CCMP (128 bits)
- GCMP uses Galois Message Authentication Code (GMAC) for its data integrity checksum

