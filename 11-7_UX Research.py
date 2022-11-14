print("""For today's content, update your notes as you move through the content.
 """)

answer = "empty"

while(answer == "empty"):
  userChoice = input()
  answer = "chosen"

  if(userChoice == "What is a wireframe?"):
    print("""A wireframe is a layout of a web page that demonstrates what interface elements will exist on key pages. It is a critical part of the interaction design process.
    """)

  if(userChoice == "What is a mockup?"):
    print("""A mockup is an artistic rendering of a design or product that showcases said product in action. A mockup can be a model, image or scene of a proposed design or product, and they’re often used for demonstration, education or promotion. 
    """)

  if(userChoice == "What is a prototype?"):
    print("""A prototype is an early sample, model or release of a product created to test a concept or process. Typically, a prototype is used to evaluate a new design to improve the accuracy of analysts and system users. It is the step between the formalization and the evaluation of an idea.
    """)

  if(userChoice == "What is UX design?"):
    print("""UX design is the process design teams use to create products that provide meaningful and relevant experiences to users. UX design involves the design of the entire process of acquiring and integrating the product, including aspects of branding, design, usability and function.
    """)
