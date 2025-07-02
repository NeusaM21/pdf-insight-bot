from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configura a chave da API do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Inicializa o app Flask
app = Flask(__name__)

# Rota de teste
@app.route("/", methods=["GET"])
def home():
    return "✅ SmartBot com Gemini está rodando!"

# Rota principal que recebe a mensagem e responde com Gemini
@app.route("/webhook", methods=["POST"])
def responder():
    try:
        dados = request.get_json()
        mensagem = dados.get("mensagem", "")

        if not mensagem:
            return jsonify({"erro": "Nenhuma mensagem recebida"}), 400

        # Cria o modelo Gemini (modelo leve e gratuito)
        modelo = genai.GenerativeModel("gemini-1.5-flash")

        # Gera a resposta com base na mensagem
        resposta = modelo.generate_content(mensagem)

        # Garante que mesmo sem texto o bot responda algo seguro
        resposta_texto = getattr(resposta, "text", "⚠️ Sem resposta gerada.")

        return jsonify({
            "mensagem_usuario": mensagem,
            "resposta_bot": resposta_texto
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Executa o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)


