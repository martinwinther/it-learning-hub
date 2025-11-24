# REST APIs

## Overview

Programming and automating networks require seamless communication between software running on various devices—from network equipment like routers and switches to servers, controllers in an SDN architecture, and the network administrator or engineer's own PC. There are two essential elements that facilitate communication between these software applications: an interface that opens up each application's data to external applications and standard data formats for exchanging information efficiently. In this chapter, we'll cover the first piece of the puzzle: application programming interfaces (APIs). APIs are software interfaces that enable two or more software applications to communicate with each other. Specifically, we will examine representational state transfer (REST) APIs, which are commonly used in network automation contexts, such as the northbound interface (NBI) of an SDN controller.

## Application Programming Interfaces (APIs)

### What are APIs?

- **Application programming interfaces (APIs)** are software interfaces that open up an application's data in a way that allows other applications to access it in a uniform manner
- APIs facilitate communications between applications, whether they're running on the same system or remote systems
- Without APIs, achieving communication between applications often requires building custom integrations between each pair of applications—a time-consuming and expensive process
- Custom integrations result in a tangled web of point-to-point connections between applications
- A custom integration between app A and app B wouldn't help either communicate with app C

### How APIs Work

- An API provides a uniform interface for external apps to access an application's internal data
- Apps don't need to know the intricate details of another app's inner workings
- They can simply make an **API call** (request) to the app's API
- The API interprets and fulfills the request, returning the relevant information in a response
- APIs simplify and standardize the way applications communicate, making an otherwise complex and costly process manageable and scalable

### API Communication Over Networks

- For applications on different machines to communicate over a network, a suitable communication protocol is required
- For most REST APIs, **HTTP** is the protocol of choice
- HTTP is a natural choice for REST APIs due to its ubiquity on the web and its alignment with REST's architectural principles
- An API call takes the form of an HTTP request, receiving a response in the form of an HTTP response
- The HTTP request includes an HTTP method and a URI, and the response includes a response code and the relevant data

## HTTP Requests and Responses

### HTTP Client-Server Architecture

- HTTP uses a client-server architecture in which clients send requests and servers send responses
- In an HTTP request, the client specifies the **Uniform Resource Identifier (URI)** of the resource it wants to access
- But specifying the resource's URI isn't enough for the server to take action
- The client needs to tell the server exactly what action it wants the server to take on the specified resource

### CRUD Operations

- Consider what kinds of actions can be taken on a resource:
  - **Create**: Create a new resource on the server (e.g., create variable "ip_address" and set value to 10.1.1.1)
  - **Read**: Retrieve a resource from the server (e.g., what is the value of variable "ip_address"?)
  - **Update**: Modify an existing resource on the server (e.g., change value of variable "ip_address" to 10.2.3.4)
  - **Delete**: Delete a resource from the server (e.g., delete variable "ip_address")
- These four types of actions are called **CRUD (Create-Read-Update-Delete) operations**
- CRUD isn't an HTTP-specific term but rather a general description of the four basic operations for manipulating and managing data

### HTTP Request Format

- HTTP request message format:
  - Begins with a **start line** containing the method, URI, and HTTP version of the request
  - Optional **headers** that provide additional information
  - A blank line separating the headers from the body
  - Optional **message body** (only present in some request types)
- The HTTP method is key because it is how the client specifies what it wants to do with the resource it is trying to access
- CCNA exam topic 6.5 specifically refers to **HTTP verbs**—another term for HTTP methods (although not all HTTP methods are verbs; some are nouns)

### HTTP Methods

- Common HTTP methods and their equivalent CRUD operations:
  - **POST**: Most often used to create a new resource on the server
  - **GET**: Used to retrieve a resource from the server (read its contents); your PC sends a GET request to retrieve a web page from a web server
  - **PUT**: Used to update a resource by replacing the specified resource
  - **PATCH**: Used to update a resource by modifying it
  - **DELETE**: Used to delete the specified resource
- Although these mappings are generally accepted, they are not 1:1 equivalents, and some can map to different CRUD operations in different situations
- For example, the PUT method can also be used to create resources
- Each API has documentation that specifies exactly how it uses the HTTP methods

### HTTP Response Format

- HTTP response uses a similar format to an HTTP request
- The key element is the **response code**, which indicates the result of the request (i.e., success or failure)
- Response codes can include Content-Type headers indicating the message body format (e.g., application/json for JSON data)

### HTTP Response Codes

