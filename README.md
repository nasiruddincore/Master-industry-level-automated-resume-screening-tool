# AI-Driven Resume Screening System

## Overview

The AI-Driven Resume Screening System is an industry-oriented ATS (Applicant Tracking System) simulation project built using Python, NLP, Machine Learning, FastAPI, and Streamlit.

The system automatically uploads resumes, extracts text from PDF/DOCX files, compares resumes with job descriptions using TF-IDF and cosine similarity, ranks candidates, and generates shortlist reports.

This project simulates how modern HR Tech and recruitment platforms automate candidate screening.

---

# Features

- Automated Resume Upload
- PDF Resume Text Extraction
- DOCX Resume Text Extraction
- NLP-Based Resume Cleaning
- TF-IDF Vectorization
- Cosine Similarity Matching
- Resume Ranking System
- Shortlisted/Rejection Decision
- CSV Report Generation
- FastAPI Backend
- Streamlit Recruiter Dashboard
- ATS Workflow Simulation

---

# Industry Relevance

This project demonstrates:

- Python Development
- NLP Engineering
- Machine Learning
- HR Tech Automation
- API Development
- Dashboard Development
- Real-world ATS Workflow
- Data Processing

Useful for roles like:

- Python Developer
- NLP Engineer
- Data Analyst
- Automation Engineer
- AI/ML Intern
- HR Tech Developer

---

# Project Workflow

```text
Resume Upload
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Skill Matching
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Resume Ranking
      ↓
Shortlist / Reject Decision
      ↓
CSV Report Generation
```

---

# Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI

## Programming Language
- Python

## Machine Learning / NLP
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Regex

## Data Processing
- Pandas
- NumPy

## Resume Parsing
- pdfplumber
- python-docx

---

# Project Structure

```text
Automated-Resume-Screening-Tool/
│
├── resumes/
├── outputs/
├── src/
│   ├── extractor.py
│   ├── cleaner.py
│   ├── matcher.py
│
├── app/
│   ├── streamlit_app.py
│   └── api.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

## Move Into Project Folder

```bash
cd AI-Driven-Resume-Screening-System
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

### Mac/Linux

```bash
python3 -m venv venv
```

---

# Activate Virtual Environment

## Windows

```bash
venv\Scripts\activate
```

## Mac/Linux

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Streamlit Dashboard

```bash
streamlit run app/streamlit_app.py
```

---

# Run FastAPI Server

```bash
uvicorn app.api:app --reload
```

---

# Run Main Project

```bash
python main.py
```

---

# How It Works

1. Upload resumes from dashboard
2. Resumes automatically save in `resumes/`
3. Resume text is extracted
4. NLP cleaning is applied
5. TF-IDF converts text into vectors
6. Cosine similarity compares resumes with job description
7. Scores are generated
8. Candidates are ranked
9. CSV report is generated automatically

---

# Sample Output

| Resume | Score | Decision |
|--------|--------|----------|
| resume1.pdf | 89.45 | Shortlisted |
| resume2.docx | 74.22 | Shortlisted |
| resume3.pdf | 31.55 | Rejected |

---

# Generated Output

```text
outputs/ranking_report.csv
```

---

# Screenshots To Add

Add screenshots inside `images/` folder:

- Dashboard UI
- Resume Upload
- Ranking Table
- CSV Output
- FastAPI Swagger UI
- GitHub Repository
- Project Folder Structure

---

# API Endpoints

## Home Endpoint

```text
GET /
```

## Health Check

```text
GET /health
```

---

# Future Improvements

- BERT Semantic Matching
- OCR Resume Parsing
- Authentication System
- PostgreSQL Database
- Recruiter Login
- Email Notifications
- Docker Deployment
- Cloud Hosting
- Advanced Skill Extraction

---

# Learning Outcomes

After building this project, you will understand:

- NLP Basics
- Resume Parsing
- TF-IDF
- Cosine Similarity
- Machine Learning Workflow
- Streamlit Dashboard Development
- FastAPI Development
- CSV/Data Processing
- ATS System Design
- GitHub Project Deployment

---

# Interview Questions

## Explain Your Project

I developed an AI-powered Resume Screening Tool using Python, NLP, TF-IDF, cosine similarity, FastAPI, and Streamlit. The system automatically uploads resumes, extracts text from PDF/DOCX files, compares candidate skills with job descriptions, ranks applicants, and generates shortlist reports similar to a real ATS system.

---

# Author

Nasir Uddin

---

# License

This project is for educational and portfolio purposes.
