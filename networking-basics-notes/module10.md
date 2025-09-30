# Module 10  
## 10.1 IPv4 Issues  
The deplition of IPv4 address space was the *motivating factor* for IPv6.  

**IPv6 -> 128 bit address space**  

**Migration Techniques**  
1. **Dual Stack (use native IPv6 connectivity)** - Allows IPv4 and IPv6 to coexist on the same network segment.
2. **Tunneling** - Method of transporting an IPv6 packet over an IPv4 network. The IPv6 packet is encapsulated inside an IPv4 packet.
3. **Translation** - Network Address Translation 64 (NAT64) helps devices using IPv6 to talk with devices using IPv4. It works by converting messages from IPv6 to IPv4 and vice versa.

**All 5 Regional Internet Registry's have exhausted IPv4 addresses, including:**  
- American Registry for Internet Numbers (ARIN)
- Asia-Pacific Network Coordination Centre (APNIC)
- Latin American and Caribbean Internet Addresses Registry (LACNIC)
- African Network Coordination Centre (AFRINIC)
- Réseaux IP Européens Network Coordination Centre (RIPE NCC)

## 10.2 IPv6 Addressing  
**IPv6** uses a *hexadecimal number system*.  

**Hextet** - segment of *16 bits* or four hexadecimal values.  

**Rule 1** - Omit leading Zeros  
- 01ab -> 1ab  
**Example**: 2001:0db8:0000:1111:0000:0000:0000:2000  
**Solution**: 2001:db8:0:1111:0:0:0:200

**Rule 2** - Double Colon  
**Example**: 2001:0db8:0000:1111:*0000:0000:0000*:2000  
**Soulution**: 2001:db8:0:1111::200
