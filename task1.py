
choice = input("If you would like to read sums from a exsisting file please enter \"read\". If you would like to enter a new sum please enter \"new sum\"\n")
choice = choice.strip( )
choice = choice.lower()

while choice == "new sum":
# Asking for first number, asking again if input invalid
    num1 = input("Please enter your first number.\n")                           
    num1 = num1.strip( )
    try:
        float(num1)
    except ValueError:
        num1 = input("Please enter a valid number (e.g 5). \n")
       
# Asking for operator and asking again if invalid
    operation = input("Please enter one of the following operations to apply to your numbers: +, -, x, / \n")
    operation = operation.strip( )
    operation = operation.lower()
    while operation != '+' and operation != '-' and operation != 'x' and operation != '/' :
        operation = input("This operation is invalid, please enter one of: +, -, x or / \n")       

# Asking for second number and aking again if invalid    
    num2 = input("Please enter your second number.\n")
    num2 = num2.strip( )
    try:
        float(num2)
    except ValueError:
        num2 = input("Please enter a valid number (e.g 5). \n")


# Writing sum to file sum.txt and asking if they would like to enter another sum or read sum
    if operation == "+" :
        answer = float(num1) + float(num2)
        with open('sum.txt', 'a') as file:
            file.write(str(num1) + " + " + str(num2) + " = " + str(answer) + "\n")
            choice = input("If you would like to repeat the process for a new sum please enter \"new sum\". \nIf you would like to read a sum from an exsisting file please enter \"read\".\n" )                   
            
    elif operation == "-":
        answer = float(num1) - float(num2)
        with open('sum.txt', 'a') as file:
            file.write(str(num1) + " - " + str(num2) + " = " + str(answer) + "\n")
            choice = input("If you would like to repeat the process for a new sum please enter \"new sum\". \nIf you would like to read a sum from an exsisting file please enter \"read\".\n" )                   
            
    elif operation == "x":
        answer = float(num1) * float(num2)
        with open('sum.txt', 'a') as file:
            file.write(str(num1) + " x " + str(num2) + " = " + str(answer)+ "\n")
            choice = input("If you would like to repeat the process for a new sum please enter \"new sum\" \nIf you would like to read a sum from an exsisting file please enter \"read\".\n" )                   
        
    elif operation == "/":
        answer = float(num1) / float(num2)
        with open('sum.txt', 'a') as file:
            file.write(str(num1) + " / " + str(num2) + " = " + str(answer) + "\n")
            print(str(num1) + " / " + str(num2) + " = " + str(answer))
            choice = input("If you would like to repeat the process for a new sum please enter \"new sum\". \nIf you would like to read a sum from an exsisting file please enter \"read\".\n" )                   

# Allowing for capitals or extra spaces in choice
choice = choice.strip( )
choice = choice.lower()

# Asking again is they didn't choose read or repeat
while choice != "read" and choice != "new sum":
    choice = input("Invalid entry, please enter \"read\" or \"new sum\".\n") 

# Asking for file, printing file content, asking again if file doesn't exsit
while choice == "read":
    file_name = str(input("Please enter the name of the file you would like to read, in the format: file.txt\n"))

    file = None
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line)
            choice = 'neither'

    except FileNotFoundError as error:
        print("The file that you are trying to open does not exist. The equations for have just calculated have been writen to sum.txt")
    finally:
        if file is not None:
            file.close()

# Once file content has printed, program ends
while choice == "neither":
    print("Thank you for using my program :)")
    break

