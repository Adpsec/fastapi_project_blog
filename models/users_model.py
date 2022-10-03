from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    name: str 
    gender: str | None = None
    username: str
    password: str 
    created_at: date | None = None
    
    
class UserInDB(BaseModel):
    username: str
    password_hash: str 
    
class UserLogin(BaseModel):
    username: str 
    password: str 
    
class UserResponseId(BaseModel):
    id: str 
    
class UserResponse(BaseModel):
    status: str
    user: UserResponseId
    

    