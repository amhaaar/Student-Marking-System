#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID: 20210734 / w1867698
#Date:06/12/2021


progress = 0
trailing = 0
retriever = 0
excluded = 0
program_counter = ""
pass_credits = 0
defer_credits = 0
fail_credits = 0
while program_counter.lower() != "q":           #program counter which loops until 'q' is entered
    def credit_input():                         #a function defined to get credits from user
        global pass_credits                     #will be able to change global variables in a locally defined function
        global defer_credits
        global fail_credits

        while True:
            try:
                pass_credits = int(input("Enter your pass credits: "))
                if pass_credits not in range(0,121,20):
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer required")
        while True:
            try:
                defer_credits = int(input("Enter your defer credits: "))
                if defer_credits not in range(0,121,20):
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer required")
        while True:
            try:
                fail_credits = int(input("Enter your fail credits: "))
                if fail_credits not in range(0,121,20):
                    print("Out of range")
                else:
                    break
            except ValueError:
                print("Integer required")

    credit_input()                          #calls the function which was defined above

    total_credits = (pass_credits + defer_credits + fail_credits)
    if total_credits !=120:
        print("Total incorrect")            #if the total credits entered does not add to 120 error message will be displayed
        credit_input()                      #calls the function again if the error occurs               

    if pass_credits ==120:
        progress +=1                        #creates a count for the number of students who porgress
        print("Progress")
    elif pass_credits == 100 and (defer_credits == 20 or fail_credits ==20):
        trailing +=1                        #creates a count for the number of students who trail
        print("Progress (module trailer)")
    elif pass_credits + defer_credits >=60:
        retriever +=1                       #creates a count for the number of students who retrieve
        print("Module retriever")
    else:
        excluded +=1                       #creates a count for the number of  students who exclude
        print("Exclude")
    total_outcomes = progress + trailing + retriever + excluded   
    program_counter = input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: ")             #asks the user if he/she wants to continue or end it and check the results

    total_outcomes = progress + trailing + retriever + excluded         #collects the total number of outcomes
print("\nProgress  ",progress,":",progress*"*","\n"                      #horizontal histogram
      "Trailer   ",trailing,":",trailing*"*","\n"
      "Retriever ",retriever,":",retriever*"*","\n"
      "Excluded  ",excluded,":",excluded*"*","\n")
if total_outcomes == 1:
    print(total_outcomes,"outcomes in total.")                      #Total number of outcomes is displayed
else:
    print(total_outcomes,"outcomes in total.")                      
    
                        

