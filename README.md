# Mini-Composer: Python Agentic Coding Demo 🤖

![Python](https://img.shields.io/badge/Language-Python-blue)
![Architecture](https://img.shields.io/badge/Pattern-Agentic%20Coding-green)

**Repo Owner:** Burak Fenerci  
**Concept:** A lightweight implementation of an AI Coding Agent (similar to Cursor Composer).

## 🎯 Motivation
Tools like **Cursor Composer** are changing software engineering. As a Forward Deployed Engineer, it is critical to understand not just how to *use* these tools, but how they function under the hood. 

This repository implements a **"Mini-Composer"** logic that:
1.  **Reads** local source code context.
2.  **Orchestrates** an LLM (OpenAI/Claude) to plan edits.
3.  **Applies** file-system changes programmatically.

## 🏗️ How it Works
[CLI Input] -> [Context Builder] -> [LLM (Code Generation)] -> [File Writer]

This mocks the "Shadow Workspace" concept used in advanced IDE agents, where code is generated and applied in a loop.

## 🚀 Usage
1. `pip install -r requirements.txt`
2. `python -m src.main`
3. Type a command like: *"Add a multiply method and docstrings to the calculator class"*