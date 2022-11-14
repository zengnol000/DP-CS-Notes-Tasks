print("""In your notes for today, include the following:
1. What is WCAG?
2. When was WCAG released?
3. Who works on WCAG?
4. What is WCAG 2.1 in comparison to WCAG 2.0?
5. Choose two guidelines or focuses (related to WCAG 2 or 3) that you think are particularly note worthy. Which two did you choose, explain why you chose each.
6. After trying out all three, which do you like best? In your notes, explain your opinion.
 """)

answer = "empty"

while(answer == "empty"):
  userChoice = input()
  answer = "chosen"

  if(userChoice == "What is WCAG?"):
    print("""Web Content Accessibility Guidenlines (WCAG) are rules that are meant to make the web and digital technology accessible. Initially strongly focused on HTML.
    """)

  if(userChoice == "When was WCAG released?"):
    print("""WCAG 1.0 was released on May 5, 1999. WCAG 2.0 was released on December 11, 2008.
    """)

  if(userChoice == "Who works on WCAG?"):
    print("""The World Wide Web Consortium (W3C) oversees WCAG to meet the needs of individuals, organizations, and governments around the world.
    """)

  if(userChoice == "What is WCAG 2.1 in comparison to WCAG 2.0?"):
    print(""" WCAG 2.1 largely builds on WCAG 2.0 and is not meant to replace it. The main difference between the two are tablets and mobile devices that make up a majority of web searches. WCAG 2.1 ensures that websites should be equally acceptable in either landscape or portrait orientation. WCAG 2.1 betters adapts to increasing mobile usability features such as hover or focus or enabling the label in name. Additionally status messages have more cues to make them more noticeable for individuals. 
    """)

  if(userChoice == "Choose two guidelines or focuses (related to WCAG 2 or 3) that you think are particularly note worthy. Which two did you choose, explain why you chose each."):
    print("""I find that WCAG 3.0 has two guidelines that I feel are super important. Firstly the inclusion of different disability groups and improved usability especially for people who rarely use the web. I find these crucial as I believe the Internet is essential for allowing humans to overcome human limitations and these same people who have trouble accessing the web under the current WCAG 2.0, are the same people who would benefit most from the implementation of new guidelines. 
    """)

  if(userChoice == "After trying out all three, which do you like best? In your notes, explain your opinion."):
    print("""I like Option 2 the best, the website: accessibe.com. Firstly, it is nicely spaced and can easily adjust to different screen sizes because of its borderless layout. Additonally, the extra help and chat features are intuitive being on the lower right hand-side. Besides, it indicates without you attempting to find it that it is there to assist you if you have any questions so you do not have to search for help. Not to mention, the color contrast is easy on the eyes and the color palette is used expertly to highlight important words and actions.
    """)
