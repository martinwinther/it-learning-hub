# Virtualization and Cloud

## Overview

Virtualization and cloud computing are two technologies that have transformed modern IT infrastructure. Virtualization refers to a variety of technologies that enable you to create virtual versions of something—servers, routers, etc.—that are abstracted from the underlying physical hardware. Taking advantage of the flexibility of virtualization, cloud computing provides on-demand computing services that can be accessed remotely over a network and scaled to meet user demands. In this chapter, we will delve into server virtualization with virtual machines (VMs), a technology that allows multiple virtual servers to run on a single physical server. We will also look at containers, a technology that runs applications in isolated environments offering flexibility, portability, and efficient resource usage. We will then explore Virtual Routing and Forwarding (VRF), which divides a single physical router into multiple virtual routers. Finally, we will cover the concept of cloud computing and the various service models used by modern enterprises of all sizes.

## Network Virtualization

### VLANs

- Before we delve into VMs and containers, think back to technology we previously covered that includes word "virtual": virtual LANs (VLANs)
- VLANs segment single physical network into multiple distinct logical networks
- Although all six PCs are connected to same physical switch and are therefore in same physical LAN
- They are grouped into three different VLANs
- Hosts in one VLAN cannot communicate directly with hosts in another VLAN
- Despite being physically connected to same switch
- VLANs create distinct virtual LANs from single physical LAN

### VPNs

- We covered another "virtual" technology in previous chapter: virtual private networks (VPNs)
- VPNs overlay private networks on top of shared infrastructure like public internet
- Creating secure tunnels between devices
- VPNs are distinct virtual networks that enable secure communication over shared physical network
- VPN is secure virtual network created over physical network

### Virtualization Concept

- VLANs and VPNs are both examples of network virtualization
- Creating logically separate networks on shared physical infrastructure
- This concept of virtualization extends beyond networking into realm of computing resources
- With topics of this section: VMs and containers
- These technologies allow operating systems and applications to run in isolated environments on single physical server
- CCNA, as networking certification, places less emphasis on VMs and containers than network virtualization technologies
- However, they are part of CCNA exam topic 1.12: Explain virtualization fundamentals (server virtualization, containers, and VRFs)
- So make sure you have solid grasp of basics that we will cover

## Virtual Machines

### Traditional Server Setup

- In past, physical server would run single operating system (OS)—for example, Windows Server or some variety of Linux
- This meant that all of hardware resources—CPU, RAM, storage, etc.—were tied to that one OS and its applications
- This often led to resource underutilization, as dedicated hardware could far exceed needs of single OS and its applications
- Modern server hardware can be very powerful
- Physical server running one OS and its apps
- Server hardware is quite expensive
- And in addition to cost of hardware itself, each server requires physical space, cooling, and electrical power
- Data center full of underutilized servers is not efficient use of these resources
- Virtualization addresses inefficiencies like these by consolidating servers and maximizing resource utilization

### Virtual Machine Overview

- Virtual machines break one-to-one relationship of hardware to OS
- Allowing multiple OSs to run on single physical server
- This is facilitated by hypervisor, layer of software that allows multiple operating systems to share single hardware host
- It sits between hardware and VMs, managing and allocating hardware resources (CPU, RAM, Storage, etc.) to each VM
- There are two main types of hypervisors

### Type 1 Hypervisors

- Type 1 hypervisors run directly on top of hardware
- Type 1 hypervisor is installed directly on underlying physical hardware
- Managing and allocating physical hardware resources to each VM running on top of it
- Type 1 hypervisor runs directly on server hardware
- Type 1 hypervisors are also called bare-metal hypervisors because they run directly on hardware (the "metal")
- Another term is native hypervisor
- Two common type 1 hypervisors are VMware ESXi and Microsoft Hyper-V
- Type 1 hypervisors are what you'll most often find used for server virtualization in data center environments (including cloud)
- By interacting directly with physical hardware without any intermediaries
- They provide very efficient use of hardware resources when compared with type 2 hypervisors

### Type 2 Hypervisors

