from fastapi import APIRouter
from models.users_model import User, UserResponse
from helpers.cypher import cypherPassword
from database.db import getConnection
from schemas.user_schema import userEntity

userRouter = APIRouter(
    tags=["Users"]
)

conn = getConnection()

def verifyUser(username):
    userFounded = conn.local.user.find_one({"username": username})
    if userFounded:
        return True
    else:
        return False

@userRouter.post("/user", response_model=User, tags=['Users'])
def createUser(user: User):
    newUser = dict(user) 
    newUser['password'] = cypherPassword(newUser['password'])
    del newUser['id']
    
    try:
        userStatus = verifyUser(newUser['username'])
        if userStatus:
            id = conn.local.user.insert_one(newUser).inserted_id
            user = conn.local.user.find_one({"_id": id})
            return {"message": "User created", "User": userEntity(user)}
        else:
            return {"message:" "User already exist"}    
    except Exception as e:
        return {"message:" "Error: ", e}
    

@userRouter.get("/user/{username}", response_model=UserResponse, tags=['Users'])
def getUserByUsername(username: str):
    return userEntity(conn.local.user.find_one({"username": username}))