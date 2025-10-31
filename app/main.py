from fastapi import FastAPI
from app.api.routes import user
from app.api.routes import note_routes

app = FastAPI(title="Note App Backend")

app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(note_routes.router, tags=["Notes"])

@app.get("/")
def root():
    return {"message": "API is running"}
