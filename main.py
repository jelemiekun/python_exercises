import sys

import constants
import variables


def print_menu() -> None:
    print(constants.MENU_MESSAGE)


def is_input_valid(input: str, valid_input: str) -> bool:
    for num in valid_input:
        if input == num:
            return True

    return False


def ask_input_integer(start: int, end: int, message: str) -> int:
    valid_input_range: range = range(start, end)

    user_input: str = input(message)

    if user_input.strip() == "":
        return -1

    if is_input_valid(user_input, str(list(valid_input_range))):
        return int(user_input)

    return -1


def input_loop_validation() -> None:
    print_menu()

    while variables.user_input == -1:
        variables.user_input = ask_input_integer(
            constants.MENU_INPUT_START,
            constants.MENU_INPUT_END,
            constants.MENU_INPUT_MESSAGE,
        )


def is_input_exit() -> None:
    if variables.user_input == 5:
        sys.exit()


def main() -> None:
    input_loop_validation()
    is_input_exit()


main()
