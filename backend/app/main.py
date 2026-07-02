from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .services.gemini_service import GeminiService
import os

app = FastAPI(title="CivicLens AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

gemini = GeminiService()

@app.get("/health")
async def health():
    return {"status": "ok", "service": "CivicLens AI Backend"}

@app.post("/api/analyze-report")
async def analyze_report(
    image: UploadFile = File(...),
    location: str = Form(""),
    notes: str = Form("")
):
    contents = await image.read()
    report = await gemini.analyze_civic_issue(contents, location, notes)
    return report

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
