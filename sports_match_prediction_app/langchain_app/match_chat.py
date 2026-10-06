import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class MatchChat:
    def __init__(self, match, details, prediction):
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY is missing. Add it to your .env file."
            )

        self.match = match
        self.details = details
        self.prediction = prediction

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            temperature=0.2,
            google_api_key=api_key,
        )

    def ask(self, question):
        context = f"""
You are a football match analysis assistant.

Answer only about this selected match.

MATCH:
{self.match['home_team']} vs {self.match['away_team']}

LEAGUE:
{self.match['league']}

STATISTICS:
{self.details}

PREDICTION:
{self.prediction}

USER QUESTION:
{question}

Rules:
- Use the supplied data.
- Do not invent statistics.
- Explain that the prediction is only an estimate.
- Keep the answer clear and beginner-friendly.
"""

        response = self.llm.invoke(context)
        return response.content
