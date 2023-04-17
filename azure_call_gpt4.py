import os
import openai
openai.api_key = "sk-"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Who are you? and what model are you using?"},
    ]
)

print(response)

print(response['choices'][0]['message']['content'])