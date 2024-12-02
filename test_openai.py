# import requests

# api_key = "AIzaSyAFA4fmbv-dOEJgj8q_qIXVVgxaA_Wgcsw"
# url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

# headers = {
#     "Content-Type": "application/json"
# }

# body = {
#     "contents": [
#         {
#             "parts": [
#                 {
#                     "text": "Generate 3 interview questions for a software developer"
#                 }
#             ]
#         }
#     ]
# }

# response = requests.post(url, headers=headers, json=body)

# if response.status_code == 200:
#     print("Response:", response.json())
# else:
#     print(f"Error: {response.status_code}, {response.text}")
