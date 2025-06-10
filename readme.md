# English Accent Analyzer API

A robust, production-ready FastAPI service for analyzing English accents from public video URLs. This tool extracts audio from videos, transcribes spoken content, classifies the speaker's English accent, and generates a concise transcript summary — empowering hiring teams to evaluate spoken English efficiently and objectively.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Architecture & Tech Stack](#architecture--tech-stack)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [API Endpoints](#api-endpoints)  
- [Environment Variables](#environment-variables)  
- [Docker Support](#docker-support)  
- [Security Considerations](#security-considerations)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview

This service accepts a public video URL, extracts the audio, and leverages state-of-the-art AI models to:

- Transcribe the spoken content (using OpenAI Whisper)
- Classify the English accent (British, American, Australian, etc.) with confidence scores
- Summarize the transcript for quick review

The output facilitates rapid, data-driven hiring decisions based on spoken English proficiency and accent.

---

## Features

- **Asynchronous and scalable API** built with FastAPI  
- Accurate **audio extraction** from any public video URL (MP4 or Loom links)  
- Accent classification powered by a DistilHuBERT-based Transformer model  
- Speech transcription using OpenAI Whisper (base model)  
- Transcript summarization via Google Gemini Pro through LangChain  
- Input validation and structured JSON responses using Pydantic  
- Secure, production-oriented design with CORS and error handling  
- Dockerized for seamless deployment and scalability  

---

## Architecture & Tech Stack

| Component                | Technology / Library               |
|--------------------------|----------------------------------|
| Web Framework            | FastAPI                          |
| Asynchronous HTTP Client  | aiohttp                         |
| Audio Extraction         | MoviePy (ffmpeg)                 |
| Audio Processing         | Torchaudio, Transformers Pipeline|
| Speech Recognition       | OpenAI Whisper                   |
| Language Model           | Google Gemini Pro via LangChain  |
| Containerization         | Docker, Docker Compose           |
| Environment Management   | python-dotenv                    |

---

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional but recommended)
- Google API key with access to Gemini Pro model
- FFmpeg installed locally if running outside Docker



### Installation (Local)

1. Clone the repository:

```bash
git clone https://github.com/yourusername/accent-analyzer.git
cd accent-analyzer
````
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Google API key:

4. Login to Hugging Face:
```bash
huggingface-cli login
```
(Follow the prompts to provide your Hugging Face token)

5. Create a `.env` file and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
LANGSMITH_API_KEY=your_langsmith_key_here
HUGGINGFACE_TOKEN=your_hg_token_here
```

6. Run the FastAPI app:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## Usage

Once running, open your browser and navigate to:

```
http://localhost:8000/docs
```

Use the interactive Swagger UI to test the `/analyze` endpoint by submitting a JSON payload with a public video URL.

Example payload:

```json
{
  "video_url": "https://example.com/sample_video.mp4"
}
```

---

## API Endpoints

### `POST /analyze`

Analyze a video URL for spoken English accent and transcript summary.

* **Request Body:**

```json
{
  "video_url": "string (valid public URL)"
}
```

* **Response:**

```json
{
  "accent": "American",
  "confidence_score": "92.35%",
  "accent_explanation": "The speaker's accent is likely American with 92.35% confidence.",
  "transcript_summary": "The speaker discusses the company's quarterly performance and growth strategies."
}
```

---

## Environment Variables

| Variable | Description | Required |
| --- | --- | --- |
| `GOOGLE_API_KEY` | API key for Google Gemini Pro model | Yes |
| `LANGSMITH_API_KEY` | API key for LangSmith | Yes |
| `HUGGINGFACE_TOKEN` | Token for HuggingFace | Yes |

---

## Docker Support

Build and run the containerized service with:

```bash
docker-compose up --build
```

The API will be accessible at `http://localhost:8000`.

---

## Security Considerations

* CORS is enabled for all origins for ease of testing — restrict in production environments.
* No authentication is currently implemented; consider adding OAuth2 or API keys for secure access.
* Rate limiting and request validation should be added to mitigate abuse in production.
* Handle sensitive API keys securely (e.g., via environment variables or secret management tools).

---

## Contributing

Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

*Built by Halil Ibrahim*

```
```


<div align="center"> <img src="https://komarev.com/ghpvc/?username=accent-analyzer&color=blue&label=VISITORS" /> </div>
