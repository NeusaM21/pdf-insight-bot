import os
from dotenv import load_dotenv
import gradio as gr
import google.generativeai as genai

# Carrega variáveis do .env
load_dotenv()

# Configura a chave do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Função para carregar o conteúdo do PDF em texto
def carregar_info_produto():
    try:
        with open("data/infos_produto.txt", "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "❌ Não foi possível carregar as informações do produto."

# Função principal que responde com base no conteúdo do PDF
def responder(pergunta):
    info = carregar_info_produto()

    prompt = f"""
Você é um assistente virtual de uma plataforma de cursos.
Use as informações abaixo para responder à pergunta do cliente:

Informações do produto:
{info}

Pergunta do cliente:
{pergunta}
"""

    try:
        modelo = genai.GenerativeModel("gemini-1.5-flash")
        resposta = modelo.generate_content(prompt)
        return getattr(resposta, "text", "❌ Erro: resposta vazia.")
    except Exception as e:
        return f"❌ Erro ao gerar resposta: {str(e)}"

# Interface visual com Gradio
iface = gr.Interface(
    fn=responder,
    inputs=gr.Textbox(
        label="Pergunte sobre os planos",
        placeholder="Ex: Quais são os planos disponíveis?",
        lines=1
    ),
    outputs=gr.Textbox(label="Resposta do Assistente"),
    title="🤖 Assistente Virtual de Cursos",
    description="Digite uma pergunta sobre os planos, certificados, formas de pagamento etc. O assistente irá responder com base no conteúdo do PDF.",
)

# Executa o app localmente (ou use share=True para gerar link público)
iface.launch()