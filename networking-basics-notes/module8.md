# Module 8  
## 8.1 Purpose of an IPv4 Address  

To communicate over the internet or a LAN, a host needs a unique IPv4 address. This address is assigned to the device's Network Interface Card (NIC) and must be unique locally (for LAN) and globally (for internet). Devices such as PC's and servers use these addresses. Routers also have IPv4 addresses.  

**Every internet packet includes a source and destination IPv4 address to ensure proper delivery and response.**  

**IPv4 addresses** are *32 bits* in lenght and are grouped into *4 octets*.  
**Example**: 11010001.10100101.11001000.00000001  
**Converted** to **decimal value**: 209.165.200.1  

## 8.2 The IPv4 Address Structure  
**Hierarchial Addressing**  
The network portion indicates the network on which each unique host address is located.  
**192.168.5.11**  
| Network    | Host   |
|------------|--------|
| 192.168.5  | .11    |

The **network address** for **172.16.4.100** with a subnet mask of *255.255.0.0* would be - **172.16.0.0**  

**Routing is required** to *enable computers* on different logical networks to *communicate* with each other.  

**Purpose** of a **subnet mask** in conjuction with an IP address is to *determine the subnet* to which the host belongs.
