# 🤖 Autonomous Technology Researcher Agent (Agentic AI Project)

An LLM-powered autonomous technology research agent built using **LangChain**, **Groq LLM**, and **Tavily Web Search**.  
The system automatically researches technology topics, analyzes multi-source information, generates structured reports, and stores them in a persistent knowledge repository.

---

## 📌 Project Overview

This project implements an Agentic AI pipeline that accepts a technology topic and performs autonomous research using tool-augmented LLM reasoning. The agent searches the web, validates findings, analyzes trends, writes structured reports, and saves results automatically.

No manual browsing is required after input.

---

## 🎯 Problem Statement

Build an autonomous LLM researcher agent that can:

- Process user technology queries  
- Use web search tools  
- Synthesize multi-source information  
- Generate structured summaries  
- Store outputs for future reference  

---

## 🧠 Agent Pipeline

User Topic  
→ Tavily Web Search Tool  
→ Research Stage  
→ Validation Stage  
→ Analysis Stage  
→ Report Writing Stage  
→ Knowledge Repository Storage  
→ Quality Evaluation  

---

## 🏗 System Architecture

User Input
↓
Search Tool (Tavily)
↓
Research Prompt Agent
↓
Validation Prompt Agent
↓
Analysis Prompt Agent
↓
Writer Prompt Agent
↓
Structured Report
↓
knowledge_repo storage
↓
Quality Scoring


---

## 📂 Project Structure

Autonomous_Tech_Research_Agent/
│
├── main.py # pipeline controller
├── agents.py # agent role prompts
├── tools.py # Tavily search integration
├── memory.py # report storage module
├── evaluator.py # quality scoring
├── config.py # environment loader
├── requirements.txt # dependencies
├── README.md
│
├── knowledge_repo/ # saved reports
│ └── sample_report.txt


---

## ⚙️ Technologies Used

- Python
- LangChain
- Groq LLM (llama-3.1-8b-instant)
- Tavily Search API
- python-dotenv
- VS Code

---

## 🔧 Installation & Setup

### 1️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
