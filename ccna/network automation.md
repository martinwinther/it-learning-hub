# Network Automation

## Overview

Enterprise networks can potentially have hundreds, or even thousands, of routers, switches, firewalls, and other network infrastructure devices. In the past, deploying, managing, and maintaining such large networks was very labor intensive, requiring manual configuration of each individual device. However, modern enterprises are increasingly adopting automation to streamline the deployment, management, and maintenance of their networks. Network automation involves the use of software to create processes that perform various network tasks without the need for manual intervention, ranging from simple scripts for routine tasks to more complex automation platforms that manage multiple interdependent configurations across a variety of devices.

## Network Automation Fundamentals

### What is Network Automation?

- Network automation is a broad category of techniques and methods used to automate network-related tasks
- It doesn't refer to any particular tool or technology but rather encompasses various approaches to automating network operations
- At its core, network automation involves using software to create processes that perform network tasks without manual intervention
- Can range from simple scripts for routine tasks to complex automation platforms managing multiple interdependent configurations

### Benefits of Network Automation

- **Efficiency**: Automation can perform configuration changes on large numbers of devices in a fraction of the time required for manual configuration
- **Accuracy**: Automated processes reduce human error, ensuring configuration changes are made accurately without typos or mistakes
- **Scalability**: Automation enables networks to scale to meet the needs of modern organizations without proportionally increasing operational overhead
- **Cost Reduction**: By improving efficiency, automation reduces operating expenses (opex) as fewer hours are required for each task
- **Consistency**: Ensures that configuration changes are made consistently across all devices

### Example: Python Script for Configuration

- Consider a scenario where you need to add Syslog and SNMP configurations to hundreds of devices
- Manual approach would require connecting to each device individually via SSH and making configurations one by one
- With automation, a Python script can reliably push configurations to all devices quickly
- Example using Netmiko library to log in to devices and apply commands:
  - Script connects to each device in a list
  - Applies specified configuration commands
  - Saves the configuration
  - Handles errors gracefully
- As long as the script is properly written, it can quickly and reliably make specified configuration changes with no typos or mistakes

## Three Logical Planes of Networking

### Overview of Network Planes

- Network devices perform a variety of functions beyond just forwarding messages
- These functions can be divided into three logical planes:
  - **Data Plane**: Functions responsible for actual forwarding of packets
  - **Control Plane**: Functions that control how the Data Plane operates
  - **Management Plane**: Functions related to configuring, managing, and monitoring devices

### Data Plane

- Includes all functions directly related to forwarding messages over the network
- Involves receiving a message on one interface, performing necessary processing, and forwarding it out of another interface
- On a switch, Data Plane functions include:
  - Forwarding and flooding frames according to destination MAC address and MAC address table
  - Permitting or denying frames according to security features like Port Security, DHCP Snooping, or DAI
  - Tagging frames with 802.1Q before forwarding them over trunk links
- On a router, Data Plane functions include:
  - Forwarding packets according to routing table
  - Encapsulating packets in frames for transmission
  - Performing any necessary packet modifications
- Data Plane functions according to predetermined rules or instructions
- A router's routing table can be thought of as a set of instructions: to forward a packet toward destination X, encapsulate it in a frame destined for next hop Y, and forward it out of interface Z

### Control Plane

- Controls the Data Plane by establishing rules and instructions that the Data Plane follows
- Functions in the Control Plane are not directly involved in forwarding messages but perform necessary overhead work to enable Data Plane operations
- Examples of Control Plane functions:
  - **OSPF**: Not directly involved in forwarding packets, but allows router to build routing table necessary for forwarding
  - **STP**: Not directly involved in forwarding frames, but informs switch about which ports should and shouldn't be used
  - **ARP**: Messages don't contain user data but are used to build ARP table, which is used in forwarding data packets
  - **MAC Address Learning**: Switch's process of examining frames' source MAC addresses is separate from forwarding but necessary to build MAC address table
