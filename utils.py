def get_integer_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


def get_float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_valid_age(message):
    while True:
        age = get_integer_input(message)

        if age > 0:
            return age

        print("Age must be greater than 0.")


def get_valid_marks(message):
    while True:
        marks = get_float_input(message)

        if 0 <= marks <= 100:
            return marks

        print("Marks must be between 0 and 100.")