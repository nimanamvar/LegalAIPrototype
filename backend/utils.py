import os
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from config import DOCUMENTS_PATH, FAISS_INDEX_PATH, MODEL_NAME



def load_documents():
    """
    Load documents from the 'docs' directory. This will be empty for now but ready to scale.
    """
    documents = []
    documents_folder = "C:\\Users\\35845\\legal-ai-prototype\\backend\\docs"
    for filename in os.listdir(DOCUMENTS_PATH):
        if filename.endswith(".txt"):
            loader = TextLoader(f"{DOCUMENTS_PATH}/{filename}")
            documents.extend(loader.load())
    return documents


def create_or_load_faiss_index(documents, faiss_index_path):
    """
    Create and save the FAISS index if it doesn't exist. If it exists, load it.
    """
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)

    if not os.path.exists(faiss_index_path):
        # Create the FAISS index from documents
        vector_store = FAISS.from_documents(documents, embeddings)
        vector_store.save_local(faiss_index_path)
        return vector_store
    else:
        # Load the FAISS index with dangerous deserialization enabled
        vector_store = FAISS.load_local(faiss_index_path, embeddings, allow_dangerous_deserialization=True)
        return vector_store
