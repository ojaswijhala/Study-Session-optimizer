# Testing Report

The project was tested using functional checks and automated tests for the priority rules.

| ID | Test | Expected Result |
|---|---|---|
| TC-01 | Add Topic | Topic added and priority displayed |
| TC-02 | View Topics | Stored topics displayed |
| TC-03 | Suggested Order | Pending topics sorted by priority |
| TC-04 | Mark Completed | Selected topic becomes completed |
| TC-05 | Progress | Counts and percentage displayed |
| TC-06 | Search | Matching topic/subject displayed |
| TC-07 | Invalid Input | Invalid value rejected and re-entered |

The automated test file is `tests/test_project.py`.
