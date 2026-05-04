userslol = {
    "username": "asd",
    "age": 18
}

def is_valid_user(user) -> bool:
    return bool(user.get("username")) and user.get("age", 0) >= 18
    
print(is_valid_user(userslol))
