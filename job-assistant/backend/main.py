from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.utils.schemas import AnalyzeRequest, AnalyzeResponse

app = FastAPI(
    title="Job Assistant API",
    version="0.1.0",
    description="Backend API for the AI Job Research Assistant"
)

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
async def health_check():
    return {"Status": "✅ OK"}

@app.post("/api/analyze-resume", response_model=AnalyzeResponse)
async def analyze_resume(payload: AnalyzeRequest):
    """
    Temporary mock endpoint
    """
    return AnalyzeResponse(
        match_score=85,
        matched_skills=["Python", "SQL", "Data Analysis"],
        missing_skills=["Deep Learning", "MLOps"],
        recommendations=[
            "Consider adding hands-on projects with TensorFlow/Pytorch"
            "Highlight experience with cloud platforms like AWS/GCP"
        ],
        hashtags=["#DataScience", "#CareerGrowth", "#AIJobs"]
    )