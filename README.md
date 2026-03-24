
# 🚀 FoodAgent – AI-Powered Restaurant Chatbot

FoodAgent is an intelligent restaurant assistant that uses **Retrieval-Augmented Generation (RAG)**, **LangGraph workflows**, and **Large Language Models (LLMs)** to deliver a seamless conversational experience.

It can search restaurants, take food orders, manage table reservations, and simulate payments using QR codes.

---

## ✨ Features

* 🔍 **Restaurant Search (RAG आधारित)**

  * Retrieves relevant restaurants using vector search (ChromaDB)
* 🍽️ **Food Ordering System**

  * Conversational ordering experience
* 📅 **Table Reservation**

  * Book tables interactively
* 💬 **Conversational AI**

  * LLM-powered chatbot (Groq API)
* 💳 **QR Code Payment Simulation**

  * Generate QR and confirm payment
* 🔀 **Multi-Agent Workflow**

  * Built using LangGraph for modular design

---

## 🧠 Architecture

User Input
→ Intent Detection
→ LangGraph Routing
  ├── Order Node
  ├── Reservation Node
  └── Search Node → Chat Node (RAG + LLM)

---

## 🛠️ Tech Stack

* Python
* LangChain
* LangGraph
* ChromaDB (Vector Database)
* HuggingFace Embeddings
* Groq LLM API
* Pandas

---

## 📂 Project Structure

```
├── main.py                # Entry point
├── graph.py               # Workflow (LangGraph)
├── rag_system.py          # RAG pipeline
├── restaurant_search.py   # Search logic
├── chat_node.py           # LLM responses
├── order_node.py          # Order handling
├── reservation_node.py    # Reservation logic
├── payment_qr.py          # QR payment
├── intent_agent.py        # Intent detection
├── agents/                # AI agents
├── data/                  # Dataset
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/foodagent.git
cd foodagent
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

### Example Queries

* "Find restaurants near me"
* "I want to order burger"
* "Book a table for 3 people"
* "Suggest good cafes"

---

## 🔮 Future Improvements

* LLM-based intent detection
* Conversation memory
* Real-time restaurant APIs
* Dynamic billing system
* Web UI (Streamlit / React)

---

## 📌 Use Cases

* Restaurant chatbots
* Food delivery platforms
* AI customer support systems
* Conversational AI research

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Ankit Kumawat**
M.Tech (AI/ML)
