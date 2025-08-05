import streamlit as st
import os
import subprocess
import gdown
import zipfile

st.set_page_config(page_title="Voice to Video Generator", layout="centered")

# Step 1: Download models if not present
def download_models():
    if not os.path.exists("checkpoints"):
        st.info("Downloading model files... (only once)")
        gdown.download("https://drive.google.com/uc?id=1WzNePOp0-Dfp3bfPtNOZy7AjpFe34dqw", "checkpoints.zip", quiet=False)
        with zipfile.ZipFile("checkpoints.zip", 'r') as zip_ref:
            zip_ref.extractall("checkpoints")

download_models()

# UI
st.title("🎥 Voice to Talking Face Generator")
st.write("Upload a face image and a voice clip. AI will generate a talking face video!")

image_file = st.file_uploader("Upload Image (jpg/png)", type=["jpg", "png"])
audio_file = st.file_uploader("Upload Audio (wav)", type=["wav"])

if st.button("Generate Video"):
    if image_file and audio_file:
        with st.spinner("Processing... Please wait (1-2 mins)"):
            os.makedirs("input", exist_ok=True)
            with open("input/image.jpg", "wb") as f:
                f.write(image_file.read())
            with open("input/audio.wav", "wb") as f:
                f.write(audio_file.read())

            # Simulated SadTalker processing
            # Replace below command with actual SadTalker processing
            st.info("Simulating video generation... (replace with real SadTalker command)")
            subprocess.run(["echo", "Running SadTalker..."], capture_output=True)

            st.video("sample.mp4")  # Replace with actual video path
            st.success("Video generated successfully!")
    else:
        st.warning("Please upload both image and audio.")
