#Collecting competitor's time for each event
swim_time = float(input("Please enter your time for the swimming event in minutes. \n"))
cycle_time = float(input("Please enter your time for the cycling event in minutes. \n"))
run_time = float(input("Please enter your time for the running event in minutes. \n"))

#Calculating total tritholon time
total_time = swim_time + cycle_time + run_time

#Displaying award
qualifying_time = 100
if total_time <= qualifying_time:
    print("You have achived the Provincial Colours Award!")
elif total_time <= qualifying_time + 5:
    print("You have achived the Provincial Half Colours Award!")
elif total_time <= qualifying_time + 10:
    print("You have achived the Provincial Scroll!")
else:
    print("You have not achived an award.")
