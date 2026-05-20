test_results = [
    {"test": "login", "status": "passed"},
    {"test": "logout", "status": "failed"},
    {"test": "register", "status": "passed"},
    {"test": "delete_user", "status": "failed"},
    {"test": "update_profile", "status": "passed"},
]

def get_failed_tests(test_results: list) -> list:
    # failed_tests = []
    # failed_tests.append(test["test"] for test in test_results if test["status"] == "failed")

    # for test in test_results:
    #     if test["status"] == "failed":
    #         failed_tests.append(test["test"])
    # return failed_tests

    return [test["test"] for test in test_results if test["status"] == "failed"]

print(get_failed_tests(test_results))