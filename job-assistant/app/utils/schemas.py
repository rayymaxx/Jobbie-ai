from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str

class AnalyzeResponse(BaseModel):
    resume_score: int
    top_skills: List[str]
    missing_skills: List[str]
    advice: str