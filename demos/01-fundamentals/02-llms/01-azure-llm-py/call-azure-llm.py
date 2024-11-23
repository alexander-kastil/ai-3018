import os
import requests
import base64

# Configuration
API_KEY = "8h0NMkksgPB5boQGE8LyDFRdA2RogW0ilBX9Ity3fslfZrB3IafyJQQJ99AKACHYHv6XJ3w3AAAAACOGpVur"
MODEL = "gpt-4o-mini"
ENDPOINT = f"https://ai-dev-openai767221091702.openai.azure.com/openai/deployments/{MODEL}/chat/completions?api-version=2024-02-15-preview"

headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Payload for the request
payload = {
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are an AI assistant that helps people find holiday."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Recommend places for beach holidays in winter"
        }
      ]
    }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 800
}

# Send request
try:
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Handle the response as needed (e.g., print or process)
print(response.json())