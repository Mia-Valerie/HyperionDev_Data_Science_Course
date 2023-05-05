#asking user for input about their holiday and checking input is valid
city_flight = input("Which city are you flying too? \nTop destinations include: Amsterdam, Paris, Copenhagen and Oslo!\n")
while city_flight != "Amsterdam" and city_flight != "Paris" and city_flight != "Copenhagen" and city_flight != "Oslo":
    city_flight = input("Sorry it seems we don't fly there yet. \nI've heard Paris is lovely this time of year. \nPlease try a new location.\n")

num_nights = input("How many nights will you be staying at a hotel? \n")
try:
    int(num_nights)
except ValueError:
    num_nights = input("Please enter a valid interger.")

rental_days = input("How many days will you be hiring a car? \n")
try:
    int(rental_days)
except ValueError:
    rental_days = input("Please enter a valid interger.")


#A function to calculate the cost of the hotel
def hotel_cost(num_nights):
    return int(num_nights) * 80


#A function to calculate flight cost
def plane_cost(city_flight):
    if city_flight == "Amsterdam":        
       return int(25)
    elif city_flight == "Paris":
       return int(45)
    elif city_flight == "Copenhagen":
       return int(35)
    elif city_flight == "Oslo":
       return int(40)


#A function to calculate car rental cost
def car_rental(rental_days):
       return int(rental_days) * 90


#Tell the user the individule costs of what they have requested, calling on functions where nessisary.
print("You have choosen to travel to " + city_flight + " this will cost £" + str(plane_cost(city_flight)) + " for return flights." )
print("Your hotel costs £80 a night and you are staying for " + str(num_nights) + " nights. So, the total cost for your accomidation will be £" + str(hotel_cost(num_nights)) + ".")
print("You have chosen to rent a car for " + str(rental_days) + " days. As your car rental is £90 a day, the total charge for car rental will be £" + str(car_rental(rental_days)) + ".")

#Calculating and printing final holiday cost, calling on functions to do so.
holiday_cost = int(hotel_cost(num_nights)) + int(car_rental(rental_days) + int(plane_cost(city_flight)))
print("Therfore, the total cost of your holiday will be £" + str(holiday_cost))
