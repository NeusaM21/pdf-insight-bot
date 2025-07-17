from dotenv import load_dotenv
import os
from utils.leitor_pdf import carregar_base_pdf

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Pega a chave da API Gemini
chave_gemini = os.getenv("GEMINI_API_KEY")

# Validação básica (opcional, mas ajuda no debug)
if not chave_gemini:
    raise ValueError("❌ A variável GEMINI_API_KEY não foi carregada. Verifique o .env.")

# Carrega os PDFs e cria a cadeia de QA
qa = carregar_base_pdf(chave_gemini=chave_gemini)

# Faz uma pergunta
pergunta = "Qual é o tema principal do documento?"
resposta = qa.invoke({"query": pergunta})

# Exibe a resposta
print("\n🤖 Resposta do bot:")
print(resposta["result"])