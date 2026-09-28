"""Central configuration for LegalEase."""
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY", "")
# gemini-1.5-pro is retired by Google; model names change often, so it is configurable.
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")
# Tried in order if the configured model is unavailable.
FALLBACK_MODELS = ["gemini-flash-latest", "gemini-2.5-flash", "gemini-2.5-pro"]

API_URL = os.getenv("LEGALEASE_API_URL", "http://localhost:8000").rstrip("/")

LOGO_PATH = BASE_DIR / "Image" / "Logo.png"            # dark logo (documents)
WEB_LOGO_PATH = BASE_DIR / "Image" / "inverseLogo.png"  # light logo (dark web UI)

COMPANY_FOOTER = "LegalEase Inc. | contact@legalease.com | All Rights Reserved."
DISCLAIMER = (
    "AI-generated draft for general information only. It is not legal advice; "
    "have a qualified lawyer review it before signing."
)
