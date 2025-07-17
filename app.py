from flask import Flask, request, Response
import google.generativeai as genai

app = Flask(__name__)

# Função para carregar as informações do produto
def carregar_info_produto():
    with open("data/infos_produto.txt", "r", encoding="utf-8") as f:
        return f.read()

# Rota principal que recebe a mensagem do WhatsApp e responde
@app.route("/webhook", methods=["POST"])
def responder():
    try:
        # Twilio envia a mensagem no campo "Body"
        mensagem = request.form.get("Body")

        if not mensagem:
            return Response("⚠️ Nenhuma mensagem recebida.", mimetype="text/plain"), 400

        # Carrega as informações do produto
        info_produto = carregar_info_produto()

        # Cria o prompt personalizado
        prompt = f"""
        Você é um assistente virtual de uma plataforma de cursos.
        Use as informações abaixo para responder perguntas dos clientes sobre os planos disponíveis.

        Informações do produto:
        {info_produto}

        Pergunta do cliente:
        {mensagem}
        """

        # Cria o modelo Gemini (modelo leve e gratuito)
        modelo = genai.GenerativeModel("gemini-1.5-flash")

        # Gera a resposta com base no prompt
        resposta = modelo.generate_content(prompt)

        # Extrai o texto da resposta
        resposta_texto = getattr(resposta, "text", "⚠️ Sem resposta gerada.")

        # Twilio espera um retorno simples em texto puro
        return Response(resposta_texto, mimetype="text/plain")

    except Exception as e:
        return Response(f"❌ Erro: {str(e)}", mimetype="text/plain"), 500

# Executa o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)


