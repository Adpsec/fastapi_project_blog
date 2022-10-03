from fastapi import APIRouter

indexRouter = APIRouter(
    tags=["Index"]
)

@indexRouter.get("/")
def goIndex():
    return {"message": "Bienvenido a la API"}
