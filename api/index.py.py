from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import google.generativeai as genai
import requests
import os
from supabase import create_client, Client
from urllib.parse import quote

app = FastAPI(title="BharatAI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# AI Keys
genai.configure(api_key=os.getenv("GEMINI_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.5-flash")
GROK_KEY = os.getenv("GROK_KEY")

# Supabase
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# UPI
UPI_ID = "yourname@upi"
MERCHANT_NAME = "BharatAI"

def call_grok(prompt):
    try:
        url = "https://api.x.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROK_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "grok-4",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 300,
            "temperature": 0.9
        }
        r = requests.post(url, json=payload, timeout=10)
        return r.json()["choices"][0]["message"]["content"]
    except:
        return