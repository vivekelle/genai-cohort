import tiktoken

# Encoder : Converts text to tokens
enc = tiktoken.encoding_for_model("gpt-4o")

text = "I want chocolate cake."

tokens = enc.encode(text)
print(f"Tokens: {tokens}")


# Decoder : Converts tokens to text
decoded_text= enc.decode([40, 1682, 20162, 22162, 13]) 
print(f"Decoded Text: {decoded_text}")