# Module 11
## 11.1 Static and Dynamic IPv4 Addressing  

If the **IP address** is *manually set*, then the following actions will be done:  
- *IP address ~ host on network*
- *Subnet mask ~ the network where the host is connected*
- *Default gateway ~ the networking device*

**Dynamic Host Configuration Protocol (DHCP)** will *automatically assign addressing information* such as the IPv4 address, subnet mask and the default gateway.  

Devices that can be a DHCP server:  
1. Router (Wireless or Wired)
2. Server with DHCP software

## 11.2 DHCPv4 Configuration
Destination address that a DHCPv4 client uses to send the initial DHCP Discover packet is *255.255.255.255*.  

**Process of DHCPv4 Configuration:**  
1. **DHCP Discover**  
  - Client initiating a message to *find a DHCP server* for network settings.
2. **DHCP Offer**  
  - DHCP server responds to the Discover message and *offers network information* (IP address).  
3. **DHCP Request**  
  - The host *accepts* the offered network configurations.
4. **DHCP Acknowledgement**  
  - Confirms that the server has accepted the request and the *network information is now assigned* to the client. The client can now use the provided configurations to *communicate on the network*.  