- Type 2 hypervisors run as application on host OS
- Whereas type 1 hypervisor runs directly on underlying hardware
- Type 2 hypervisor runs as application on OS, like regular computer application
- Type 2 hypervisor runs as application on host OS
- Another name for type 2 hypervisor is hosted hypervisor
- Two common type 2 hypervisors are Oracle VM VirtualBox and VMware Workstation
- VirtualBox is free, and Workstation has free and paid versions
- OS running directly on hardware is called host OS
- And OS running in VM is called guest OS
- Unlike type 1 hypervisors, which have direct access to hardware resources
- Type 2 hypervisors must go through host OS to access these resources
- Furthermore, host OS itself consumes hardware resources
- Both of these points mean that type 2 hypervisors are less resource-efficient than type 1 hypervisors
- Making them less suited for resource-intensive applications
- Type 2 hypervisors are rare in context of virtual servers in data center environment
- However, advantage of type 2 hypervisors lies in their ease of setup and use
- User can install and run type 2 hypervisor on their PC just like any other application
- Making it more accessible for those who may not have technical expertise to set up type 1 hypervisor
- This also means that type 2 hypervisor can coexist with other applications on host OS
- Allowing PC to be used for virtualization without needing dedicated hardware
- For these reasons, type 2 hypervisors are more common on personal-use devices
- Example: if Mac/Linux user needs to run app that is only supported on Windows (or vice versa)
- Type 2 hypervisor can be used to easily run another OS without need to buy another computer
- Type 2 hypervisors are also popular for software development, testing, and educational purposes

### VM Networking

- Each VM—whether it is running on type 1 or type 2 hypervisor—operates as independent host on network
- Much like physical computer
- Although VM doesn't have its own physical network interface card (NIC) like standalone physical host
- It uses virtual NIC (vNIC)
- Through this vNIC, VM can communicate with other hosts
- Whether they are other VMs on same physical server or devices on external physical network
- To manage network traffic to and from VMs, hypervisor uses virtual switch
- Which forwards frames between vNICs of VMs and physical NIC (or NICs) of host machine
- VMs connect to each other and external physical network via virtual switch
- VMs are often segmented into separate VLANs, requiring trunk links
- Figure shows two NICs on physical server
- It's common for servers to have multiple NICs (each connected to different physical switch) to provide redundancy
- Allowing server to remain accessible if one NIC or switch fails
- Just like physical switch, virtual switch's ports can operate in access or trunk mode
- Enabling use of VLANs to segment VMs
- To allow VMs in different VLANs to communicate over network
- Virtual switch connects to physical host's NICs via trunk links
- Likewise, physical host's NICs connect to external physical switches via trunk links
- Although switch ports connected to end hosts are almost always access ports
- Ports connected to servers running VMs are rare examples of trunk ports connected to end hosts
- They need to be able to carry traffic to and from VMs in multiple VLANs

### VM Benefits

- **Reduced costs**: By efficiently using server hardware resources, fewer physical servers are needed, reducing capital expenses (upfront costs). This also reduces space, cooling, and power demands, reducing operating expenses (ongoing costs)
- **Mobility**: Entire VM can be easily saved as file. This facilitates easy transfer, duplication, or migration (for example, if problem occurs on one physical server)
- **Isolation**: Each VM operates independently from others, providing enhanced security and stability. Problems within one VM, such as crashes or malware infections, do not affect rest of system
- **Faster provisioning**: New VMs can be rapidly provisioned and deployed. This allows organization to quickly respond to changing business needs, with ability to roll out new applications and services in minutes rather than days or weeks required for setting up new physical servers

## Containers

### Container Overview

- While VMs offer full hardware virtualization, providing complete OSs for their applications
- More agile approach is gaining prominence in modern IT infrastructure: containers
- Container is lightweight, stand-alone package that includes everything needed to run particular application
- Container is similar to VM in that it provides isolated environment for application
- But is different in that it's more lightweight (smaller in size), requiring less overhead
- Instead of running independent OS, container only contains application and its dependencies (various files and services it needs to run)

### Container Architecture

- Containers run on container engine; popular example is Docker Engine
- Container engine itself runs on host OS (usually Linux)
- Notice that each container does not run its own OS
- Containers run on container engine, such as Docker Engine
- Container engine runs on host OS, but each container does not run guest OS

### Container Orchestration

