# Packet Tracer Lab 1

## Goal
Build a Packet Tracer lab from scratch that includes:
- 1 router
- 2 switches
- 2 VLANs
- Router-on-a-stick inter-VLAN routing
- DHCP for both VLANs
- NAT/PAT toward a simulated internet
- 1 ACL that blocks VLAN 20 from reaching VLAN 10, while still allowing VLAN 10 to reach VLAN 20

---

## Suggested topology

### Devices
- 1x Cisco 2911 router (`R1`)
- 2x Cisco 2960 switches (`SW1`, `SW2`)
- 4x PCs minimum:
  - `PC1` and `PC2` in VLAN 10 (Staff)
  - `PC3` and `PC4` in VLAN 20 (Servers)
- 1 optional extra device to simulate the internet side if needed, or use a loopback for testing NAT conceptually

### VLANs
- VLAN 10 = Staff
- VLAN 20 = Servers

### Example addressing
- VLAN 10: `192.168.10.0/24`
- VLAN 20: `192.168.20.0/24`
- Outside/NAT side: `203.0.113.0/24`

### Example interface plan
- `R1 G0/0` <-> `SW1 G0/1` = trunk
- `SW1 G0/2` <-> `SW2 G0/1` = trunk
- PCs connect to access ports on the switches
- `R1 G0/1` = outside interface toward simulated internet

---

## Build order
1. Place all devices on the Packet Tracer canvas.
2. Cable the network.
3. Configure VLANs on both switches.
4. Assign access ports to the correct VLANs.
5. Configure trunks.
6. Configure router-on-a-stick subinterfaces on `R1`.
7. Configure DHCP pools on the router.
8. Configure NAT/PAT.
9. Configure the ACL.
10. Test connectivity.
11. Break things on purpose, fix them, and document each issue.

---

## Step 1: Physical layout and cabling

### Place these devices
- `R1`
- `SW1`
- `SW2`
- `PC1`
- `PC2`
- `PC3`
- `PC4`

### Cable like this
- `R1 G0/0` -> `SW1 G0/1`
- `SW1 G0/2` -> `SW2 G0/1`
- `PC1` -> `SW1 F0/1`
- `PC2` -> `SW1 F0/2`
- `PC3` -> `SW2 F0/1`
- `PC4` -> `SW2 F0/2`
- `R1 G0/1` -> simulated outside network if using one

Use copper straight-through cables for router-to-switch and PC-to-switch connections.

---

## Step 2: Configure SW1

Enter these commands on `SW1`:

```bash
enable
configure terminal
hostname SW1

vlan 10
 name Staff
vlan 20
 name Servers

interface range fastethernet 0/1 - 2
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 exit

interface gigabitethernet 0/1
 switchport mode trunk
 exit

interface gigabitethernet 0/2
 switchport mode trunk
 exit

end
write memory
```

---

## Step 3: Configure SW2

Enter these commands on `SW2`:

```bash
enable
configure terminal
hostname SW2

vlan 10
 name Staff
vlan 20
 name Servers

interface range fastethernet 0/1 - 2
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 exit

interface gigabitethernet 0/1
 switchport mode trunk
 exit

end
write memory
```

---

## Step 4: Configure router-on-a-stick on R1

Enter these commands on `R1`:

```bash
enable
configure terminal
hostname R1

interface gigabitethernet 0/0
 no shutdown
 exit

interface gigabitethernet 0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ip nat inside
 exit

interface gigabitethernet 0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ip nat inside
 exit
```

These subinterfaces become the default gateways for each VLAN:
- VLAN 10 gateway = `192.168.10.1`
- VLAN 20 gateway = `192.168.20.1`

---

## Step 5: Configure the outside interface for NAT

If using `G0/1` as the outside interface:

```bash
interface gigabitethernet 0/1
 ip address 203.0.113.2 255.255.255.0
 ip nat outside
 no shutdown
 exit
```

If you attach another router, cloud, or test device to this interface, give that side a matching address such as `203.0.113.1/24`.

---

## Step 6: Configure DHCP on the router

Still on `R1`:

```bash
ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp excluded-address 192.168.20.1 192.168.20.20

ip dhcp pool VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 8.8.8.8
 exit

ip dhcp pool VLAN20
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
 dns-server 8.8.8.8
 exit
```

After this, set all PCs to DHCP in Packet Tracer.

---

## Step 7: Configure NAT/PAT

Still on `R1`:

```bash
access-list 1 permit 192.168.10.0 0.0.0.255
access-list 1 permit 192.168.20.0 0.0.0.255

ip nat inside source list 1 interface gigabitethernet 0/1 overload
```

This allows both inside VLANs to share the outside interface IP using PAT.

---

## Step 8: Configure the ACL between VLANs

Goal:
- Block VLAN 20 from reaching VLAN 10
- Allow VLAN 10 to reach VLAN 20

Apply the ACL inbound on subinterface `G0/0.20`:

```bash
ip access-list extended BLOCK_V20_TO_V10
 deny ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255
 permit ip any any
 exit

interface gigabitethernet 0/0.20
 ip access-group BLOCK_V20_TO_V10 in
 exit

end
write memory
```

Why here:
- Traffic from VLAN 20 enters the router through `G0/0.20`
- The ACL stops VLAN 20 from going to VLAN 10 as soon as it reaches the router
- VLAN 20 can still go elsewhere unless explicitly denied

