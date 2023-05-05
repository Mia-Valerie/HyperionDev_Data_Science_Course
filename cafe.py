# The cafe's menu is stored in a list
menu = ["Fish & Chips", "Sunday Roast", "Ham, Egg & Chips", "Hunters Chicken"]

#The cafe's stock is stored in a dictionary
stock = {"Fish & Chips" : 57,
         "Sunday Roast" : 30,
         "Ham, Egg & Chips" : 51,
         "Hunters Chicken" : 9}

#The cafe's prices are stored in a dictionary
price = {"Fish & Chips" : 11,
         "Sunday Roast" : 14,
         "Ham, Egg & Chips" : 11,
         "Hunters Chicken" : 9}


total_stock = 0                                                             #the value of stock is defined as zero before loop
for items in menu:                                                          #Every item in list menu is iterated over,
    item_value = (stock[items]*price[items])                                #Finding the product of each item in the stock dictionary its value in the price dictionary.
    total_stock += item_value                                               #This product is them added to the total_stock sum until all items in menu have been iterated over.
print("The value of the cafe's total stock is £" + str(total_stock))        #This is outside the for loop so only the final result after all iternations is printed.
