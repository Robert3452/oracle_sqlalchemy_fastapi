from fastapi import FastAPI, Depends
from routes.user import user
from routes.product import product
import uvicorn

app = FastAPI()

app.include_router(user)
app.include_router(product)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
