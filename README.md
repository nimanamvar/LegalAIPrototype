
# LegalAIPrototype

**LegalAIPrototype** is an AI-powered legal assistant designed to analyze legal documents and provide concise, accurate answers to user queries. The application leverages modern natural language processing techniques to improve accessibility to legal information while maintaining a user-friendly experience.

---

## Features

- **Document Uploading**: Upload legal documents to the backend for analysis.
- **Query Processing**: Ask questions related to uploaded legal documents and receive accurate responses.
- **Interactive UI**: A modern, responsive frontend that offers a smooth user experience.
- **Backend Intelligence**: Uses cutting-edge AI models to extract and retrieve relevant legal information.

---

## Tech Stack

- **Frontend**: React (with TailwindCSS for styling)
- **Backend**: FastAPI (Python)
- **Database/Storage**: FAISS for semantic search and document indexing
- **AI Models**: OpenAI-powered language models for query answering

---

## Installation and Setup

Follow these steps to set up and run the project locally.

### Prerequisites

- Node.js (v14 or later)
- Python (v3.8 or later)
- Pip
- Git
- A compatible OpenAI API key

### Clone the Repository

```bash
git clone https://github.com/nimanamvar/LegalAIPrototype.git
cd LegalAIPrototype
```

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the backend server:
   ```bash
   uvicorn app:app --reload --port 8000
   ```

   By default, the backend runs on [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the frontend development server:
   ```bash
   npm start
   ```

   By default, the frontend runs on [http://localhost:3000](http://localhost:3000).

---

## Usage

1. Start the backend and frontend servers as outlined above.
2. Open the frontend in your browser at [http://localhost:3000](http://localhost:3000).
3. Upload legal documents through the UI.
4. Enter questions in the query field to receive AI-generated answers based on the uploaded documents.

---

## Folder Structure

```
LegalAIPrototype/
│
├── backend/
│   ├── app.py                 # FastAPI backend application
│   ├── utils.py               # Utility functions for processing
│   ├── docs/                  # Document storage for indexing
│   └── requirements.txt       # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── App.js             # Main entry point for React app
│   │   └── index.js           # React DOM rendering
│   ├── public/                # Public files for frontend
│   └── package.json           # Frontend dependencies
│
└── README.md                  # Project documentation
```

---

## Troubleshooting

### Common Issues

- **CORS Error**: Ensure the backend allows requests from the frontend's origin.
- **Missing Dependencies**: Run the appropriate installation commands (`pip install -r requirements.txt` or `npm install`).
- **Port Conflicts**: Check if another application is using the default ports (8000 for backend, 3000 for frontend).

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your descriptive message here"
   ```
4. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request.

---

## License

*This section is intentionally left blank.*

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for backend development
- [React](https://reactjs.org/) for the frontend
- [OpenAI](https://openai.com/) for AI model integration

---

