def predict_match(data):
    """
    Very simple educational prediction model.

    This is NOT a professional betting model.
    It is intentionally simple for the first version.
    """

    home_form = sum(data["home_form"])
    away_form = sum(data["away_form"])

    home_attack = data["home_goals_avg"]
    away_attack = data["away_goals_avg"]

    home_defense = data["home_conceded_avg"]
    away_defense = data["away_conceded_avg"]

    home_score = (
        home_form * 0.35
        + home_attack * 0.25
        + away_defense * 0.15
        + 0.25  # home advantage
    )

    away_score = (
        away_form * 0.35
        + away_attack * 0.25
        + home_defense * 0.15
    )

    total = home_score + away_score

    home_probability = home_score / total
    away_probability = away_score / total

    # Reserve some probability for a draw.
    draw_probability = 0.20
    remaining = 0.80

    home_probability = home_probability * remaining
    away_probability = away_probability * remaining

    # Normalize.
    total_probability = (
        home_probability + draw_probability + away_probability
    )

    home_probability /= total_probability
    draw_probability /= total_probability
    away_probability /= total_probability

    probabilities = {
        "home": home_probability,
        "draw": draw_probability,
        "away": away_probability,
    }

    best = max(probabilities, key=probabilities.get)

    if best == "home":
        result = data["home_team"] + " Win"
    elif best == "away":
        result = data["away_team"] + " Win"
    else:
        result = "Draw"

    expected_home = max(0, round(
        (data["home_goals_avg"] + data["away_conceded_avg"]) / 2
    ))

    expected_away = max(0, round(
        (data["away_goals_avg"] + data["home_conceded_avg"]) / 2
    ))

    return {
        "result": result,
        "home_win": round(home_probability * 100, 1),
        "draw": round(draw_probability * 100, 1),
        "away_win": round(away_probability * 100, 1),
        "expected_score": f"{expected_home}-{expected_away}",
    }
