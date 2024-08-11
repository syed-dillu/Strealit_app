import streamlit as st

st.title("Streamlit App")

user_name = st.text_input("Enter your name:")

if st.button("Submit"):
    st.write(f"Hello, {user_name}!")

age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is: {age}")

hobby = st.checkbox("Do you like coding?")
if hobby:
    st.write("That's awesome! Coding is fun!")

option = st.selectbox("What's your favorite programming language?", 
                      ["Python", "JavaScript", "Java", "C++", "Other"])
st.write(f"You selected: {option}")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(f"Uploaded file: {uploaded_file.name}")