---

## Step 9: Client testing checklist

After setting all PCs to DHCP, verify:

### DHCP
On each PC, confirm it receives:
- An IP address in the correct subnet
- The correct default gateway
- A DNS server

### VLAN and inter-VLAN routing
- `PC1` should ping `192.168.10.1`
- `PC3` should ping `192.168.20.1`
- `PC1` should be able to ping `PC3`
- `PC3` should NOT be able to ping `PC1`

### NAT/outside reachability
- Try to ping the simulated outside address from a VLAN 10 client
- Try to ping the simulated outside address from a VLAN 20 client

### Useful verification commands
On switches:

```bash
show vlan brief
show interfaces trunk
```

On router:

```bash
show ip interface brief
show ip route
show ip dhcp binding
show ip nat translations
show access-lists
```

---

## Step 10: Break and fix exercises

### Break 1: Wrong DNS server in DHCP
Change the DHCP pool to use a bad DNS server:

```bash
configure terminal
ip dhcp pool VLAN10
 dns-server 1.1.1.250
 exit
ip dhcp pool VLAN20
 dns-server 1.1.1.250
 exit
```

Then renew client addresses if needed.

#### Expected symptom
- Clients still get IP addresses
- Ping by IP may still work
- Name resolution fails

#### Fix
Set the DNS server back to a valid value:

```bash
configure terminal
ip dhcp pool VLAN10
 dns-server 8.8.8.8
 exit
ip dhcp pool VLAN20
 dns-server 8.8.8.8
 exit
end
```

---

## Break DNS
- Symptom: Clients receive IP settings, but name resolution fails when trying to use hostnames.
- Test run: Check client IP configuration with `ipconfig /all`, then test connectivity by IP and compare it to hostname-based tests.
- Root cause: The DHCP pools were handing out an incorrect DNS server address.
- Fix: Change the `dns-server` value in both DHCP pools back to a valid DNS server and renew the clients' DHCP leases.

---

### Break 2: Break the trunk
On `SW1`, intentionally change the router-facing trunk to access mode:

```bash
configure terminal
interface gigabitethernet 0/1
 switchport mode access
 end
```

#### Expected symptom
- Inter-VLAN routing fails
- One or both VLANs lose connectivity through the router-on-a-stick link

#### Fix
Restore trunk mode:

```bash
configure terminal
interface gigabitethernet 0/1
 switchport mode trunk
 end
```

Also verify the switch-to-switch link is still trunking.

---

## Break trunk
- Symptom: Clients can no longer route between VLANs, and default gateway reachability may fail for one or both VLANs.
- Test run: Use `show interfaces trunk` on the switch and run pings from a VLAN 10 PC to a VLAN 20 PC or to the remote VLAN gateway.
- Root cause: The router-facing link was changed from trunk mode to access mode, so VLAN tags no longer reached the router subinterfaces correctly.
- Fix: Reconfigure the interface as a trunk and confirm trunk status with `show interfaces trunk`.

---

### Break 3: Break NAT
Remove the PAT overload statement on `R1`:

```bash
configure terminal
no ip nat inside source list 1 interface gigabitethernet 0/1 overload
end
```

#### Expected symptom
- Internal hosts may still reach internal networks
- Internal hosts cannot reach the outside network through translated addresses

#### Fix
Re-add the NAT overload command:

```bash
configure terminal
ip nat inside source list 1 interface gigabitethernet 0/1 overload
end
```

Verify with:

```bash
show ip nat translations
```

---

## Break NAT
- Symptom: Internal hosts can still communicate inside the lab, but they can no longer reach the outside network.
- Test run: Ping the simulated outside address from a client, then check `show ip nat translations` on the router.
- Root cause: The NAT overload statement was removed, so inside addresses were no longer being translated to the outside interface.
- Fix: Reapply `ip nat inside source list 1 interface gigabitethernet 0/1 overload` and test again.

---

## Subnetting drill
Use the base network `172.16.0.0/16`.

### Problem 1: /24 subnet
Example subnet: `172.16.5.0/24`
- Network address: `172.16.5.0`
- Broadcast address: `172.16.5.255`
- First usable host: `172.16.5.1`
- Last usable host: `172.16.5.254`
- Usable hosts: `254`

### Problem 2: /26 subnet
Example subnet: `172.16.5.0/26`
- Network address: `172.16.5.0`
- Broadcast address: `172.16.5.63`
- First usable host: `172.16.5.1`
- Last usable host: `172.16.5.62`
- Usable hosts: `62`

### Problem 3: another /26 subnet
Example subnet: `172.16.5.64/26`
- Network address: `172.16.5.64`
- Broadcast address: `172.16.5.127`
- First usable host: `172.16.5.65`
- Last usable host: `172.16.5.126`
- Usable hosts: `62`

Optional extra practice:
- `172.16.5.128/26`
- `172.16.5.192/26`

---

## Quick command summary

### Switch verification
```bash
show vlan brief
show interfaces trunk
show running-config
```

### Router verification
```bash
show ip interface brief
show running-config
show ip route
show ip dhcp binding
show ip nat translations
show access-lists
```

### Client verification
```bash
ipconfig /all
ping <ip>
```

