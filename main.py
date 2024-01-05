from fastapi import FastAPI
import uvicorn

from src.routes import find_verify_email


app = FastAPI()
app.include_router(find_verify_email.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)