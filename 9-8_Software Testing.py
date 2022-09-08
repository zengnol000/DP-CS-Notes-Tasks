https://sites.google.com/springbranchisd.com/compsci-digital-media/dp-cs-evenodd/1q/software-testinghttps://sites.google.com/springbranchisd.com/compsci-digital-media/dp-cs-evenodd/1q/software-testingprint("""Starting Systems

- Notes -
.........
1) debugging
2) validation vs verification
3) testing & types of testing:
  -dry-run
  -functional
  -unit
  -integration
  -user acceptance
  -alpha
  -beta
4) types of data used in testing:
  -normal
  -at the limits
  -extreme
  -abnormal

""")

answer = "empty"

while(answer == "empty"):
  userChoice = input()
  answer = "chosen"

  if (userChoice == "1"):
    print("""Debugging is super important as bugs in code can prove expensive or fatal in real life. Debugging requires you to isolate the source of the bug, identify the cause of the bug, determine a fix for the bug, apply the fix, and test it. 
  
  """)
  elif(userChoice == "2"):
    print("""Verification is a process that determines the quality of the software. Validation on the other hand is a process which the requirements of the customer are actually met by the software functionality.



  """)

  elif(userChoice == "3"):
    print("""There are different types of testing. Testing can be dynamic and static and can come in multiple ways. Dry-run testing is when you manually move through the code with pen-and-paper to determine the result when the code is run. Functional tests individual commands, text input, menu functions, etc. Unit testing separetly tests the individual components or parts of the system or software. Integration testing is when the components are tested together within the system or software to check that everything works together well. User acceptance is if the system satisfies the customer's needs. Alpha testing is when the tsts are conducted in a laboratory or stage setting while beta tests are done by real users.
  
  """)

  elif(userChoice == "4"):
    print("""A normal data is typically expected data that will be accepted by the system. Extreme data are on the upper and lower boundaries and are on the outer edges. At the limits data is data at the limits and sorts out data before or beyond the range of the data. Abnormal test data that falls out of the data are outliers and should be restricted.
  
  """)

  else:
    print("INVALID INPUT, please try again")
    answer = "empty"
