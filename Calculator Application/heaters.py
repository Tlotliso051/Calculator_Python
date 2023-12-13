def print_welcome_message(welcome_message):
    """
    Function prints out heater welcome message.
    """
    print()
    print(welcome_message.center(50, "-"))


def display_operator():
    """
    Function display operators to user.
    """
    print_welcome_message("LIST OF OPERATORS")
    print("add (+)\nsubtract (-)\ndivide (/)\nmultiply (*)")