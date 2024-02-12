import time as t

import numpy as np
import pandas as pd

import streamlit as st

st.title("Title")

st.header("Header")

st.subheader("Sub Header")

st.info("Info")

st.warning("Warning")

st.error("Error")

st.success("Success")

st.write("Write")

st.markdown("# Markdown 1")
st.markdown("## Markdown 2")
st.markdown("### Markdown 3")

st.markdown(":moon:")

st.text("Text")
st.text_input("Text Input")
st.text_area("Text Area")

st.caption("Caption")

st.latex("a+b^2")

st.image("Portfolio.png")

st.checkbox("Checkbox")

st.button("Button")

st.radio("Radio", ["R", "A", "D", "I", "O"])

st.selectbox("Select Box", ["S", "B"])

st.multiselect("Multi Select", ["M", "S"])

st.select_slider("Select Slider", [0, 1, 2, 3, 4, 5])
st.slider("Slider")  # 0-100 By Default
st.slider("Slider", 5, 10)

st.number_input("Number Input")
st.number_input("Number Input", 0, 100)

st.date_input("Date Input")

st.time_input("Time Input")

st.file_uploader("File Uploader")

st.color_picker("Color Picker")

st.progress(90)

# with st.spinner("Wait"):
#     t.sleep(1)

st.balloons()

st.sidebar.title("Sidebar")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password")
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
submit_button = st.sidebar.button("Submit")

if (submit_button and len(username) > 0 and len(password) > 0):
    st.write("Username: ", username)
    st.write("Password: ", password)
    st.write("Gender: ", gender)
    st.info("User Successfully Logged In!")
else:
    st.error("Please Fill The Required Details!")

st.title("Bar Chart")
data = pd.DataFrame(np.random.randn(50, 2), columns=["X", "Y"])
st.bar_chart(data)

st.title("Line Chart")
st.line_chart(data)
