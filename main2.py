import streamlit as st
import os
from PIL import Image, UnidentifiedImageError
import requests
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="Textile Section",
    page_icon="🛍️",
    layout="wide",
)

# Path to the logo image file
logo_path = 'mynta_logo.png'

# Check if the logo image file exists
if os.path.exists(logo_path):
    st.image(logo_path, width=250)
else:
    st.warning("Logo image not found. Please ensure 'mynta_logo.png' is in the same directory as this script.")

# Title of the website
st.title("Textile Section")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ["Home", "Design Your Dream Dress"])

# Home page
if page == "Home":
    st.header("Explore Our Vast Variety of Textiles")
    
    # Sample textile data with image paths
    textiles = [
        {"image": "cotton.png", "name": "Cotton", "price": "90/m"},
        {"image": "silk.png", "name": "Silk", "price": "300/m"},
        {"image": "lace.png", "name": "Lace", "price": "185/m"},
        {"image": "wool.png", "name": "Wool", "price": "600/kg"},
        {"image": "chiffon.png", "name": "Chiffon", "price": "2003/m"},
        {"image": "crepe.png", "name": "Crepe", "price": "216/m"},
        {"image": "denim.png", "name": "Denim", "price": "699/m"},
        {"image": "velvet.png", "name": "Velvet", "price": "255/m"},
        {"image": "rayon.png", "name": "Rayon", "price": "255/m"},
        {"image": "satin.png", "name": "Satin", "price": "255/m"},
    ]

    # Create a grid layout using columns
    num_columns = 3
    columns = st.columns(num_columns)
    for idx, textile in enumerate(textiles):
        with columns[idx % num_columns]:
            if os.path.exists(textile["image"]):
                st.image(textile["image"], width=200)
            else:
                st.warning(f"Image for {textile['name']} not found.")
            st.subheader(textile["name"])
            st.write(f"Price: {textile['price']}")

# Function to generate images from Bing Image Creator
def generate_images(prompt):
    U_cookie_api_key_value = '1qrzH2Ny4oXLJHwvjBjMbExX4dHBK1HW6YvNRc2cbLkZbkqkjbolasRo9o6AJNGuDO2E5Q1vRIjFcdNSdBrZ7IVA2MqxbYQqezL5u0l0g5HYsg8BcaaV_E_Fr-Uhs02qUl7ww_wFn9HU_-V9dKzsBuyCuz8s2LU99aGUQm80vZ6nSOnbC9TR97y_j9IuaQnWCcxykxrsnwSJlV7308-oTC09STBDkZV6nK1nItLIbpw8'
    command = f'python -m BingImageCreator --prompt "{prompt}" -U "{U_cookie_api_key_value}"'
    os.system(command)

    # Assuming the command outputs URLs of generated images
    # Here we mock the URLs for demonstration purposes
    image_urls = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg",
        "https://example.com/image4.jpg",
        "https://example.com/image5.jpg"
    ]
    return image_urls

# Design Your Dream Dress page
if page == "Design Your Dream Dress":
    st.header("Design Your Dream Dress")
    
    # Text input for dress description
    dress_description = st.text_area("Describe your dream dress", height=150)
    
    if st.button("Generate Outfit"):
        st.write(f"Your description: {dress_description}")
        
        # Generate images
        image_urls = generate_images(dress_description)
        displayed_images = 0

        for image_url in image_urls:
            if displayed_images >= 3:
                break
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content))
                st.image(img, width=300)
                img_byte_arr = BytesIO()
                img.save(img_byte_arr, format='JPEG')
                img_byte_arr = img_byte_arr.getvalue()
                
                # Provide download button for each generated image
                st.download_button(
                    label="Download Image",
                    data=img_byte_arr,
                    file_name="generated_outfit.jpg",
                    mime="image/jpeg"
                )
                displayed_images += 1
            except (UnidentifiedImageError, requests.RequestException):
                st.warning(f"Could not load image from {image_url}.")
