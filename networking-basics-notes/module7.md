# Module 7  
## 7.1 Encapsulation and the Ethernet Frame  

The process of *placing one message format* (the letter) *inside another message format* (the envelope) is called **encapsulation**.  
**De-encapsulation** occurs when the process is reversed by the recipient (the letter is removed from the envelope).  

**Encapsulation** is the process of prepending protocol information with information from another protocol.  

When an Ethernet Frame is sent out on interface, the destination MAC address indicates the MAC address of the device that is present on the network, and that will receive the Ethernet frame.  
**The Preamble** and **Start Frame Delimiter (SFD)** indicate the *beginning* of an **Ethernet Frame**.  

**Ethernet = Layer 2 of OSI Model (Data Link Layer)**

## 7.2 The Access Layer  
**Ethernet switches** make their forwarding decisions *based on* **destination MAC address**.  
**Ethernet switches** *add entries* to their MAC address table *based* on the **source MAC address**.  

When a switch receives an Ethernet frame and the destination MAC address of that frame is not in its MAC address table, the switch will forward the frame out all ports except the incoming port.  

Ethernet hubs are considerate obsolete.  

**Layer 2 Switch** - determines which interface is used to forward a frame based on the destination MAC address.  

**Fields** that are found in a 802.3 Ehternet frame; *source physical destination address* and *Frame Check Sequence*.  

Adressing information that is recorded by a switch to build its MAC address table is the source Layer 2 address of incoming frames.  

**What will a Layer 2 switch do when the destination MAC address of a received frame is not in the MAC address table?**  
It forwards the frame out to all ports except for the port at which the frame was received.  

**Frame forwarding decisions** are *based* on *MAC address* and *port mappings* in the MAC address table.  

A host on an Ethernet network will discard the frame if it receives a frame with a unicast destination MAC address that doesn't match its own MAC address.
