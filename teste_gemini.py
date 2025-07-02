import requests
import json
import os
from dotenv import load_dotenv

# Carrega a chave do arquivo .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Modelo leve e gratuito
MODEL = "gemini-1.5-flash"

# URL da API Gemini
url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

# Mensagem de teste
mensagem = "Qual o horário de funcionamento de vocês?"

# Corpo da requisição
body = {
    "contents": [
        {
            "parts": [
                {"text": mensagem}
            ]
        }
    ]
}

# Cabeçalhos HTTP
headers = {
    "Content-Type": "application/json"
}

# Envio da requisição
response = requests.post(url, headers=headers, json=body)

# Tratamento da resposta
if response.status_code == 200:
    resposta = response.json()
    print("✅ Resposta do Gemini:")
    print(resposta["candidates"][0]["content"]["parts"][0]["text"])
else:
    print("❌ Erro ao chamar a API:")
    print(response.status_code)
    print(response.text)
