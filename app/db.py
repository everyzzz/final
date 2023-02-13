from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://root:root@rickandmorty.ofyi9c4.mongodb.net/?retryWrites=true&w=majority')

db = client["rickandmorty"]
