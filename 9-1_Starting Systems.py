print("""Starting Systems

- Notes -
.........

Please choose one of the options below, and press enter to get notes.

1) System Changeover
2) Implementation Methods
3) related to Data Migration
4) phases in Data Migration
5) issues in Data Migration
6) related to Business M&A
7) Merger vs Acquisition
8) System Integration follow M&A

""")

answer = "empty"

while(answer == "empty"):
  userChoice = input()
  answer = "chosen"
  
  if(userChoice == "1"):
    print("""System changeover is the process of changing systems. The larger the environment, the more problematic and complicated the process becomes. A system changeover may replace part of an organization's or company's operations or can be implemented into an existing larger system or series of systems. There are short term costs associated with switching systems such as manhours, training, and potential financial expenses.
""")
  elif(userChoice == "2"):
    print("""There are 4 types of system implementation: Parallel, Big Bang/Direct/Immediate, Pilot, and Phased. Parallel works in tandem for a short period of time allowing measurement of the new system's output before the old system is taken offline. The Big Bang/Direct/Immediate is the least taxing on computer and network resources where one system is entirely stopped and the new system is adopted. Pilot takes a small portion to test the system and fix issues withi lower risk before widespread implementation. Phased converts one part of the system at a time over to the new system over a period of time.
""")
  elif(userChoice == "3"):
    print("""Data migration has a common misconception of being a relatively easy task when in reality it is quite difficult and crucial. Data migration is taking a look at the assets you've got in the legacy system, transforming in the optimal fashion into your new landscape in an efficient manner.
    """)
  elif(userChoice == "4"):
    print("""Phases in data migration include: plan, migrate, and validate. Planning includes determining the requirements, future environment development, and documentation of migration plan. During migration, the plan is communicated, all needed software and hardware is obtained, installed and configured, and the migration actually occurs. Validation tests check the data is in the same state before and after migration though it is recommended you also run tests pre-migration also.
    """)
  elif(userChoice == "5"):
    print("""Issues in data migration may include: changing formats, types of storage, and computer systems. There could be problems in changing mediums such as incompatibility of data types. Issues could also be data being misinterpretted or the data migration timing out, failing, and encountering other errors.
    """)
  elif(userChoice == "6"):
    print("""Business mergers try to result in a competitive advantage for the new merged company. The system will have to be adapted as entities are integrated into one.
    """)
  elif(userChoice == "7"):
    print("""It can be done through sizing down or reorganization. A large company absorbing a smaller company is called an acquisition. Mergers have combination of leadership of both companies. Employees have to face lots of changes in mergers while in acquisitions, employees conform to the larger company. 
    """)
  elif(userChoice == "8"):
    print("""There are 4 types of M&A Events: Horizontal, Vertical, Concentric, and Conglomerate. Hortizontal is between companies who sell similar parts and they come together in the benefit of trade to improve market share power. Vertical is when company purchases a smaller or larger company to improve its control over the supply chain. Concentric happen when two companies with different products but same customer base come together to cross-sell products and extend the top-line of a product. Conglomerate would be acquisition of different businesses of products, services, and customers to diversify the company which has fallen out of favor towards niche companies.
    """)
  else:
    print("INVALID INPUT, please try again")
    answer = "empty"
