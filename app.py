import os
import streamlit as st
import sounddevice as sd
import soundfile as sf
import tempfile
import whisper
import torch
from diffusers import StableDiffusionPipeline

st.set_page_config(page_title="Sound to Image Generator", page_icon="🎤")
st.title("🎤🔊 Sound to Image Generator (Local Whisper + Stable Diffusion)")

# --- Load Whisper ---
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("tiny")

whisper_model = load_whisper_model()

# --- Load Stable Diffusion ---
@st.cache_resource
def load_sd_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = pipe.to(device)
    pipe.enable_attention_slicing()
    return pipe

sd_pipe = load_sd_model()

# --- Recording ---
duration = st.slider("🎙️ Recording Duration (seconds)", 2, 10, 5)
fs = 44100  # Sample rate

if st.button("Start Recording"):
    st.info("Recording... 🎙️ Speak now!")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    st.success("✅ Recording complete!")

    # Save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
        sf.write(tmpfile.name, audio, fs)
        audio_path = tmpfile.name

    st.audio(audio_path)

    # --- Transcribe ---
    st.subheader("🧠 Transcribing Speech to Text...")
    result = whisper_model.transcribe(audio_path)
    prompt = result["text"]
    st.success(f"Transcribed Text: {prompt}")

    # --- Generate Image ---
    st.subheader("🎨 Generating Image from Prompt...")
    with st.spinner("Generating image, please wait..."):
        image = sd_pipe(prompt).images[0]
        image_path = "generated_image.png"
        image.save(image_path)

    st.image(image_path, caption="🖼️ Generated Image")

