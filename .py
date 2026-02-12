import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- CONFIGURATION ---
# PASTE YOUR API KEY HERE BETWEEN THE QUOTES
GOOGLE_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"

# Configure the AI model
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- APP UI ---
st.set_page_config(page_title="SnapChef", page_icon="🍳")

st.title("🍳 SnapChef")
st.write("Snap a photo of your fridge or pantry. I'll tell you what to cook!")

# File Uploader
uploaded_file = st.file_uploader("Upload a photo of ingredients...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Your Ingredients', use_container_width=True)
    
    # The "Magic" Button
    if st.button("👨‍🍳 Find Recipes"):
        with st.spinner("Analyzing your ingredients..."):
            try:
                # The AI Prompt
                prompt = """
                Look at this image. 
                1. List the edible ingredients you see clearly.
                2. Suggest 3 distinct recipes I can make using MAINLY these ingredients.
                3. For each recipe, list the missing ingredients (if any) I might need (like spices or oil).
                
                Format the output nicely with bold headers and emojis.
                """
                
                # Generate content using Gemini Vision
                response = model.generate_content([prompt, image])
                
                # Display result
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.info("Make sure your API key is correct!")

# --- FOOTER ---
st.markdown("---")
st.caption("Powered by Gemini 1.5 Flash & Streamlit")

