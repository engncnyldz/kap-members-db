from . import models
from fastapi import FastAPI
from .database import engine
from .routers import member


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(member.router)

@app.get("/")
def root():
    return {"message": f"Welcome to KAP Members DB application, go to {member.router.prefix} to list all members exist in the database."}


