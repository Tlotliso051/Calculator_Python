from operations import *
from heaters import display_operator , print_welcome_message
from user_inputs import *
print_welcome_message("WELCOME TO CODSOFT CALCULATOR")
def handle_calculations(operator,first_value,second_value):
    """
    Funtion handles all operations in the calculator.
    """
    if operator in "add+":
        add(first_value,second_value)
    elif operator in "subtract-":
        subtract(first_value,second_value)
    elif operator in "divide/":
        divide(first_value,second_value)
    elif operator in "multiply*":
        multiply(first_value,second_value)
    

def main():
    """
    Function is the main of the Caculator.
    """
    display_operator()
    print()
    while True:
        operator = choose_operator("Choose operator from list: ").lower()
        try:
            first_value = int(get_numbers_from_user(mes()))
            second_value = int(get_numbers_from_user(mes()))
        except:
            print("Please enter only numeric values.")

        handle_calculations(operator,first_value,second_value)


if __name__ == "__main__":
    main()