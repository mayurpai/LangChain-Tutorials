import os

import streamlit as st
from dotenv import load_dotenv
from langchain import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")


def get_open_ai_response(question):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.5,
                 model_name="text-davinci-003")
    response = llm(question)
    return response


def get_hugging_face_hub_response(question):
    llm = HuggingFaceHub(repo_id="google/flan-t5-large",
                         model_kwargs={"temperature": 0.3, "max_length": 64})
    prompt_template = PromptTemplate(
        input_variables=['country'], template="What Is The Capital Of {country}")
    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain.run(question)
    return response


st.set_page_config(page_title="QnA Demo")
st.header("LangChain Application")


input = st.text_input("Input: ", key="input")
submit = st.button("Ask The Question!")
# response = get_open_ai_response(input)
response = get_hugging_face_hub_response(input)


if submit:
    st.subheader("The Response Is: ")
    st.write(response)