- There are five main categories of response codes, indicated by their first digit:
  - **1xx informational**: A provisional response. The initial part of the request has been received, and additional actions may be expected to follow
  - **2xx successful**: The request was received without problems, understood, and processed as expected
  - **3xx redirection**: Additional steps are required to complete the request
  - **4xx client error**: Points to an error on the client's part, either due to incorrect syntax or because the request is infeasible
  - **5xx server error**: Indicates that the server encountered an error and can't perform the request, even though the request appears to be valid
- Each response code consists of a three-digit numeric code and a short name
- Common response codes:
  - **102 Processing**: The server is processing the request, but the response is not yet available
  - **200 OK**: The request succeeded
  - **201 Created**: The request succeeded and a new resource was created
  - **301 Moved Permanently**: The requested resource has been moved
  - **403 Forbidden**: The client is not authorized to access the resource
  - **404 Not Found**: The requested resource was not found
  - **500 Internal Server Error**: The server encountered something unexpected that prevented it from fulfilling the request

## REST Architecture

### What is REST?

- **Representational state transfer (REST)** is a type of software architecture that forms the basis of the World Wide Web
- APIs that conform to REST architecture are called **REST APIs** or **RESTful APIs**
- Most REST APIs are HTTP-based, using the various HTTP methods described in the previous section to interact with resources

### REST Constraints

- REST architecture is defined by six constraints:
  1. Uniform interface
  2. Client-server
  3. Stateless
  4. Cacheable or noncacheable
  5. Layered system
  6. Code on demand (optional)
- For the purpose of the CCNA exam, it's not worth digging into the details of all six constraints, but understanding a few key ones is important

### Client-Server Architecture

- REST APIs employ a client-server architecture
- Clients use API calls (HTTP requests) to access resources on the server, which receives, processes, and responds to those requests
- The strict separation between the client and server applications is essential
- The client and the server must be able to change and evolve independently without breaking the interface between them (the API)

### Stateless Nature

- REST API exchanges are **stateless**, meaning that each API exchange is a separate event, independent of all past exchanges between the client and server
- We've covered stateful and stateless concepts previously:
  - **Stateful**: Stateful firewalls, TCP
  - **Stateless**: Access control lists (ACLs), UDP
- Stateful firewalls and TCP are considered stateful because they remember and keep track of past interactions to make decisions about future interactions
- ACLs and UDP do neither of those things and are therefore stateless; each message is its own event, independent of those before or after it
- In the context of REST APIs, stateless means that the server does not store information about previous requests from the client to determine how it should respond to new requests
- Although REST APIs use HTTP, which employs TCP (stateful) as its Layer 4 protocol, HTTP and REST APIs themselves are stateless
- Don't forget that the functions of each layer of the TCP/IP model are independent!

### Stateless Authentication Implications

- One implication of REST's stateless nature is that if authentication is required, the client must provide authentication credentials in every single request
- This can be done with a simple username/password that is included with each request
- A more robust approach is to require clients to generate an **access token** (also called an **authorization token**)
- We'll examine a few authentication methods in the next section

### Cacheable Resources

- If a resource is **cacheable**, it means that it can be cached—temporarily stored for reuse
- This can significantly improve efficiency; there's no need to retrieve the same resource repeatedly when accessing it multiple times
- For example, frequently accessed web pages can be cached to improve load times
- However, not all resources should be cached; sensitive and frequently updated information should not be cached
- Example: A user's personal dashboard showing a real-time account balance in a banking application is not a good candidate for caching
- Caching the data could lead to outdated information being displayed, and it poses a security risk if the sensitive data is stored inappropriately
- In REST architecture, resources can be cacheable or noncacheable, but they must be marked as such, whether implicitly or explicitly
- Cacheable resources must be marked as cacheable, and noncacheable resources must be marked as noncacheable

## REST API Authentication

### Authentication Overview

- APIs provide access to an application and its data, so security is a major concern when designing and using APIs
- Instead of responding to all requests, the server should properly authenticate and authorize clients
- If the process is successful, the server fulfills the request
- If the process fails (e.g., due to invalid credentials or insufficient permissions), the server refuses the request

### Basic Authentication

- **Basic authentication** is a simple method where a username and password are provided in the HTTP header for authentication
- While simple and convenient to implement, basic authentication is not considered secure because it suffers from the same weaknesses as other simple username/password-based solutions
- If a malicious user obtains the credentials, they can gain access to the API
- If using basic authentication, it's critical to use HTTPS to encrypt the API calls
- If using standard HTTP, the credentials are sent in unencrypted cleartext

