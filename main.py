from fastapi import FastAPI
from routes.index_routes import indexRouter
from routes.blog_routes import blogRouter
from routes.user_routes import userRouter
from database.db import getConnection

app = FastAPI(
    description="Simple REST API for Blog",
    version="0.0.1"
)

app.include_router(indexRouter)
app.include_router(blogRouter)
app.include_router(userRouter)
