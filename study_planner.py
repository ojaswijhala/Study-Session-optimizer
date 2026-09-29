"""Study-order generation."""

from priority_calculator import get_priority_level


def get_pending_topics(topics):
    """Return pending topics sorted by descending priority."""
    pending_topics = [
        topic for topic in topics if not topic["completed"]
    ]
    pending_topics.sort(
        key=lambda topic: topic["priority"],
        reverse=True,
    )
    return pending_topics


def show_study_order(topics):
    """Display the suggested study order."""
    if not topics:
        print("\nNo topics available.")
        return

    pending_topics = get_pending_topics(topics)

    if not pending_topics:
        print("\nAll topics are completed!")
        return

    print("\n========== SUGGESTED STUDY ORDER ==========")

    for number, topic in enumerate(pending_topics, start=1):
        priority_level = get_priority_level(topic["priority"])

        print(f"\n{number}. {topic['name']}")
        print("   Subject:", topic["subject"])
        print("   Difficulty:", topic["difficulty"])
        print("   Deadline:", topic["deadline"])
        print("   Days Left:", topic["days_left"])
        print("   Study Time:", topic["study_time"], "hours")
        print("   Priority Score:", topic["priority"])
        print("   Priority Level:", priority_level)
