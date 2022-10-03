from pydantic import BaseModel
from datetime import date

class Post(BaseModel):
    title: str
    author: str
    publicationDate: date
    category: str
    tags: list[str] = []
    published: bool
    
class PostResponse(BaseModel):
    title: str 
    author: str 
    publicationDate: date
    
