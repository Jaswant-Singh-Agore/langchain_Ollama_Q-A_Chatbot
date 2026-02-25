import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

os.environ["LANCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Ollama"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are helpfull assistant, Please respond to user queries"),
        ("user", "Question: {question}")
    ]
)


def generate_response(question, model_name, temperture, max_tokens):
    model = ChatOllama(
        model=model_name,
        temperature=temperture,
        num_predict=max_tokens,
    )

    outpout_parser = StrOutputParser()
    chain = prompt | model | outpout_parser
    
    return chain.invoke({"question": question})



# Streamlit UI
st.title("Enhanced Q&A Chatbot With Ollama")

# Sidebar
st.sidebar.title("Settings")

models = ["phi3:mini", "nomic-embed-text:latest", "gemma3:latest"]
model_name = st.sidebar.selectbox("Select Model", models)
model = ChatOllama(model=model_name)

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 50, 500, 150)

# Main Interface
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(
        user_input,
        model_name,
        temperature,
        max_tokens,
    )
    st.write(response)
else:
    st.write("Please provide user input.")
