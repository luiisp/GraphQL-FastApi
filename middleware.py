from main import app
from fastapi.middleware.cors import CORSMiddleware
from config import CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS['allow_origins'],
    allow_credentials=CORS['allow_credentials'],
    allow_methods=CORS['allow_methods'],
    allow_headers=CORS['allow_headers'],
)