from time import time

def main():

     questions = ["1) What distinguishes 'software engineering' from 'programming' or 'computer science'?",
                 "2) Software engineering can be thought of as 'programming integrated over time'.What practices can we introduce to our code to make it sustainable (able to react to necessary change) over its life cycle, from conception to introduction to maintenance to deprecation?",
                 "3) Why if you are maintaining a project that is used by other engineers, the most important lesson about 'it works' versus 'it is maintainable' is given by the 'Hyrum’s Law' and discussions of change and maintenance over time must be aware of it?",
                 "4) Teamwork is without doubt the best route to producing great software, so how does one build (or find) a great team and what are the related 'three pillars' of social skills?",
                 "5) Perhaps no software engineering tool is quite as universally adopted throughout the industry as version control. What are the differences between Centralized VCS Versus Distributed VCS and why their use has become such an unambiguous norm in software engineering?",
                 "6)",
                 "7)",
                 "8)",
                 "9)",
                 "10)"]
     Correctanswers = ["The field of Software Engineering focuses on applying engineering processes to the creation, maintenance and design of software at every level,so it implies the application of some theoretical knowledge to build something real and precise",
                "There are mainly three fundamental principles that software organizations should keep in mind when designing, architecting, and writing their code: Time and Change (How code will need to adapt over the length of its life), Scale and Growth (How an organization will need to adapt as it evolves) and Trade-os and Costs (how an organization makes decisions, based on the lessons of Time and Change) and Scale and Growth.",
                "Hyrum’s Law represents the practical knowledge that—even with the best of intentions, the best engineers, and solid practices for code review—we cannot assume perfect adherence to published contracts or best practices. As an API owner, you will gain some flexibility and freedom by being clear about interface promises, but in practice, the complexity and difficulty of a given change also depends on how useful a user finds some observable behavior of your API.",
                "These three principles are the foundation on which all healthy interaction and collaboration are based. Pillar 1: 'Humility', you are not the center of the universe (nor is your code!). You’re neither omniscient nor infallible. You’re open to self-improvement. Pillar 2: 'Respect', you genuinely care about others you work with. You treat them kindly and appreciate their abilities and accomplishments. Pillar 3: 'Trust', you believe others are competent and will do the right thing, and you’re OK with letting them drive when appropriate. If you perform a root-cause analysis on almost any social conflict, you can ultimately trace it back to a lack of humility, respect, and/or trust.",
                "In centralized VCS implementations, the model is one of a single central repository (likely stored on some shared compute resource for your organization), while a Distributed VCS world does not enforce the constraint of a central repository: if you have a copy (clone, fork) of the repository, you have a repository that you can commit to as well as all of the metadata necessary to query for information about things like revision history. Recall that software engineering is programming integrated over time; we’re drawing a distinction (in dimensionality) between the instantaneous production of source code and the act of maintaining that product over time. That basic distinction goes a long way to explaining the importance of, and hesitation toward, VCS: at the most fundamental level, version control is the engineer’s primary tool for managing the interplay between raw source and time. We can conceptualize VCS as a way to extend a standard filesystem.",
                "",
                "",
                "",
                "",
                ""]
     wrongAnswers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

     goOn = True
     while(goOn):
         # Set variables to 0
         correctAnsw=0
         totTime=0
         for i in range(0, 10):
             wrongAnswers[i] = 0;

         # Loop to display the 10 questions
         for i in range(0,10):
             print(questions[i])
             t0 = time()
             answer=input("Enter your answer: ")
             t1 = time()
             totTime+=(t1-t0) # Compute elapsed time for the current question
             if answer!='':
                 correctAnsw+=1
             else :
                 wrongAnswers[i] = 1

         print("Time elapsed: %.2f" %(totTime))
         print("Number of correct answer: ", correctAnsw)

         # Print the answer to the wrong question
         for i in range(0,10):
             if (wrongAnswers[i] == 1):
                 print(f'Your answer to the question n.°{i+1} is wrong, the correct one is:\n {Correctanswers[i]}')




         cont = input("Continue the test. (press c)\nQuit. (press any key)\n")
         if cont == 'c':
                 goOn = True
         else:
                 goOn = False






# Call the main function to start the program
main()
