from llm.ollama_client import generate_response

prompt = "Explain what an ORM framework is in simple terms."

answer = generate_response(prompt)

print("\nLLM Response:")
print(answer)