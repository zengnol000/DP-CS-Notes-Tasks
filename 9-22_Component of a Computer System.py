print("""Choose input for the following variables:

1. Hardware
2. Software
3. Peripheral Devices
4. Computer Network
5. Human ResourcesDumb 
6. Terminal
7. Thin Client
8. Client
9. Email Server
10. Router
11. DNS Server
12. Firewall
13. Client-server

 """)

answer = "empty"

while(answer == "empty"):
  userChoice = input()
  answer = "chosen"

  if(userChoice == "Hardware"):
    print("""Hardware consists of the physical parts of a system.
    """)

  if(userChoice == "Software"):
    print("""Software is the set of instructions which makes the computer system do something useful. These sets of instructions are collected together in workable groups known as programs. Without programs of instructions, computer would not be able to function as they would not know what to do.
    """)

  if(userChoice == "Peripheral Devices"):
    print("""These are hardware devices that are outside the computer processor. Peripheral devices are typically conneted to the computer by cables. Examples include a printer and a hard disk. They come in three types: input, output, and storage.
    """)

  if(userChoice == "Computer Network"):
    print("""A set of computer systems taht are interconnected and share resources, as well as data. For example: Local Area Netowrk, Wide Area Network, etc.
    """)

  if(userChoice == "Human Resources"):
    print("""People who are part of (or could be part of) an organization, business, or economy. 
    """)

  if(userChoice == "Dumb Terminal"):
    print("""A terminal that doesn't perofrm local processing of entered information but serves only as an input/output device for an attached or network-linked processor. 
    """)

  if(userChoice == "Thin Client"):
    print("""In computer networking, a thin client is a simple computer that has been optimized for establishing a remote connection with a server-based computing environment. They are sometimes known as network computers, or in their simplest form as zero clients.
    """)

  if(userChoice == "Client"):
    print("""In computing, a client is a piece of computer hardware or software that accesses a service made available by a server as part of the client–server model of computer networks. The server is often on another computer system, in which case the client accesses the service by way of a network. 
    """)

  if(userChoice == "Email Server"):
    print("""An email server, also called a mail server, is essentially a computer system that sends and receives emails. When you send an email, it goes through a series of servers to reach its final destination
    """)

  if(userChoice == "Router"):
    print("""A router is a networking device that forwards data packets between computer networks. Routers perform the traffic directing functions on the Internet. Data sent through the internet, such as a web page or email, is in the form of data packets.
    """)

  if(userChoice == "DNS Server"):
    print("""The Domain Name System (DNS) Server is a server that is specifically used for matching website hostnames (like example.com)to their corresponding Internet Protocol or IP addresses. The DNS server contains a database of public IP addresses and their corresponding domain names.
    """)

  if(userChoice == "Firewall"):
    print("""In computing, a firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. A firewall typically establishes a barrier between a trusted network and an untrusted network, such as the Internet.
    """)

  if(userChoice == "Client-Server"):
    print(""" Client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients. 
    """)
