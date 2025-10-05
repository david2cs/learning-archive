# Module 15
## 15.1 TCP and UDP
**User Datagram Protocol (UDP)** - Primarly used in streaming or real-time communication (VoIP)  
**Transmission Control Protocol (TCP)** - Primarly used for web browsing, email and downloads  

**UDP - fast but may lose some data**  
**TCP - reliable, ensures all data arrives**  

The transport layer in both TCP/IP and OSI models is **responsible** for ensuring packets are **sent realiably** and any *missing packets* are **resent**.  

TCP keeps track of the numeber of segments that have been sent to a specific host from a specific application.  
UDP is a "best effort" delivery system that doesn't require acknowledgement of receipt.  

## 15.2 Port Numbers  
| TCP/IP Layer   | Protocol        |
|----------------|-----------------|
| Application    | HTTP, SMTP, DNS |
| Transport      | TCP, UDP        |
| Internet       | IP              |
| Network Access | Network         |

Ports are assigned and managed by the Internet Corporation for Asigned Names and Numbers (ICANN).  

Ports are can range from 1 -> 65535, and are divided into three categories:  
1. **Well-known Ports** - ports that are associated with common network applications: 1 -> 1023
2. **Registered Ports** - either source or destination ports used by organisations to register specific applications: 1024 -> 49151
3. **Private Ports** - used by any application but often used as source ports: 49152 -> 65535

**Well known Ports and Associated Applications**  
| Port  | Transport | Application Protocol |
|-------|-----------|----------------------|
| 20    | TCP       | FTP - Data           |
| 21    | TCP       | FTP - Control        |
| 22    | TCP       | Secure Shell (SSH)   |
| 23    | TCP       | Telnet               |
| 25    | TCP       | SMTP                 |
| 53    | TCP, UDP  | DNS                  |
| 67    | UDP       | DHCP - Server        |
| 68    | UDP       | DHCP - Client        |
| 69    | UDP       | TFTP                 |
| 80    | TCP       | HTTP                 |
| 110   | TCP       | POP3                 |
| 143   | TCP       | IMAP                 |
| 161   | UDP       | SNMP                 |
| 443   | TCP       | HTTPS                |

Source IP address and source port or Destination IP address and destination port are known as a **socket**.
