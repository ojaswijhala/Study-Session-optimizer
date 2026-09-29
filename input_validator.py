"""Input validation helpers for console interaction."""

from datetime import datetime


def get_valid_difficulty():
    while True:
        difficulty = input(
            "Enter difficulty (Easy/Medium/Hard): "
        ).lower()

        if difficulty in ["easy", "medium", "hard"]:
            return difficulty.capitalize()

        print("Please enter Easy, Medium, or Hard.")


def get_valid_deadline():
    while True:
        deadline = input("Enter deadline (DD-MM-YYYY): ")

        try:
            datetime.strptime(deadline, "%d-%m-%Y")
            return deadline
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.")


def get_valid_study_time():
    while True:
        try:
            study_time = float(
                input("Enter estimated study time (hours): ")
            )

            if study_time > 0:
                return study_time

            print("Study time must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def get_valid_topic_number(prompt, maximum):
    """Read a topic number and return a zero-based index, or None on error."""
    try:
        number = int(input(prompt))
        if 1 <= number <= maximum:
            return number - 1
        print("\nInvalid topic number.")
    except ValueError:
        print("\nPlease enter a valid number.")
    return None
