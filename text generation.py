import streamlit as st
from transformers import pipeline

# Page settings
st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🤖"
)

# Background color (Purple)
st.markdown("""
<style>
.stApp {
    background-color: #D8B4FE;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 AI Text Generator")
st.write("✨ Enter a sentence and let AI complete it!")

# Load AI model
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="distilgpt2"
    )

generator = load_model()

# Text input
prompt = st.text_area(
    "✍️ Enter your text:",
    placeholder="Example: Artificial Intelligence is changing the world because..."
)

# Generate button
if st.button("🚀 Generate"):
    if prompt.strip():
        result = generator(
            prompt,
            max_new_tokens=50,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.8
        )

        st.subheader("✨ Generated Text")
        st.write(result[0]["generated_text"])
    else:
        st.warning("⚠️ Please enter some text!")