- Control Plane functions influence but aren't directly involved in the message-forwarding process
- Whereas Data Plane is the "brawn" (processes that move messages), Control Plane is the "brains" (processes that determine how messages should be moved)

### Management Plane

- Includes functions related to configuring, managing, and monitoring network devices
- Functions don't directly influence forwarding of messages
- Some protocols whose functions are part of Management Plane:
  - **SSH/Telnet**: Used to connect to CLI of network devices
  - **Syslog**: Used to keep logs of events that occur on a device
  - **SNMP**: Used to monitor operations of a device
  - **NTP**: Used to maintain accurate time across the network
- Although Management Plane functions don't directly influence forwarding, actions performed in Management Plane can influence Control Plane, thereby having indirect effect on Data Plane
- Example: OSPF configurations made via CLI (Management Plane) affect how router shares routing information (Control Plane), influencing how router forwards packets (Data Plane)

## Software-Defined Networking (SDN)

### Traditional Network Architecture

- In traditional network architectures, each individual network device contains necessary intelligence for Control Plane functions
- Each router runs a routing protocol (such as OSPF), communicates with neighboring routers, and independently calculates best route to each destination
- This is called a **distributed Control Plane**—the "brains" of the network are distributed among each individual network device
- Each device operates independently with its own Control Plane intelligence

### SDN Architecture

- SDN takes a different approach, centralizing some or all Control Plane functions in a **controller**
- This is called a **centralized Control Plane**
- Instead of routers communicating with each other using OSPF and independently calculating routes, the controller performs these tasks centrally
- Controller has global view of the network, applies its own routing logic, and distributes necessary forwarding instructions to each device
- Each network device's role is simply to forward messages according to controller's instructions
- Although Control Plane is centralized, Data Plane remains distributed among network devices

### SDN Layers

- SDN architecture consists of three layers:
  - **Application Layer**: Consists of applications that communicate network requirements and desired behaviors to the SDN controller
  - **Control Layer**: Translates high-level requirements from Application Layer into actionable instructions for network devices
  - **Infrastructure Layer**: Network devices like routers and switches that execute commands received from Control Layer

### SDN Interfaces

- Communication between the three layers is achieved using **application programming interfaces (APIs)** and various communication protocols
- **Northbound Interface (NBI)**: Interface between Application and Control Layers
  - Typically uses **representational state transfer (REST) API** with HTTP messages
  - Named "northbound" because Application Layer is depicted on top (north) in SDN architecture diagrams
- **Southbound Interface (SBI)**: Interface between Control and Infrastructure Layers
  - Named "southbound" because Infrastructure Layer is depicted at bottom (south) in diagrams
  - Various APIs and communication protocols can be used:
    - **OpenFlow**: Open source protocol that allows controller to directly interact with and control Data Plane of network devices
    - **NETCONF**: Industry-standard protocol defined by IETF, used for modifying configurations of network devices
    - **OpFlex**: Developed by Cisco, used with Application-Centric Infrastructure (ACI)
    - **SSH, SNMP**: Traditional protocols can also be used in SBI to manage network devices

### SDN Solutions

- SDN isn't one single solution; various vendors have developed different SDN solutions
- Three Cisco SDN solutions:
  - **Cisco Software-Defined Access (SD-Access)**: SDN solution for wired and wireless campus LANs
  - **Cisco SD-WAN**: SDN solution for WANs
  - **Application Centric Infrastructure (ACI)**: SDN solution for data center networks
- All three solutions work by building virtual network of tunnels (the **overlay**) on top of underlying physical network (the **underlay**)
- Combination of underlay and overlay—the network infrastructure as a whole—is called the **fabric**
- Remember: underlay is physical, overlay is virtual, fabric is the network as a whole

### SD-Access

