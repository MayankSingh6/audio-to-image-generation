# 🎤➡️🎨 Audio-to-Image Generation using AI

Convert spoken audio into AI-generated images using **Whisper (Speech-to-Text)** and **Stable Diffusion / DALL·E (Text-to-Image)**.

---

## 🚀 Overview

This project builds a **multimodal AI pipeline**:

🎤 Speech → 🧠 Text → 🎨 Image

It allows users to:
- Record audio directly from the browser
- Convert speech into text using Whisper
- Generate images from that text using AI models

---

## 🧠 Tech Stack

- **Streamlit** → Web UI  
- **OpenAI Whisper (local)** → Speech-to-text  
- **Stable Diffusion (local)** → Image generation  
- **DALL·E (optional)** → Cloud-based image generation  
- **PyTorch + Diffusers** → Model execution  

---

## 🔄 System Pipeline

1. User records audio  
2. Audio is saved locally  
3. Whisper transcribes speech → text  
4. Text is used as prompt  
5. Stable Diffusion generates image  
6. Image is displayed in UI  

---

## ⚙️ Implementation Details

### 🎤 Audio Recording
- Uses `sounddevice` to capture microphone input  
- Stores audio temporarily as `.wav`  

### 🧠 Speech-to-Text
- Whisper "tiny" model used for fast inference  
- Runs locally (no API required)  

### 🎨 Image Generation

Two approaches implemented:

#### 1. Local Stable Diffusion
- Model: `runwayml/stable-diffusion-v1-5`  
- GPU support if available  
- Uses attention slicing for optimization  

#### 2. OpenAI DALL·E (Optional)
- API-based image generation  
- Higher quality but requires API key 

---

## 📸 Results

### 🖼️ Generated Output 1
![Output1](result.png)

### 🖼️ Generated Output 2
![Output2](generated_image.png)

---

## 🧪 Sample Flow

**Input (spoken):**  
> "A futuristic city at sunset with glowing skyscrapers"

**Output:**  
→ AI-generated image based on prompt

---

## 📁 Code Structure

- `app.py` → Main Streamlit app 
- `generate_image.py` → DALL·E integration   
- `requirements.txt` → Dependencies   

---

## ▶️ How to Run

### 1. Clone repo
```bash
git clone https://github.com/MayankSingh6/audio-to-image-generation.git
cd audio-to-image-generation
pip install -r requirements.txt
streamlit run app.py
