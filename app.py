import streamlit as st
from pathlib import Path
import google.generativeai as genai
from system_prompt import system_prompt
from api_key import api_key

# ---- Configuration ----
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096
}

safety_settings = [
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": 2},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": 2},
    {"category": "HARM_CATEGORY_SEXUAL", "threshold": 2},
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# ---- Streamlit UI ----
st.set_page_config(page_title="Medical Diagnosis", page_icon=":robot:")
st.image("Logo.png", width=200)

st.title("Medical Diagnosis Analytics")
st.subheader("AI assist in users to identify diseases using Images")

upload_file = st.file_uploader("Upload medical image", type=["jpg", "jpeg", "png"])

if upload_file:
    st.image(upload_file, width=300, caption="Uploaded Image")

    if st.button("Generate Analysis"):
        # Convert image to byte stream
        image_data = upload_file.getvalue()

        # Prepare Gemini image format
        gemini_image = {
            "mime_type": "image/jpeg",
            "data": image_data
        }

        # Combine system prompt and image
        prompt_parts = [
            {"text": system_prompt},
            gemini_image
        ]

        # Generate content
        st.title("🧠 AI Diagnostic Report")
        try:
            response = model.generate_content(prompt_parts)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error during analysis: {e}")
