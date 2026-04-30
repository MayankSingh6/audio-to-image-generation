from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="replace this with your OPENAI key")  # Replace with your key

def generate_image_from_text(prompt: str) -> str:
    prompt = prompt.strip() or "a robot eating an ice cream on Mars"

    print("🟡 Sending prompt to DALL·E:", prompt)
    try:
        # Use DALL·E 3 for high-quality generation
        response = client.images.generate(
            model="dall-e-3",           # or "dall-e-2"
            prompt=prompt,
            size="1024x1024",
            n=1
        )

        image_url = response.data[0].url
        print("✅ Image URL:", image_url)
        return image_url

    except Exception as e:
        print("❌ DALL·E request failed:", e)
        return None
