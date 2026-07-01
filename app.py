import streamlit as st
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
    llm = ChatOpenAI(api_key=api_key, model=llm, temperature=temperature, max_tokens=max_tokens)

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    answer = chain.invoke({"question": question})
    return answer


## Title of the app
st.title("Enhanced Q&A Chatbot with OpenAI")

## Sidebar settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")

model = st.sidebar.selectbox("Choose Model", ["gpt-4-turbo", "gpt-4", "gpt-4o", "gpt-4o-mini"])

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

max_tokens = st.sidebar.slider("Max Tokens", min_value=100, max_value=2048, value=500, step=50)

## Chat interface
user_input = st.text_area("Ask a question:")

## Generate response
if st.button("Generate Response"):
    if user_input:
        response = generate_response(user_input, api_key, model, temperature, max_tokens)
        st.write("Answer:", response)
    else:
        st.error("NO INPUT")