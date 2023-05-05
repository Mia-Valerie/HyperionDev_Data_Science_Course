import math
print("investment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on a home loan \n")
investment_bond_choice = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: \n"))

if investment_bond_choice.lower() == "investment":

#Collecting information about investment from user
    deposit = input("How much money are you depositing? \n")
    deposit = float(deposit.strip("£"))

    interest_rate = input("Please enter the intrest rate. \n")
    interest_rate = float(interest_rate.strip("%"))/100

    length_of_investment = (input("How many years do you intend to invest for? \n"))
    length_of_investment = float(length_of_investment.strip(" years"))

    interest = input("Would you like simple or compound interest? \n")

#calculating simple intrest rate
    if interest.lower() == "simple":      #want to strip this too, but intrest.lower.strip(" intrest") didn't seem to work
        final_amount = deposit*(1 + interest_rate * length_of_investment)
        print("The total amount in account with intrest at the end of the investment will be £" + str(final_amount))

#calculating compound intrest rate
    elif interest.lower() == "compound":
        final_amount = deposit*math.pow((1 + interest_rate),length_of_investment)
        print("The total amount in account with intrest at the end of the investment will be £" + str(final_amount))


elif investment_bond_choice.lower() == "bond":

#Collecting information about bond from user
    house_value = input("What is the current value of the house? \n")
    house_value = float(house_value.strip("£"))

    interest_rate = input("What is the interest rate? \n")
    interest_rate = (float(interest_rate.strip("%"))/100)/12       #the /100 turns percent into decimal and /12 turns a yearly intrest rate into monthly

    repayment_time = input("How many months do you intend to take to pay back the bond? \n")
    repayment_time = float(repayment_time.strip(" months"))

#calculating monthly bond repayments
    repayment = (interest_rate * house_value)/ (1 - (1 + interest_rate) ** (-repayment_time))
    print("The amount you will be required to pay back each month is £" + str(repayment))

#error message is bond or investment is not entered in first step.
else:
    print("Invalid responce, you were required to enter \'bond\' or \'investment\'.")
