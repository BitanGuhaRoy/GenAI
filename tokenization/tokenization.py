import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, this is a test"
tokens = enc.encode(text)

print(tokens)
print("Token count:", len(tokens))
