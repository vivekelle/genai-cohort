#1. Ingestion: Loading document -> Extract Text
#2. Chunking: Splitting extracted text into chunks (can be paragraphs, etc.)
#3. Indexing: Create Vector Embeddings for each chunk -> Store them in Vector DB
#4. Retrieval: Input User Query -> Get Vector Embedding of User query -> Search for relevant chunk, by checking similarity with embedding of query.
#5. User query + [Relevant Chunks] -> LLM -> Output + Page number (if required)

from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

pdf_path = Path(__file__).parent / "nodejs.pdf" 
loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load() # Read PDF file
print("Docs: ", docs[5])