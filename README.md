
# 🤖 Local LLM Chatbot – Powered by Ollama + Streamlit

Welcome to your very own locally running chatbot!  
This project uses [Ollama](https://ollama.com) to run large language models (like `llama3`) *fully offline* and a clean UI built with **Streamlit**.

---

## What This Project Does

-  Loads local LLMs like `llama3` using Ollama
-  Interactive chat UI using Streamlit
-  No cloud, no API keys - Very private

---

##  Requirements

Make sure Python 3.8+ is installed. Then:

```bash
pip install streamlit requests
```

Also make sure you have [Ollama installed](https://ollama.com/download).

Then pull a model:
```bash
ollama pull llama3
```

---

## Run

1. Clone this repo (or copy files)
2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv env
source env/bin/activate
```

3. Run the chatbot:

```bash
streamlit run app.py
```

Make sure Ollama is running in another terminal:

```bash
ollama run llama3
```

---

## 📁 Project Structure

```
local-llm-chatbot/
│
├── app.py              # Streamlit UI
├── ollama_utils.py     # LLM API interface
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---


Built by **Manu K**  
Drop a like if this helped you or fork it to add more features like:
-  Streaming responses
-  Persona-switching bots
-  Memory / context windows

---

## Chat With Me

Want to collab, ask something, or roast this bot?  
[LinkedIn](https://www.linkedin.com/in/manu-kedarasetti-b7a02112a)
