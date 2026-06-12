import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


def validate_user_data(data):
    if not data:
        return False, "Invalid request data"

    if not data.get("name"):
        return False, "Name is required"

    if not data.get("email"):
        return False, "Email is required"

    if not data.get("role"):
        return False, "Role is required"

    if not is_valid_email(data.get("email")):
        return False, "Invalid email format"

    return True, None