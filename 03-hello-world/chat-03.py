from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI()

#Zero-shot Prompting: The model is given a direct question or task.

SYSTEM_PROMPT =  """
You are an AI Persona of Piyush Garg. You have to answer every question as if you are Piyush Garg ans sound natural and human tone.
Use the below examples to understand how Piyush talks and background about him.

Examples

User: Hi
Output: Hanjiiii

"""

response = client.chat.completions.create(
    model = "gpt-4.1-mini",
    messages = [
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content": "Hey, My name is Vivek"},
        {"role":"assistant","content": "Hey Vivek! How can I help you with Python today?"},
        {"role":"user","content": "How to make chocolate cake"},
        {"role":"assistant","content": "Hey Vivek, I’m a Python expert, not a chef! If you want help with Python code, I’m all ears. For chocolate cake, maybe Google is your best friend! 🍰😄"},
        {"role":"user","content": "How to write code in python to add two numbers ? "},
    ]
)

print(response.choices[0].message.content)  