from fastapi import FastAPI, Request
from auth.common import JWTBearer, sign_jwt, lifespan

app = FastAPI(lifespan=lifespan)

app.middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
)

app.middleware(LoggingMiddleware)

@app.get("/")
def index():
    return {"success": True, "message": "Success!"}

