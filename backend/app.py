from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="InternShield AI")


class AnalyzeRequest(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    text = request.text
    return {
        "length": len(text),
        "word_count": len(text.split()),
    }