- Software platform called container orchestrator is typically used to automate deployment, management, and scaling of containers
- Kubernetes, originally designed by Google, is industry standard
- In small numbers, manual operation is possible
- But large-scale systems can use many thousands (sometimes hundreds of thousands) of containers
- This is especially true of applications that employ microservices architecture
- Which breaks application into many small, self-contained services
- Containers are perfect for this, as they can isolate and manage these services independently

### VMs vs Containers

- **Startup time**: VMs can take minutes to boot up as each runs its own OS. Containers can boot up in milliseconds
- **Disk space**: VMs take up more disk space (often many gigabytes) due to requiring full OS. Containers take up relatively little disk space (megabytes)
- **CPU/RAM efficiency**: VMs use more CPU/RAM resources; once again, this is because each VM runs its own OS. Containers share OS and therefore use fewer CPU/RAM resources
- **Portability**: VMs are portable across different physical systems running same hypervisor. Containers offer even greater portability—they are smaller, are faster to start, and can run on any modern container engine with Docker compatibility
- **Isolation**: VMs offer strong isolation; problem on one VM won't affect others. Containers run on same host OS, so problem on that host OS can affect all containers
- Although there is major movement toward use of containers, especially with rise of microservices, automation, and DevOps (combination of software development and IT operations)
- VMs and containers serve different needs, and both are widely used

## Virtual Routing and Forwarding (VRF)

### VRF Overview

- Let's move away from virtual machines and containers back to network virtualization
- Similar to how VLANs segment switch into multiple virtual switches
- Virtual Routing and Forwarding (VRF) segments router into multiple virtual routers
- Service providers often use VRF to allow customer's traffic to travel over service provider's shared infrastructure
- While remaining isolated from other customers
- As mentioned in previous chapter, MPLS L3VPNs implement VRF for this purpose
- VRF segments physical router into multiple virtual routers

### VRF Isolation

- Like VLANs, each VRF is isolated from other VRFs
- Traffic in one VRF cannot be forwarded out of interface that belongs to another VRF
- There is one exception; VRF leaking can be configured to allow traffic to pass between VRFs
- However, VRF leaking and its use cases are more advanced topic beyond scope of CCNA

### VRF Configuration

- Although VRF configuration itself isn't tested on CCNA exam, it's useful tool to demonstrate how VRF works
- So let's walk through basic VRF configuration and examine its effects
- SPR1 is divided into three VRFs
- Because each VRF functions as independent router, overlapping IP addresses are not problem
- As mentioned previously, VRF is often used to enable MPLS L3VPNs
- VRF without MPLS is called VRF-lite, and that's what we're covering in this example
- MPLS L3VPN implementation is more advanced topic

### VRF Configuration Steps

1. Create VRFs
2. Assign interfaces to each VRF
3. Configure routing for each VRF

### Creating VRFs

- To create VRF, use `ip vrf vrf-name` command in global config mode
- That will bring you to VRF configuration mode, from which you can configure various VRF-related settings
- However, for most basic VRF-lite configuration, just creating VRF is sufficient
- Can verify with `show ip vrf`

### Assigning Interfaces to VRFs

- Next step is to assign interfaces to each VRF
- In example network, all three VRFs use overlapping IP addresses in 192.168.1.0/30 and 192.168.4.0/30 subnets
- As following example shows, this is not possible on router without using VRFs
- Because purpose of router is to connect different networks, it can't have multiple interfaces connected to same network (multiple interfaces in same subnet)
- If there is any overlap between interfaces' subnets, IOS will reject command
- VRFs, however, are virtually isolated from each other
- Interfaces in different VRFs can use overlapping subnets and even identical IP addresses
- This allows for different customers to maintain their addressing schemes without worrying about other customers' addressing
- In our example, each VRF is used to support different customer network
- And each customer network uses same subnets
- To assign interface to VRF, use `ip vrf forwarding vrf-name` command in interface config mode
- If interface already has IP address, it will be removed when you assign interface to VRF
- Must reconfigure IP address after assigning interface to VRF

### VRF Routing Tables

- Although we won't cover how to configure static and dynamic routing when using VRFs
- Let's look at connected and local routes that are automatically added to routing table after configuring IP addresses on router's interfaces
- `show ip route` command on its own doesn't show any routes
- That's because router builds unique routing table for each VRF
- And you have to specify which VRF's routing table you want to see with `show ip route vrf vrf-name`
- Other commands require you to specify particular VRF too
- Example: ping command requires VRF specification when using VRFs

