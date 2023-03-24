import requests
import json

API_KEY = ""  # Replace this with your actual API key
API_ENDPOINT = "https://api.openai.com/v1/images/generations"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

data = {
    "prompt": "A beautiful sunset over a beach",  # Describe the image you want to generate
    "n": 1,  # Number of images you want to generate
    "size": "512x512",  # Output image size
    "model": "image-model",  # Replace with the desired image generation model
}

response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_data = response.json()
    images = response_data["data"]
    for idx, image in enumerate(images):
        with open(f"generated_image_{idx}.png", "wb") as f:
            f.write(image)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
