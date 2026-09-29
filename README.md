# Study Session Optimizer

A rule-based study planning and progress tracking system developed in Python for CSE1021 – Problem Solving and Programming.

## Features
- Add study topics
- Validate difficulty, deadline, and study time
- Calculate a rule-based priority score
- Generate a suggested study order
- Mark topics as completed
- Search by topic name or subject
- Display progress summary
- Handle common invalid inputs

## Technologies
- Python 3
- Standard Python library only
- Console interface

## Project Structure
- `main.py` — application menu and program entry point
- `topic_manager.py` — topic creation and display
- `priority_calculator.py` — priority calculation and priority levels
- `study_planner.py` — pending-topic filtering and study ordering
- `progress_tracker.py` — completion and progress tracking
- `search_manager.py` — topic/subject search
- `input_validator.py` — console input validation
- `tests/test_project.py` — automated non-interactive tests

## How to Run
Run:

```bash
python main.py
```

## Testing
Run:

```bash
python -m unittest discover -s tests -v
```

The repository should be tested again after any final changes.

## Storage
Topics are stored in memory only while the program is running. Restarting the application clears the current topic list.
