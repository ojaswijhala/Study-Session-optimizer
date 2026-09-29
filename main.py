"""Main console application for the Study Session Optimizer."""

from topic_manager import add_topic, display_topics
from study_planner import show_study_order
from progress_tracker import mark_completed, progress_summary
from search_manager import search_topic


def main():
    topics = []

    while True:
        print("\n")
        print("==========================================")
        print("       STUDY SESSION OPTIMIZER")
        print("==========================================")

        print("\n1. Add Topic")
        print("2. View All Topics")
        print("3. Suggested Study Order")
        print("4. Mark Topic as Completed")
        print("5. Search Topic")
        print("6. Progress Summary")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            add_topic(topics)

        elif choice == "2":
            display_topics(topics)

        elif choice == "3":
            show_study_order(topics)

        elif choice == "4":
            mark_completed(topics)

        elif choice == "5":
            search_topic(topics)

        elif choice == "6":
            progress_summary(topics)

        elif choice == "7":
            print("\nThank you for using Study Session Optimizer!")
            break

        else:
            print("\nInvalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
