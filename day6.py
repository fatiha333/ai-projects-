"""
Day 6
Your first AI program — talking to Gemini in Python
Goal: write code that sends a message to an AI and prints the response
1
Install Gemini library
pip3 install google-generativeai
2
Write a program that takes user input and gets an AI response
Ask user to type any question. Send it to Gemini. Print the answer. That's it. No UI yet. Just terminal. When this works you will feel it — this is the moment everything becomes real.
3
Make it loop — a basic chatbot in terminal
Wrap it in a while loop so the user can keep asking questions until they type "quit". You just built a chatbot. In Python. From scratch.
google-generativeai
API key setup
model.generate_content()
Get the exact starter code for Day 6 ↗

"""
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=""
)

def ask_ai(question):
    response = client.chat.completions.create(
        model="nex-agi/nex-n2-pro:free",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content
x=""
while(x!="quit"):
 x=input("enter a question")
 y=ask_ai(x)
 print(y)

