errors = [
    {"code": 404, "message": "Not found"},
    {"code": 200, "message": "OK"},
    {"code": 500, "message": "Internal Server Error"},
    {"code": 200, "message": "OK"},
    {"code": 403, "message": "Forbidden"},
]

def get_errors(errors_in):
    errors_out = []
    for error in errors_in:
        if error["code"] != 200:
            errors_out.append(error)

    return errors_out

print(get_errors(errors))