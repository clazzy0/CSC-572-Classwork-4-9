import streamlit as st
import openai
from dotenv import load_dotenv
import os
import requests
from PIL import Image
from io import BytesIO

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set page config
st.set_page_config(
    page_title="Italian Brainrot Generator",
    page_icon="🍝",
    layout="centered"
)

# Title and description
st.title("🍝 Italian Brainrot Image Generator 🍕")
st.markdown("""
Generate the most cursed Italian images you've ever seen! 
This AI will create images that would make any Italian nonna cry! 
""")

# Input for customization
topic = st.text_input("Enter a topic (optional):", "pizza")

# Generate button
if st.button("Generate Italian Brainrot Image"):
    if not openai.api_key:
        st.error("Please set your OpenAI API key in the .env file!")
    else:
        try:
            # Generate image prompt
            image_prompt = f"Create a humorous, cartoon-style illustration of an Italian scene about {topic}. Make it over-the-top and stereotypically Italian, with lots of pasta, pizza, and Italian flags. Style: digital art, vibrant colors, exaggerated expressions, meme-like quality."

            # Generate image using DALL-E 3
            image_response = openai.images.generate(
                model="dall-e-3",
                prompt=image_prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )

            # Display the generated image
            st.markdown("### Your Generated Italian Brainrot Image:")
            image_url = image_response.data[0].url
            
            # Download and display the image
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            st.image(img, caption="Italian Brainrot Visualization", use_column_width=True)

            # Add download button for the image
            st.download_button(
                label="Download Image",
                data=response.content,
                file_name="italian_brainrot.png",
                mime="image/png"
            )

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ and 🍝") 