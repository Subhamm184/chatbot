# import requests
# API_TOKEN = "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"
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {API_TOKEN}"
# }
# payload = {
#     "inputs": "Generate 5 job interview questions for a Fresher with skills: python.",
#     "parameters": {"temperature": 0.7, "max_new_tokens": 500}
# }

# response = requests.post(
#     "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7b",
#     headers=headers,
#     json=payload
# )
# print(response.status_code, response.json())
import requests

API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7b"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

payload = {
    "inputs": "Generate 5 clear and concise job interview questions for a Fresher with skills: Python.",
    "parameters": {"temperature": 0.7, "max_new_tokens": 100}
}

response = requests.post(API_URL, headers=headers, json=payload)
if response.status_code == 200:
    response_json = response.json()
    if isinstance(response_json, list):
        generated_text = response_json[0].get("generated_text", "")
        questions = generated_text.split("\n\n")
        for question in questions:
            print(question.strip())
else:
    print(f"Error {response.status_code}: {response.json()}")
