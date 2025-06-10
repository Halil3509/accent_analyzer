import os
import torch
import torchaudio
import whisper
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from transformers import pipeline
from langsmith import Client


WHISPER_MODEL = whisper.load_model("base.en")

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

accent_pipe = pipeline(
    "audio-classification", 
    model="kaysrubio/accent-id-distilhubert-finetuned-l2-arctic2"
)

def transcribe_audio(audio_path: str) -> str:
    result = WHISPER_MODEL.transcribe(audio_path)
    return result['text']

def classify_accent(audio_path: str) -> dict:
    audio, sr = torchaudio.load(audio_path)
    audio = torchaudio.transforms.Resample(orig_freq=sr, new_freq=16000)(audio)
    audio = audio.mean(dim=0).numpy()  # Ensure mono

    result = accent_pipe(audio, top_k=6)
    best = result[0]
    return {
        "accent": best['label'],
        "confidence_score": round(best['score'] * 100, 2),
        "explanation": f"The speaker's accent is likely {best['label']} with {round(best['score'] * 100, 2)}% confidence."
    }


def summarize_text(text: str) -> str:
    # Initialize LangSmith client
    client = Client()

    # Pull the prompt from LangSmith cloud (replace "summarize-transcript" with your actual prompt name/id)
    prompt = client.pull_prompt("summarize-transcript")

    # Initialize the Gemini model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        google_api_key=GOOGLE_API_KEY,
    )

    # Combine the prompt and model into a chain
    chain = prompt | llm

    # Invoke the chain with the text to summarize
    response = chain.invoke({"text": text})

    return response.content