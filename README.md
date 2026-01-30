# Resume Ranker

Resume Ranker is a lightweight, end-to-end prototype that demonstrates how resume search and ranking can be implemented using vector-based similarity techniques and deployed on cloud infrastructure.

This project was built as an **assessment / demonstration** to showcase system design, cloud deployment, and practical AI engineering decisions under resource constraints.

---

## What Problem Does This Solve?

Hiring teams often receive large volumes of resumes with no effective way to search them based on role requirements.

Resume Ranker allows an employer to:
- Enter role requirements or skills in natural language
- Automatically rank resumes based on relevance
- Review the most suitable candidates first

---

## Key Features

- PDF resume ingestion
- Text extraction and preprocessing
- Vector-based ranking using TF-IDF
- Cosine similarity for relevance scoring
- Clean browser-based UI
- Deployed and tested on AWS EC2

---

## Tech Stack

**Backend**
- Python
- FastAPI

**Search & Ranking**
- TF-IDF (scikit-learn)
- Cosine similarity

**Frontend**
- HTML + JavaScript (served via FastAPI)

**Cloud**
- AWS EC2 (t3.micro, Amazon Linux)

---

## Why TF-IDF Instead of Embeddings?

For this demonstration, TF-IDF was intentionally chosen to:
- Avoid heavy dependencies and large model downloads
- Stay within AWS free-tier limits
- Ensure reliable and reproducible deployment

The architecture is modular and can be extended to neural embeddings (FAISS / pgvector / hosted models) in a production setting.

---

## How It Works

1. Resumes are uploaded as PDF files
2. Text is extracted from each resume
3. Resumes are converted into vector representations
4. Employer queries are vectorized
5. Cosine similarity is used to rank candidates
6. Top results are displayed in the UI

---

## Status

This project is a **demonstration prototype** created for evaluation purposes and is not intended as a full production hiring platform.
