import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Hello World!"}


# for Lambda environment
if os.getenv("LAMBDA_TASK_ROOT"):
    from mangum import Mangum

    handler = Mangum(app)