- Cisco's SDN solution for automating and securing wired and wireless campus LANs
- SD-Access fabric consists of physical network (underlay) and virtual network of tunnels (overlay) using **Virtual Extensible LAN (VXLAN)**
- VXLAN is a protocol that allows creation of virtual Layer 2 networks over a Layer 3 underlay
- **Cisco Catalyst Center** (formerly called Digital Network Architecture (DNA) Center) functions as the SDN controller
- Catalyst Center can also be used in non-SD-Access networks as a network management platform

### SD-WAN

- Cisco's SDN solution for WANs
- Creates overlay of IPsec tunnels over any physical WAN underlay: internet, MPLS, cellular 4G/5G, satellite, etc.
- Fabric is managed by a few different SDN controllers:
  - One dedicated to onboarding new routers into fabric
  - One dedicated to Control Plane functions
  - One dedicated to Management Plane functions

### Application-Centric Infrastructure (ACI)

- Cisco's data center SDN solution
- Creates overlay of VXLAN tunnels over underlay, which is a physical spine-leaf network
- **Application Policy Infrastructure Controller (APIC)** is the SDN controller used in ACI
- APIC is responsible for translating high-level network policies into specific network configurations and deploying them across network fabric

### Intent-Based Networking (IBN)

- One advantage of SDN is that it facilitates **intent-based networking (IBN)**
- Goal of IBN is to allow engineer to communicate their intent for network behavior to controller, which takes care of details of actual configurations and policies
- Instead of focusing on individual devices and CLI configurations, IBN allows focus on high-level policies
- Example: Engineer states intent "I want to prioritize video conferencing traffic over other types"
- Controller then implements necessary configurations across network to make this reality, without engineer having to configure QoS settings on each device

## Artificial Intelligence and Machine Learning

### Artificial Intelligence Overview

- **Artificial intelligence (AI)** refers to simulation of intelligence in computers, allowing them to exhibit behaviors typically associated with humans such as learning and problem-solving
- AI systems are programmed to analyze data, identify patterns, and make predictions or take actions based on those insights
- **Machine learning (ML)** is a field within AI that allows computers to learn on their own, without requiring explicit programming
- ML is a subfield of AI, and deep learning is a further subset of machine learning using artificial neural networks

### Machine Learning Types

- With ML, computers can learn from vast data sets in different ways:
  - **Supervised learning**: ML algorithm is trained on labeled data sets, meaning each training example has corresponding label
    - Algorithm learns relationships between data and given label
    - Example: Training algorithm to recognize cats and dogs by inputting thousands of labeled photos
  - **Unsupervised learning**: ML algorithm is trained on unlabeled data sets
    - Algorithm tries to learn underlying structure of data by identifying patterns without predefined labels
    - Groups data into clusters based on patterns, but doesn't assign labels (requires human interpretation)
  - **Reinforcement learning**: ML algorithm learns by interacting with environment and receiving positive or negative feedback
    - Example: Training AI to play chess by playing many games, receiving feedback for winning/losing
- **Semi-supervised learning**: Middle ground between supervised and unsupervised learning, involving combination of labeled and unlabeled data

### Deep Learning

- **Deep learning (DL)** is a subset of machine learning that uses **artificial neural networks** to analyze and learn from large amounts of data
- Artificial neural network is computational model inspired by biological neural networks in human brain
- Consists of many interconnected layers of nodes like neurons in human brain
- Can be trained using supervised, unsupervised, semi-supervised, and reinforcement learning
- Complex architecture allows extraction of more complex patterns and relationships from data than traditional ML algorithms
- Has gained prominence due to success in complex tasks such as image and speech recognition, natural language processing, and autonomous driving
- Has led to significant advancements in AI-driven technologies, such as large language models (LLMs) like OpenAI's GPT-4, Google's Gemini, and Meta's Llama

### Predictive AI

