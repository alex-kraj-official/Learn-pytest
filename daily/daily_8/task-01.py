test_results = [
    {"test": "login", "status": "passed"},
    {"test": "logout", "status": "failed"},
    {"test": "register", "status": "passed"},
    {"test": "delete_user", "status": "failed"},
    {"test": "update_profile", "status": "passed"},
    {"test": "reset_password", "status": "skipped"},
]

# {
#     "passed": ["login", "register", "update_profile"],
#     "failed": ["logout", "delete_user"],
#     "skipped": ["reset_password"]
# }

def group_by_status(test_results: list) -> dict:
    passed_results = [t["test"] for t in test_results if t["status"] == "passed"]
    failed_results = [t["test"] for t in test_results if t["status"] == "failed"]
    skipped_results = [t["test"] for t in test_results if t["status"] == "skipped"]

    grouped_results = {
        "passed": passed_results,
        "failed": failed_results,
        "skipped": skipped_results
    }
    
    return grouped_results

print(group_by_status(test_results))