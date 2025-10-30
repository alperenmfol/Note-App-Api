from fastapi import FastAPI
from app.api.routes import user

app = FastAPI(title="Note App Backend")

app.include_router(user.router, prefix="/user", tags=["User"])

@app.get("/")
def root():
    return {"message": "API is running"}
