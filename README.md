🚀 CrewAI Multi-Agent System (Python)

This repository demonstrates the implementation of a multi-agent AI system using CrewAI concepts, inspired by Krishnaik’s tutorial.
The project showcases how autonomous agents can be defined, assigned tasks, equipped with tools, and orchestrated together to solve a problem collaboratively.

📌 Project Overview

The goal of this project is to understand and implement agentic AI workflows using Python by:

Creating multiple AI agents with specific responsibilities

Defining tasks that agents can execute

Orchestrating agent collaboration using a central crew manager

Designing a modular and extensible project structure

This project focuses on architecture and workflow design, not just model usage.

🧠 Key Concepts Demonstrated

Multi-Agent Systems (MAS)

Agent orchestration and coordination

Task decomposition and execution

Tool-based agent capabilities

Modular Python project design

Agentic AI fundamentals

📂 Repository Structure
├── agents.py        # Defines AI agents and their roles
├── task.py          # Task definitions and execution logic
├── tools.py         # Custom tools used by agents
├── crew.py          # Crew orchestration and workflow manager
├── requirements.txt # Project dependencies


Each file is intentionally separated to follow clean architecture principles commonly used in production-grade AI systems.

⚙️ Tech Stack

Python

CrewAI (conceptual implementation)

Agent-based architecture

Modular code design

▶️ How to Run

Clone the repository

git clone https://github.com/shivamrustagi03/crewAI-tutorial-krishnaik.git
cd crewAI-tutorial-krishnaik


(Optional) Create a virtual environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run the crew

python crew.py

📈 What This Project Proves (ATS-Friendly)

Designed and implemented a multi-agent AI system using Python

Applied agentic AI principles such as autonomy, task delegation, and collaboration

Built a scalable and modular codebase suitable for real-world AI workflows

Demonstrated understanding of AI system design beyond single-model usage

Resume-ready line:

Built a Python-based multi-agent AI system demonstrating agent orchestration, task management, and tool integration using CrewAI concepts.

🔮 Future Improvements

Integrate real LLMs (OpenAI / Open-source models)

Add memory and long-term context for agents

Logging and visualization of agent interactions

API or UI interface for live task execution

👤 Author

Shivam Rustagi
Aspiring AI / Data Engineer
Focused on Agentic AI, Data Science, and Scalable Systems
