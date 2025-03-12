import streamlit as st #To create the UI of web app
import random #Libarary to generate random characters
import string #Libarary to use string characters

#Funtion to generate the password based on user preferences
def password_generator(length, use_digits, use_special_chars):
    characters = string.ascii_letters #Provides uppercase and lowercase letters
    if use_digits:
        characters += string.digits #Provides numbers (0-9)
    if use_special_chars:
        characters += string.punctuation #Provides special characters (e.g. !@#)
    #Generate the password of the specified length
    return ''.join(random.choice(characters) for _ in range(length)) 

#Streamlit UI
st.set_page_config(page_title="Password Generator", page_icon="🔒", layout="centered")

# Styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #E4599C !important;
        color: white !important;
        font-size: 18px !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
    }
    .stTextInput>div>div>input {
        font-size: 16px !important;
    }
    .stSlider>div {
        font-size: 16px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("## 🔑 Secure Password Generator")
st.write("Create strong and secure passwords instantly!")

#To select the length of password
length = st.slider("Select Password length", min_value=8, max_value=32, value=12)

#To include digits in password
use_digits = st.checkbox("Include Digits")

#To include special characters in password
use_special_chars = st.checkbox("Include Special Characters")

#Generating password conditionally
if st.button("🔐 Generate Password"):
    #Call the fuction to generate the password
    password = password_generator(length, use_digits, use_special_chars)
    #Display the password
    st.success("🔑 Your Secure Password:")
    st.code(password, language="")
    # #Button to copy the password
    # st.button("📋 Copy to Clipboard", key="copy_btn")

# Footer
st.write("---")
st.markdown("🚀 Built with 💖 by [**Aashra Saleem**](#)")