- **Predictive AI** uses historical data to predict future events
- Uses ML and DL to identify patterns and relationships within data sets
- Leverages these insights to make predictions about unseen data
- Common use cases:
  - **Weather forecasting**: Predicting future weather patterns
  - **Stock market predictions**: Using historical data and economic indicators to predict stock prices and market trends
  - **Customer behavior analysis**: E-commerce platforms analyze purchase history and browsing behavior for personalized recommendations
  - **Healthcare**: Analyzing patient data to predict outcomes and personalize treatment plans

### Generative AI

- **Generative AI** leverages ML and DL to create new content
- After learning underlying patterns and relationships within existing data, AI can produce novel outputs that resemble training data
- Well-known use cases:
  - **Text generation**: Chatbots like OpenAI's ChatGPT and Google's Gemini use large language models (LLMs) to generate human-like text
  - **Image generation**: Tools like Midjourney and OpenAI's DALL-E create detailed images from text descriptions

## AI in Network Operations

### Predictive AI Applications

- ML and DL can analyze vast amounts of network data to uncover patterns, anomalies, and insights
- Predictive AI applications in network operations:
  - **Traffic forecasting**: AI models analyze network traffic patterns to predict future network load, enabling proactive resource provisioning or QoS policy optimization
  - **Predictive maintenance**: By analyzing data from network devices, AI models can identify potential hardware failures before they occur, enabling proactive maintenance scheduling
  - **Capacity planning**: Predictive AI helps plan for future network capacity by analyzing trends in traffic and user behavior
  - **Security threat prediction**: By analyzing historical security data and identifying patterns associated with cyber attacks, predictive AI can forecast potential security threats

### Generative AI Applications

- In current state, generative AI has fewer use cases in networking than predictive AI
- However, combined with human oversight, generative AI can greatly improve network operations:
  - **Automated script creation**: Generative AI can generate scripts or templates for network automation tasks
  - **Network diagram generation**: AI tools can gather information about network and automatically generate network diagrams
  - **Network documentation**: AI can analyze information about network to generate documentation about configurations, policies, etc.
  - **Device configuration**: AI can generate device configurations based on given requirements, reducing manual effort
  - **Network design**: Generative AI can assist in creating optimal network designs according to given requirements
  - **Virtual assistant**: Chatbots can function as virtual assistants, providing real-time answers to queries (though you should always verify chatbot responses)

### Cisco Catalyst Center AI Features

- Cisco Catalyst Center includes several AI features:
  - **AI endpoint analytics**: Uses deep packet inspection and other techniques to identify endpoint devices when they access network, then classifies endpoints and assigns policies based on classification
  - **AI enhanced radio resource management (RRM)**: By analyzing past radio frequency (RF) data, Catalyst Center can predict future network conditions and recommend optimal configurations for wireless LANs
  - **Machine reasoning (MR) engine**: Automates network troubleshooting by using AI to perform root cause analysis when network issues arise, and can take corrective actions to potentially resolve problems without manual intervention

## Summary

