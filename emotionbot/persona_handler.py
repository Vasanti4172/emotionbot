import os
import requests
import json

API_KEY = "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"  # Replace with your real key
MODEL_NAME = "meta-llama/llama-3-8b-instruct"

def load_role_prompt(role):
    with open(f"roles/{role}.txt", "r", encoding="utf-8") as f:
        return f.read()

def query_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        data=json.dumps(payload)
    )

    try:
        res = response.json()
        if "choices" in res:
            return res["choices"][0]["message"]["content"]
        elif "error" in res:
            return f"❌ LLM Error: {res['error'].get('message', 'Unknown error')}"
        else:
            return f"⚠️ Unexpected response:\n{res}"
    except Exception as e:
        return f"❌ Exception: {e}\nRaw: {response.text}"

# Full bot response function with persona and mood
def respond_as(role, message, mood):
    role_prompt = load_role_prompt(role)
    full_prompt = f"{role_prompt}\nThe user seems {mood}. They said: {message}\nRespond empathetically."
    return query_openrouter(full_prompt)



'''def load_role_prompt(role):
    with open(f"roles/{role}.txt", "r", encoding="utf-8") as f:
        return f.read()

def respond_as(role, message, mood):
    role_prompt = load_role_prompt(role)
    # Simple simulated logic; replace with LLM call
    return f"{role_prompt}\n\nYou seem {mood}. Here's what I think:\n\n{message[::-1]}"  # reversed message for placeholder
'''
'''import os
import google.generativeai as genai

# ✅ Use correct model name and setup
genai.configure(api_key="AIzaSyB_GK9IEWWNXAtGITSa-AG8sJXkf1lJft8")

def load_role_prompt(role):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "roles", f"{role}.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def respond_as(role, message, mood):
    role_prompt = load_role_prompt(role)
    full_prompt = f"{role_prompt}\n\nUser seems {mood}. They said: {message}\nRespond supportively."

    model = genai.GenerativeModel(
        model_name="models/gemini-pro"  # ✅ CORRECT model path
    )

    response = model.generate_content(full_prompt)
    return response.text.strip()'''

