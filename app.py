from flask import Flask, request, Response
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

# Rota principal que recebe a mensagem do WhatsApp e responde
@app.route("/webhook", methods=["POST"])
def responder():
    try:
        # Twilio envia a mensagem no campo "Body"
        mensagem = request.form.get("Body")

        if not mensagem:
            return Response("⚠️ Nenhuma mensagem recebida.", mimetype="text/plain"), 400

        # Cria o modelo Gemini (modelo leve e gratuito)
        modelo = genai.GenerativeModel("gemini-1.5-flash")

        # Gera a resposta
        resposta = modelo.generate_content(mensagem)

        # Extrai o texto da resposta
        resposta_texto = getattr(resposta, "text", "⚠️ Sem resposta gerada.")

        # Twilio espera um retorno simples em texto puro
        return Response(resposta_texto, mimetype="text/plain")

    except Exception as e:
        return Response(f"❌ Erro: {str(e)}", mimetype="text/plain"), 500

# Executa o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)


