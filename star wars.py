import requests
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.starwars
collection = db.characters

# Clear existing data in the collection
collection.delete_many({})

# Fetch data from SWAPI
base_url = "https://swapi.dev/api/people/"

characters = []
while base_url:
    response = requests.get(base_url)
    data = response.json()
    characters.extend(data['results'])
    base_url = data['next']

# Insert data into MongoDB
collection.insert_many(characters)

print(f"Inserted {len(characters)} characters into the 'characters' collection.")
