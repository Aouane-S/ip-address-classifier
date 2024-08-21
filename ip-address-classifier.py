import re,sys,os,platform
# Regular expression 
address_pub = [
    r"^(?:[1-9]|1[1-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|10[0-9]|11[0-9]|12[0-6])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$",     #class A        index address_pub[0]
    r"^(?:12[8-9]|13[0-9]|14[0-9]|15[0-9]|16[0-8]|17[0-1]|17[3-9]|18[0-9]|19[1-1])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$",                           #class B        index address_pub[1]
    r"^(?:16[9-9])\.(?:[1-9]?[0-9]|1[0-9]{2}|25[0-3]|25[5-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$",                                                                                               #class B        index address_pub[2]
    r"^(?:17[2-2])\.(?:[0-9]|1[0-5]|3[2-9]||4[0-9]||5[0-9]||6[0-9]||7[0-9]||8[0-9]||9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$",                                   #class B        index address_pub[3]
    r"^(?:19[3-9]|20[0-9]|21[0-9]|22[0-9]|23[0-0])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$",                                                           #class C        index address_pub[4]
    r"^(?:22[4-9]|23[0-9])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$",                                                                                   #class D        index address_pub[5]
    r"^(?:24[0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$"                                                                                    #class E        index address_pub[6]
               ]
address_prive = [
    r"^(?:1[0-0])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$",                                                                                            #class A        index address_prive[0]
    r"^(?:17[2-2])\.(?:1[6-9]|2[0-9]|3[0-1])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$",                                                                                                                #class B        index address_prive[1]
    r"^(?:19[2-2])\.(?:16[8-8])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$"                                                                                                                              #class C        index address_prive[2]
    ]

address_ip = [
    r"^(?:12[7-7])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",                                                                                                                                                           #class A        index address_ip[0]      address boucle
    r"^(?:16[9-9])\.(?:25[4-4])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$"                                                                                                                              #class B        index address_ip[1]      address APIPA
    ]
address_reseau = [
    r"^(?:[1-9]|1[1-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|10[0-9]|11[0-9]|12[0-6])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                    #class A        index address_reseau[0]             address reseau public
    r"^(?:12[8-9]|13[0-9]|14[0-9]|15[0-9]|16[0-8]|17[0-1]|17[3-9]|18[0-9]|19[1-1])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                          #class B        index address_reseau[1]             address reseau public
    r"^(?:16[9-9])\.(?:[1-9]?[0-9]|1[0-9]{2}|25[0-3]|25[5-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                                                                                              #class B        index address_reseau[2]             address reseau public
    r"^(?:17[2-2])\.(?:[0-9]|1[0-5]|3[2-9]||4[0-9]||5[0-9]||6[0-9]||7[0-9]||8[0-9]||9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                                  #class B        index address_reseau[3]             address reseau public
    r"^(?:19[3-9]|20[0-9]|21[0-9]|22[0-9]|23[0-0])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                                                          #class C        index address_reseau[4]             address reseau public
    r"^(?:22[4-9]|23[0-9])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                                                                                  #class D        index address_reseau[5]             address reseau public
    r"^(?:24[0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                                                                                  #class E        index address_reseau[6]             address reseau public
    r"^(?:1[0-0])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                                                                                           #class A        index address_reseau[7]             address reseau prive 
    r"^(?:17[2-2])\.(?:1[6-9]|2[0-9]|3[0-1])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                                                                                                               #class B        index address_reseau[8]             address reseau prive
    r"^(?:19[2-2])\.(?:16[8-8])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                                                                                                                            #class C        index address_reseau[9]             address reseau prive
    r"^(?:12[7-7])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                                                                                          #class A        index address_reseau[10]            address reseau boucle
    r"^(?:16[9-9])\.(?:25[4-4])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[0-0])$",                                                                                                                                            #class B        index address_reseau[11]            address reseau APIPA
    r"^(?:[0-0])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"                                                                                                             #               index address_reseau[12]            address address default
   ]
