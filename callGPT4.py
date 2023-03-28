import requests

def generate_text(prompt, api_key, model="gpt-4"):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "prompt": prompt,
        "max_tokens": 100, # Adjust this value depending on your desired output length
    }
    
    response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        generated_text = result["choices"][0]["text"].strip()
        return generated_text
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")


if __name__ == "__main__":
    api_key = "sk-"
    prompt = "What is the capital of France?"
    response_text = generate_text(prompt, api_key)
    print(response_text)
