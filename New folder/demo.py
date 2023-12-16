from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from dataCollection import print_hotels_below_price_and_city

origin_location = input("Enter the original location:")
destination_location = input("Enter the destination:")

geolocator = Nominatim(user_agent="distance_calculator")

origin_coords = geolocator.geocode(origin_location)
destination_coords = geolocator.geocode(destination_location)

if origin_coords and destination_coords:

    distance = geodesic((origin_coords.latitude, origin_coords.longitude),
                       (destination_coords.latitude, destination_coords.longitude)).kilometers

 
    print(f"The distance between {origin_location} and {destination_location} is approximately {distance:.2f} kilometers.")
else:
    print("Location not found. Please check the provided locations.")

budget = int(input("Enter your total budget: "))
person = int(input("Enter the number of people travelling: "))

days = int(input("How many days do want?"))

expenses = int(input("Enter the amount you want to spend for food and others:"))


remaining_money = budget - expenses


total_cost_of_train_tciket = ((0.5)*distance*person)
total_updown_train = 2*total_cost_of_train_tciket

total_cost_of_flight_tciket = 5*distance*person
total_updown_flight = 2*total_cost_of_flight_tciket

total_cost_of_uptrain_downflight = total_cost_of_flight_tciket + total_cost_of_train_tciket
total_updown_train = 2*total_cost_of_train_tciket
total_updown_flight = 2*total_updown_flight


def calculate_rest_amount(case_value):
    if case_value == 1:
        return remaining_money - total_cost_of_train_tciket
    elif case_value == 2:
        if remaining_money <= total_cost_of_flight_tciket:
            print("You cant afford flight")
            return calculate_rest_amount(3)
        else:
            return remaining_money - total_cost_of_flight_tciket
    else:
        if remaining_money <= total_cost_of_uptrain_downflight:
            print("You cant afford up by flight and down by train or vice versa)")
            return calculate_rest_amount(1)
        else:
            return remaining_money - total_cost_of_uptrain_downflight
case_value = int(input("Enter a number (1: Train, 2: Flight, 3:upTrain & downFlight or vice-versa): "))

rest_amount = calculate_rest_amount(case_value)

price_per_day = rest_amount / days
print_hotels_below_price_and_city(destination_location, price_per_day)
