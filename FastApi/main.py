from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FAST API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, name: str = None):
    return {"item_id": item_id, "name": name}