### Bearer Authentication

- In **bearer authentication**, the client obtains a token (the "access token" mentioned earlier) that it then provides for authentication in its API calls
- This token can be obtained in various ways; often, the client obtains the token from an authorization server by first going through a separate authentication process, often using a username and password
- Access tokens are typically valid for a limited time, requiring renewal for continued use
- Bearer authentication is generally considered more secure than basic authentication because the client does not have to repeatedly transmit the same username/password
- However, like basic authentication, bearer authentication should only be used with HTTPS to ensure the token is transmitted securely
- Even though the token itself doesn't contain sensitive information like a username/password, it grants access to API resources
- Interception of the token could allow an attacker unauthorized access to the resources
- In some cases, the same server might function as both the authorization server and the resource server in bearer authentication

### API Key Authentication

- **API key authentication** involves the use of a unique identifier assigned to each client application
- The client application includes this key in its API calls, similar to an access token used in bearer authentication
- However, it's important to note that an API key identifies an application, not a user
- For user-based authentication and authorization, access tokens are more appropriate
- Unlike access tokens, which are generally short-lived and expire after a set period of time, API keys typically do not automatically expire (unless revoked by the server)
- This makes them less secure if not managed properly, as they can be used indefinitely if compromised
- API keys are usually easier to implement and use, but they lack the fine-grained control and security features offered by more sophisticated authentication methods
- Once again, if security is a concern, always use HTTPS to encrypt API calls; otherwise, the API key can easily be intercepted in transit

### OAuth 2.0

- **Open Authorization 2.0 (OAuth 2.0)** is an industry-standard framework that is widely used in modern web applications
- OAuth 2.0 provides **access delegation**, allowing third-party applications to access resources (i.e., via a REST API) on behalf of a user without sharing the user's credentials
- You've almost certainly used OAuth 2.0 before
- Common examples:
  - **Logging in with Google**: Many websites and apps offer the option to log in using your Google account instead of creating a new account on the website itself. OAuth 2.0 allows the website or app to access your basic Google profile information without sharing your password with the third-party service
  - **Connecting apps to social media accounts**: When you connect apps to your account on Instagram, Facebook, LinkedIn, or other social media platforms, OAuth 2.0 is used to grant these tools permission to read your social media data or post on your behalf
  - **Calendar integration**: A third-party tool might request access to your Google Calendar to check your availability and schedule meetings. When you authorize this, Google provides an access token to the tool, which allows it to view and manage your calendar without needing your Google account password

### OAuth 2.0 Process

