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
while program_counter.lower() != "q":
    def credit_input():
        global pass_credits
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

    credit_input()

    total_credits = (pass_credits + defer_credits + fail_credits)
    if total_credits !=120:
        print("Total incorrect")
        credit_input()

    if pass_credits ==120:
        progress +=1
        print("Progress")
    elif pass_credits == 100 and (defer_credits == 20 or fail_credits ==20):
        trailing +=1
        print("Progress (module trailer)")
    elif pass_credits + defer_credits >=60:
        retriever +=1
        print("Module retriever")
    else:
        excluded +=1
        print("Exclude")
        break
    program_counter = input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: ")

    total_outcomes = progress + trailing + retriever + excluded
print("\nProgress  Trailing  Retriever  Excluded \n")        # vertical histogram is displayed from here
while progress > 0 or trailing > 0 or retriever > 0 or excluded > 0 :
    if progress > 0 :
        print("    *    ", end="")
    else:
        print("         ", end="")
    progress -= 1
    if trailing > 0 :
        print("    *    ", end="")
    else:
        print("         ", end="")
    trailing -= 1
    if retriever > 0 :
        print("      *    ", end="")
    else:
        print("           ", end="")
    retriever -= 1
    if excluded > 0 :
        print("      *    ")
    else:
        print("           ")
    excluded -= 1

if total_outcomes ==1:
    print(total_outcomes,"outcomes in total.")
else:
    print(total_outcomes,"outcomes in total.")

credit = [[120,0,0],[100,0,20],[80,20,20],[60,0,60],[40,0,80]]
for i in credit:
    if int(i[0]) == 120 :
        print("Progress -", *i, sep=",")
    elif int(i[0]) == 100 :
        print("Progress (module trailer)-", *i, sep=",")
    elif int(i[0]) + int(i[1]) >= 60 :
        print("Module retriever -", *i, sep=",")
    else:
        print("Exclude -", *i, sep=",")
                
