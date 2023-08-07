import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("true_images/my_photo.jpg", width=300)
with col2:
    st.title("Katerina Vasilakou")
    content = """
    Hi, I am Katerina! I will graduate from Kapodidtrian's Physics department in 2024 and I am currently 
    exploring the world of programming. The applications you see below were built with Python through an internet 
    course I took.
    """
    st.info(content)

content2 = "Here are some apps I have built with Python. Feel free to contact me!"
st.text(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("true_data.csv", sep=";")

with col3:
    for index, row in df[:8].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("true_images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[8:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("true_images/" + row["image"])
        st.write(f"[Source code]({row['url']})")






