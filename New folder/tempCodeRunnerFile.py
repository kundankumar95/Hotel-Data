# Budget = 10000
# person = 2 
# room = 1
#days = 3
# location = Kolkata to lucknow 
# hotel lagbe
# ar expenses er input nebe



############################################################################################################################
#This part of code finds out the distance between two place
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Replace these with the actual locations you want to find the distance between.
origin_location = input("Enter the original location:")
destination_location = input("Enter the destination:")

# Initialize the geolocator
geolocator = Nominatim(user_agent="distance_calculator")

# Get the coordinates of the locations
origin_coords = geolocator.geocode(origin_location)
destination_coords = geolocator.geocode(destination_location)

if origin_coords and destination_coords:
    # Calculate the distance
    distance = geodesic((origin_coords.latitude, origin_coords.longitude),
                       (destination_coords.latitude, destination_coords.longitude)).kilometers

    # Print the distance
    print(f"The distance between {origin_location} and {destination_location} is approximately {distance:.2f} kilometers.")
else:
    print("Location not found. Please check the provided locations.")

####################################################################################################################
budget = int(input("Enter your total budget: "))
person = int(input("Enter the number of people travelling: "))
# room = int(input("How many rooms dou want?"))
days = int(input("How many days do want?"))
# destination_location = input("Enter your travel destination: ")
# travel_month = input("Enter the month you'll be travelling (e.g., December): ")
# current_location = input("Enter your current location state: ")
expenses = int(input("Enter the amount you want to spend for food and others:"))
# hotel_type = input("Enter the hotel type (3star, 4star, 5star, normal): ").lower()








###################################################################################################################
remaining_money = budget - expenses


#UP-DOWN TRAIN JOURNEY COST APPROX.
#case1
total_cost_of_train_tciket = ((0.5)*distance*person)
total_updown_train = 2*total_cost_of_train_tciket

#UP-DOWN TRAIN JOURNEY COST APPROX.
#case2
total_cost_of_flight_tciket = 5*distance*person
total_updown_flight = 2*total_cost_of_flight_tciket

#UP-DOWN TRAIN JOURNEY COST APPROX.
#case
total_cost_of_uptrain_downflight = total_cost_of_flight_tciket + total_cost_of_train_tciket
total_updown_train = 2*total_cost_of_train_tciket
total_updown_flight = 2*total_updown_flight

print("The remaining money after expenses = " + str(remaining_money))
print("The up-down in train cost ="+ str(total_updown_train))
print("The up-down in flight cost ="+ str(total_updown_flight ))
print("The up-down in train+flight cost ="+ str(total_cost_of_uptrain_downflight))

print("waiting...fetching result")

if(remaining_money <= total_updown_train):
    print("You cant afford up down in Train")
else:
    print("You can afford up down in Train")
        

if(remaining_money <= total_cost_of_uptrain_downflight):
    print("You cant afford up in Train and down in flight or vice versa")
else:
    print("You can afford up in Train and down in flight or vice versa")    

if(remaining_money <= total_updown_flight):
    print("You cant afford up down flight ") 
else:
    print("You can afford up down flight ")