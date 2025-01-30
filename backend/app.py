from fastapi import FastAPI, HTTPException, UploadFile, File, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import load_documents, create_or_load_faiss_index
from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer
import logging
import shutil
import os

# Initialize FastAPI app
app = FastAPI()

# Allow CORS for frontend
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Admin Token
ADMIN_TOKEN = "my_super_secret_admin_token"

# Load documents
documents = load_documents()
logger.info(f"Loaded {len(documents)} documents.")

# Load or create FAISS index
faiss_index_path = "faiss_index"
if os.path.exists(faiss_index_path):
    shutil.rmtree(faiss_index_path)  # Delete the old FAISS index folder
vector_store = create_or_load_faiss_index(documents, faiss_index_path)

# Load LegalBERT for QA
MODEL_NAME = "nlpaueb/legal-bert-small-uncased"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
qa_model = AutoModelForQuestionAnswering.from_pretrained(MODEL_NAME)
qa_pipeline = pipeline("question-answering", model=qa_model, tokenizer=tokenizer)


# Define request model for questions
class Question(BaseModel):
    question: str


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    logger.info("Health check accessed.")
    return {"status": "OK"}


@app.post("/ask")
async def ask_question(request: Question):
    """
    Answer legal questions using LegalBERT.
    """
    question = request.question
    logger.info(f"Question received: {question}")

    # Retrieve top documents
    docs = vector_store.similarity_search(question, k=5)
    logger.info(f"Top documents: {[doc.page_content[:200] for doc in docs]}")
    context = " ".join([doc.page_content for doc in docs])

    # Use LegalBERT for answering
    result = qa_pipeline(question=question, context=context)
    answer = result.get("answer", "I couldn't find an answer.")

    logger.info(f"Answer generated: {answer}")
    return {"question": question, "answer": answer}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...), authorization: str = Header(None)):
    """
    Upload legal documents.
    """
    if authorization != ADMIN_TOKEN:
        logger.warning("Unauthorized access attempt to /upload.")
        raise HTTPException(status_code=403, detail="Unauthorized access")

    upload_dir = "./uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    logger.info(f"File uploaded successfully: {file.filename}")

    return {"message": "File uploaded successfully", "filename": file.filename}
