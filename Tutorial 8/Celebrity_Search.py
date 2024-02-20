# Integrate our code OpenAI API
import os

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain import HuggingFaceHub
from langchain.memory import ConversationBufferMemory

import streamlit as st

HUGGINGFACEHUB_API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"]

# streamlit framework

st.title('Celebrity Search Results')
input_text = st.text_input("Search the topic u want")

# Prompt Templates

first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# Memory

person_memory = ConversationBufferMemory(
    input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(
    input_key='person', memory_key='chat_history')
descr_memory = ConversationBufferMemory(
    input_key='dob', memory_key='description_history')

llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",  model_kwargs={"temperature": 0, "max_length": 64})
chain = LLMChain(
    llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)

# Prompt Templates

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="when was {person} born"
)

chain2 = LLMChain(
    llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)
# Prompt Templates

third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events happened around {dob} in the world"
)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt,
                  verbose=True, output_key='description', memory=descr_memory)
parent_chain = SequentialChain(
    chains=[chain, chain2, chain3], input_variables=['name'], output_variables=['person', 'dob', 'description'], verbose=True)


if input_text:
    st.write(parent_chain({'name': input_text}))

    with st.expander('Person Name'):
        st.info(person_memory.buffer)

    with st.expander('Major Events'):
        st.info(descr_memory.buffer)
