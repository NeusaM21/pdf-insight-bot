import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

def carregar_base_pdf(pasta_pdf=None, chave_gemini=None):
    if not chave_gemini:
        raise ValueError("Você precisa fornecer sua chave da API Gemini.")
    
    # Define caminho absoluto se não for passado
    if pasta_pdf is None:
        pasta_pdf = os.path.join(os.getcwd(), "data", "documents")

    # Carrega todos os PDFs da pasta
    documentos = []
    for arquivo in os.listdir(pasta_pdf):
        if arquivo.endswith(".pdf"):
            caminho = os.path.join(pasta_pdf, arquivo)
            loader = PyPDFLoader(caminho)
            documentos.extend(loader.load())

    if not documentos:
        raise ValueError("Nenhum PDF encontrado na pasta.")

    # Divide o texto em pedaços
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs_processados = splitter.split_documents(documentos)

    # Cria embeddings com Gemini
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=chave_gemini)

    # Cria a base vetorial FAISS
    db = FAISS.from_documents(docs_processados, embeddings)

    # Cria o modelo LLM para perguntas e respostas
    modelo = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=chave_gemini)

    # Cria a cadeia de QA (question answering)
    qa_chain = RetrievalQA.from_chain_type(
        llm=modelo,
        retriever=db.as_retriever(),
        return_source_documents=False
    )

    return qa_chain