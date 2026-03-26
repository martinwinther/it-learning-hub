# Wireshark Basics Notes

## DHCP capture
I captured DHCP traffic while releasing and renewing the client IP address and filtered the packets with `dhcp` / `bootp`. In the exchange I could see the normal DORA process: **Discover**, **Offer**, **Request**, and **ACK**, which shows the client asking for an address and the DHCP server assigning one. This made it very clear that DHCP is not just “the PC gets an IP automatically,” but an actual multi-step negotiation between the client and the server.

## DNS capture
I then captured DNS traffic by opening a website in the browser and filtering with `dns`. In the capture I could see a DNS query from the client for the website’s domain name and a matching response from the DNS server returning the resolved IP address. This showed the practical role of DNS very clearly: before the browser can reach a website by name, the client first has to translate that name into an IP address.

## Web request and TCP handshake
For the web traffic capture, I filtered with `http` / `tls.handshake` and followed the connection setup before the actual request. I identified the TCP 3-way handshake as **SYN → SYN-ACK → ACK**, which established the connection between the client and the remote server before the HTTP or TLS traffic began. After that, I could see the start of the web session, which helped connect the theory of TCP connection setup to a real packet capture.

## Short summary
Yes, I can open a `.pcap` in Wireshark without freezing up and work with basic filters to narrow the traffic down. I can explain in normal words what happened in a capture at a high level, especially for DHCP, DNS, and the start of a web connection.

I can also identify a TCP 3-way handshake in a real capture by finding the **SYN**, **SYN-ACK**, and **ACK** packets in order before the application traffic begins. What still feels a little unclear is following larger captures when there is a lot of noise, and being fully confident about which packets belong to the exact session I want without second-guessing myself. That feels like the best starting point for the next session.
