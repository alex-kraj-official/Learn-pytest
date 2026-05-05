def get_user_from_db(user_id: int) -> dict:
    db = {
        1: {"name": "Alice", "active": True},
        2: {"name": "Bob", "active": False},
    }
    return db[user_id]