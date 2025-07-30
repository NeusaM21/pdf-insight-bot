🇧🇷 Versão em Português: [README.md](README.md)  
📖 You’re reading the **English version** of this project description.

---

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-✓-purple)
![Gemini](https://img.shields.io/badge/Gemini_API-Google_AI-yellow?logo=google)
![License](https://img.shields.io/github/license/NeusaM21/pdf-insight-bot)

![Project Banner](capa.png)

# 📄 PDF Insight Bot (with Gemini API)

This project is an **intelligent PDF agent** that reads, understands, and answers questions about documents using **Google AI’s Gemini 1.5 Flash model**. Perfect for studying applied AI, building your portfolio, or even automating support based on technical or commercial PDFs.

---

## 📚 Table of Contents

* [💡 Features](#-features)
* [💬 Usage Example](#-usage-example)
* [📂 Project Structure](#-project-structure)
* [🛠️ Technologies Used](#️-technologies-used)
* [🚀 How to Run Locally](#-how-to-run-locally)
* [📈 Future Improvements](#-future-improvements)
* [✍️ Author](#️-author)
* [📝 License](#-license)

---

## 💡 Features

✅ **Gemini API integration** (Google AI)  
✅ Automatically reads **multiple PDFs**  
✅ Embedding generation with **LangChain + FAISS**  
✅ **Contextual answers** based on real PDF content  
✅ **Smart keyword highlighting** in the terminal  
✅ Lightweight, educational, and portfolio-ready

✨ **Bonus feature:**  
✅ Visual highlights in the terminal for keywords like **Topic, Technology, Industry** to make AI answers easier to read.

---

## 💬 Usage Example

**Question:** What is the main topic of the document?

**Answer:** The 📚 **TOPIC** of the document is the impact of 🧠 **TECHNOLOGY**—specifically blockchain—on the market and the regulation of virtual currencies.

![Terminal demonstration of the PDF Insight Bot](assets/pdf-insight-bot-terminal.gif)

---

## 📂 Project Structure

```
pdf-insight-bot/
├── utils/
│ └── leitor_pdf.py
├── data/
│ └── documents/
│ ├── inteligencia_artificial.pdf
│ ├── blockchain_no_mercado.pdf
│ └── impacto_da_automacao.pdf
├── teste_leitor_pdf.py
├── .env.example
├── README.md
└── capa.png
```
---

## 🛠️ Technologies Used

**Python 3**, **LangChain**, **Gemini API (Google AI)**, **FAISS**, **python-dotenv**

---

## 🚀 How to Run Locally

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/MrsM21/pdf-insight-bot.git
    cd pdf-insight-bot
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file with your Gemini API key:**
    ```
    GEMINI_API_KEY=your-key-here
    ```

4.  **Add your PDF files into:**
    `data/documents/`

5.  **Run the test script:**
    ```bash
    python teste_leitor_pdf.py
    ```

---

## 📈 Future Improvements

* [ ] Save FAISS vector database as `.pkl`
* [ ] Web interface with Gradio or Streamlit
* [ ] Online version with free deploy (Replit, Render)
* [ ] Integration with mini-CRM to store queries and contacts

---

## ✍️ Author

Project created by [**NeusaM21**](https://github.com/NeusaM21) as part of her Applied AI portfolio. Built with passion, study, and ✨ lots of coffee.

---

## 📝 License

This project is under the [MIT License](https://github.com/NeusaM21/pdf-insight-bot/blob/main/LICENSE). Use it, adapt it, and share it—just don’t forget to give credit. 😉
