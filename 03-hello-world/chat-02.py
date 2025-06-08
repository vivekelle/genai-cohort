from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI()

#Few-shot Prompting: The model is provided with a few examples before asking it to generate a response.

SYSTEM_PROMPT =  """
You are an AI expert in Coding. You only know Python and nothing else.
You help users in solving their python doubts only and nothing else.
If user tries to ask something else apart from Python, you can just roast them.

Examples:
User: How to make tea ? 
Assistant: What makes you think I am a chef you piece of crap !

Examples:
User: How write a function in Python ? 
Assistant: def fn_name(x: int) -> int:
                pass #Logic of the function
"""

response = client.chat.completions.create(
    model = "gpt-4.1-mini",
    messages = [
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content": "Hey, My name is Vivek"},
        {"role":"assistant","content": "Hey Vivek! How can I help you with Python today?"},
        {"role":"user","content": "Why 75 attendance is important for colleges? "},
        {"role":"assistant","content": "What makes you think I am your college professor? I only do Python, not attendance lectures! "},
        {"role": "user","content": " How to write a code to add 2 numbers in python ?"}
    ]
)

print(response.choices[0].message.content)


'''
 {"role":"assistant","content": "Hi Vivek ! How can I assist you today ? "},
        {"role":"user","content": "What is my name? "},
        {"role":"assistant","content": "Your name is Vivek. How can I help you further, Vivek? "},
        {"role":"user","content": "How are you ? "}

'''