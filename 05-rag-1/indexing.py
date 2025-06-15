#1. Ingestion: Loading document -> Extract Text
#2. Chunking: Splitting extracted text into chunks (can be paragraphs, etc.)
#3. Indexing: Create Vector Embeddings for each chunk -> Store them in Vector DB
#4. Retrieval: Input User Query -> Get Vector Embedding of User query -> Search for relevant chunk, by checking similarity with embedding of query.
#5. User query + [Relevant Chunks] -> LLM -> Output + Page number (if required)

from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
load_dotenv()

pdf_path = Path(__file__).parent / "nodejs.pdf" 

# Loading
loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load() # Read PDF file
# print("Docs[5]: ", docs[5])

# Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400

)
split_docs = text_splitter.split_documents(documents=docs)

# Vector Embedding

embedding_model = OpenAIEmbeddings(
    model = "text-embedding-3-large"
)

# Using [embedding_model] create embeddings of split_docs and store in DB

vector_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    url = "http://localhost:6333",
    collection_name = "learning_vectors",
    embedding=embedding_model
)

print("Indexing of Documents Done...")