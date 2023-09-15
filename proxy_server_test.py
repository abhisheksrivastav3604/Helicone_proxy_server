import openai

openai.api_type  = "azure"
openai.api_version  = "2023-03-15-preview"
openai.api_key  = "dvdffbfgbfb"
openai.api_base = "http://127.0.0.1:2451/request"

# Create the completion request
delta = openai.ChatCompletion.create(
    headers={
        "authorization-key": "Bearer sk-helicone-kjll5bq-ywceloy-ujfo7ea-5jh7wwq",
        "user-id": "Abhishek Srivastav",
        "prompt-text": "Hii!!"
    },
    engine="GPT4-8k",
)
print(delta)
