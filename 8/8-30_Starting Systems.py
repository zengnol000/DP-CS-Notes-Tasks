print("""Starting Systems

- Notes -
.........

Please choose one of the options below, and press enter to get notes.

1) Systems
2) Legacy Systems
3) Planning
4) Feasibility, including TELOS
5) Change Management
6) Business Merger
7) Real World Example:...... US Post Office
8) Hypothetical Example:.... Encyclopedia Sales

""")

answer = "empty"

while(answer == "empty"):
  userChoice = input()
  answer = "chosen"
  
  if(userChoice == "1"):
    print("""A 'computer system' is the software, hardware, the people, and the immediate environment. It can even include processes like training the employees and/or users and maintaining and protecting data or hardware. Despite systems costing a lot to implement, it should improve the cost-to-benefit ratio in comparison to no system.
""")
  elif(userChoice == "2"):
    print("""A legacy system is the system being replaced by a new system. However, you don't always throw out the legacy system because it may have lots of data or storage. Therefore, it is usually important for the new system to work in tandem with the legacy system.
""")
  elif(userChoice == "3"):
    print("""When planning, you should consider if there is a lack of organizational and business strategy, stakeholder and end-user participation, and end-user 'ownership'. They should also pay attention to required training, organizational issues including group culture, design of tasks and job roles, and overall usability of the system when implementing systems.
    """)
  elif(userChoice == "4"):
    print("""Feasibility should consider TELOS:
T = Technical Feasibility
E = Economic Feasibility
L = Legal Feasibility
O = Operational Feasibility
S = Schedule Feasibility
    """)
  elif(userChoice == "5"):
    print("""Change management is in charge of shifting, hiring, or letting employees or whole departments go. It also changes the process or work the employees do. Its goal is to maximize benefits and minimum negatives for all the stakeholders involved in the process. 
    """)
  elif(userChoice == "6"):
    print("""The goal of business mergers is to create a new, larger organization with more market share. It is meant to join certain operations like manufacturing to streamline processes and reduce cost.
    """)
  elif(userChoice == "7"):
    print("""The U.S. postal office reads letter-writer's terrible writing by the 3+1. So they take the first three charactes in the city name and the two character state or territory abbreviation. The street address is all the numbers, the first three characters, and the city, state.
    """)
  elif(userChoice == "8"):
    print("""The system change will create a more streamlined system as there is no disconnect between the salesperson and the company as if it was when there was a middleman (the secretary) in between. Though it does provide a bit more responsibility on the salesman, they probably take down the customer name and their order anyways so they could bring them the correct goods. This would reduce costs as there is no secretaray, and there is less room for error for input of data.
    """)
  else:
    print("INVALID INPUT, please try again")
    answer = "empty"
