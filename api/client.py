import requests
import streamlit as st

def get_gemma_resp(text):
    response = requests.post("http://localhost:8000/gemma/chat/invoke", json={'input':{'question':text}})
    return response.json()["output"]
def get_phi_resp(text):
    response = requests.post("http://localhost:8000/phi3/poem/invoke",json={'input':{'question':text}})
    return response.json()["output"]

st.title('Langchain demo with phi3 and gemma:2b')
text1 = st.text_input('Write a question')
text2 = st.text_input('Write a question about a poem')

if text1:
    st.write(get_gemma_resp(text1))
if text2:
    st.write(get_phi_resp(text2))