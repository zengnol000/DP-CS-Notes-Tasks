print("""Starting Systems

- Notes -
.........

Please choose one of the options below, and press enter to get notes.

1) SaaS
2) On-Premise Software
3) System Life Cycle
4) Functional Testing
5)Choose a streaming service. 
Is it SaaS or on-premise?
List some of the functionalities of the service that you would test prior to its release
6)Choose an app or software that is NOT a streaming service. 
Is it SaaS or on-premise?
List some of the functionalities of the service that you would test prior to its release.

""")

answer = "empty"

while(answer == "empty"):
  userChoice = input()
  answer = "chosen"

  if (userChoice == "1"):
    print("""Software as a Service, aka "on-demand software" and before "software plus services," is not run on the local computer system but uses the internet to connect to remote servers. It is lower initial costs, regular maintenance and updates, no staff needed, typically has more system support, and on-site natural disasters do not put data at risk.
    
    """)

  elif(userChoice == "2"):
    print("""On-Premise Software, aka "shrinkwrap" software, is installed and runs on computers on the premises of the person or organization using the software rather than on a remote server farmer or cloud. It typically needs IT on-site.
    
    """)

  elif(userChoice == "3"):
    print("""It requires of 7 phases: planning, requirement analysis, design, implementation/coding, testing, deployment, and maintenance. 
    
    """)
  elif(userChoice == "4"):
    print("""A type of testing that seeks to establish whether each application feature works as per the software requirements. You test for mainline functions, basic usability, accessibility, and error conditions.

    """)
  elif(userChoice == "5"):
    print("""Twitch is SaaS because it is a cloud service platform. For Twitch I would test whether content creators can post livestreams and whether or not the users can interact with the lives.
    
    """)
  elif(userChoice == "6"):
    print("""Kingdom Rush is on-site because it is stored locally though you can save your data onto the cloud now. For Kingdom Rush, I would definitely test if the game can save its data on individual devices and whether the data will reset or not whenever you uninstall the game.
    
    """)
  else:
    print("INVALID INPUT, please try again")
    answer = "empty"
