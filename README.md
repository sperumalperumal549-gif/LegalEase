# LegalEase - AI Legal Document Generator

Streamlit frontend + FastAPI backend + Google Gemini.

## Setup (Windows / Mac / Linux)
```bash
python -m venv venv
venv\Scripts\activate          # Windows   |   source venv/bin/activate  (Mac/Linux)
pip uninstall -y fpdf          # only if the old "fpdf" package is installed
pip install -r requirements.txt
copy .env.example .env         # Mac/Linux: cp .env.example .env
```
Open `.env` and paste your Gemini API key (https://aistudio.google.com/apikey).

## Run
Two terminals (venv active in both), from the project root:
```bash
uvicorn legalEaseAPI.main:app --reload      # backend  -> http://localhost:8000
streamlit run frontend/app.py               # frontend -> http://localhost:8501
```
Or one command: `run.bat` (Windows) / `./run.sh` (Mac/Linux).

## Notes
- No API key? The app still runs in DEMO mode with an offline template.
- `gemini-1.5-pro` is retired; set `GEMINI_MODEL` in `.env` to any current Gemini model.
- PDF uses core fonts (Latin-1 only); other scripts show as `?` in the PDF. DOCX/TXT keep all characters.
- Offline self-check: `python tests/smoke_test.py`
- AI output is a draft, not legal advice.
