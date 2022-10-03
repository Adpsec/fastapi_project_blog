from fastapi import APIRouter, Query
from models.post_model import Post

blogRouter = APIRouter(
    tags=["Blog"]
)
global idPost

@blogRouter.get('/blog')
def getBlogs(limit: int | None = Query(default=None)):
    blogsLimit = limit
    if blogsLimit != None:
        return {"No of Posts": blogsLimit}
    else:
        return {"message": "All published Posts"}
    

@blogRouter.get('/blog/unpublished')
def getPostsUnpublished():
    return {"Postsunpublished": ['A', 'B', 'C']}

@blogRouter.get('/blog/{id}')
def getPostById(id: int):
    idPost = id
    return {"ID blog": idPost}

@blogRouter.get('/blog/{id}/comments')
def getCommentsPost(id: int):
    idBlog = id
    pass

@blogRouter.post('/blog')
def createPost(post: Post):
    return {"Title": post.title}