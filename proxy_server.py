from flask import Flask, request, jsonify
import openai
import os
app = Flask(__name__)

@app.route("/request/openai/deployments/GPT4-8k/chat/completions", methods=["POST"])
def process_request():
    try:
        helicone_auth = request.headers.get("authorization-key")
        user_name = request.headers.get("user-id")
        prompt = request.headers.get("prompt-text")
        print(helicone_auth)
        openai.api_type  = "azure"
        openai.api_version  = "2023-03-15-preview"
        openai.api_key  = "azure_api_key"
        openai.api_base = "https://oai.hconeai.com"


        delta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        headers={
        "Helicone-Auth": helicone_auth,
        "Helicone-User-Id": user_name,
        "Helicone-OpenAI-Api-Base": "https://bvruseast.openai.azure.com/",
            },
        engine="GPT4-8k",
        )
        return delta.choices[0].message
    
    except Exception as e:
        error_message = str(e)
        print(error_message)
        return jsonify({"error": error_message})

if __name__ == "__main__":
    app.run(port=2451)