### Global Routing Instance

- Even when using VRFs, router can have interfaces that aren't assigned to any particular VRF
- These interfaces are part of global routing instance
- And their associated routes are part of global routing table
- This is "normal" routing table you can view with `show ip route` (without specifying VRF)
- If you issue ping without specifying VRF, router will search for ping's destination in global routing table
- However, in our example network, all interfaces are assigned to specific VRF instances and none to global routing instance
- So global routing table does not contain any routes

### VRF Summary

- VRF divides physical router into multiple virtual routers (VRFs), each with its own routing table
- VRF allows for use of overlapping subnets on same physical router (although they must be in different VRFs)
- Traffic in one VRF will only be forwarded within same VRF, not to different VRFs (or global routing instance)

## Traditional IT Infrastructure

### On-Premises

- Now that we've covered foundational technologies of VMs, containers, and VRF
- We're almost ready to ascend into cloud
- These virtualization technologies underpin vast and scalable architectures of cloud
- Enabling dynamic provisioning, management, and deployment capabilities that are characteristic of cloud computing
- But before we look at cloud computing, let's briefly consider bedrock of traditional IT infrastructure: on-premises and colocation setups
- On-premises (often abbreviated as on-prem) solutions represent classic approach
- In which company's infrastructure (servers and key network devices) is located within its own facilities
- Offering complete control over IT environment
- All equipment is purchased and owned by company using it
- And company is responsible for necessary space, power, cooling, and physical security

### Colocation

- In contrast, colocation services allow business to rent space in third-party data centers to house its infrastructure
- While business is still responsible for purchasing and operating servers
- Necessary space, power, and cooling are provided by data center
- As well as robust physical security
- Proximity to colocation data center's other customers also has benefit of facilitating connections between customers
- Enabling them to share resources efficiently
- Two customers (Enterprise A and Enterprise B) house their servers in colocation data center
- They connect their networks in data center, allowing them to share resources

## Cloud Computing

### Cloud Computing Overview

- Cloud computing is third approach that provides on-demand access to shared computing resources over network
- It provides alternative to on-prem and colocation solutions that is not only hugely popular but is also continuing to grow year on year
- In rest of this section, we'll explore exactly what cloud computing is
- Covering its essential characteristics, service models, and deployment models

### NIST Definition

- In 2011, American National Institute of Standards and Technology (NIST) published paper titled "The NIST Definition of Cloud Computing"
- Despite being published over decade ago, it remains cornerstone for understanding cloud computing fundamentals
- PDF file is seven pages in length, but actual substance of paper is only last two pages
- In this section, I will mainly expand upon and provide diagrams to help clarify contents of NIST's paper
- But I highly recommend reading paper yourself

## Cloud Computing Characteristics

### Five Essential Characteristics

- On-demand self-service
- Broad network access
- Resource pooling
- Rapid elasticity
- Measured service

### On-Demand Self-Service

- On-demand self-service means that customer is able to use service (or stop using service) as needed
- Without direct human interaction with service provider—for example, via web portal
- AWS web portal through which customers can access services
- Human-to-human interaction with AWS isn't necessary
- Amazon Web Services (AWS) is most popular public cloud service provider
- Some other major players in business are (in order of market share, with AWS at top):
  - Microsoft Azure
  - Google Cloud Platform (GCP)
  - Alibaba Cloud
  - IBM Cloud

### Broad Network Access

- Broad network access means that services should be made available over standard network connections (i.e., internet or private WAN connections)
- And should be accessible by many kinds of devices, including mobile phones, desktop PCs, etc.
- Cloud resources are accessible over standard network connections
- For example, private WAN connections, simple internet connections, or internet VPNs can be used to access cloud resources

### Resource Pooling

- Resource pooling means that shared pool of resources is provided to serve multiple customers
- When customer requests service, resources to fulfill that request are dynamically allocated from shared pool
- AWS, for example, has data centers all over world with countless powerful servers
- When customer creates VM on AWS, small portion of that huge resource pool is dynamically allocated to new VM
- If customer deletes VM, allocated resources are released back into pool

### Rapid Elasticity

