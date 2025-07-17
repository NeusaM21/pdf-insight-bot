from dotenv import load_dotenv
import os
import re
from utils.leitor_pdf import carregar_base_pdf

# Cores para destacar no terminal
def destacar_keywords(texto):
    # Dicionário de palavras-chave e emojis
    palavras = {
        r"\btema\b": "📚 TEMA",
        r"\btecnologia\b": "🧠 TECNOLOGIA",
        r"\binteligência artificial\b": "🤖 INTELIGÊNCIA ARTIFICIAL",
        r"\baprendizado supervisionado\b": "📈 APRENDIZADO SUPERVISIONADO",
        r"\baprendizado não supervisionado\b": "📉 APRENDIZADO NÃO SUPERVISIONADO",
        r"\bmercado de trabalho\b": "💼 MERCADO DE TRABALHO",
        r"\bsetor(?:es)?\b": "🏢 SETOR",
    }

    for palavra, destaque in palavras.items():
        texto = re.sub(palavra, destaque, texto, flags=re.IGNORECASE)

    return texto

# Carrega variáveis do .env
load_dotenv()
chave_gemini = os.getenv("GEMINI_API_KEY")

if not chave_gemini:
    raise ValueError("❌ A variável GEMINI_API_KEY não foi carregada. Verifique o .env.")

# Carrega a base vetorial com PDFs
qa = carregar_base_pdf(chave_gemini=chave_gemini)

# Faz uma pergunta
pergunta = "Qual é o tema principal do documento?"
resposta = qa.invoke({"query": pergunta})["result"]

# Aplica destaque
resposta_destacada = destacar_keywords(resposta)

# Exibe a resposta com destaque
print("\n🧠 Resposta do bot com destaques:\n")
print(resposta_destacada)