#this just for devlop the script
#address_prodcust = [
#    r"^(?:[1-9]|1[1-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|10[0-9]|11[0-9]|12[0-6])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                    #class A        index address_prodcust[0]             address prodcust public
#    r"^(?:12[8-9]|13[0-9]|14[0-9]|15[0-9]|16[0-8]|17[0-1]|17[3-9]|18[0-9]|19[1-1])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                                          #class B        index address_prodcust[1]             address prodcust public
#    r"^(?:16[9-9])\.(?:[1-9]?[0-9]|1[0-9]{2}|25[0-3]|25[5-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                                                                                                              #class B        index address_prodcust[2]             address prodcust public
#    r"^(?:17[2-2])\.(?:[0-9]|1[0-5]|3[2-9]||4[0-9]||5[0-9]||6[0-9]||7[0-9]||8[0-9]||9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                                                  #class B        index address_prodcust[3]             address prodcust public
#    r"^(?:19[3-9]|20[0-9]|21[0-9]|22[0-9]|23[0-0])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                                                                          #class C        index address_prodcust[4]             address prodcust public
#    r"^(?:22[4-9]|23[0-9])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                                                                                                  #class D        index address_prodcust[5]             address prodcust public
#    r"^(?:24[0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                                                                                                  #class E        index address_prodcust[6]             address prodcust public
#    r"^(?:1[0-0])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                                                                                                           #class A        index address_prodcust[7]             address prodcust prive 
#    r"^(?:17[2-2])\.(?:1[6-9]|2[0-9]|3[0-1])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                                                                                                                               #class B        index address_prodcust[8]             address prodcust prive
#    r"^(?:19[2-2])\.(?:16[8-8])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                                                                                                                                            #class C        index address_prodcust[9]             address prodcust prive
#    r"^(?:12[7-7])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$",                                                                                                          #class A        index address_prodcust[10]            address prodcust boucle
#    r"^(?:16[9-9])\.(?:25[4-4])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:25[5-5])$"                                                                                                                                             #class B        index address_prodcust[11]            address prodcust APIPA  
#]

