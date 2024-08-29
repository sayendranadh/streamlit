import streamlit as st
import random
from PIL import Image
import base64

# Sample quotes
quotes = [
    "The best way to predict the future is to invent it. - Alan Kay",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs"
]

# Function to get a random quote
def get_random_quote():
    return random.choice(quotes)

# Function to get base64 encoding of an image
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Title of the app
st.title("Random Quote Generator")

# Display an image
image_path = r'C:\Users\sayen\Downloads\pexels-suzyhazelwood-1629236.jpg'  # Use raw string
base64_image = get_base64_image(image_path)

# Generate quote button
if st.button("Generate Quote"):
    quote = get_random_quote()
    st.markdown(
        f"""
        <div style="position: relative; text-align: center; color: white;">
            <img src="data:image/jpeg;base64,{base64_image}" style="width: 100%; height: auto;">
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 24px; font-weight: bold; background-color: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 10px;">
                {quote}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Add some styling
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        padding: 10px 24px;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)