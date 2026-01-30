from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import pdfplumber
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Serve static files (future use)
app.mount("/static", StaticFiles(directory="static"), name="static")

documents = []
tfidf_matrix = None
vectorizer = None


def load_resumes():
    global documents, tfidf_matrix, vectorizer
    texts = []

    for file in os.listdir("resumes"):
        path = os.path.join("resumes", file)
        text = ""

        if file.lower().endswith(".pdf"):
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
        else:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()

        texts.append(text)

    documents = texts
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(texts)


load_resumes()


class Query(BaseModel):
    query: str


@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/search")
def search_resumes(q: Query):
    query_vec = vectorizer.transform([q.query])
    scores = cosine_similarity(query_vec, tfidf_matrix)[0]
    top_indices = scores.argsort()[-3:][::-1]
    results = [documents[i] for i in top_indices]
    return {"results": results}