# Function to validate IP address
summary_class_A = """


Summary  -----------------------------------------------------------------------------------------
        The range from 1.0.0.0 to 126.0.0.0 includes a mix of public IP address
        blocks assigned to major service providers like AT&T, AWS, and IBM,
        as well as regional internet registries such as APNIC and RIPE NCC.
        This range is utilized for various purposes including cloud services,
        public DNS, enterprise networking, and infrastructure across different geographic regions.
"""
summary_class_A_B_C_prive = """


Summary  -----------------------------------------------------------------------------------------
        Private IP addresses in Classes A, B, and C are reserved for use within internal networks and are not routable on the public internet.
        **Class A private addresses** (10.0.0.0 to 10.255.255.255) are used in large networks, providing over 16 million addresses.
        **Class B private addresses** (172.16.0.0 to 172.31.255.255) serve medium-sized networks, offering around 1 million addresses.
        **Class C private addresses** (192.168.0.0 to 192.168.255.255) are commonly used in smaller networks,
        such as home and small business networks, with 65,536 available addresses.
        These private ranges allow organizations to manage internal network traffic without consuming public IP resources.
        
"""
summary_class_B = """


Summary  -----------------------------------------------------------------------------------------
        Class B public IP addresses, ranging from 128.0.0.0 to 191.255.255.255, 
        are designed for medium to large networks, offering a balance between network size and host capacity.
        With a default subnet mask of 255.255.0.0, each Class B network can support up to 65,534 hosts.
        These addresses are used for public networks and are routable on the internet, making them essential for organizations such as corporations, educational institutions, and ISPs. 
        While the address space is limited, Class B addresses continue to play a vital role in the global IPv4 infrastructure.
                    
"""
summary_class_C = """


Summary  -----------------------------------------------------------------------------------------
        Class C public IP addresses, ranging from 192.0.0.0 to 192.167.255.255 and 192.169.0.0 to  223.255.255.255, are intended for smaller networks, 
        such as those used by small businesses and local networks. With a default subnet mask of 255.255.255.0,
        each Class C network can support up to 254 hosts. These addresses are widely used for public internet connections,
         making them a key part of the IPv4 address space. Due to their limited host capacity,
        Class C networks are ideal for organizations that need fewer IP addresses but still require a routable internet presence.

"""
summary_class_D = """


Summary  -----------------------------------------------------------------------------------------
       Class D IP addresses, ranging from 224.0.0.0 to 239.255.255.255,
       are reserved for multicast networking rather than traditional host addressing.
       Unlike Classes A, B, and C, Class D addresses do not have a subnet mask because they are used to send data to multiple destinations simultaneously in multicast groups.
       These addresses are crucial for applications like streaming media, online gaming, and other services that require efficient one-to-many communication.
       Class D is not used for standard unicast (one-to-one) communication but plays a vital role in optimizing network traffic for specific applications. 
"""
summary_class_E = """


Summary  -----------------------------------------------------------------------------------------
       Class E IP addresses, ranging from 240.0.0.0 to 255.255.255.255, 
       are reserved for experimental and research purposes and are not intended for general use in public networks.
       These addresses are typically used for testing and future development within network research environments.
       Since Class E is reserved, it is not routable on the public internet and is not assigned to any specific organization.Although largely unused in practice,
         this address space serves as a reserve for potential future applications and innovations in networking technology.

"""
summary_address_boucle = """

Summary  -----------------------------------------------------------------------------------------
       Loopback addresses, most commonly represented by 127.0.0.1, are used to test network software and configurations on a local machine.
       These addresses allow a computer to communicate with itself, bypassing network hardware.
       The entire 127.0.0.0/8 range is reserved for loopback purposes, but 127.0.0.1 is the standard address used in practice.
       Loopback addresses are essential for testing network applications and diagnosing issues without affecting the actual network or requiring external connectivity.

"""
summary_address_APIPA = """

Summary  -----------------------------------------------------------------------------------------
       
       APIPA (Automatic Private IP Addressing) addresses, in the range 169.254.0.0 to 169.254.255.255,
       are automatically assigned by devices when a DHCP server is unavailable. This feature enables basic network communication within a local network without requiring manual IP configuration.
       APIPA addresses allow devices to communicate with each other on the same network segment, but they are not routable on the broader internet.
       APIPA is particularly useful in small networks and for troubleshooting connectivity issues when DHCP fails.

"""
summary_address_default = """

Summary  -----------------------------------------------------------------------------------------
       
      The IP address **0.0.0.0** is a special-purpose address with multiple uses. In networking,
      it is commonly used to represent an unknown or unspecified address. For instance, in routing tables, it can indicate the default route,
      directing traffic to any network destination. Additionally, it is used in certain configurations to denote "any address" or as a placeholder during network initialization.
      The address **0.0.0.0** is not routable on the public internet and has specific applications in network configuration and diagnostics. 

"""


