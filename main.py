from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
app.title = "My First API"

@app.get("/")
def message():
    return JSONResponse(content={"message": "Hello World"})