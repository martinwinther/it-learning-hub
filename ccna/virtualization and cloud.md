# Virtualization and Cloud

## Overview

Virtualization and cloud computing allow many logical systems to share the same physical infrastructure. Virtual machines, containers, and VRFs create virtualized compute and network resources, while cloud providers deliver these resources as on demand services.

## Network virtualization

### VLANs

- Virtual LANs (VLANs) segment a single physical LAN into multiple logical LANs.
- All hosts connect to the same physical switch but belong to different VLANs.
- Hosts in one VLAN cannot communicate directly with hosts in another VLAN without routing.
- VLANs provide separate broadcast domains on shared hardware.

### VPNs

- Virtual private networks (VPNs) build private networks over shared infrastructure such as the internet.
- Encrypted tunnels carry private traffic across public networks.
- VPNs create logically separate, secure networks on top of a shared physical network.

### Virtualization concept

- VLANs and VPNs are examples of network virtualization.
- Network virtualization creates logical separation on shared physical infrastructure.
- The same idea applies to compute resources with virtual machines and containers.
- CCNA exam topics include server virtualization, containers, and VRFs at a basic level.

## Virtual machines

### Traditional server setup

- A physical server traditionally ran a single operating system.
- All hardware resources (CPU, RAM, storage) were dedicated to that one OS and its applications.
- Modern servers are powerful, so running a single OS often leaves resources underused.
- Each physical server requires space, power, cooling, and physical security.
- Large numbers of underutilized servers increase capital and operating costs.

### Virtual machine overview

- Virtual machines remove the one to one relationship between hardware and OS.
- A hypervisor allows multiple OS instances to run on a single physical server.
- The hypervisor manages CPU, memory, storage, and network access for each VM.
- The physical machine is the host, and the OS inside each VM is the guest.

### Type 1 hypervisors

- Run directly on physical hardware (bare metal).
- Provide efficient access to hardware resources.
- Common examples: VMware ESXi, Microsoft Hyper-V.
- Widely used for server virtualization in data centers and cloud environments.

### Type 2 hypervisors

- Run as applications on top of a host operating system.
- The host OS uses resources, and the hypervisor must pass through the host OS to reach hardware.
- Less resource efficient than type 1 hypervisors.
- Common examples: Oracle VM VirtualBox, VMware Workstation.
- Useful for personal use, development, testing, and education on existing PCs.
- The OS on hardware is the host OS, and each VM runs a guest OS.

### VM networking

- Each VM behaves like an independent host on the network.
- VMs use virtual network interface cards (vNICs) instead of physical NICs.
- A virtual switch forwards frames between vNICs and the physical NICs of the host.
- Virtual switch ports can operate in access or trunk mode.
- Servers running many VMs often connect to physical switches with trunk ports to carry multiple VLANs.
- Redundant physical NICs on the host provide link and switch redundancy for the VMs.

### VM benefits

- Reduced costs  
  Fewer physical servers are needed, reducing hardware, space, power, and cooling requirements.

- Mobility  
  VMs can be saved as files, copied, and moved between hosts for migration or recovery.

- Isolation  
  Each VM is separate from others. Problems such as crashes or malware in one VM do not directly affect others.

- Faster provisioning  
  New VMs can be created quickly from templates, reducing deployment time for new services.

## Containers

### Container overview

- Containers provide a lightweight form of virtualization.
- A container packages an application and its dependencies into an isolated environment.
- Containers do not include a full guest OS.
- Multiple containers share the same host OS kernel.

### Container architecture

- A container engine, such as Docker Engine, runs on the host OS.
- Containers run on top of the container engine.
- Each container includes the application and its libraries, not a separate kernel.
- Most engines run on Linux, but container support exists on other platforms as well.

### Container orchestration

- Container orchestrators automate deployment, scaling, and management of containers.
- Kubernetes is the most widely used orchestrator.
- Large applications using microservices can involve thousands of containers.
- Orchestrators handle placement, scaling, health checks, and restarts.

### VMs vs containers

- Startup time  
  VMs can take minutes to boot a full OS. Containers typically start in milliseconds.

- Disk space  
  VMs require full OS images, often several gigabytes. Containers are smaller and share common layers.

- CPU and RAM efficiency  
  VMs each run a full OS. Containers share the host OS and usually consume fewer resources.

- Portability  
  VMs are portable between hosts running the same hypervisor. Containers are highly portable across any host that supports the container engine format.

- Isolation  
  VMs provide strong isolation between guest OS instances. Containers share a kernel, so kernel level problems can affect all containers on the same host.

VMs and containers solve different problems and both are common in modern environments.

## Virtual Routing and Forwarding (VRF)

### VRF overview

- VRF divides a physical router into multiple virtual routers.
- Each VRF has its own routing table and interfaces.
- Service providers use VRFs to keep customer traffic separate on shared infrastructure.
- MPLS Layer 3 VPNs use VRFs to provide isolated customer networks.
- VRF without MPLS is often called VRF lite.

### VRF isolation

- Interfaces are assigned to specific VRFs.
- Traffic in one VRF is forwarded only within that VRF.
- Traffic cannot exit an interface belonging to another VRF or the global table.
- VRF leaking allows selected routes to be shared between VRFs but is outside CCNA scope.

### VRF configuration concepts

- Create a VRF in global configuration mode:

  ```cisco
  ip vrf CUSTOMER1
  ```

- Assign an interface to a VRF in interface configuration mode:

  ```cisco
  interface GigabitEthernet0/0
   ip vrf forwarding CUSTOMER1
   ip address 192.168.1.1 255.255.255.252
  ```

- Assigning a VRF removes any existing IP address from the interface, so the IP address must be reconfigured.
- Each VRF maintains its own routing table:

  ```cisco
  show ip vrf
  show ip route vrf CUSTOMER1
  ```

