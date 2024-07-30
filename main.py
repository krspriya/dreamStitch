import streamlit as st
import os

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
        { "image": "cotton.png","name": "Cotton", "price": "90/m"},
        { "image": "silk.png", "name": "Silk", "price": "300/m"},
        { "image": "lace.png", "name": "Lace", "price": "185/m"},
        {"image": "wool.png","name": "Wool", "price": "600/kg"},
        { "image": "chiffon.png", "name": "Chiffon", "price": "2003/m"},
        { "image": "crepe.png", "name": "Crepe", "price": "216/m"},
        { "image": "denim.png", "name": "Denim", "price": "699/m"},
        { "image": "velvet.png", "name": "Velvet", "price": "255/m"},
        { "image": "rayon.png", "name": "Rayon", "price": "255/m"},
        { "image": "satin.png", "name": "Satin", "price": "255/m"},
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
            #st.write(f"Category: {textile['category']}")
            st.write(f"Price: {textile['price']}")
          #  st.write(f"Discount: {textile['discount']} off")

# Design Your Dream Dress page
elif page == "Design Your Dream Dress":
    st.header("Design Your Dream Dress")
    
    # Text input for dress description
    dress_description = st.text_area("Describe your dream dress", height=150)
    
    if st.button("Generate Outfit"):
        st.write(f"Your description: {dress_description}")
        
        # Here you would send the description to an API or a model to generate the outfit
        # For now, let's assume we generate a placeholder image
        outfit_image = "generated_outfit.jpg"  # Replace with actual generation logic or API call
        
        if os.path.exists(outfit_image):
            st.image(outfit_image, width=300)
        else:
            st.warning("Generated outfit image not found.")
