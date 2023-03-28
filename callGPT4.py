import openai

def askGPT(text):
    openai.api_key = "sk-"
    response = openai.Completion.create(
        engine = "davinci",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    return response.choices[0].text

def main():
    Q = 'What is the meaning of life?'
    # print('GPT: Ask me a question\n')
    # myQn = input()
    print(askGPT(Q))

main()
