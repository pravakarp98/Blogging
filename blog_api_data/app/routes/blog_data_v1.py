import jwt
from fastapi import APIRouter, Depends
# from fastapi.response import JSONResponse
# from auth.common import sign_jwt, create_jwt_tokens

router = APIRouter(prefix="/api/blog-data/v1", tags=["blog-data"])

@router.get("/blog-data")
async def get_blog_data():
    return {"success": True, "message": "Returning blog data"}