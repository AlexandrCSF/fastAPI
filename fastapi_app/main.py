import uvicorn
from core.logger import logger
from fastapi import FastAPI

from fastapi_app.serializers import RequestCalcModel


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/calc")
async def calc(body: RequestCalcModel):
    num2 = body.num2 if body.num2 is not None else 0
    logger.info(f" num1 :{body.num1}, num2: {num2}. sum: {body.num1 + num2}")
    return {"sum": body.num1 + num2}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
