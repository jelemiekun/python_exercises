import datetime

import constants
import variables


def is_input_valid(input: str, valid_input: str) -> bool:
    for num in valid_input:
        if input == num:
            return True

    return False


def ask_input_integer(start: int, end: int, message: str) -> int:
    valid_input_range: range = range(start, end)

    while True:
        user_input: str = input(message)

        if user_input.strip() == "":
            print("ERROR: Please provide input.")

        if is_input_valid(user_input, str(list(valid_input_range))):
            return int(user_input)

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
