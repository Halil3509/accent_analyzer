from pydantic import BaseModel, HttpUrl

class VideoRequest(BaseModel):
    video_url: str

class AnalysisResponse(BaseModel):
    accent: str
    confidence_score: str
    accent_explanation: str
    transcript_summary: str
