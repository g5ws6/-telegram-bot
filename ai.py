import requests

def ask_ai(message):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json",
    }

    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]

    return "حدث خطأ أثناء الاتصال بالذكاء الاصطناعي."
