from fastapi import FastAPI
from user.routes import user

app = FastAPI()
app.include_router(user)

