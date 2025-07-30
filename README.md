📖 Você está lendo a **versão em Português** desta descrição de projeto.  
🇺🇸 English version available here: [README.en.md](README.en.md)

---

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-✓-purple)
![Gemini](https://img.shields.io/badge/Gemini_API-Google_AI-yellow?logo=google)
![License](https://img.shields.io/github/license/NeusaM21/pdf-insight-bot)

![Capa do Projeto](capa.png)

# 📄 PDF Insight Bot — Assistente Inteligente de PDFs com Gemini API

Este projeto é um **agente inteligente de PDF** que lê, entende e responde perguntas sobre documentos, usando o modelo **Gemini 1.5 Flash da Google AI**. Ideal para estudar IA aplicada, criar portfólio ou até mesmo automatizar atendimento com base em documentos técnicos e comerciais.

---

## 📚 Sumário

* [💡 Funcionalidades](#-funcionalidades)
* [💬 Exemplo de uso](#-exemplo-de-uso)
* [📂 Estrutura do Projeto](#-estrutura-do-projeto)
* [🛠️ Tecnologias Usadas](#️-tecnologias-usadas)
* [🚀 Como executar localmente](#-como-executar-localmente)
* [📈 Próximas melhorias](#-próximas-melhorias)
* [✍️ Autor](#️-autor)
* [📝 Licença](#-licença)

---

## 💡 Funcionalidades

✅ **Integração com a API Gemini** (Google AI)  
✅ Leitura de **múltiplos PDFs automaticamente**  
✅ Geração de **embeddings com LangChain e FAISS**  
✅ Respostas **contextuais** com base no conteúdo real dos PDFs  
✅ Destaque inteligente de palavras-chave no terminal  
✅ Projeto leve, didático e pronto para portfólio  

✨ **Funcionalidade extra:**  
✅ Destaque visual no terminal com palavras-chave como **Tema, Tecnologia, Setor** para facilitar a leitura da resposta da IA.

---

## 🎥 Veja o Assistente em Ação

<img src="assets/demo-assistente-virtual.gif" alt="Demonstração do Assistente Virtual de Cursos" width="100%" />

🎯 Teste essa versão com interface gráfica localmente:

```bash
python web_app.py
```

---

## 💬 Exemplo de uso

**Pergunta:** Qual é o tema principal do documento?

**Resposta:** O 📚 **TEMA** principal do documento é o impacto da 🧠 **TECNOLOGIA** blockchain no mercado e a regulamentação das moedas virtuais.

![Demonstração do PDF Insight Bot no terminal](assets/pdf-insight-bot-terminal.gif)

---

## 📂 Estrutura do Projeto

> 📌 Observação: Os nomes dos arquivos permanecem em português para refletir a estrutura original. Todas as instruções estão traduzidas e bem explicadas.

```
pdf-insight-bot/
├── assets/
│ ├── demo-assistente-virtual-v2.gif
│ └── pdf-insight-bot-terminal.gif
├── data/
│ └── documents/
│ ├── inteligencia_artificial.pdf
│ ├── blockchain_no_mercado.pdf
│ └── impacto_da_automacao.pdf
├── utils/
│ └── leitor_pdf.py
├── .env.example
├── README.md
├── README.en.md
├── requirements.txt
├── requirements-full.txt
├── teste_leitor_pdf.py
├── teste_gemini.py
├── web_app.py
└── capa.png
```
---

## 🛠️ Tecnologias Usadas

**Python 3**, **LangChain**, **Gemini API** (Google AI), **FAISS**, **python-dotenv**

---

## 🚀 Como executar localmente

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/MrsM21/pdf-insight-bot.git
    cd pdf-insight-bot
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Crie o arquivo .env:**
    ```
    GEMINI_API_KEY=sua-chave-aqui
    ```

4.  **Adicione seus arquivos .pdf na pasta:**
    `data/documents/`

5.  **Execute o script de teste:**
    ```bash
    python teste_leitor_pdf.py
    ```

---

## 📈 Próximas melhorias

* [ ] Salvar a base vetorial (FAISS) em .pkl
* [ ] Interface web com Gradio ou Streamlit
* [ ] Versão online com deploy gratuito (Replit, Render)
* [ ] Integração com mini-CRM para armazenar perguntas e contatos

---

## ✍️ Autor

Projeto criado por [**NeusaM21**](https://github.com/NeusaM21) como parte do seu portfólio em IA aplicada. Feito com carinho, estudo e ✨ café.

---

## 📝 Licença

Este projeto está sob a [MIT License](https://github.com/NeusaM21/pdf-insight-bot/blob/main/LICENSE). Use, adapte e compartilhe — só não esquece os créditos. 😉
