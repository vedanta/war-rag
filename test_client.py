from llm_client import LLMClient

llm = LLMClient()
response = llm.chat([
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the capital of Colorado ?"}
])

print(response)

