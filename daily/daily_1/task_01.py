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

def is_success_response(resp: dict) -> bool:
    got_an_active_user = False
    for user_active in resp["data"]["users"]:
        if user_active["active"]: got_an_active_user = True
        break
    return resp["status"] == 200 and got_an_active_user

print(is_success_response(api_response))