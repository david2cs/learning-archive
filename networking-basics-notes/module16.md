# Module 16
## 16.1 Client and Server Interaction 
**Server** - host running a software application that provides information to other hosts connected to the network.  

**Client - Internet - Server**  

**Types of Server Software**:  
- **Email** - Microsoft Oulook or Gmail
- **Web** - Chrome or Firefox
- **File** - Windows File Explorer

**Uniform Resource Identifiers (URI)** are addresses for resources on the internet like web pages or images. They *help identify* and *locate* these resources.  
Example: https://www.example.com/author/book.html#page2  

**Parts of URI**:  
1. **Scheme/Protocol** - The method used to access the resource  
~ https://
2. **Hostname** - The domain name or IP address where the resource is stored  
~ www.example.com
3. **Path and File Name** - The specific location or file on the server  
~ /author/book.html
4. **Fragment** - A specific section within the resource  
~ #page2

**Common Protocols and their Description**  
- **Domain Name System (DNS)** - Resolves internet names to IP addresses
- **Secure Shell (SSH)** - Used to provide remote access to servers and networking devices
- **Simple Mail Transfer Protocol (SMTP)** - Sends email messages and attachements (images, documents etc.) from client to server and from servers to other email servers
- **Internet Message Access Protocol (IMAP)** - Used by email clients to retrieve emails and attachements from remote servers
- **Hypertext Transfer Protocol (HTTP)** - Used by web browsers to request web pages and web servers to transfer the files that make up the web pages

**Telnet** is *worse* than **SSH** as SSH is more *secure*.  
**SSH**  
1. Allows remote access to computers by creating virtual terminals over a network
2. Been around since the 1970s, uses TCP Port 23
3. Mimics a physical terminal, letting users run commands on the server remotely
