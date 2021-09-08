from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient,AsyncIOMotorDatabase

# client = AsyncIOMotorClient("mongodb+srv://buildfast:buildfast1011@cluster0.rnure.mongodb.net")
# client = MongoClient("mongodb+srv://buildfast:buildfast1011@cluster0.rnure.mongodb.net/outify?retryWrites=true&w=majority")
client = MongoClient("mongodb://localhost:27017/")
db = client.outify
