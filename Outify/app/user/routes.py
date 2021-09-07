from fastapi import APIRouter
from bson.objectid import ObjectId
from .utils import ToJson

from .models import User
from .db import db

user = APIRouter()

# To get all the users
@user.get('/api/v1/user/')
async def get_all_user():
    collection = db["user"]
    users = collection.find()
    res = ToJson()
    json_res = res.mongo_to_json(users, many=True)
    return json_res

# To get specific user
@user.get('/api/v1/user/{name}')
async def get_user(name: str):
    collection = db['user']
    user = collection.find_one({'name': name})
    res = ToJson()
    if user is not None:
        json_res = res.mongo_to_json(user) 
    else:
        json_res = res.dict_to_json({'message': 'Please enter valid user name'})
    return json_res
    
# To create new user
@user.post('/api/v1/user/')
async def create_user(user: User):
    collection = db['user']
    result = collection.insert_one(user.dict())
    # print(result.inserted_id)
    user = collection.find_one({"_id": result.inserted_id})
    res = ToJson()
    json_res = res.mongo_to_json(user)
    return json_res


# To delete specific user
@user.delete('/api/v1/user/{id}')
async def delete_user(id: str):
    collection = db['user']
    user = collection.find_one({'_id': ObjectId(id)})
    res = ToJson()
    if user is not None:
        collection.delete_one({'_id': ObjectId(id)})
        json_res = res.mongo_to_json(user)
    else:
        json_res = res.dict_to_json({'message': 'Please enter valid id'})
    return json_res


