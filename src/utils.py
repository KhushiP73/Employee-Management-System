from datetime import datetime

def get_integer(prompt, allow_zero=False):
    while True:
        try:
            value = int(input(prompt))
            if not allow_zero and value <= 0:
                print("Please enter a positive number.")
                continue

            if allow_zero and value < 0:
                print("Please enter zero or a positive number.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
                continue
            return value

        except ValueError:
            print("Please enter a valid number.")


def get_required_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_email(prompt):
    while True:
        email = input(prompt).strip()
        if "@" in email and "." in email.split("@")[-1]:
            return email
        print("Please enter a valid email address.")


def get_date(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return datetime.strptime(
                value,
                "%Y-%m-%d"
            ).date()

        except ValueError:
            print("Please use YYYY-MM-DD format.")


def get_attendance_status():
    valid_statuses = {
        "present": "Present",
        "absent": "Absent",
        "leave": "Leave",
    }
    while True:
        status = input(
            "Status (Present/Absent/Leave): "
        ).strip().lower()
        if status in valid_statuses:
            return valid_statuses[status]
        print(
            "Invalid status. "
            "Choose Present, Absent or Leave."
        )