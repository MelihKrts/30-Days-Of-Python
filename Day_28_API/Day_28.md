# Day 28 Exercise API

# Table Of Content
- [Day 28 Exercise API](#day-28-exercise-api)
- [Table Of Content](#table-of-content)
- [What is an API](#what-is-an-api)
  - [How do API's Work?](#how-do-apis-work)
    - [Remote Procedure Call (RPC)](#remote-procedure-call-rpc)
    - [Service Object Access Protocol (SOAP)](#service-object-access-protocol-soap)
    - [Representational State Transfer (REST)](#representational-state-transfer-rest)
- [What is HTTP](#what-is-http)
  - [What is an HTTP Method](#what-is-an-http-method)
      - [GET](#get)
      - [POST](#post)
      - [HEAD](#head)
      - [PUT](#put)
      - [DELETE](#delete)
      - [TRACE](#trace)
      - [OPTIONS](#options)
      - [PATCH](#patch)
      - [CONNECT](#connect)
  - [HTTP Response Status Code](#http-response-status-code)
    - [Informational Responses](#informational-responses)
    - [Successful Responses](#successful-responses)
    - [Redirection Responses](#redirection-responses)
    - [Client Error Responses](#client-error-responses)
- [Bibliography](#bibliography)

<br>

# What is an API
<p align="justify">An API, or <i>application programming interface</i>, is a set of rules or protocol that let software applications communicate with each other to exchange data, features and functionality.</p>

<p align="justify">API's simplify application development by allowing developers to integrate data, services and capabilities from other applications, instead of developing them from scratch</p>

<br>

## How do API's Work?
<p align="justify">The working principle of an API is commonly expressed through the request-response communication between a client and a server. The client is any front-end application that a user interacts with.</p>

![how api works](../image/day_27_api.png "How API WORKS")

<br>

### Remote Procedure Call (RPC)
<p align="justify">Web API's may adhere to resource exchange principles based on a Remote Procedure Call or RPC. This protocol specifies the interaction between applications based on the client server architecture.</p>

<br>

### Service Object Access Protocol (SOAP)
<p align="justify"> SOAP is a lightweight protocol for exchanging structured information in a decentralized, distributed environment, according to the definition by Microsoft that developed it.</p>

<br>

### Representational State Transfer (REST)
<p align="justify">The term <i>REST</i> was introduced by computer scientist <i>Roy Fielding</i> in a <a href="https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm">dissertion</a> in 2000. Unlike SOAP, which is a protocol REST is a software architectural style with <a href="https://www.geeksforgeeks.org/rest-api-architectural-constraints/">six constraints</a> for building applications that work over HTTP, often web services.</p>

<br>

# What is HTTP
<p align="justify">The Hypertext Transfer Protocol (HTTP) is the foundation of the World Wide Web, and is used to load webpages using hypertext links.HTTP is an application layer protocol designed to transfer information between networked devices and runs on top of other layers of the network protocol stack. A typical flow over HTTP involves. a client machine making a request to a server, which then sends a response message.</p>

## What is an HTTP Method
<p align="justify">An HTTP method, sometimes referred to as an HTTP verb, indicates the action that the HTTP request excepts from the queried server. <br>

1. GET

2. PUT
3. POST
4. DELETE
5. PATCH
6. HEAD
7. OPTIONS
8. TRACE
9. CONNECT
    
<br>

#### GET
<p align="justify">The most commonly used HTTP method is GET. The purpose of the GET method is to simply retreive data from the server.</p>



#### POST
<p align="justify">The POST HTTP request method sends data to the server for processing. The data sent to the server is typically in the following form: <br>

- Input fields from online forms.
  
- XML or JSON data.
  
- Text data from query parameters.
</p>

#### HEAD
<p align="justify">The HTTP HEAD method simply returns metadata about a resource on the server.</p>

#### PUT
<p align="justify">The HTTP PUT method in used to completely replace a resource identified with a given URL.<p>

#### DELETE
<p align="justify">The HTTP DELETE method is self-explanatory. After execution, the resource a DELETE operation points to is removed from the server.</p>

#### TRACE
<p align="justify">The TRACE HTTP method is used for diagnostics, debugging and troubleshotting. It simply returns a diagnostics trace that logs data from the request-response cycle.</p>

#### OPTIONS
<p align="justify">The server does not have to support every HTTP method for every resource it managers. The HTTP OPTIONS method returns a listing of which HTTP methods are supported and allowed.</p>

#### PATCH
<p align="justify">The PATH HTTP method, allows for updates of existing resources. It is significantly more efficient, for example, to send a small payload rather than a complete resource representation to the server.</p>

#### CONNECT
<p align="justify">The connect operation is used to create a connection with a server-side</p>

<br>

## HTTP Response Status Code
<p align="justify">

- Informational Responses (100 - 199)
  
- Successful Responses (200 - 299)
- Redirection Responses (300- 399)
- Client Error Responses (400- 499)
- Server Error Responses (500- 599)
</p>

### Informational Responses
<p align="justify">An informational response indicates that the request was received and understood. It is issued on a provisional basis while request processing continues. It alerts the client to wait for a final response.</p>

### Successful Responses
<p align="justify">This class of status codes indicates the action requested by the client was received, understood and accepted.</p>

### Redirection Responses
<p align="justify">This class of status code indicates the client must take additional action to complete the request.</p>

### Client Error Responses
<p align="justify"></p>

# Bibliography
- [Altexsoft](https://www.altexsoft.com/blog/what-is-api-definition-types-specifications-documentation/)
  
- [GeeksforGeeks](https://www.geeksforgeeks.org/rest-api-architectural-constraints/)
- [IBM](https://www.ibm.com/topics/api)
- [Dissertation](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm)
- [Cloudfare](https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/)
- [TheServerSide](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/HTTP-methods)