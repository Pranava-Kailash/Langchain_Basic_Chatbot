from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Setting up the environment variables
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGSMITH_TRACING')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGSMITH_API_KEY')

# Writing the prompt template
prompt = ChatPromptTemplate.from_messages([
    {'role': 'system', 'content': 'You are a language model AI assistant. You can help me with my writing, answer questions, and provide information.'},
    {'role': 'user', 'content': 'Question:{question}'}
])

# Framework for the chatbot
st.title('LangChain Chatbot With OpenAI')
input_text = st.text_area('Enter your question here:')

# OpenAI LLM
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
