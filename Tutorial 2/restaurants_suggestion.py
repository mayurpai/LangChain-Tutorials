import os

import langchain_helper
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

st.set_page_config(page_title="Restaurant Name Generator")
selected_cuisine = st.sidebar.selectbox(
    "Pick A Cuisine", ("Indian", "French", "Japanese", "Greek"))


if (selected_cuisine):
    response = langchain_helper.generate_restaurant_name_and_items(
        selected_cuisine)
    st.header("Restaurant Name: " + response["restaurant_name"].strip())
    menu_items = response["menu_items"].strip().split(",")
    st.header("Menu Items")
    for items in menu_items:
        st.write("-", items)
