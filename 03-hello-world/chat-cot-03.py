from dotenv import load_dotenv
load_dotenv()
import json
from openai import OpenAI

client = OpenAI()

#Chain of Thought Prompting: The model is encouraged to break down the reasoning step by step before arriving at a answer.

SYSTEM_PROMPT =  """
You are an helpful AI assistant who is helpful in resolving user query.
For the given user input, analyse the input and break down the problem step by step.

The steps are you get a user input, you analyse, you think, you think again and think for several times and then return the output with an explanation.

Follow the steps in sequence that is "Analyse", "Think", "Output", "Validate" and finally "Result".

Rules: 
1. Follow the strict JSON output as per schema.
2. Always perform one step at a time and wait for the next input.
3. Carefuly analyse the query, 

Output Format: 
{{"step": "string","content":"string"}}

Example:
Input: What is "2 + 2 ? 
Output: {{"step":"analyse","content":"Alright the user in interested in maths query and he is asking a basic arthemetic operation"}}
Output: {{"step":"think","content":"To perform this addition , I must go from left to right and add all the operands"}}
Output: {{"step":"output","content":"4"}}
Output: {{"step":"validate","content":"Seems like 4 is correct answer for 2 + 2"}}
Output: {{"step":"result","content":"2 + 2  = 4 and this is calculated by adding all numbers"}}
"""
# response = client.chat.completions.create(
#     model = "gpt-4.1-mini",
#     response_format={"type": "json_object"},
#     messages = [
#         {"role":"system","content":SYSTEM_PROMPT},
#         {"role":"user","content": "What is 5 / 2 * 3 to the power 4 ?"},
#         {"role":"assistant","content": json.dumps({"step":"analyse","content":"The user is asking for the result of the mathematical expression 5 divided by 2, multiplied by 3 raised to the power of 4."})},
#         {"role":"assistant","content": json.dumps({"step": "think", "content": "I need to follow the order of operations (PEMDAS/BODMAS). First, calculate the exponent 3^4, then perform the division 5/2, and finally multiply the results."})},   
#         {"role":"assistant","content": json.dumps({"step": "output", "content": "3^4 = 81; 5/2 = 2.5; then 2.5 * 81 = 202.5"})},
#         {"role":"assistant","content": json.dumps({"step": "validate", "content": "Calculating 3^4 = 81 is correct, 5/2 = 2.5 is correct, multiplying 2.5 by 81 results in 202.5 which is the correct final answer."})}
#     ]
# )
# print("\n\n🤖: ", response.choices[0].message.content,"\n\n")


messages = [
    {"role": "system","content": SYSTEM_PROMPT}
]

query = input("> ")
messages.append({"role":"user","content":query})

while True : 
    response = client.chat.completions.create(
        model = "gpt-4.1",
        response_format={"type": "json_object"},
        messages=messages
    )

    messages.append({"role":"assistant","content":response.choices[0].message.content})
    parsed_response = json.loads(response.choices[0].message.content)

    if parsed_response.get("step") != "result":
        print("       🧠:",parsed_response.get("content"))
        continue

    print("🤖: ",parsed_response.get("content"))
    break







'''
 {"role":"assistant","content": "Hi Vivek ! How can I assist you today ? "},
        {"role":"user","content": "What is my name? "},
        {"role":"assistant","content": "Your name is Vivek. How can I help you further, Vivek? "},
        {"role":"user","content": "How are you ? "}

'''