# Design Decisions

- Console interface keeps the implementation focused on programming fundamentals.
- A list of dictionaries stores topic records during execution.
- `datetime.strptime` validates deadlines and calculates days remaining.
- Sorting by priority in descending order generates the suggested study order.
- Input loops handle invalid difficulty, date, and study-time entries.
- Search is case-insensitive and checks both topic name and subject.
