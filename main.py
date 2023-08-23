import os 
from dotenv import load_dotenv
import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator

load_dotenv()

app = FastAPI()
app.title = "My First API"
os.environ["OPENAI_API_KEY"] = os.getenv('API_KEY')

@app.post("/")
def message(query: str):
    try:
        loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
        index = VectorstoreIndexCreator().from_loaders([loader])
        answer = index.query(query)
        return JSONResponse(content={"message": answer})
    except:
        logging.exception("Error occurred:")
        return JSONResponse(content={"error": "An error ocurred"})