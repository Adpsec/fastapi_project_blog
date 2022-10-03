from fastapi import APIRouter
from models.users_model import User

userRouter = APIRouter(
    tags=["Users"]
)

@userRouter.post("/user")
def createUser(user: User):
    pass 

