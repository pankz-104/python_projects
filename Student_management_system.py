import os
import platform

global listStd # making listStd as global variable
listStd = ["pankaj","sandesh","abyakta"]    # list of student 

def manageStudent(): # function to manage student
    x = "#" * 37
    y = "*" * 34
    global bye
    bye = (f" \n {x} \n# {y} #\n#==>  STUDENT MANAGEMENT SYSTEM  <==#\n# {y} #\n# {x}")

    # printing welcome message
    print("""
    -------------------------------------------------
    |================================================|
    |===== Welcome To Student Management System =====|
    |================================================|
    -------------------------------------------------

    Enter 1 : To view Student's list
    Enter 2 : To Add New Student
    Enter 3 : To Search Student
    Enter 4 : To Remove Student
    """)

    try:    # Using exceptions for validations
        userInput = int(input("Please Select Any Above Options: "))
    except ValueError: # Error message 
        print(" Hey! That's not a number")
    else:
        print("\n") # print new line 
        
    # checking user options
    if userInput == 1: # This will print list of students
        print("List Students")
        for students in listStd:
            print(f"=> {students}")

    elif userInput == 2: # This will add student to list
        newStd = input("Enter new student: ")
        # condition checking if newStd is already present or not 
        if newStd in listStd:
            print(f"This student {newStd} is already enrolled ")
        else:
            # adding students if not present already
            listStd.append(newStd)
            print(f"{newStd} is now admitted to the school")
            for students in listStd:
                print(f"{students}")
    elif userInput == 3:  # This will check if the student is present already or not
        stdName = input("Enter name to find student ")
        if stdName in listStd:
            print(f"{stdName} is Present in the school")
        else:
            print(f"{stdName} is not present in the school")

    elif userInput == 4: # This will remove student from the list
        remStd = input("Whom do you want to remove ??")
        if remStd in listStd:
            listStd.remove(remStd)
            print(f"{remStd} is removed from school")
        else:
            print(f"{remStd} is not present in the school")
    elif userInput < 1 or userInput > 4:
        print("Please select valid option: ")
        
        
manageStudent()

def runAgain(): # to run the program again
    runAgn = input("Want to run again ?? Y/N ")
    if (runAgn.lower() == 'y'):
        if(platform.system() == "windows"):
           print(os.system('cls'))
        else:
            print(os.system('clear'))
        manageStudent()
        runAgain()
    else:
        quit(bye) # print goodbye message and exit
runAgain()
