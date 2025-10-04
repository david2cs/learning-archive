# Module 14
## 14.1 The Need for Routing
**Reasons for dividing a network:**  
1. Security
2. Maintain smaller broadcast networks
3. Moving things to different locations

**Routing** is the process where a router figures out the best way to send the data to its destination.  

*Devices outside* the local network are called **remote hosts**.  

## 14.2 The Routing Table
Routers use the **routing table** to *determine* which interface to use to *forward* a message to its intended destination.  
**If it can't determine it, it will drop it.**  

When a device wants to send a message to another device on the **same local network**, it *sends the message directly*. To do this it *finds* the **device's MAC address** using **ARP**. The message is *encapsulated* in a frame that contains the **destination MAC address** and then it is sent *directly* to that device.  
But, if the device needs to send the message to a **remote network**, it has to send the message to a **router** first. The message will still *have* the **destination IP address**, but the *source MAC address* will **be changed** to the **router's MAC address**.  
To know the router's MAC address, the host gets the IP address from the **default gateway setting** in its own network configuration. **The default gateway** is the *router connected to that local network*. Once the host knwos the router's IP address, it uses **ARP** to *find out* the **MAC address**.  

## 14.3 Create a LAN
All local networks within a LAN are under one **administrative control**.  

**Local Network Segment**  
**Single local segment (all hosts)**  
- **Advantages**
1. Appropriate for simpler networks  
2. Less complexity and network cost  
3. Allows devices to be "seen" by others  
4. Faster data transfer ~ direct communication  
5. Ease of device access  
- **Disadvantages**  
1. All hosts are in one broadcast domain which causes more traffic, may hinder network performance  
2. Harder to implement Quality of Service (QoS)  
3. Harder to implement security


**Remote Network Segment**  
**Hosts on a Remote Segment**  
- **Advantages**
1. More appropriate for larger + complex networks  
2. Splits broadcast domains and decreases traffic  
3. Can improve performance on each segment  
4. Makes the machines invisible to those on other local network segments  
5. Can provide increased security  
6. Can improve network organisation  
- **Disadvantages**
1. Requires the use of routing  
2. Router can slow traffic between segments
3. More complexity and expense  

When a router *receives* a frame on an interface, it *strips* the **Layer 2 frame header**. It *checks* the **routing table** to determine which *interface* to use to send the packet to its destination. Once the interface is known, the packet is encapsulated with a **new frame header** containing *different source* and *destiantion MAC addresses*.  
