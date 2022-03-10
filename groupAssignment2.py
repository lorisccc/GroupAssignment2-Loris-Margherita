from time import time

def main():
    # Open file contain
    questions = []
    answers = []
     infile = open("C:\\Users\\cocci\\Desktop\\questions.txt", "r")
     goOn = True
     correctAnsw=0
     totTime=0
     for line in infile:
         if goOn:
             print(line)
             t0 = time()
             answer=input("Enter your answer: ")
             t1 = time()
             totTime+=(t1-t0)
             if answer!='':
                 correctAnsw+=1
             cont = input("Continue the test. (press c)\nQuit. (press any key)\n")
             if cont == 'c':
                goOn = True
             else:
                goOn = False
     print("Number of correct answer: ", correctAnsw)
     print("Time elapsed: ", totTime)
     infile.close()

# Call the main function to start the program
main()
