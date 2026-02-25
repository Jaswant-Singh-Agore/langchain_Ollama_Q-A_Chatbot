# langchain_Ollama_Q-A_Chatbot
# 🦙 Ollama Q&A Chatbot  
Local LLM Chat Application using LangChain & Streamlit

A professional Q&A chatbot built using locally running Large Language Models (LLMs) via Ollama, powered by modern LangChain (v1.2.x) architecture and deployed with Streamlit.

This project demonstrates practical LLM integration, modular design, and real-world deployment awareness.

---

## 📌 Overview

This application allows users to interact with open-source LLMs running locally through Ollama.  
It provides a clean web interface for real-time question answering while keeping full control over data privacy and model execution.

Unlike cloud-based LLM apps, this chatbot runs entirely on your local machine.

---

## 🚀 Features

- Local LLM inference using Ollama  
- Built with LangChain 1.2.x (LCEL architecture)  
- Dynamic model selection  
- Adjustable temperature & token control  
- Streamlit interactive UI  
- Optional LangSmith tracing support  
- Clean and extensible code structure  

---

## 🏗️ Architecture

User Input (Streamlit UI)  
↓  
ChatPromptTemplate (LangChain)  
↓  
ChatOllama (Local LLM via Ollama Server)  
↓  
StrOutputParser  
↓  
Response Displayed in UI  

Core LangChain pipeline:

```python
chain = prompt | llm | StrOutputParser()
```

---

## 🛠️ Tech Stack

- Python 3.10+
- LangChain 1.2.x
- langchain-ollama
- Ollama
- Streamlit
- LangSmith

---

## 📂 Project Structure

```
ollama-qa-chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository
### 2. Install Dependencies

```
pip install -r requirements.txt
```

Or manually:

```
pip install streamlit langchain langchain-ollama python-dotenv
```

---

## 🦙 Install & Setup Ollama

Download Ollama:

https://ollama.com

Verify installation:

```
ollama --version
```

---

### Pull a Model

Example:

```
ollama pull phi3:mini
ollama pull gemma:3b
ollama pull mistral
```

Check installed models:

```
ollama list
```

---

### Start Ollama Server

```
ollama serve
```

Default endpoint:

http://localhost:11434

---

## ▶️ Run the Application

```
streamlit run app.py
```

Open in browser:

http://localhost:8501

---

## 🔧 Configuration

You can modify:

- Model name (e.g., phi3:mini, gemma:3b)
- Temperature
- Token limit (num_predict for Ollama)

Optional: Enable LangSmith tracing:

```
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=your_key_here
```

---

## ⚠️ Deployment Notes

Ollama requires a running local server.

This means:

- Streamlit Cloud cannot run Ollama directly.
- You must deploy on a VPS, local server, or Dockerized environment.

Recommended deployment options:

- AWS EC2
- DigitalOcean
- Azure VM
- Local machine server
- Docker container

---

## 🐛 Common Issues

Model Not Found:

```
ollama pull model_name
```

Connection Refused (WinError 10061):

```
ollama serve
```

---

## 📈 Future Improvements

- Add chat memory
- Add RAG (Retrieval-Augmented Generation)
- Add streaming responses
- Convert to agent-based system
- Docker support
- Authentication layer

---

## 👨‍💻 Author

Built using modern LLM architecture principles with LangChain and Ollama.

If you found this project useful, consider giving it a star on GitHub.
