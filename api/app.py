from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]='true'
os.environ["LANCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title='Lanchain Server',
    version='1.0',
    description = 'A simple API server'
)

add_routes(
    app,
    Ollama(model='gemma:2b'),
    path='/gemma'
)
model = Ollama(model='gemma:2b')
llm = Ollama(model='phi3')

prompt1 = ChatPromptTemplate.from_messages(
    [
        ("system","You re a helpful assistant. Please respond to the user queries."),
        ("user","Question:{question}")
    ]
)
prompt2 = ChatPromptTemplate.from_messages(
    [
        ("system","You re a helpful assistant. Please respond to the user queries as a poem."),
        ("user","Question:{question}")
    ]
)

add_routes(
    app,
    prompt1|model,
    path='/gemma/chat'
)

add_routes(
    app,
    prompt2|llm,
    path='/phi3/poem'
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)