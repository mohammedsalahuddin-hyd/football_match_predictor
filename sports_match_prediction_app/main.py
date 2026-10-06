from api.sports_api import SportsAPI
from prediction.predictor import predict_match
from langchain_app.match_chat import MatchChat


def print_matches(matches):
    print("\n" + "=" * 60)
    print("           SPORTS MATCH PREDICTION APP")
    print("=" * 60)

    if not matches:
        print("\nNo matches found.")
        return

    print("\nCurrent matches:\n")
    for i, match in enumerate(matches, start=1):
        print(
            f"{i}. {match['home_team']} vs {match['away_team']} "
            f"| {match['league']} | {match['date']}"
        )


def main():
    api = SportsAPI()

    print("Fetching current football matches...")
    matches = api.get_current_matches()

    print_matches(matches)

    if not matches:
        return

    try:
        choice = int(input("\nChoose a match number: "))
        if choice < 1 or choice > len(matches):
            print("Invalid choice.")
            return
    except ValueError:
        print("Please enter a number.")
        return

    selected_match = matches[choice - 1]

    print("\nFetching match statistics...")
    details = api.get_match_details(selected_match)

    prediction = predict_match(details)

    print("\n" + "=" * 60)
    print("MATCH PREDICTION")
    print("=" * 60)
    print(f"\n{selected_match['home_team']} vs {selected_match['away_team']}")
    print(f"\nPredicted result : {prediction['result']}")
    print(f"Home win        : {prediction['home_win']}%")
    print(f"Draw            : {prediction['draw']}%")
    print(f"Away win        : {prediction['away_win']}%")
    print(f"Expected score  : {prediction['expected_score']}")

    print("\nType 'exit' to quit the AI chat.")
    chat = MatchChat(selected_match, details, prediction)

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            answer = chat.ask(question)
            print(f"AI: {answer[0]['text']}")
        except Exception as e:
            print(f"AI error: {e}")


if __name__ == "__main__":
    main()
