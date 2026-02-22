#  AI Resume Analyzer (LLM + NLP Mini Project)

## Project Overview

The **AI Resume Analyzer** is an LLM-based application that analyzes resumes using Large Language Models (via OpenRouter API).
It provides structured feedback similar to an HR reviewer by identifying:

*  Strengths
*  Weaknesses
*  Missing Skills
*  Improvement Suggestions

This project demonstrates practical use of **LLMs, NLP concepts, prompt engineering, and AI app deployment**.

---

##  Objectives

* Learn how to integrate LLM APIs into real applications
* Understand prompt engineering for structured outputs
* Work with document parsing (PDF & DOCX resumes)
* Build an interactive AI UI using Streamlit
* Deploy an AI project to the cloud

---

##  Key Features

* Upload resume in **PDF or DOCX format**
* Option to paste resume text manually
* AI-generated structured resume feedback
* Clean Streamlit frontend
* Secure API key handling using `.env`
* Easy deployment on Streamlit Cloud

---

##  Tech Stack

### Core AI & NLP

* LLM via **OpenRouter API**
* Prompt engineering for HR-style analysis

### Backend

* Python
* OpenAI Python SDK (OpenRouter compatible)
* PyPDF2 (PDF text extraction)
* python-docx (DOCX extraction)

### Frontend

* Streamlit

### Environment & Deployment

* python-dotenv
* GitHub version control
* Streamlit Cloud deployment

---

##  Project Structure

```
AI_Resume_Analyzer/
│
├── app.py              # Streamlit frontend + LLM logic
├── .env                # API key (not pushed to GitHub)
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Installation Steps

### Clone Repository

```
git clone <your-repo-link>
cd AI_Resume_Analyzer
```

###  Create Virtual Environment

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

###  Install Dependencies

```
pip install -r requirements.txt
```

---

###  Setup API Key

Create `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

###  Run App Locally

```
streamlit run app.py
```

---

## Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Go to **share.streamlit.io**
3. Select repository
4. Set:

   * Branch: `main`
   * Main file: `app.py`
5. Add environment variable:

   ```
   OPENROUTER_API_KEY=your_key
   ```
6. Deploy 

---


## Author

**Divya Bansal**
B.Tech Computer Science (Data Science)
AI & NLP Enthusiast

---


