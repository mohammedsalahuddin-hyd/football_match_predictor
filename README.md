# Sports Match Prediction App

A beginner-friendly terminal application using:

- Python
- API-Football
- LangChain
- Google Gemini

## 1. Create virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 2. Install packages

```bash
pip install -r requirements.txt
```

## 3. Create .env

Copy:

```text
.env.example
```

to:

```text
.env
```

Then add:

```text
SPORTS_API_KEY=your_api_football_key
GOOGLE_API_KEY=your_gemini_key
```

Do not share your real API keys.

## 4. Run

```bash
python main.py
```

## Important

This is the BASIC version.

The current prediction engine uses sample statistics so that the complete application flow can be tested.

Next version will replace the sample statistics with real:

- Recent form
- Team standings
- Home/away performance
- Head-to-head data
- Goals scored/conceded

The prediction is educational and should not be treated as guaranteed or professional betting advice.
