#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID: 20210734 / w1867698
#Date:06/12/2021


while True:           #loop contiues until the keyword break                                  
    while True:
        try:
            pass_credits = int(input("Enter your pass credits: "))
            if pass_credits not in range(0,121,20):         #Checks if the input integer is in the range of (0,20,40,60,80,100,120)
                print("Out of range")
            else:
                break
        except ValueError:
                print("Integer required")                   #Error message 'integer required' is sent if the user has not entered an integer value 
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
    total_credits = (pass_credits + defer_credits + fail_credits)
    if total_credits != 120:
        print("Total incorrect")            #if total is not equal to 120 error message is displayed
    elif pass_credits ==120:
        print("Progress")                       
        break
    elif pass_credits == 100 and (defer_credits == 20 or fail_credits == 20):
        print("Progress (module trailer)")
        break
    elif pass_credits + defer_credits >= 60:
        print("Module retriever")
        break
    else:
        print("Exclude")
        break
    
