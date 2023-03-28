import os
import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "sk-"
available_models = openai.Model.list()

# Extract and print the model IDs
for model in available_models["data"]:
    print(model.id)
