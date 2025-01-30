from langchain_core.prompt import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

st.title("CHATBOT by Meera")
input_txt = st.text_input("Please enter your queries..")

prompt = ChatPromptTemplate.from_messages(
    [("system","You are a helpful AI Assistant, name is Meera's Assistant"),
     ("user","user query:{query}")
    ])
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({"query":input_txt}))
    
