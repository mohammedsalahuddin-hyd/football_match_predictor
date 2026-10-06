import os
from datetime import datetime, timezone
import requests
from dotenv import load_dotenv

load_dotenv()


class SportsAPI:
    """
    Basic API-Football client.

    This starter uses API-Football's fixtures endpoint.
    Put your API key in .env as SPORTS_API_KEY.
    """

    BASE_URL = "https://v3.football.api-sports.io"

    def __init__(self):
        self.api_key = os.getenv("SPORTS_API_KEY")

    def _headers(self):
        return {"x-apisports-key": self.api_key}

    def get_current_matches(self):
        if not self.api_key:
            print("\nSPORTS_API_KEY is missing.")
            print("Copy .env.example to .env and add your API key.")
            return []

        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        try:
            response = requests.get(
                f"{self.BASE_URL}/fixtures",
                headers=self._headers(),
                params={"date": today},
                timeout=15,
            )
            response.raise_for_status()
            data = response.json()

            matches = []

            for item in data.get("response", []):
                fixture = item["fixture"]
                teams = item["teams"]
                league = item["league"]

                matches.append({
                    "id": fixture["id"],
                    "date": fixture["date"],
                    "status": fixture["status"]["short"],
                    "home_team": teams["home"]["name"],
                    "away_team": teams["away"]["name"],
                    "league": league["name"],
                    "country": league["country"],
                })

            return matches[:20]

        except requests.RequestException as e:
            print(f"\nSports API error: {e}")
            return []

    def get_match_details(self, match):
        """
        Basic version: returns placeholder/simple data so the prediction
        pipeline can be tested even before adding more API endpoints.
        """

        # TODO:
        # In the next version, use API-Football endpoints for:
        # - team form
        # - standings
        # - head-to-head
        # - goals statistics

        return {
            "home_team": match["home_team"],
            "away_team": match["away_team"],
            "home_form": [1, 1, 0, 1, 0],
            "away_form": [1, 0, 1, 0, 1],
            "home_goals_avg": 1.5,
            "away_goals_avg": 1.2,
            "home_conceded_avg": 1.0,
            "away_conceded_avg": 1.1,
        }
