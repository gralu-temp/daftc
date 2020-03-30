
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Pozdro Grzesiek! Zoba jaki diploj!"}

@app.get("/hello/{name}")
def root():
    return {"message": f"Hello {name}"}