- Rapid elasticity means that customers can quickly scale their cloud resources up or down as needed
- This scaling can often be automated, adjusting to resource demands in real time
- To understand utility of rapid elasticity, imagine e-commerce business gearing up for Christmas season
- Anticipating increased website traffic, company can easily scale up its cloud resources to accommodate surge
- Once holiday rush calms down, they can just as easily scale down
- Ensuring they only pay for resources they need
- Without cloud, business would be forced to maintain enough physical servers to support their peak periods year-round
- Resulting in unnecessary costs for servers that are underutilized most of year

### Measured Service

- Final essential characteristic is measured service
- Which means that cloud service provider measures customer's use of cloud resources
- Providing transparency for both provider and customer
- Customer is typically charged based on their usage (for example, X dollars per gigabyte of storage per day)
- GCP billing report shows cost increasing and decreasing according to use
- Cloud providers like GCP measure customers' resource usage and charge according to that usage

## Cloud Service Models

### Three Service Models

- In traditional on-prem or colocation setup, enterprise purchases its own resources
- Using them according to its specific needs
- Cloud computing service providers like AWS, Microsoft Azure, and GCP offer these resources
- Servers, storage, networking, and even entire platforms and applications—as services on subscription basis
- Customer benefits from access to these resources without responsibilities of ownership and maintenance
- But what kinds of services are available through these providers?
- Cloud service providers offer variety of different services that can largely be categorized into three main types:
  - Software as a Service (SaaS)
  - Platform as a Service (PaaS)
  - Infrastructure as a Service (IaaS)
- Spectrum of what is offered in each cloud service model in comparison to colocation and on-prem solutions
- Runtime refers to environment that executes application code
- While middleware provides essential services and capabilities, such as database management systems
- That enable applications to communicate and manage data

### Software as a Service (SaaS)

- Software as a Service (SaaS) delivers applications as service over network (typically internet)
- Instead of installing and using applications on their own devices, users simply access them via internet
- SaaS applications run on provider's infrastructure and are typically accessible from any device with web browser
- Some popular examples of SaaS are:
  - Microsoft 365 (formerly Office 365): Word, Excel, PowerPoint, Outlook, etc.
  - Google Workspace (formerly G Suite): Gmail, Docs, Drive, Calendar, etc.
  - Slack
  - Dropbox
  - Zoom

### Platform as a Service (PaaS)

- Platform as a Service (PaaS) provides platform for customers to develop, run, and manage applications
- Without complexity of building and maintaining infrastructure typically associated with developing and launching app
- As shown in figure, service includes everything except applications themselves
- Which customer develops using provided platform
- They don't have name recognition of famous SaaS products
- But some popular PaaS offerings are AWS Lambda, Azure App Service, and Google App Engine

### Infrastructure as a Service (IaaS)

- Infrastructure as a Service (IaaS) offers essential computing resources, storage, and networking capabilities on demand
- Customers can create virtual machines, install OSs, run applications, etc., on provider's infrastructure
- Customizing CPU, RAM, and storage for each virtual machine
- And configuring their interconnections to form virtual network
- Some popular examples are AWS EC2, Azure Virtual Machines, and Google Compute Engine
- Of these three cloud service models, IaaS provides greatest control to customer
- Service provider is responsible for data center that hosts physical infrastructure
- Physical infrastructure itself
- And virtualization platforms that enable customers to freely create, run, and manage virtual machines with their choice of OSs and applications
- On other end of spectrum, SaaS provides least control
- Service provider offers complete software product for customer to use

## Cloud Deployment Models

### Four Deployment Models

- When you think of "the cloud," cloud service providers like AWS probably come to mind
- However, NIST defines four distinct cloud deployment models, encompassing variety of cloud environments:
  - Public cloud
  - Private cloud
  - Community cloud
  - Hybrid cloud
- AWS, Azure, GCP, and similar services fit into public cloud deployment model—most common of four
- But understanding all four deployment models is essential

### Public Cloud

- In public cloud deployment, infrastructure, which is located on cloud provider's premises
- Is available for open use by public (for fee, of course)
- Anyone who wants to use cloud resources is free to become customer
- This is by far most common deployment and is used by individuals and organizations of all sizes
- Customers of all sizes can connect to and use public cloud resources

### Private Cloud

