# gemini_client.py
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# ✅ load .env from project root (same folder as this file)
ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash").strip()

def _get_api_key() -> str:
    key = (os.getenv("GEMINI_API_KEY", "")).strip()
    if key.startswith('"') and key.endswith('"'):
        key = key[1:-1].strip()
    if not key:
        raise ValueError(
            f"Missing GEMINI_API_KEY. Put it in: {ENV_PATH}\n"
            "Example:\nGEMINI_API_KEY=your_key_here\nGEMINI_MODEL=gemini-2.0-flash"
        )
    return key

def generate_text(system_prompt: str, user_prompt: str, temperature: float = 0.3, model: str | None = None) -> str:
    key = _get_api_key()
    client = genai.Client(api_key=key)
    model_name = (model or DEFAULT_MODEL).strip()

    try:
        resp = client.models.generate_content(
            model=model_name,
            contents=[{
                "role": "user",
                "parts": [{"text": f"SYSTEM:\n{system_prompt}\n\nUSER:\n{user_prompt}"}],
            }],
            config={"temperature": float(temperature)},
        )
        return (resp.text or "").strip()

    except Exception as e:
        msg = str(e)
        if "RESOURCE_EXHAUSTED" in msg or "429" in msg or "quota" in msg.lower():
            raise RuntimeError("GEMINI_QUOTA_EXCEEDED") from e
        raise
