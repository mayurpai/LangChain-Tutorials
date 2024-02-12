import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain

st.set_page_config(page_title="QnA 🌿")

btn = st.button("Create Knowledgebase")

if btn:
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])
