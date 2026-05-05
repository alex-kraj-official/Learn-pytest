api_response = {
    "status": 200,
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "active": True},
            {"id": 2, "name": "Bob", "active": False},
            {"id": 3, "name": "Carol", "active": True},
        ]
    }
}

def get_active_users(resp : dict) -> list:
    # ["Alice", "Carol"]
    active_users = []
    for user in resp["data"]["users"]:
        if user["active"]:
            active_users.append(user["name"])
    return active_users

print(get_active_users(api_response))