import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Summarize in 3 concise business lines: {text}"}],
            max_tokens=100
        )
        return response['choices'][0]['message']['content']
    except:
        return "Summary unavailable."
