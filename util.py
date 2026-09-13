import datetime

import constants
import variables


def is_input_valid_integer(input: str) -> bool:
    for char in input:
        if char not in constants.VALID_INPUT_INTEGERS:
            return False

    return True


def ask_input_integer(start: int, end: int, message: str) -> int:

    while True:
        user_input: str = input(message)

        if user_input.strip() == "":
            print("ERROR: Please provide input.")
            continue

        if not is_input_valid_integer(user_input):
            print("ERROR: Invalid character(s) detected.")
            continue

        user_input_integer: int = int(user_input)

        if user_input_integer >= start and user_input_integer <= end:
            return user_input_integer

        print(f"ERROR: Invalid input. Accepable range: {start} to {end - 1}")


def add_operation_to_list(
    operation_type: constants.Operation_Type,
    inputs: list[dict[str, int]],
    outputs: list[dict[str, float]],
) -> None:
    variables.history_count += 1
    timestamp: datetime.datetime = datetime.datetime.now()

    variables.history.append(
        (variables.history_count, timestamp, operation_type, inputs, outputs)
    )
