import aiohttp
import os
import tempfile
from moviepy import VideoFileClip
import yt_dlp


async def download_video(video_url: str, save_path: str) -> None:
    """
    Download a video from a direct URL using aiohttp.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(video_url) as response:
            response.raise_for_status()
            content = await response.read()
            with open(save_path, 'wb') as f:
                f.write(content)


def download_youtube_video(youtube_url: str, save_path: str) -> None:
    """
    Download video from YouTube using yt-dlp.
    """
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': save_path,
        'merge_output_format': 'mp4',
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


def extract_audio(video_path: str, audio_path: str) -> None:
    """
    Extract audio from video and save it as WAV.
    """
    if not os.path.exists(video_path) or os.path.getsize(video_path) == 0:
        raise ValueError("Downloaded video file is empty or corrupted.")
    
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path, fps=16000, codec='pcm_s16le')
