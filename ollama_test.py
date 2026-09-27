import ollama

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "write few lines about prabhas."
        }
    ]
)

print(response["message"]["content"])
