# Module 5

## 5.3 Network Communication Models  
**TCP/IP Model**  
**1. Application** - HTTP  
**2. Transport** - TCP  
**3. Internet** - IP  
**4. Network Access** - Ethernet  

**Order of TCP/IP Model**  
**Ethernet Protocol** - Used for NIC to NIC communications in the same network  
**IP Protocol** - Makes sure that the message gets from the original source to the final destination  
**TCP (Transimission Control Protocol)** - Makes sure that the information gets to the destination reliably  
**HTTP** - Governs the exchange of transfer of HTML  

**OSI Model**  
**7. Application** - The application layer contains protocols that are used for process-to-process communications  
**6. Presentation** - The layer provides for common representation of the data transferred between application layer services  
**5. Session** - Provides services to the presentation layer to organise its dialogue and data  
**4. Transport** - Defines services to segment, transfer and reassemble data for individual communications between end devices  
**3. Network** - Provides services to exchange the individual piece of data over the network between identified end devices  
**2. Data link** - Describes methods for exchanging data frames between devices on common media  
**1. Physical** - Describes the mechanical, electrical, functional and procedural means for bit transmission to and from a network devices  

The **TCP/IP Model** is specific to the internet protocol suite, describing the interactions of protocol within. It doesn't cover general networking functions.  

The **OSI Model** provides more comprenhensive framework, breaking down the networking process into 7 layers, including details on physical media access and data enconding which are not specified in the TCP/IP Model.  

The OSI Model is better than the TCP/IP Model due to its comprenhensive framework (more detailed).  

| OSI Model    | TCP/IP Model   |
|--------------|----------------|
| Application  | Application    |
| Presentation |                |
| Session      |                |
| Transport    | Transport      |
| Network      | Internet       |
| Data link    | Network Access |
| Physical     |                |
