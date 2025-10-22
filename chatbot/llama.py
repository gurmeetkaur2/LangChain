# LANGCHAIN_API_KEY="lsv2_xxx"
# OPENAI_API_KEY="sk-xxx"
# LANGCHAIN_PROJECT="chatbot-first"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# LangSmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

# creating chatbot
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please provide response to the user queries."),
        ("user","Question:{question}")
    ]
)

# streamlit framework
st.title("LangChain Demo With Llama2 API")
input_text=st.text_input("Search the topic you want")

#open AI LLM call
llm=ollama(model="llama2")
output_parser=StrOutputParser()

# chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))