def validate_ip_(ip):
    if re.match(address_pub[0], ip):                      #class A        index address_pub[0]
            if re.match(r"^1\.\d\.\d\.\d$",ip):               # address 1.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  1.1.1.1: Public DNS service provided by Cloudflare, known for its speed and privacy features.
    --  1.0.0.0/24: Sometimes used by various service providers within the Asia-Pacific region.
    --  Characteristics: This block is part of the larger APNIC allocation, covering a significant portion of the Asia-Pacific region.

    """)
            if re.match(r"^(?:100.64)\D\d\D\d$",ip):               # address NAT
                print(f"""

    More Inofrmation of Address IP {ip}
    --  Carrier-Grade NAT (RFC 6598)
    --  This range is reserved for Carrier-Grade NAT, where ISPs use it to allow multiple customers to share a single public IP address.
    Like private IP addresses, it is non-routable on the public internet.
    100.64.0.0/10: (100.64.0.0 - 100.127.255.255)
    """)
                return f"- This is Address {ip} -------->  Adress Class A  and Address NAT"

            if re.match(r"^2\.\d\.\d\.\d$",ip):               # address 2.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  2.2.2.2: Public IP address often used in network configuration examples.
    --  2.0.0.0/24: Used by various ISPs and organizations in Europe and surrounding regions.
    --  Characteristics: This block is managed by RIPE NCC and serves Europe, the Middle East, and parts of Central Asia.

    """)   
            if re.match(r"^3\.\d\.\d\.\d$",ip):               # address 3.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Amazon Web Services (AWS)
    --  3.3.3.3: Used by AWS for its cloud computing services, including EC2 instances and other infrastructure.
    --  Characteristics: This block is utilized by AWS for a wide range of cloud-based services and applications.

    """)                                                         
            if re.match(r"^4\.\d\.\d\.\d$",ip):               # address 4.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Level 3 Communications (now part of CenturyLink/Lumen Technologies)
    --  4.2.2.2: Public DNS server operated by Level 3 Communications.
    --  Characteristics: Used for backbone services and enterprise networks, serving a significant role in internet infrastructure.

    """)                                                             
            if re.match(r"^5\.\d\.\d\.\d$",ip):               # address 5.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Originally allocated to RIPE NCC, now used by various ISPs and organizations in Europe.
    --  5.5.5.5: Sometimes seen in network configuration examples.
    --  Characteristics: This block is used for public-facing services and infrastructure within Europe.

    """)                                                         
            if re.match(r"^6\.\d\.\d\.\d$",ip):               # address 6.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  United States Department of Defense (DoD)
    --  6.6.6.6: Public IP addresses in this range may be used for DoD-related infrastructure.
    --  Characteristics: Used for military and defense-related networks.

    """)                                                             
            if re.match(r"^7\.\d\.\d\.\d$",ip):               # address 7.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  United States Department of Defense (DoD)
    --  7.7.7.7: Public IP addresses in this range may be used for DoD-related infrastructure.
    --  Characteristics: Similar to 6.0.0.0/8, used for defense-related applications.

    """)                                                          
            if re.match(r"^8\.\d\.\d\.\d$",ip):               # address 8.0.0.0/8
                print(f"""

    Inofrmation of Address IP {ip}
    --  Level 3 Communications (now part of CenturyLink/Lumen Technologies)
    --  8.8.8.8: Public DNS service operated by Google, known for its speed and reliability.
    --  Characteristics: Used for internet backbone services and public DNS services.

    """)                                                          
            if re.match(r"^9\.\d\.\d\.\d$",ip):               # address 9.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  IBM
    --  9.9.9.9: Public DNS service operated by IBM (formerly by Quad9).
    --  Characteristics: Used for IBM’s global network infrastructure and services.

    """) 
            if re.match(r"^11\.\d\.\d\.\d$",ip):               # address 11.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Various organizations and ISPs.
    --  11.0.0.0/24: Often used by smaller organizations or for specific internal purposes.
    --  Characteristics: Part of the public IP space, typically used by enterprises and service providers.

    """)
            if re.match(r"^12\.\d\.\d\.\d$",ip):               # address 12.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  AT&T
    --  12.0.0.0/24: Used by AT&T for various networking services.
    --  Characteristics: This block is used by AT&T for its network services and infrastructure.

    """)
            if re.match(r"^13\.\d\.\d\.\d$",ip):               # address 13.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Various organizations, including some large enterprises and service providers.
    --  13.0.0.0/24: Used for various internal and public-facing services.
    --  Characteristics: This range is used by different entities, often for large-scale infrastructure and services.

    """)
            if re.match(r"^14\.\d\.\d\.\d$",ip):               # address 14.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  APNIC
    --  14.0.0.0/24: Used by various service providers in the Asia-Pacific region.
    --  Characteristics: This block is managed by APNIC and serves the Asia-Pacific region.

    """)
            if re.match(r"^15\.\d\.\d\.\d$",ip):               # address 15.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Various organizations, including some large ISPs.
    --  15.0.0.0/24: Used by various ISPs and enterprises.
    --  Characteristics: This range is used for diverse purposes, including public and private services.

    """)
            if re.match(r"^16\.\d\.\d\.\d$",ip):               # address 16.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  AT&T
    --  16.0.0.0/24: Used for network services and infrastructure by AT&T.
    --  Characteristics: Similar to other blocks assigned to AT&T, used for various networking purposes.

    """)
            if re.match(r"^17\.\d\.\d\.\d$",ip):               # address 17.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Various organizations, including some large technology companies.
    --  17.0.0.0/24: Used for enterprise and public-facing services.
    --  Characteristics: This range includes addresses used by a variety of entities for different purposes.

    """)
            if re.match(r"^18\.\d\.\d\.\d$",ip):               # address 18.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  IBM
    --  18.0.0.0/24: Used for IBM’s global network and services.
    --  Characteristics: This block is used by IBM for various infrastructure and network services.

    """)
            if re.match(r"^19\.\d\.\d\.\d$",ip):               # address 19.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Various organizations and service providers.
    --  19.0.0.0/24: Typically used for enterprise and public services.
    --  Characteristics: This range includes addresses used for diverse networking purposes.

    """)
            if re.match(r"^20\.\d\.\d\.\d$",ip):               # address 20.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --   Various organizations and ISPs.
    --  20.0.0.0/24: Used by different ISPs and enterprises.
    --  Characteristics: This block is used for public-facing services and infrastructure.

    """)
            if re.match(r"^21\.\d\.\d\.\d$",ip):               # address 21.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  APNIC
    --  21.0.0.0/24: Used in the Asia-Pacific region for various services.
    --  Characteristics: This range is part of APNIC’s allocation and is used for regional network services.

    """) 
            if re.match(r"^22\.\d\.\d\.\d$",ip):               # address 22.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Various organizations and ISPs.
    --  22.0.0.0/24: Used for public and enterprise services.
    --  Characteristics: This range includes addresses used by multiple entities for diverse networking needs.

    """)
            if re.match(r"^23\.\d\.\d\.\d$",ip):               # address 23.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Amazon Web Services (AWS)
    --  23.0.0.0/24: Used by AWS for its cloud services.
    --  Characteristics: This block is used by AWS for cloud infrastructure and services.

    """)
            if re.match(r"^24\.\d\.\d\.\d$",ip):               # address 24.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Various ISPs and organizations.
    --  24.0.0.0/24: Used by different ISPs and public services.
    --  Characteristics: This range is used for a variety of public-facing services.

    """)
            if re.match(r"^25\.\d\.\d\.\d$",ip):               # address 25.0.0.0/8
                print(f"""
    More Inofrmation of Address IP {ip}
    --  Various organizations and ISPs.
    --  25.0.0.0/24: Used for enterprise and public services.
    --  Characteristics: This block is used for diverse networking needs.

    """)
            if re.match(r"^26\.\d\.\d\.\d$",ip):               # address 26.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Various organizations and ISPs.
    --  26.0.0.0/24: Used for enterprise and public-facing services.
    --  Characteristics: Addresses in this range are used by multiple entities.

    """)
            if re.match(r"^27\.\d\.\d\.\d$",ip):               # address 27.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  APNIC
    --  27.0.0.0/24: Used by various organizations in the Asia-Pacific region.
    --  Characteristics: Managed by APNIC, used for regional services.

    """)
            if re.match(r"^28\.\d\.\d\.\d$",ip):               # address 28.0.0.0/8
                print(f"""
    Inofrmation of Address IP {ip}
    --  Various organizations.
    --  28.0.0.0/24: Used for diverse networking purposes.
    --  Characteristics: Includes addresses used for public and private services.

    """)

            if re.match(r"^(?:34|35|52|54|63|67|68|69|70|71|72|73|75|76|77|96|103|104|105|107|108)\D\d\D\d\D\d$",ip):               # address AWS
                print(f"""

More Inofrmation of Address IP {ip}
--  Amazon Web Services (AWS)
--  Amazon Web Services (AWS) uses several IP address ranges for its cloud services and infrastructure.
These ranges are managed and published by AWS to ensure that users can configure their network settings and security rules effectively.

""")

            if re.match(r"^(?:100)\D([0-9]|1[0-9]|2[0-9]|3[0-9]4[0-9]|5[0-9]|6[0-3]|6[5-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\D\d\D\d$",ip):               # address AWS
                print(f"""

    More Inofrmation of Address IP {ip}
    --  Amazon Web Services (AWS)
    --  Amazon Web Services (AWS) uses several IP address ranges for its cloud services and infrastructure.
    These ranges are managed and published by AWS to ensure that users can configure their network settings and security rules effectively.

    """)

            if re.match(r"^(?:36|39|42|49|58|59|60|61|101|103|106|110|111|112|113|114|115|116|117)\D\d\D\d\D\d$",ip):               # address APNIC
                print(f"""

    More Inofrmation of Address IP {ip}
    --  APNIC (Asia-Pacific Network Information Centre)
    --  APNIC (Asia-Pacific Network Information Centre) is the regional internet registry for the Asia-Pacific region.
    APNIC allocates and manages IP address space for this region, including IPv4 and IPv6 addresses.

    """)

            if re.match(r"^(?:32|40|44|63|67|69|70|72|73|74|75)\D\d\D\d\D\d$",ip):               # address AT&T
                print(f"""

    More Inofrmation of Address IP {ip}
    --  AT&T
    --  AT&T, a major telecommunications provider, utilizes a variety of IP address ranges for its network infrastructure and services.
    These ranges are used for internet connectivity, data centers, enterprise solutions, and other network-related functions.
    """)

            if re.match(r"^(?:2\.(1[6-9]|[2-9][0-9])\.[0-9]{1,3}\.[0-9]{1,3}|5\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|31\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|37\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|46\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|62\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|77\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|78\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|79\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|80\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|81\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|82\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})$",ip):               # address AT&T
                print(f"""

    More Inofrmation of Address IP {ip}
    --  RIPE NCC (Réseaux IP Européens Network Coordination Centre)
    --  RIPE NCC (Réseaux IP Européens Network Coordination Centre) is the regional internet registry (RIR) responsible for managing and allocating IP address resources in Europe,
    the Middle East, and parts of Central Asia. The public IP address ranges managed by RIPE NCC are used for various internet services,
    including network infrastructure, data centers, and end-user connectivity.
    """)
            print(f"- This is Address {ip} -------->  Adress Class A  and Address Public")
            print(summary_class_A)
        
    elif re.match(r"^(?:192|)\.(?:[1-9]?[0-9]|10[0-9]|11[0-9]|12[0-9]|13[0-9]|14[0-9]|15[0-9]|16[0-7]|16[9-9]|17[0-9]|18[0-9]|19[0-9]|2[0-4][0-9]|25[0-5])\.(?:[1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.(?:[1-9]|1[0-0]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip):                                                                  #class B        index address_pub 192.0.0.0 to 192.168.167.0 and 192.169.0.0
            if re.match(r"^(?:192)\D\d\D\d\D(?:0)$",ip):               # address 192.0.0.0 192.167.0.0 and 192.169.0.0 192.255.255.255
                  if re.match(r"^(?:192)\D\d\D\d\D(?:255)$",ip):
                      print(f"- This is {ip} Address  -------->  Brodcust Class B , Public")
                  print(f"- This is {ip} Address  -------->  Reseau Class B  and Public") 
            print(summary_class_B)
    elif re.match(address_pub[1], ip):                                                                  #class B        index address_pub[1]
            if re.match(r"^(?:129|130|131|132|133|134|135|136|137|138|139)\D\d\D\d\D\d$",ip):               # address AWS
                    print(f"""

        More Inofrmation of Address IP {ip}
        --  Amazon Web Services (AWS)
        --  Amazon Web Services (AWS) uses several IP address ranges for its cloud services and infrastructure.
        These ranges are managed and published by AWS to ensure that users can configure their network settings and security rules effectively.

        """)
            elif re.match(r"^(?:176\D(3[2-9]|4[0-7])\D\d\D\d)$",ip):               # address AWS
                        print(f"""

        More Inofrmation of Address IP {ip}
        --  Amazon Web Services (AWS)
        --  Amazon Web Services (AWS) uses several IP address ranges for its cloud services and infrastructure.
        These ranges are managed and published by AWS to ensure that users can configure their network settings and security rules effectively.

        """)
            print(f"- This is Address {ip} -------->  Adress Class B  and Address Public")
            print(summary_class_B)
    elif re.match(address_pub[2], ip):                                                                  #class B        index address_pub[2]
        print(f"- This is Address {ip} -------->  Adress Class B  and Address Public")
        print(summary_class_B)
    elif re.match(address_pub[3], ip):                                                                  #class B        index address_pub[3]
        print(f"- This is Address {ip} -------->  Adress Class B  and Address Public")
        print(summary_class_B)
    
    elif re.match(address_pub[4], ip):                                                                  #class C        index address_pub[4]
    
        print(f"- This is Address {ip} -------->  Adress Class C  and Address Public")
        print(summary_class_C)
    elif re.match(address_pub[5], ip):                                                                  #class D        index address_pub[5]
    
        print(f"- This is Address {ip} -------->  Adress Class D  and Address Public")
        print(summary_class_D)
    elif re.match(address_pub[6], ip):                                                                  #class E        index address_pub[6]
    
        print(f"- This is Address {ip} -------->  Adress Class E  and Address Public")
        print(summary_class_E)
    ##################################################################################
    elif re.match(address_prive[0], ip):                                                                    #class A        index address_prive[0]
        print(f"- This is Address {ip} -------->  Adress Class A  and Address Prive")
        print(summary_class_A_B_C_prive)  

    elif re.match(address_prive[1], ip):                                                                  #class B        index address_prive[1]
        print(f"- This is Address {ip} -------->  Adress Class B  and Address Prive")
        print(summary_class_A_B_C_prive)

    elif re.match(address_prive[2], ip):                                                                  #class C        index address_prive[2]
        print(f"- This is Address {ip} -------->  Adress Class B  and Address Prive")
        print(summary_class_A_B_C_prive)
    ##################################################################################
    elif re.match(address_ip[0], ip):                                                                    #class A        index address_ip[0]      address boucle
        print(f"- This is Address {ip} -------->  Adress Class A  and Address Boucle ") 
        print(f"""

More Inofrmation of Address IP {ip}
--  Loopback Address
--  The loopback address, most commonly 127.0.0.1, is used by a device to refer to itself.
It is used for internal communication within the device and is not routable to other networks.
127.0.0.0/8: (127.0.0.0 - 127.255.255.255)
""")

    elif re.match(address_ip[1], ip):                                                                  #class B        index address_ip[1]      address APIPA
        print(f"- This is Address {ip} -------->  Adress Class B  and Address APIPA") 
        print(f"""

More Inofrmation of Address IP {ip}
--  Link-Local Addresses (RFC 3927)
--  This range is used for automatic IP addressing when a device cannot obtain an IP address from a DHCP server.
Devices using link-local addresses can communicate with other devices on the same local network but cannot connect to the internet directly.
169.254.0.0/16: (169.254.0.0 - 169.254.255.255)
""")


###########################################################################################
    elif re.match(address_reseau[0], ip):                                                                    #class A        index address_reseau[0]             address reseau public
        print(f"- This is {ip} Address  -------->  Reseau Class A  and Public")
        return summary_class_A
    elif re.match(address_reseau[1], ip):                                                                    #class B        index address_reseau[1]             address reseau public
        print(f"- This is {ip} Address  -------->  Reseau Class B  and Public")
        return summary_class_B
    elif re.match(address_reseau[2], ip):                                                                    #class B        index address_reseau[2]             address reseau public
        print(f"- This is {ip} Address  -------->  Reseau Class B  and Public")
        return summary_class_B
    elif re.match(address_reseau[3], ip):                                                                    #class B        index address_reseau[3]             address reseau public
        print(f"- This is {ip} Address  -------->  Reseau Class B  and Public")
        return summary_class_B
    elif re.match(address_reseau[4], ip):                                                                    #class C        index address_reseau[4]             address reseau public
        print(f"- This is {ip} Address  -------->  Reseau Class C  and Public")
        return summary_class_C
    elif re.match(address_reseau[5], ip):                                                                    #class D        index address_reseau[5]             address reseau public
        print(f"- This is {ip} Address  -------->  Reseau Class D  and Public")
        return summary_class_D
    elif re.match(address_reseau[6], ip):                                                                    #class E        index address_reseau[6]             address reseau public
        print(f"- This is {ip} Address  -------->  Reseau Class E  and Public")
        return summary_class_E
    elif re.match(address_reseau[7], ip):                                                                    #class A        index address_reseau[7]             address reseau prive
        print(f"- This is {ip} Address  -------->  Reseau Class A  and Prive")
        return summary_class_A
    elif re.match(address_reseau[8], ip):                                                                    #class B        index address_reseau[8]             address reseau prive
        print(f"- This is {ip} Address  -------->  Reseau Class B  and Prive")
        return summary_class_B
    elif re.match(address_reseau[9], ip):                                                                    #class C        index address_reseau[9]             address reseau prive
        print(f"- This is {ip} Address  -------->  Reseau Class C  and Prive")
        return summary_class_C
    elif re.match(address_reseau[10], ip):                                                                   #class A        index address_reseau[10]            address reseau boucle
        print(f"- This is {ip} Address  -------->  Reseau Class A  and Boucle Local")
        return summary_address_boucle 
    elif re.match(address_reseau[11], ip):                                                                   #class B        index address_reseau[11]            address reseau APIPA
        print(f"- This is {ip} Address  -------->  Reseau Class B  and APIPA")
        return summary_address_APIPA
    elif re.match(address_reseau[12], ip):                                                                   #class A        index address_reseau[12]            address address default
        print(f"- This is Address {ip} -------->  Reserved for special purposes") 
        print(f"""

More Inofrmation of Address IP {ip}
--  0.0.0.0/8
--  0.0.0.0/8: Reserved for special purposes, such as self-identification and representing "any network" in routing tables.
These addresses are not routable on the public internet.
""")
        return summary_address_default
    else:
        print("""
        ___________________________________------------------
        Please Type Address IP --> example (192.168.1.1)
        ___________________________________------------------ 
""")

def clearscr():
    if platform.system() == "Windows":
        os.system('cls')  # Clear screen for Windows
    else:
        os.system('clear')

      

def boucle_():
    while True:
        check = input("""
        ____________________________________________________________________________________________
                                Welcome To Prgramme check The Ip Address and Take Information
                    To use the Programme type ( continue )
                    To exit Programme type ( exit )
                    To clear screen type ( clear )
        ____________________________________________________________________________________________            
                : """)
        if check == "continue":
            clearscr()
            ip = input("""
                       
        enter to check address ip 
                       
                :----->      """)
            clearscr()
            print(f"""
                You Type This ---------> {ip}
""")
            validate_ip_(ip)
        elif check=="exit":
            clearscr() 
            sys.exit(0)
        elif check=="clear":
            clearscr()
        else:   
            print("please type (continue) or (clear) or (exit)")             

boucle_()