import streamlit as st
from gemini_utils import generate_script

st.set_page_config(page_title="🎬 YouTube Script Generator", layout="centered")

st.title("🎬 YouTube Script Generator with Gemini AI")
st.write("Enter a topic and audience — get a scene-by-scene YouTube script!")

topic = st.text_input("🎯 Enter Topic", placeholder="e.g. How to Start Investing at 18")
audience = st.text_input("👥 Target Audience", placeholder="e.g. Teenagers, Beginners")

if st.button("Generate Script") and topic and audience:
    with st.spinner("Generating with Gemini..."):
        script = generate_script(topic, audience)
        st.success("✅ Script generated!")
        st.text_area("📄 Your Script", script, height=500)

        # Download
        st.download_button("⬇️ Download Script", data=script, file_name="youtube_script.txt")
