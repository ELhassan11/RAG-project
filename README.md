# 📄 RAG Application Using Gemini AI

This project is a **Retrieval-Augmented Generation (RAG)** application built with **Streamlit** and **Google Gemini AI**.
It allows users to upload a **PDF file**, search its content using semantic similarity, and generate accurate answers based on the most relevant document chunks.

The system combines:

* **PDF document loading**
* **Text embeddings**
* **Vector similarity search (FAISS)**
* **Large Language Model (Gemini)**



---

## 🚀 Features

* Upload and process PDF documents
* Convert PDF text into embeddings using **Sentence Transformers**
* Store embeddings in **FAISS** for fast similarity search
* Chat-style interface using **Streamlit**
* Generate contextual answers using **Gemini AI**
* Session-based chat history

---

## 🧠 How It Works (Pipeline)

1. User uploads a PDF file
2. PDF text is extracted page by page
3. Text is converted into vector embeddings
4. Embeddings are stored in a FAISS index
5. User enters a question
6. The most similar document chunk is retrieved
7. Gemini AI generates an answer based on retrieved context

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – Web interface
* **FAISS** – Similarity search
* **Sentence Transformers** – Text embeddings
* **LangChain (PyPDFLoader)** – PDF processing
* **Google Gemini AI** – Text generation
* **NumPy**

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/rag-gemini-app.git
cd rag-gemini-app
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install streamlit numpy faiss-cpu sentence-transformers langchain google-generativeai
```

---

## 🔑 Environment Setup

You must set your **Google Gemini API Key** as an environment variable.

### Windows (PowerShell)

```powershell
setx GEMINI_API_KEY "your_api_key_here"
```

### Linux / macOS

```bash
export GEMINI_API_KEY="your_api_key_here"
```

---

## ▶️ Run the Application

```bash
streamlit run Rag.py
```

---

## 💬 Usage

1. Open the Streamlit app in your browser
2. Upload a PDF file
3. Wait until processing completes
4. Enter a question in the chat input
5. Receive AI-generated answers based on PDF content

---

## 📁 Project Structure

```text
.
├── Rag.py          # Main Streamlit application
├── README.md       # Project documentation
```

---

## ⚠️ Notes & Limitations

* Only **PDF files** are supported
* Retrieves **top-1** similar document chunk (k = 1)
* Large PDFs may take longer to process
* Requires an active Gemini API key

---

## 📌 Future Improvements

* Support multiple retrieved chunks (k > 1)
* Add PDF preview
* Improve prompt engineering
* Enable multiple file uploads
* Add chunking for better retrieval accuracy

---

## 📜 License

This project is for **educational purposes**.
You may modify and extend it as needed.

