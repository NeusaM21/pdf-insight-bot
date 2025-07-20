import logging
from flask import Flask, request, Response
import google.generativeai as genai

# Configura o logger para registrar erros
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Função para carregar as informações do produto
def carregar_info_produto():
    """
    Carrega o conteúdo do arquivo 'infos_produto.txt'.
    Retorna:
        str: Conteúdo do arquivo.
    """
    try:
        with open("data/infos_produto.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        logging.error("Erro: O arquivo 'data/infos_produto.txt' não foi encontrado.")
        return "Informações do produto não disponíveis."
    except Exception as e:
        logging.error(f"Erro ao carregar informações do produto: {e}")
        return "Informações do produto não disponíveis."

# Rota principal que recebe a mensagem do WhatsApp e responde
@app.route("/webhook", methods=["POST"])
def responder():
    """
    Recebe mensagens do webhook do WhatsApp (Twilio), processa-as
    com o modelo Gemini e retorna uma resposta.
    """
    try:
        # Twilio envia a mensagem no campo "Body"
        mensagem = request.form.get("Body")
        logging.info(f"Mensagem recebida: {mensagem}")

        if not mensagem:
            logging.warning("Nenhuma mensagem recebida no corpo da requisição.")
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
        logging.info("Prompt gerado para o Gemini.")

        # Cria o modelo Gemini (modelo leve e gratuito)
        modelo = genai.GenerativeModel("gemini-1.5-flash")

        # Gera a resposta com base no prompt
        resposta = modelo.generate_content(prompt)
        logging.info("Resposta do Gemini recebida.")

        # Extrai o texto da resposta
        # Usa getattr para acesso seguro ao atributo 'text', com fallback se não existir
        resposta_texto = getattr(resposta, "text", "⚠️ Sem resposta gerada.")
        if "⚠️ Sem resposta gerada." in resposta_texto:
            logging.warning("O modelo Gemini não retornou um texto válido.")

        # Twilio espera um retorno simples em texto puro
        return Response(resposta_texto, mimetype="text/plain")

    except Exception as e:
        # Loga o erro detalhado para depuração interna
        logging.error(f"Erro inesperado no webhook: {e}", exc_info=True)
        # Retorna uma mensagem genérica para o usuário/Twilio
        return Response("❌ Ocorreu um erro interno. Por favor, tente novamente mais tarde.", mimetype="text/plain"), 500

# Executa o servidor Flask
if __name__ == "__main__":
    # ATENÇÃO: debug=True NUNCA deve ser usado em ambiente de produção,
    # pois pode expor vulnerabilidades e detalhes internos do servidor.
    # Use um servidor WSGI (como Gunicorn ou uWSGI) para produção.
    app.run(debug=True)

