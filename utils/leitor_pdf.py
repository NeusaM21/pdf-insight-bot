import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

def carregar_base_pdf(pasta_pdf=None, chave_gemini=None):
    if not chave_gemini:
        raise ValueError("❌ Você precisa fornecer sua chave da API Gemini.")

    print("📁 Verificando PDFs...")
    
    # Define caminho
    if pasta_pdf is None:
        pasta_pdf = os.path.join(os.getcwd(), "data", "documents")
    
    print(f"📂 Pasta de PDFs: {pasta_pdf}")

    documentos = []
    for arquivo in os.listdir(pasta_pdf):
        if arquivo.endswith(".pdf"):
            caminho = os.path.join(pasta_pdf, arquivo)
            print(f"📄 Carregando: {arquivo}")
            loader = PyPDFLoader(caminho)
            try:
                documentos.extend(loader.load())
            except Exception as e:
                print(f"⚠️ Erro ao carregar {arquivo}: {e}")

    if not documentos:
        raise ValueError("❌ Nenhum PDF válido foi carregado.")

    print(f"✅ PDFs carregados: {len(documentos)} documentos")

    # Quebra em pedaços
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs_processados = splitter.split_documents(documentos)

    print(f"📎 Frases divididas: {len(docs_processados)}")

    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=chave_gemini)
        print("🔗 Embeddings criados com sucesso")
    except Exception as e:
        print(f"❌ Erro ao criar embeddings: {e}")
        raise

    try:
        db = FAISS.from_documents(docs_processados, embeddings)
        print("📊 Base vetorial FAISS criada")
    except Exception as e:
        print(f"❌ Erro ao criar base vetorial: {e}")
        raise

    try:
        modelo = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=chave_gemini)
        print("🤖 Modelo Gemini carregado")
    except Exception as e:
        print(f"❌ Erro ao carregar modelo Gemini: {e}")
        raise

    qa_chain = RetrievalQA.from_chain_type(
        llm=modelo,
        retriever=db.as_retriever(),
        return_source_documents=False
    )

    print("✅ Cadeia de perguntas e respostas pronta!")
    return qa_chain