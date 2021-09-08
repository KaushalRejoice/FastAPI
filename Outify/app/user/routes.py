from fastapi import APIRouter, HTTPException
from bson.objectid import ObjectId
from pydantic.utils import Obj
from pymongo import collection
from .utils import ToJson, to_dict, to_list_of_dict
from bson import ObjectId

from .models import User
from .db import db

user = APIRouter()

# To get all the users
@user.get('/api/v1/user/')
async def get_all_user():
    collection = db["user"]
    users = collection.find()
    return to_list_of_dict(users)


# To get specific user
@user.get('/api/v1/user/{id}')
async def get_user(id: str):
    collection = db['user']
    user = collection.find_one({'_id': ObjectId(id)})
    if user is not None:
        return to_dict(user)

    raise HTTPException(status_code=404, detail='Invalid username')
    
# To create new user
@user.post('/api/v1/user/')
async def create_user(user: User):
    collection = db['user']
    result = collection.insert_one(user.dict())
    user = collection.find_one({"_id": result.inserted_id})
    return to_dict(user)

# Update User
@user.put('/api/v1/user{id}')
async def update_user(id, user: User):
    collection = db['user']
    collection.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(user)})
    updated_user = collection.find_one({'_id': ObjectId(id)})
    return to_dict(updated_user)


# To delete specific user
@user.delete('/api/v1/user/{id}')
async def delete_user(id: str):
    collection = db['user']
    user = collection.find_one_and_delete({'_id': ObjectId(id)})
    if user is not None:
        return to_dict(user)

    raise HTTPException(status_code=404, detail='Invalid user ID')


# Test API routes
@user.get('/api/v1/test')
async def test_user():
    collection = db['user']
    user = collection.find_one({'name': 'test'})
    users = collection.find()
    return to_list_of_dict(users)


