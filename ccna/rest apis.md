
# REST APIs

## Overview

REST APIs provide a standard way for software applications to exchange data over HTTP. For CCNA, the focus is on understanding what an API is, how HTTP requests and responses work, and the basic properties of REST, including stateless behavior and common authentication methods.

## Application programming interfaces

- An application programming interface (API) is a software interface that exposes data and functions in a consistent way.
- APIs let applications communicate without needing to understand each other's internal code.
- Instead of building custom integrations between every pair of applications, each application exposes a well defined API and other applications call that API.
- APIs can be local or remote. In network automation most APIs are reached over the network using HTTP.

## HTTP basics for REST

### Client server model

- HTTP uses a client server model.
- Clients send HTTP requests to servers.
- Servers process the request and send back HTTP responses.
- Each request targets a resource identified by a Uniform Resource Identifier (URI).

### CRUD operations

- Typical actions on resources fit into four categories:
  - Create
  - Read
  - Update
  - Delete
- These four actions are often called CRUD operations.
- CRUD is a general data concept and is not specific to HTTP.

### HTTP request format

An HTTP request has three main parts:

- Start line with:
  - HTTP method
  - URI of the resource
  - HTTP version
- Optional headers with extra information such as authentication or content type.
- Optional body that carries data for some methods.

The method is important because it tells the server which CRUD style action is requested.

### HTTP methods and CRUD mapping

Common HTTP methods and typical CRUD mappings:

- `POST`  
  Often used to create a new resource on the server.

- `GET`  
  Reads a resource from the server. A browser uses GET to retrieve a web page.

- `PUT`  
  Replaces a resource. Often used to update a resource and can sometimes create one.

- `PATCH`  
  Modifies part of a resource.

- `DELETE`  
  Deletes the specified resource.

Exact behavior is defined by the API documentation. The mapping to CRUD is a guideline rather than a strict rule.

### HTTP response format

An HTTP response mirrors the structure of a request:

- Start line with HTTP version, numeric status code, and short reason phrase.
- Optional headers such as `Content-Type`.
- Optional body that carries the returned data. For REST APIs this is often JSON.

### HTTP response codes

Response codes are grouped by the first digit:

- 1xx informational  
  Request received and being processed.

- 2xx successful  
  Request understood and processed successfully.  
  Common codes:
  - `200 OK`
  - `201 Created`

- 3xx redirection  
  Client needs to take additional steps such as following a new location.  
  Example: `301 Moved Permanently`.

- 4xx client error  
  Problem with the request.  
  Examples:
  - `400 Bad Request`
  - `403 Forbidden`
  - `404 Not Found`

- 5xx server error  
  Request seemed valid but the server failed to process it.  
  Example: `500 Internal Server Error`.

## REST architecture

### REST definition

- Representational State Transfer (REST) is an architectural style used by many web and API systems.
- APIs that follow REST principles are called REST APIs or RESTful APIs.
- Most REST APIs use HTTP as the transport protocol.

### Key REST constraints for CCNA

REST is defined by several constraints. For CCNA, focus on these:

- Uniform interface  
  All requests follow a consistent style for resources, methods, and representations.

- Client server  
  Client and server are separate roles. Each can evolve independently as long as the API interface remains stable.

- Stateless  
  Each request from client to server is independent of previous requests. The server does not need to remember earlier interactions to process a new request.

- Cacheable or not cacheable  
  Responses indicate whether they can be cached. Cacheable responses may be stored and reused to avoid repeated work. Sensitive or frequently changing data is usually marked as not cacheable.

- Layered system  
  Clients may not know whether they are talking directly to the origin server or to an intermediate such as a proxy. This enables scalable, layered designs.

Code on demand is another REST constraint but is optional and not a focus at CCNA level.

### Stateless behavior and authentication

- Because REST exchanges are stateless, the server does not keep session state about previous client requests.
- Any required context, such as authentication data, must be included in each request.
- This often takes the form of credentials or tokens in HTTP headers.

## REST API authentication

REST APIs often require authentication before granting access to resources. Several common methods appear in documentation and exam material.

### Basic authentication

- Username and password are sent in the HTTP header using a standard encoding.
- Simple to implement but not very secure on its own.
- Must be used with HTTPS so that credentials are encrypted in transit.
- If credentials are captured, an attacker can reuse them until they are changed.

### Bearer tokens

- Client first obtains an access token from an authorization service.
- Later API calls include the token in an HTTP header, often `Authorization: Bearer <token>`.
- Token is usually valid for a limited time and can be revoked.
- More secure than sending the same username and password with every request.
- Still requires HTTPS to protect the token on the wire.

### API keys

- Server issues a unique key to each client application.
- Client sends the key on each request, often in a header or query string.
- Identifies the application rather than an individual user.
- Keys often do not expire automatically, so key management is important.
- Should also be protected with HTTPS.

### OAuth 2.0

- Open standard framework that allows access delegation.
- A client application can access resources on behalf of a user without learning the user's password.
- Typical flow:
  1. Client redirects the user to an authorization server login page.
  2. User authenticates and approves the requested access.
  3. Authorization server returns an authorization grant to the client.
  4. Client exchanges the grant for an access token.
  5. Client uses the access token to call the resource server's API.
- Access token has a defined scope that limits what the client can do.
- Tokens are usually short lived. A refresh token may be used to obtain new access tokens without asking the user to log in again.

## Example REST workflow

A common pattern for network APIs:

1. Client sends a `POST` request with credentials to an authentication endpoint.  
   - Response contains an access token if credentials are valid.
2. Client stores the token temporarily.
3. Client sends `GET`, `POST`, `PUT`, `PATCH`, or `DELETE` requests to other API endpoints.  
   - Each request includes the token in an HTTP header.
4. When the token expires, the client obtains a new one and repeats the process.

In practice, tools such as Postman or curl are often used during testing. Automation scripts later perform the same sequence programmatically.

## Quick review

- APIs expose application data and functions in a consistent way so that other software can access them.  
- REST APIs most often use HTTP and the client server model. Each request targets a resource identified by a URI.  
- HTTP methods such as GET, POST, PUT, PATCH, and DELETE are typically mapped to CRUD style actions on resources.  
- HTTP responses use status codes that indicate success or failure, grouped into 1xx to 5xx categories.  
- REST constraints to remember are client server, stateless behavior, cacheable or not cacheable responses, uniform interface, and layered system.  
- Stateless behavior means the server does not track per client session state and any needed context must be sent with each request.  
- Common REST authentication methods are basic authentication, bearer tokens, API keys, and OAuth 2.0 access delegation.  
- Many network APIs use a token based pattern: authenticate once, receive a token, then include that token in subsequent API calls over HTTPS.
