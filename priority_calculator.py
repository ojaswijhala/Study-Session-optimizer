"""Priority calculation for the Study Session Optimizer."""

from datetime import datetime


def calculate_priority(difficulty, deadline, study_time):
    """Return (priority_score, days_left) using the project's existing rules."""
    if difficulty.lower() == "easy":
        difficulty_points = 1
    elif difficulty.lower() == "medium":
        difficulty_points = 2
    elif difficulty.lower() == "hard":
        difficulty_points = 3
    else:
        difficulty_points = 0

    deadline_date = datetime.strptime(deadline, "%d-%m-%Y")
    today = datetime.today()
    days_left = (deadline_date - today).days

    if days_left <= 2:
        deadline_points = 5
    elif days_left <= 5:
        deadline_points = 4
    elif days_left <= 10:
        deadline_points = 3
    elif days_left <= 20:
        deadline_points = 2
    else:
        deadline_points = 1

    if study_time >= 4:
        study_time_points = 3
    elif study_time >= 2:
        study_time_points = 2
    else:
        study_time_points = 1

    priority_score = difficulty_points + deadline_points + study_time_points
    return priority_score, days_left


def get_priority_level(priority):
    """Return the display label used by the original study-order feature."""
    if priority >= 9:
        return "HIGH"
    elif priority >= 6:
        return "MEDIUM"
    return "LOW"
