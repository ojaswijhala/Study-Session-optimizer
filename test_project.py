"""Non-interactive tests for the modular Study Session Optimizer."""

import sys
from pathlib import Path
from datetime import datetime, timedelta
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from priority_calculator import calculate_priority, get_priority_level
from study_planner import get_pending_topics
from progress_tracker import get_progress
from search_manager import search_topics


class TestStudySessionOptimizer(unittest.TestCase):

    def test_priority_calculation(self):
        deadline = (datetime.today() + timedelta(days=1)).strftime("%d-%m-%Y")
        score, days_left = calculate_priority("Hard", deadline, 4)
        self.assertEqual(score, 11)
        self.assertLessEqual(days_left, 1)

    def test_priority_levels(self):
        self.assertEqual(get_priority_level(9), "HIGH")
        self.assertEqual(get_priority_level(6), "MEDIUM")
        self.assertEqual(get_priority_level(5), "LOW")

    def test_study_order_excludes_completed_and_sorts(self):
        topics = [
            {"name": "A", "priority": 6, "completed": False},
            {"name": "B", "priority": 10, "completed": False},
            {"name": "C", "priority": 12, "completed": True},
        ]
        pending = get_pending_topics(topics)
        self.assertEqual([t["name"] for t in pending], ["B", "A"])

    def test_progress_summary_values(self):
        topics = [
            {"completed": True},
            {"completed": False},
            {"completed": False},
        ]
        total, completed, pending, progress = get_progress(topics)
        self.assertEqual((total, completed, pending), (3, 1, 2))
        self.assertAlmostEqual(progress, 100 / 3, places=10)

    def test_search_by_topic_or_subject(self):
        topics = [
            {"name": "Calculus", "subject": "Mathematics"},
            {"name": "Networks", "subject": "Computer Science"},
        ]
        self.assertEqual(len(search_topics(topics, "calculus")), 1)
        self.assertEqual(len(search_topics(topics, "computer")), 1)

    def test_empty_progress(self):
        self.assertEqual(get_progress([]), (0, 0, 0, 0))


if __name__ == "__main__":
    unittest.main()
