from typesafe_sdk import Choice, Score, TypeSafeClient


def main() -> None:
    print("Jev support-ticket triage POC")
    ticket = input("\nPaste a support ticket (or press Enter for the sample): ").strip()
    if not ticket:
        ticket = (
            "Our API integration started returning 500 errors about 20 minutes ago. "
            "We can't process customer orders until this is fixed."
        )

    with TypeSafeClient(model="jev-latest") as client:
        result = client.system_one(
            state=ticket,
            questions={
                "category": Choice(
                    instructions="Which team should handle this support ticket?",
                    criteria={
                        "technical": "Product bugs, outages, or integration problems",
                        "billing": "Payments, invoices, or subscription problems",
                        "account": "Login, access, or account settings",
                        "other": "Anything that does not fit the other categories",
                    },
                ),
                "urgency": Score(
                    instructions="How urgent is it to respond to this ticket?",
                    criteria=[
                        "Low: no time pressure and no meaningful impact",
                        "Normal: a problem, but work can continue",
                        "High: significant customer impact or a time-sensitive issue",
                    ],
                ),
            },
        )

    category = result.choices["category"]
    urgency = result.scores["urgency"]
    print("\nTriage result")
    print(f"  Team: {category.choice}")
    print(f"  Team confidence: {category.confidence:.0%}")
    print(f"  Urgency score: {urgency.score:.2f} (0=low, 2=high)")
    print(f"  Urgency confidence: {urgency.confidence:.0%}")
    print("\nThese are decision signals for the demo; a real support system should keep a human in the loop.")


if __name__ == "__main__":
    main()
