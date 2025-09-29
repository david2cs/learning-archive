# Module 9  
## 9.1 IPv4 Unicast, Broadcast and Multicast  

**Unicast** transmission refers to one device *sending a message* to another device in *1 to 1* communication.  
**Broadcast** transmission is a device *sending a message* to *all devices* on the network. **Routers don't forward broadcasts**.  
- 255.255.255.255

**Multicast transmission** is used when a device *sends a message* to a *select group* of devices.  
- 224.0.0.0 -> 239.0.0.0  

**A source IP address can only be a unicast address.**  

## 9.2 Types of IPv4 Addresses  

**Public IPv4 addresses** are *globally routed* between ISP routers.  

**Private IPv4 addresses** are used by organisations to *assign* IPv4 addresses to *internal hosts*.  

**Network Address Translator (NAT)** - Used to *translate between* **private IPv4 and public IPv4 addresses**.  

**Legacy Classful Addressing**  
1. Class A (0.0.0.0/8 -> 127.0.0.0/8)
   - Designed for large networks with more than 16 million host addresses.
2. Class B (128.0.0.0/16 -> 191.255.0.0/16)
   - Designed for moderate to large networks with less than 65,000 host addresses.
3. Class C (192.0.0.0/24 -> 223.255.255.0/24)
   - Designed for small networks with a max of 254 host addresses.

**Private IPv4 addresses** are assigned to devices within an organisation's intranet and any organisation (home) can use the 10.0.0.0/8 address.  

**Regional Internet Registries (RIR's)** receive IP addresses from **Internet Assigned Numbers Authority (IANA)** and are *responsible* for *allocating* these addresses to ISP's and other organisations.  

## 9.3 Network Segmentation  
*Devices talk to each other* using special messages called **broadcasts**. One common use is the **Address Resolution Protocol (ARP)** that *helps identifying the MAC address* on the same network when it known its IP address.  

When a device joins a network, it often uses **Dynamic Host Configuration Protocol (DHCP)** to *get its IP address*. DHCP sends out broadcasts messages to find a DHCP server to give it an address.  

*Switches are network devices that connect computers*. When a switch receives a broadcast message, it sends copies to all other devices connected to it except the one that originally sent it.  

**Routers don't pass broadcast messages to other networks.**  

**Problem with Large Broadcast Domains**  
- Slow network operations due to significant amount of traffic.  

**Solution**  
- Reduce the size of the network to create smaller broadcast domains = Subnetting.

**Basics of subnetting**: using host bits to create additional subnets.  
**Subnet = Network**  

**Types of Broadcasts**  
1. **Directed Broadcast** - Sent to all devices on a specific network  
2. **Limited Broadcast** - Sent only within the current device's network  

**Types of Addresses**  
1. **Loopback address** - Special IP address that a device uses to send messages to itself.
   127.0.0.1
2. **Experimental address** - Special IP address reserved for testing and development purposes (private).  
   192.0.0.0 -> 192.255.255.255 / 240.0.26.255  
3. **Link-local address** - Special IP address used for communication between devices on the same local network without a router.  
   169.254