- In private cloud deployment, cloud infrastructure is provided for use by single organization
- Typically very large organization (i.e., government or large business)
- Cloud resources can be used by different consumers within that organization (i.e., different departments of business)
- But are not available for use by those outside of specific organization
- Although cloud is private—reserved for use by single organization—it may be owned by third party
- Example: AWS provides private cloud services for US Department of Defense (DoD)
- DoD connecting to private cloud provided by AWS, separate from AWS public cloud

### Community Cloud

- Community cloud is collaborative effort where cloud infrastructure is reserved for use by consumers in multiple organizations
- This provides balance between shared model of public cloud and dedicated resources of private cloud
- Infrastructure itself can be managed by one or more of organizations or third-party provider
- And can exist on or off premises of any of member organizations

### Hybrid Cloud

- Final deployment model is hybrid cloud
- Which is any combination of two or more of previous models
- Example use case for hybrid cloud is private cloud that can offload work to public cloud when necessary
- When private cloud does not have sufficient resources

## Cloud Benefits

### Cost Efficiency

- Upfront capital expenditures for hardware, software, and data centers are significantly reduced or even eliminated

### Global Scaling

- Cloud services can scale globally at rapid pace
- Services can be set up and offered to customers from geographic location close to them, reducing latency

### Speed and Agility

- Services are provided on demand, and vast amounts of resources can be provisioned within minutes if needed

### Productivity

- By outsourcing physical infrastructure concerns, cloud services reduce need for labor-intensive tasks associated with hardware setup and other routine IT management chores

### Reliability

- Backing up systems in cloud is simple, and data can be mirrored at multiple sites in diverse geographic locations to support disaster recovery (i.e., if natural disaster affects one site)

### Cloud Considerations

- Despite these advantages, moving infrastructure to cloud is not always correct answer
- If you follow tech-related news, you will occasionally see stories about companies that gained huge savings by moving their infrastructure out of cloud
- Returning to on-prem/colocation setups
- Each organization should carefully consider whether moving its infrastructure to cloud will deliver net benefit
- Many organizations use combination of all three

## Real-World Applications

- **Server consolidation**: Reducing number of physical servers through virtualization
- **Application deployment**: Rapidly deploying applications using containers
- **Network segmentation**: Using VRF to isolate customer networks
- **Cloud migration**: Moving workloads to cloud for scalability and cost savings
- **Hybrid infrastructure**: Combining on-prem, colocation, and cloud resources

## Troubleshooting

### Common Issues

- **VM performance**: Check resource allocation and host server utilization
- **Container connectivity**: Verify network configuration and container networking
- **VRF routing**: Verify VRF assignment and routing table configuration
- **Cloud connectivity**: Check network connections and VPN tunnels

### Troubleshooting Steps

1. Verify virtualization platform: Check hypervisor or container engine status
2. Check resource allocation: Verify CPU, RAM, and storage allocation
3. Test network connectivity: Verify VM/container network configuration
4. Review VRF configuration: Verify interface assignments and routing tables
5. Test cloud connectivity: Verify VPN tunnels and network connections

## Best Practices

- Choose appropriate virtualization technology based on requirements
- Monitor resource utilization and performance
- Implement proper network segmentation with VLANs and VRFs
- Plan for scalability and growth
- Document virtualization and cloud architecture
- Test disaster recovery and backup procedures
- Consider cost vs. performance tradeoffs
- Implement security best practices for virtualized environments

## Summary

