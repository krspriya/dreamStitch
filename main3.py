import streamlit as st
import os
from PIL import Image
from streamlit_image_zoom import image_zoom
import shutil
import time

# Set page configuration
st.set_page_config(
    page_title="Fabric Section",
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
st.title("Fabric Section")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ["Home", "Design Your Dream Dress"])

# Home page
if page == "Home":
   # st.header("Explore Our Vast Variety of Textiles")
    
    # Sample textile data with image paths
    textiles = [
        { "image": "cotton.png", "name": "Cotton", "price": "90/m" },
        { "image": "silk.png", "name": "Silk", "price": "300/m" },
        { "image": "lace.png", "name": "Lace", "price": "185/m" },
        { "image": "wool.png", "name": "Wool", "price": "600/kg" },
        { "image": "chiffon.png", "name": "Chiffon", "price": "2003/m" },
        { "image": "crepe.png", "name": "Crepe", "price": "216/m" },
        { "image": "denim.png", "name": "Denim", "price": "699/m" },
        { "image": "velvet.png", "name": "Velvet", "price": "255/m" },
        { "image": "rayon.png", "name": "Rayon", "price": "255/m" },
        { "image": "satin.png", "name": "Satin", "price": "255/m" },
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

# Function to check if an image is corrupted
def is_image_corrupted(filepath):
    try:
        img = Image.open(filepath)
        img.verify()
        return False
    except Exception:
        return True

# Function to generate images based on a prompt
def generate_images(prompt):
    U_cookie_api_key_value = '1qrzH2Ny4oXLJHwvjBjMbExX4dHBK1HW6YvNRc2cbLkZbkqkjbolasRo9o6AJNGuDO2E5Q1vRIjFcdNSdBrZ7IVA2MqxbYQqezL5u0l0g5HYsg8BcaaV_E_Fr-Uhs02qUl7ww_wFn9HU_-V9dKzsBuyCuz8s2LU99aGUQm80vZ6nSOnbC9TR97y_j9IuaQnWCcxykxrsnwSJlV7308-oTC09STBDkZV6nK1nItLIbpw8'

    # Update the prompt to specify no humans and focus on dress design
    command = f'python -m BingImageCreator --prompt "{prompt} - no humans, just the dress design, unique dress design, specific colors only" -U "{U_cookie_api_key_value}"'

    os.system(command)

    image_dir = "OUTPUT"
    images = os.listdir(image_dir)
    non_corrupted_images = []

    for image in images:
        image_path = os.path.join(image_dir, image)
        if not is_image_corrupted(image_path):
            non_corrupted_images.append(image)
            if len(non_corrupted_images) == 5:
                break

    return non_corrupted_images

# Initialize session state for storing images
if "generated_images" not in st.session_state:
    st.session_state.generated_images = []

# Function to delete all previous and corrupted images in the OUTPUT folder
def clean_output_folder():
    image_dir = "OUTPUT"
    if os.path.exists(image_dir):
        shutil.rmtree(image_dir)
    os.makedirs(image_dir)

# Design Your Dream Dress page
if page == "Design Your Dream Dress":
    st.header("Design Your Dream Dress")
    
    # Text input for dress description
    dress_description = st.text_area("Describe your dream dress", height=150)
    
    if st.button("Generate Outfit"):
        st.write(f"Your description: {dress_description}")
        
        # Clean the output folder
        clean_output_folder()
        
        # Show loader while generating images
        with st.spinner("Generating images, please wait..."):
            # Generate images based on the description
            image_list = generate_images(dress_description)
            time.sleep(5)  # Simulate image generation time
        
        # Display the generated images without rerunning the whole script
        if image_list:
            st.session_state.generated_images = image_list
            st.write("Generated images:")
            for image_file in st.session_state.generated_images:
                image_path = os.path.join("OUTPUT", image_file)
                if os.path.exists(image_path):
                    # Open the image using Pillow
                    img = Image.open(image_path)
                    # Display the zoomable image
                    image_zoom(img)
                    with open(image_path, "rb") as file:
                        st.download_button(
                            label="Download Image",
                            data=file,
                            file_name=image_file,
                            mime="image/jpeg"
                        )
        else:
            st.warning("No images generated or all generated images were corrupted.")
    
    # Option to generate next outfit
    if st.session_state.generated_images and st.button("Generate Next Outfit"):
        # Clear previous images
        st.session_state.generated_images = []
        st.experimental_rerun()
