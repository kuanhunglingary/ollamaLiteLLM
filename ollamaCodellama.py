import ollama

stream = ollama.chat(
    model="codellama",
    messages=[
        {
            "role": "user",
            "content": "Write a python script to output numbers 1 to 100 and then the user_proxy agent should run the script",
        }
    ],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