- Interfaces not placed in a VRF belong to the global routing instance.
- The global routing table is shown with `show ip route` without a VRF name.

### VRF summary

- VRF splits a single router into multiple virtual routers.
- Each VRF has its own interfaces and routing table.
- Overlapping subnets can exist on the same physical router as long as they are in different VRFs.

## Traditional IT infrastructure

### On premises

- On premises (on prem) infrastructure is located in facilities owned or controlled by the organization.
- The organization purchases and owns the hardware.
- Local staff are responsible for space, power, cooling, and physical security.
- On prem provides maximum control over hardware and environment.

### Colocation

- Colocation means placing owned equipment in a third party data center.
- The data center provides space, power, cooling, and physical security.
- The customer owns and manages the servers and network devices.
- Proximity to other customers in the data center can simplify interconnections between organizations.

## Cloud computing

### Cloud computing overview

- Cloud computing delivers shared compute, storage, and network resources as services over a network.
- Resources are hosted in provider data centers and consumed on demand.
- Cloud complements on prem and colocation options and is widely used in combination with them.

### NIST definition

- The NIST definition of cloud computing describes five essential characteristics, three service models, and four deployment models.
- The full paper is short and remains a useful reference for cloud fundamentals.

## Cloud computing characteristics

### Five essential characteristics

- On demand self service
- Broad network access
- Resource pooling
- Rapid elasticity
- Measured service

### On demand self service

- Customers provision and release services as needed.
- Actions are performed through portals or APIs without manual intervention by the provider.

### Broad network access

- Services are reachable over standard networks such as the internet or private WANs.
- Access is possible from many device types, including PCs, laptops, and mobile devices.

### Resource pooling

- Provider resources are pooled to serve multiple customers.
- Computing, storage, and network capacity is allocated dynamically.
- Customers share the underlying pool while remaining logically isolated.

### Rapid elasticity

- Resources can scale up or down quickly.
- Capacity can adjust to peaks and drops in demand.
- Automation can trigger scaling in response to load.

### Measured service

- Usage is measured and recorded by the provider.
- Billing is typically usage based, such as per gigabyte of storage or per instance hour.
- Customers can view and track their consumption over time.

## Cloud service models

### Overview

Cloud providers offer different layers of service. The main models are Software as a Service, Platform as a Service, and Infrastructure as a Service.

### Software as a Service (SaaS)

- Delivers complete applications over the network.
- Users access applications through web interfaces or thin clients.
- Provider manages infrastructure, platform, and application.
- Examples: Microsoft 365, Google Workspace, Slack, Zoom.

### Platform as a Service (PaaS)

- Provides a platform for developing and running applications.
- Includes runtime, middleware, and supporting services.
- Customers focus on application code while the provider manages infrastructure and platform.
- Examples: AWS Lambda, Azure App Service, Google App Engine.

### Infrastructure as a Service (IaaS)

- Offers basic compute, storage, and network resources as virtual infrastructure.
- Customers create VMs, choose OSs, and manage applications.
- Provider manages the physical data center and virtualization layer.
- Examples: AWS EC2, Azure Virtual Machines, Google Compute Engine.
- Of the three models, IaaS gives the most control to the customer and SaaS the least.

## Cloud deployment models

### Public cloud

- Cloud infrastructure is owned and operated by a provider and offered to the public.
- Any customer can subscribe and consume resources.
- Examples: AWS, Microsoft Azure, Google Cloud Platform.

### Private cloud

- Cloud infrastructure is dedicated to a single organization.
- May be operated by the organization or by a third party.
- May be located on premises or in an external data center.

### Community cloud

- Cloud infrastructure is shared by multiple organizations with common requirements.
- Can be managed by one or more member organizations or by a third party.
- Can be located on or off premises of member organizations.

### Hybrid cloud

- Combines two or more of the other deployment models.
- Example: private cloud that can burst workloads into a public cloud when needed.

## Cloud benefits and considerations

### Benefits

- Cost efficiency  
  Reduces or eliminates upfront capital expenses for hardware and facilities.

- Global scaling  
  Services can be deployed in multiple regions to reduce latency and reach users worldwide.

- Speed and agility  
  New services and resources can be provisioned in minutes instead of weeks or months.

- Productivity  
  Offloading hardware management allows IT staff to focus on higher level tasks.

- Reliability  
  Data can be replicated across sites to support backup and disaster recovery.

### Considerations

- Cloud is not always the lowest cost option.
- Some workloads are more economical on prem or in colocation.
- Many organizations combine on prem, colocation, and cloud to match different needs.

## Quick review

- VLANs and VPNs are forms of network virtualization that create logical networks on shared physical infrastructure.  
- Virtual machines use hypervisors to run multiple guest OSs on a single physical server, with type 1 hypervisors running on bare metal and type 2 on a host OS.  
- VMs rely on virtual switches and vNICs for networking and provide isolation, mobility, and faster provisioning compared to physical servers.  
- Containers package applications and dependencies in lightweight, isolated environments that share a host OS and are typically managed at scale by orchestrators such as Kubernetes.  
- VRF divides a router into multiple virtual routers with separate routing tables, allowing overlapping IP ranges and traffic isolation per VRF.  
- On premises and colocation are traditional deployment models where the organization owns the hardware, either on site or in a third party data center.  
- Cloud computing provides shared resources as services with five key characteristics: on demand self service, broad network access, resource pooling, rapid elasticity, and measured service.  
- SaaS delivers complete applications, PaaS provides platforms for application development, and IaaS delivers basic virtual infrastructure.  
- Public, private, community, and hybrid clouds describe how cloud infrastructure is deployed and shared among customers.  