- Network automation is a broad category of techniques and methods used to automate network-related tasks, ranging from simple scripts for routine tasks to more complex automation platforms
- For example, a Python script can be used to reliably perform configuration changes on large numbers of devices in a fraction of the time required for manual configuration
- Traditional network devices perform a variety of functions on top of forwarding messages, such as building routing/ARP/MAC address tables, using Syslog to log events, and using SSH to accept remote CLI connections
- The various functions can be divided into three logical planes: the Data Plane, the Control Plane, and the Management Plane
- The Data Plane includes all functions directly related to forwarding messages over the network: receiving a message on one interface, performing any necessary processing, and then forwarding it out of another interface
- The Control Plane controls the Data Plane. Functions in the Control Plane are not directly involved in the process of forwarding messages but instead perform necessary overhead work to enable the Data Plane's operations
- The Management Plane includes a variety of functions that don't directly influence the forwarding of messages—functions related to configuring, managing, and monitoring network devices
- Traditional network architectures use a distributed Control Plane—the "brains" of the network (the Control Plane) are distributed among each network device. For example, each router uses OSPF to learn routes and build a routing table
- SDN takes a different approach, centralizing some or all of the Control Plane functions in a controller. This is called a centralized Control Plane
- In SDN architecture, each network device's role is simply to forward messages according to the controller's instructions. Although the Control Plane is centralized, the Data Plane remains distributed among the network devices
- SDN facilitates the programmatic control of the network through applications that interact with the SDN controller, resulting in a three-layer architecture consisting of the Application, Control, and Infrastructure Layers
- The Application Layer consists of applications that communicate network requirements and desired behaviors to the SDN controller
- The Control Layer translates high-level requirements from the Application Layer into actionable instructions for the network devices
- The Infrastructure Layer consists of network devices like routers and switches that execute the commands received from the Control Layer
- Communication between the three layers is achieved using application programming interfaces (APIs) and various communication protocols
- The interface between the Application and Control Layers is the northbound interface (NBI). It typically uses a representational state transfer (REST) API with HTTP messages
- The interface between the Control and Infrastructure Layers is the southbound interface (SBI). A variety of APIs and communication protocols can be used in the SBI, such as OpenFlow, NETCONF, OpFlex, and traditional protocols like SSH and SNMP
- SDN isn't a single solution. Cisco's SDN solutions include SD-Access for wired and wireless campus LANs, SD-WAN for WAN networks, and Application Centric Infrastructure (ACI) for data center networks
- These SDN solutions work by building a virtual network of tunnels (the overlay) on top of the underlying physical network (the underlay). The combination of virtual and physical networks is called the fabric
- Software-Defined Access (SD-Access) is Cisco's SDN solution for campus LANs. The SD-Access fabric consists of a physical underlay of switches and a virtual overlay of tunnels using Virtual Extensible LAN (VXLAN)
- Cisco Catalyst Center, formerly called Digital Network Architecture (DNA) Center, functions as the SDN controller in SD-Access
- Software-Defined WAN (SD-WAN) is Cisco's SDN solution for WANs. SD-WAN creates an overlay of IPsec tunnels over any physical WAN underlay: the internet, MPLS, cellular 4G/5G, satellite, etc.
- Application-Centric Infrastructure (ACI) is Cisco's data center SDN solution. Like SD-Access, ACI creates an overlay of VXLAN tunnels over the underlay, which is a physical spine-leaf network
- The SDN controller used in ACI is called the Application Policy Infrastructure Controller (APIC)
- Artificial intelligence (AI) refers to the simulation of intelligence in computers, allowing them to analyze data, identify patterns, and make predictions or take actions based on those insights
- Machine learning (ML) is a field within AI that allows computers to learn on their own, without requiring explicit programming
- With ML, computers can learn from vast data sets in a few different ways:
  - Supervised learning: The ML algorithm is trained on labeled data sets
  - Unsupervised learning: The ML algorithm is trained on unlabeled data sets
  - Reinforcement learning: The ML algorithm learns by interacting with an environment and receiving positive or negative feedback
- Semi-supervised learning is a middle ground between supervised and unsupervised learning that involves a combination of labeled and unlabeled data
- Deep learning (DL) is a subset of machine learning that uses artificial neural networks to analyze and learn from large amounts of data. These neural networks can extract more complex patterns and relationships from data than traditional ML algorithms
- Predictive and generative AI are two important applications of ML and DL
- Predictive AI uses historical data to predict future events, such as weather forecasts and stock market predictions
- Generative AI leverages ML and DL to create new content, such as text and image generation
- ML and DL can be used to analyze vast amounts of network data to uncover patterns, anomalies, and insights
- Predictive AI has applications in network operations such as traffic forecasting, predictive maintenance, capacity planning, and security threat prediction
- Generative AI has applications in network operations such as automated script creation, network diagram generation, network documentation, device configuration, network design, and virtual assistants
