from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]='true'
os.environ["LANCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You re a helpful assistant. Please respond to the user queries."),
        ("user","Question:{question}")
    ]
)

st.title('Langchain Demo with Phi 3 api')
input_text = st.text_input('Search the topic you want')

llm = Ollama(model='phi3')
op = StrOutputParser()
chain = prompt|llm|op
if input_text:
    st.write(chain.invoke({'question':input_text}))