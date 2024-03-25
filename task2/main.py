from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def fastapi_hello_world():
    return "Hello, World!"