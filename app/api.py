import os
import tempfile
import logging
from fastapi import APIRouter, HTTPException
from app.models import VideoRequest, AnalysisResponse
from app.utils import download_video, extract_audio, download_youtube_video
from app.services import transcribe_audio, classify_accent, summarize_text

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["Accent Analysis"])

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_video(request: VideoRequest):
    logger.info("Received video analysis request for URL: %s", request.video_url)
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            video_path = os.path.join(tmpdir, "video.mp4")
            audio_path = os.path.join(tmpdir, "audio.wav")

            logger.info("Downloading video...")
            if "youtube.com" in request.video_url or "youtu.be" in request.video_url:
                download_youtube_video(request.video_url, video_path)
            else:
                await download_video(request.video_url, video_path)

            logger.info("Extracting audio from video...")
            extract_audio(video_path, audio_path)

            logger.info("Transcribing audio...")
            transcript = transcribe_audio(audio_path)

            logger.info("Classifying accent...")
            accent_info = classify_accent(audio_path)

            logger.info("Summarizing transcript...")
            summary = summarize_text(transcript)

            logger.info("Analysis complete. Returning response.")
            return AnalysisResponse(
                accent=accent_info["accent"],
                confidence_score=f"{accent_info['confidence_score']}%",
                accent_explanation=accent_info["explanation"],
                transcript_summary=summary
            )

    except Exception as e:
        logger.error("Error during video analysis: %s", str(e))
        raise HTTPException(status_code=500, detail=str(e))