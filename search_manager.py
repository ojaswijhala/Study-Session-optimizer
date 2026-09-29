"""Topic and subject search."""

def search_topics(topics, search):
    """Return topics whose name or subject contains the search text."""
    search = search.lower()
    return [
        topic
        for topic in topics
        if search in topic["name"].lower()
        or search in topic["subject"].lower()
    ]


def search_topic(topics):
    """Interactively search topics and display matching results."""
    if not topics:
        print("\nNo topics available.")
        return

    search = input(
        "\nEnter topic name or subject to search: "
    ).lower()

    found_topics = search_topics(topics, search)

    print("\n========== SEARCH RESULTS ==========")

    for topic in found_topics:
        status = "Completed" if topic["completed"] else "Pending"

        print("\nTopic:", topic["name"])
        print("Subject:", topic["subject"])
        print("Difficulty:", topic["difficulty"])
        print("Deadline:", topic["deadline"])
        print("Priority Score:", topic["priority"])
        print("Status:", status)

    if not found_topics:
        print("No matching topic found.")
