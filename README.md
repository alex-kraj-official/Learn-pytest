# Learn-pytest

Structured daily Python & pytest practice. Each session contains small, self-contained tasks solved from scratch — no AI assistance during solving, just problem-solving and testing.

The goal is to build real understanding of Python fundamentals and test automation patterns, not just produce working code.

---

## What's in here

### `daily/` — Daily practice sessions

Each `daily_N` folder contains one or more tasks with accompanying tests.

| Session | Topics covered |
|---------|---------------|
| `daily_0` | Dict validation, `pytest.fixture`, edge case testing (missing key, empty string, boundary age) |
| `daily_1` | Nested dict/list traversal, `pytest.raises`, `monkeypatch` for faking HTTP requests |
| `daily_2` | List filtering, `any()`, fixtures returning computed results, empty list edge cases |
| `daily_3` | `max()` with `lambda`, list comprehension, `None` return handling |
| `daily_4` | `ValueError` with message matching, multi-assert tests, `.copy()` to protect test isolation, dict summarization |
| `daily_5` | Grouping and aggregating by category using `sum()` and comprehensions |

### `others/` — Standalone experiments

- `character.py` / `character_test.py` — OOP with inheritance: `Character` base class with `Warrior`, `Mage`, `Hunter` subclasses; HP/armor damage and healing logic
- `utils.py` / `utils_test.py` — Type annotations, basic utility functions
- `report.py` / `report_test.py` — JSON file generation

---

## Techniques practiced

- `pytest.fixture` for test setup and reusable test data
- `pytest.raises` for testing exceptions (including message matching with `match=`)
- `monkeypatch` for replacing external dependencies (e.g. HTTP calls)
- `.copy()` to prevent test pollution when modifying shared data
- Type hints (`-> dict`, `list[int]`, etc.)
- List comprehensions and generator expressions
- `any()`, `sum()`, `max()` with lambdas
- OOP: classes, inheritance, `super()`

---

## How to run

```bash
# Install dependencies
pip install pytest

# Run all tests from project root
pytest

# Run a specific session
pytest daily/daily_4/
```

---

## Stack

- Python 3.14
- pytest 9.0.3
