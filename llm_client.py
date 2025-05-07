import os
import requests
import json
from typing import List
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self):
        self.use_ollama = os.getenv("USE_OLLAMA", "true").lower() == "true"
        self.use_openai = os.getenv("USE_OPENAI", "false").lower() == "true"

        # Ollama config
        self.ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.ollama_model = os.getenv("OLLAMA_MODEL", "llama3")

        # OpenAI config
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

    def chat(self, messages: List[dict]) -> str:
        if self.use_ollama:
            return self._call_ollama(messages)
        elif self.use_openai:
            return self._call_openai(messages)
        else:
            raise ValueError("No LLM provider enabled. Set USE_OLLAMA or USE_OPENAI.")

    def _call_ollama(self, messages: List[dict]) -> str:
        url = f"{self.ollama_url}/api/chat"
        response = requests.post(url, json={
            "model": self.ollama_model,
            "messages": messages
        }, stream=True)

        content = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    if "message" in data:
                        content += data["message"].get("content", "")
                except Exception:
                    continue  # skip malformed lines

        return content.strip()

    def _call_openai(self, messages: List[dict]) -> str:
        import openai  # Lazy import
        openai.api_key = self.openai_api_key
        openai.api_base = self.openai_base_url

        response = openai.ChatCompletion.create(
            model=self.openai_model,
            messages=messages
        )
        return response.choices[0].message.content.strip()
