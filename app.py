import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv(override=True)

## For LangSmith Tracking
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY") or os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT") or os.getenv("LANGCHAIN_PROJECT")
 
## Usually optional for hosted LangSmith, but safe to set
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")

## Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer the following question."),
    ("user", "Question: {question}")
])

## Temperature is parameter of llm model, value between 0 to 1, where the higher value means the model will be more creative
def generate_response(question, api_key, llm, temperature, max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model=llm)

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    answer = chain.invoke({"question": question})
    return answer
