"""Topic creation and display functions."""

from input_validator import (
    get_valid_deadline,
    get_valid_difficulty,
    get_valid_study_time,
)
from priority_calculator import calculate_priority


def create_topic():
    """Collect topic information and return a topic dictionary."""
    print("\n========== ADD NEW TOPIC ==========")

    subject = input("Enter subject: ")
    topic_name = input("Enter topic name: ")
    difficulty = get_valid_difficulty()
    deadline = get_valid_deadline()
    study_time = get_valid_study_time()

    priority_score, days_left = calculate_priority(
        difficulty, deadline, study_time
    )

    return {
        "subject": subject,
        "name": topic_name,
        "difficulty": difficulty,
        "deadline": deadline,
        "study_time": study_time,
        "days_left": days_left,
        "priority": priority_score,
        "completed": False,
    }


def add_topic(topics):
    """Create and append a topic to the supplied topic list."""
    topic = create_topic()
    topics.append(topic)

    print("\nTopic added successfully!")
    print("Priority Score:", topic["priority"])


def display_topics(topics):
    """Display all topics in the same console format as the original."""
    if not topics:
        print("\nNo topics have been added yet.")
        return

    print("\n========== ALL TOPICS ==========")

    for number, topic in enumerate(topics, start=1):
        status = "Completed" if topic["completed"] else "Pending"

        print("\nTopic", number)
        print("Subject:", topic["subject"])
        print("Topic:", topic["name"])
        print("Difficulty:", topic["difficulty"])
        print("Deadline:", topic["deadline"])
        print("Study Time:", topic["study_time"], "hours")
        print("Days Left:", topic["days_left"])
        print("Priority Score:", topic["priority"])
        print("Status:", status)
