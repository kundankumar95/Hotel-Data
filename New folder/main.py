import json
from pymongo import MongoClient
from pymongo.errors import PyMongoError

def print_hotel_details(price):
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017")
        db = client["Hotel_Detail"]
        collection = db["Data_Hotel"]

        # Load data from the JSON file
        with open(r'C:\Users\Kundan\Downloads\New folder (2)\data.json') as json_file:
            data = json.load(json_file)

        # Insert data into the MongoDB collection
        collection.insert_many(data)

        # Convert the user input price to a string to match the data type in MongoDB
        query = {"Room": {"$elemMatch": {"price": str(price)}}}

        # Set to keep track of processed hotels
        processed_hotels = set()

        # Retrieve matching documents
        matching_documents = collection.find(query)

        for document in matching_documents:
            hotel_name = document.get("name")

            # Check if the hotel has already been processed
            if hotel_name not in processed_hotels:
                processed_hotels.add(hotel_name)

                print("Hotel Name:", hotel_name)
                for room in document["Room"]:
                    print("Room Type:", room["type"])
                    print("Availability:", room["availability"])
                print("Location:", document.get("Location", "N/A"))
                print()

    except PyMongoError as e:
        print(f"MongoDB error: {e}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the room price.")

    finally:
        if 'client' in locals() and client is not None:
            client.close()

try:
    user_input_price = int(input("Enter the price of the room: "))
    print_hotel_details(user_input_price)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