- The basic OAuth 2.0 process:
  1. The client (third-party tool) requests authorization from the resource owner (you) to access the resource (your Google Calendar data)
  2. The resource owner grants the authorization by logging into their account and giving permission
  3. The client exchanges the authorization grant for an access token from the auth server (Google's authorization server)
  4. The auth server provides an access token to the client
  5. The client uses the access token to request the protected resource from the resource server (Google's server)
  6. The resource server validates the access token and provides the requested resource (calendar data) to the client
- The access token granted in step 4 functions just like the access token used in bearer authentication
- The token grants access to the specified resources within the appropriate scope of access and is typically valid only for a limited period, requiring regular renewal
- This could require the user to manually grant authorization again, or the client might receive a **refresh token** from the authorization server that allows it to automatically refresh its access token multiple times within a longer period of time
- The access token granted to the client has a specific **scope** that dictates exactly what resources the client can access and what actions it can perform; this scope is enforced by the resource server
- It's best to be cautious about granting third-party apps access to your accounts beyond what is necessary

## Making REST API Calls

### Example: Cisco Catalyst Center

- We can make API calls to Cisco's always-on Catalyst Center sandbox
- To do so, we'll use **Postman**, a versatile platform for building, testing, and using APIs
- You can access Postman at <https://www.postman.com/>
- Another option is Insomnia, available at <https://insomnia.rest/>

### Generating an Access Token

- Our objective is to retrieve Catalyst Center's inventory list—the list of devices it manages
- First, we need to generate an access token
- Steps to generate an access token:
  1. Specify the POST method and URI: <https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token>
  2. Click Authorization, and select Basic Auth
  3. Enter the username devnetuser and password Cisco123!
  4. Click Send to send the API call to Catalyst Center
  5. Copy the token from the response
- After sending the POST, you should receive a response with code 200 OK and the token itself
- The token is a long string of characters inside of double quotes (JSON-formatted)
- Don't copy the double quotes themselves

### Retrieving Device Inventory

- Steps to retrieve the inventory list:
  1. Specify the GET method and URI: <https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device>
  2. Select Header to add an additional HTTP header to the API call
  3. Add the key X-Auth-Token, and paste the token you generated previously as the value
  4. Click Send to send the API call to Catalyst Center
- The response will include device information including details like MAC address, software version, hostname, and serial number
- This data uses the JSON format

### Summary of API Calls

- We made two API calls to Catalyst Center:
  - A POST request to generate an access token
  - A GET request to retrieve Catalyst Center's inventory list
- For more detailed walkthrough and further resources on Catalyst Center, you can check out guides on Cisco DevNet
- **DevNet** is a program by Cisco to support developers and other IT professionals looking to create applications and integrations using Cisco's suite of products and APIs
- It provides resources such as documentation, courses, learning labs, and sandbox platforms for experimentation
- If you want to dive deeper into network automation, DevNet is an invaluable resource

## Summary

- Application programming interfaces (APIs) are software interfaces that open up an application's data in a way that allows other applications to access it in a uniform manner, facilitating communications between applications
- To access an application's internal data, other applications can simply make an API call (request) to the application's API. The API interprets and fulfills the request, returning the relevant information in a response
- For applications on different machines to communicate over a network, a communication protocol is required. For most REST APIs, HTTP is the protocol of choice
- HTTP uses a client-server architecture in which clients send requests and servers send responses
- The essential actions that can be taken on a resource are called CRUD (Create-Read-Update-Delete) operations
- An HTTP request can include various pieces of information. The two key elements are the HTTP method (also called the HTTP verb), which defines the request's desired action (CRUD operation), and the Uniform Resource Identifier (URI), which indicates the target of the request
- HTTP methods can generally be mapped to one of the four CRUD operations: create (POST), read (GET), update (PUT, PATCH), and delete (DELETE)
- An HTTP response uses a similar format to an HTTP request. The key element is the response code, which indicates the result of the request
- There are five main categories of HTTP responses, indicated by their first digit:
  - 1xx informational
  - 2xx successful
  - 3xx redirection
  - 4xx client error
  - 5xx server error
- Some common response codes are 102 Processing, 200 OK, 201 Created, 301 Moved Permanently, 403 Forbidden, 404 Not Found, and 500 Internal Server Error
- Representational State Transfer (REST) is a type of software architecture that forms the basis of the World Wide Web. APIs that conform to REST architecture are called REST APIs or RESTful APIs
- REST architecture is defined by six constraints:
  - Uniform interface
  - Client-server
  - Stateless
  - Cacheable or noncacheable
  - Layered system
  - Code on demand (optional)
- REST APIs employ a client-server architecture. The client and server applications must be able to change and evolve independently without breaking the interface between them (the API)
- REST API exchanges are stateless, meaning that each API exchange is a separate event, independent of all past exchanges between the client and server
- The server does not store information about previous requests from the client to determine how it should respond to new requests
- If a resource is cacheable, it means that it can be cached—temporarily stored for reuse. This can significantly improve efficiency because there's no need to retrieve the same resource repeatedly when accessing it multiple times
- Frequently updated and sensitive information should not be cached. Caching such data could lead to outdated information being displayed, and it poses a security risk if sensitive data is stored inappropriately
- In REST architecture, resources can be cacheable or noncacheable, but they must be marked as such, whether implicitly or explicitly
- REST APIs can use a variety of methods to authenticate requests. Some common authentication types include basic authentication, bearer authentication, API key authentication, and OAuth 2.0
- Basic authentication uses a username and password (provided in the HTTP header) for authentication. While simple and convenient to implement, it is not considered secure
- In bearer authentication, the client obtains an access token from an authorization server, which it then uses to access the desired resource. The token is typically valid for a limited time, requiring renewal for continued use
- API key authentication involves the use of a unique identifier assigned to each client application. The client application includes this key in its API calls, similar to an access token used in bearer authentication. The API key uniquely identifies an application, not a user
- Unlike access tokens, API keys typically do not automatically expire, making them less secure if not managed properly
- Open Authorization 2.0 (OAuth 2.0) is an industry-standard framework that provides access delegation, allowing third-party applications to access resources (i.e., via a REST API) on behalf of a user without sharing the user's credentials
- The client application requests authorization from the resource owner, receives an authorization grant, and then uses the authorization grant to obtain an access token from the authorization server. It then uses the access token to access the desired resource on the resource server
