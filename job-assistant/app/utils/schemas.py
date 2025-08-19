from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    resume_text: str
    target_role: str
    tone: str
    experience_level: str
    session_id: str

class AnalyzeResponse(BaseModel):
    match_score: int
    matched_skills: List[str]
    missing_skills: List[str]
    recommendations: List[str]
    hashtags: List[str]