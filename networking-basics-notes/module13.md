# Module 13
## 13.1 MAC and IP
**Primary addresses assigned:**  
- **Physical address (MAC)** - used for *NIC to NIC communication*.
- **Logical address (IP)** - used to *send the packet* from the *source device -> destination device*.

**Layer 2 Ethernet frame:**  
- Destination MAC address
- Source MAC address

**Layer 3 IP packet:**  
- Source IPv4 address
- Destination IPv4 address

When sending a frame to another device on the same local network, the device sending the frame will use the *MAC address of the destination device*.  

When sending data to a device on a different network, the device sends the frame to the *router's MAC address (the default gateway)*.  

## 13.2 Broadcast Containment  
When a host received a message sent to the broadcast address, it treats it as if it was sent *directly to it*. When a broadcast message is sent, the switch sends that message to all hosts connected on the same network, because of this, it is also called a **broadcast domain**.  

To keep the network running efficiently, routers are used to split one large network into smaller ones called **multiple broadcast domains**.  

If a host wants to send a message but it only knows the *logical IP address of the destination host*, it can use an IPv4 protocol called **Address Resolution Protocol (ARP)** to *discover the MAC address of the host* on the same network.  

**Destination MAC address of an Ethernet broadcast** in *hexadecimal* would look like this:  
FFFF.FFFF.FFFF