- VLANs and VPNs are forms of network virtualization
- VLANs segment physical LAN into separate logical LANs
- Whereas VPNs create secure, private network connections over shared or public networks like internet
- Virtual machines (VMs) and containers are also examples of virtualization
- Allowing operating systems and applications to run in isolated environments on server
- Before virtualization, physical server would run single operating system (OS)
- This meant that all of hardware resources were tied to that one OS and its applications
- This often led to resource underutilization
- Virtual machines (VMs) break one-to-one relationship of hardware to OS
- Allowing multiple OSs to run on single physical server
- VMs are facilitated by hypervisor that sits between hardware and VMs
- Managing and allocating hardware resources to each VM
- Another name for hypervisor is virtual machine monitor (VMM)
- Type 1 hypervisor is installed directly on underlying physical hardware
- Other names for this are bare-metal or native hypervisor
- Type 1 hypervisors are most often used for server virtualization in data center environments (including cloud)
- By interacting directly with physical hardware, they provide very efficient use of those resources
- Type 2 hypervisor runs as program on OS, like regular computer application
- OS running directly on hardware is called host OS
- And OS running in VM is called guest OS
- Type 2 hypervisors use hardware resources less efficiently than type 1 hypervisors
- But their advantage lies in their ease of setup and use
- They are more common on personal-use devices for software development, testing, and educational purposes
- Each VM operates as independent host on network
- Instead of physical network interface card (NIC), it has virtual NIC (vNIC)
- To manage network traffic to and from VMs, hypervisor uses virtual switch
- Which forwards frames between vNICs of VMs and physical NICs of host machine
- Just like physical switch, virtual switch's ports can operate in access or trunk mode
- Enabling use of VLANs to segment VMs
- While VMs offer full hardware virtualization, providing complete OSs for their applications
- Containers provide more agile approach
- Container is lightweight, stand-alone package that includes everything needed to run particular application
- Containers are more lightweight than VMs, requiring less overhead
- Instead of running independent OS, container only contains application and its dependencies
- Containers do not run independent OSs
- Containers run on container engine such as Docker Engine
- Container engine runs on host OS (usually Linux)
- Container orchestrator (such as Kubernetes) is typically used to automate deployment, management, and scaling of containers
- Virtual Routing and Forwarding (VRF) segments router into multiple virtual routers
- Service providers often use VRF to allow customer's traffic to travel over shared infrastructure while remaining isolated from other customers
- Each VRF virtual router is called VRF instance or simply VRF
- Each VRF is isolated from other VRFs
- Traffic in one VRF cannot be forwarded out of interface that belongs to another VRF
- VRF is often used to enable MPLS L3VPNs
- VRF without MPLS is called VRF-lite
- Use `ip vrf vrf-name` to create VRF and `show ip vrf` to view existing VRFs
- Use `ip vrf forwarding vrf-name` in interface config mode to assign interface to particular VRF
- Router builds separate routing table for each VRF
- Use `show ip route vrf vrf-name` to view routing table of specified VRF
- Before cloud, traditional IT infrastructure was typically combination of on-premises and colocation setups
- On-premises (on-prem) means company's infrastructure (servers and key network devices) are located within its own facilities, offering complete control
- All equipment is purchased by company using it, and company is responsible for necessary space, power, cooling, and physical security
- Colocation services allow business to rent space in third-party data centers to house its infrastructure
- Cloud computing is third approach that provides on-demand access to shared computing resources over network (such as internet)
- Five essential characteristics of cloud computing are:
  - On-demand self-service: Customer is able to use (or stop using) service as needed without direct human-to-human interaction
  - Broad network access: Services should be made available over standard network connections and accessible by many kinds of devices
  - Resource pooling: Shared pool of resources is provided to serve multiple customers. Resources are dynamically allocated as needed
  - Rapid elasticity: Customers can quickly scale their cloud resources up or down as needed
  - Measured service: Cloud service provider measures customer use of cloud resources and typically charges based on usage
- Three main cloud service models are Software as a Service (SaaS), Platform as a Service (PaaS), and Infrastructure as a Service (IaaS)
- SaaS delivers applications as service over network (typically internet)
- Instead of installing applications on their own devices, users simply access them over internet
- Popular examples are Microsoft 365 and Google Workspace
- PaaS provides platform for customers to develop, run, and manage applications without complexity of building and maintaining necessary infrastructure
- IaaS offers essential computing resources, storage, and networking capabilities on demand
- Customers can create VMs, install OSs, run applications, etc., on provider's infrastructure
- Four cloud deployment models are public, private, community, and hybrid
- In public cloud deployment, infrastructure, which is located on cloud provider's premises, is available for use by public
- Popular examples are Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP)
- In private cloud deployment, cloud infrastructure is provided for use by single organization
- Cloud infrastructure may be owned by third party and may be on or off premises of organization that uses cloud
- Community cloud is collaborative effort where cloud infrastructure is reserved for use by consumers in multiple organizations
- Infrastructure can be managed by one or more of member organizations or third party and can exist on or off premises of any of member organizations
- Hybrid cloud is combination of two or more of other deployment models (for example, private cloud that can offload work to public cloud when necessary)
