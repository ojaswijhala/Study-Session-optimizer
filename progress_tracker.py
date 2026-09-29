"""Completion and progress tracking."""

from input_validator import get_valid_topic_number
from topic_manager import display_topics


def mark_completed(topics):
    """Mark a selected topic as completed."""
    if not topics:
        print("\nNo topics available.")
        return

    display_topics(topics)
    index = get_valid_topic_number(
        "\nEnter topic number to mark completed: ",
        len(topics),
    )

    if index is None:
        return

    if topics[index]["completed"]:
        print("\nThis topic is already completed.")
    else:
        topics[index]["completed"] = True
        print("\nTopic marked as completed!")


def get_progress(topics):
    """Return total, completed, pending, and percentage."""
    total = len(topics)
    completed = sum(1 for topic in topics if topic["completed"])
    pending = total - completed
    progress = (completed / total) * 100 if total else 0
    return total, completed, pending, progress


def progress_summary(topics):
    """Display the current progress summary."""
    total, completed, pending, progress = get_progress(topics)

    if total == 0:
        print("\nNo topics available.")
        return

    print("\n========== PROGRESS SUMMARY ==========")
    print("Total Topics:", total)
    print("Completed:", completed)
    print("Pending:", pending)
    print("Progress:", round(progress, 2), "%")

    if progress == 100:
        print("All topics completed! Great work!")
    elif progress >= 75:
        print("Most of your topics are completed.")
    elif progress >= 50:
        print("You are more than halfway through.")
    else:
        print("Keep working through your pending topics.")
