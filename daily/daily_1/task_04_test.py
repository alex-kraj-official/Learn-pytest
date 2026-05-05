import pytest
import task_04

class FakeResponse:
    def json(self):
        return {"id": 1, "name": "Alice"}

def test_fetch_user(monkeypatch):
    monkeypatch.setattr("requests.get", lambda url: FakeResponse())
    result = task_04.fetch_user(1)
    assert result["name"] == "Alice"