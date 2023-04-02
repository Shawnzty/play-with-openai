import openai

openai.api_key = "sk-"

def askGPT(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[],
        prompt=text,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

def main():
    Q = 'What is the meaning of life?'
    print(askGPT(Q))

if __name__ == '__main__':
    main()