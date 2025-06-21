import uvicorn
from fastapi import FastAPI

from src.authorization.endpoints import router as user_router

app = FastAPI()
app.include_router(user_router)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
