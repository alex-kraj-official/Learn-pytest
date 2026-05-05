api_response = {
    "status": 201,
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "active": True},
            {"id": 2, "name": "Bob", "active": False},
            {"id": 3, "name": "Carol", "active": True},
        ]
    }
}

def validate_api_response(resp: dict) -> bool:
    if resp["status"] != 200:
        raise ValueError(f"Unexpected status code: {resp["status"]}")
    else:
        return True

print(validate_api_response(api_response))