#This program asks the user for a number, keeps asking until the expected input is entered. Then calculates and prints the average value of incorrect guesses.

correct_number = -1                                                                            #This is the number the program is looking for.
storing_failed_attempts = 0                                                                    #This is the variable that the sum of entered numbers is saved as.
counter = 0                                                                                    #This varible keeps track of how many attempts at a correct input the user has made.

entered_number = int(input("Please enter a number. \n"))                                       #The program asks user to input a number

while entered_number != correct_number:                                                        #If the incorrect value is entered the following steps are undergone
        storing_failed_attempts += entered_number                                              #This adds the entered value to the sum of incorrect values entered
        counter += 1                                                                           #This recorods the failed attempt
        entered_number = int(input("Incorrect number, please try again. \n"))                  #The user is asked to try again and the while loop continues.  

result = storing_failed_attempts / counter                                                    #This is outside the while loop, is what happens when the correct value is entered by user. The avreage incorrect entered value is found.
print("Correct, this is the average value of your failed attempts is " + str(result))         #The average value of attempts is printed.
