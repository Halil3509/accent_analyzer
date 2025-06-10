from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
import uvicorn
import os 

os.environ['HUGGINGFACE_TOKEN'] = os.getenv("HUGGINGFACE_TOKEN")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

app = FastAPI(title="English Accent Analyzer")

# Add CORS & Security Headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, limit this!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Accent Analyzer API."}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

