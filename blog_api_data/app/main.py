from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from app.routes.blog_data_v1 import router as login_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"success": True, "message": "Success!"}

app.include_router(login_router)