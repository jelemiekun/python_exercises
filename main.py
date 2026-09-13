import constants
import data_processing
import geometry
import util
import variables


def print_menu() -> None:
    print(constants.MENU_MESSAGE)


def input_loop_validation() -> None:
    print_menu()

    variables.user_input = util.ask_input_integer(
        constants.MENU_INPUT_START,
        constants.MENU_INPUT_END,
        constants.MENU_INPUT_MESSAGE,
    )

    print("\n")


def is_input_exit() -> bool:
    return variables.user_input == constants.MENU_INPUT_END


def determine_user_operation() -> None:
    # If menu gets updated, update this also
    match variables.user_input:
        case 1:
            variables.operation_type = constants.Operation_Type.OPERATION_NAME_CIRCLE
        case 2:
            variables.operation_type = constants.Operation_Type.OPERATION_NAME_RECTANGLE
        case 3:
            variables.operation_type = constants.Operation_Type.OPERATION_NAME_TRIANGLE
        case 4:
            variables.operation_type = constants.Operation_Type.OPERATION_NAME_DISTANCE
        case 5:
            variables.operation_type = constants.Operation_Type.OPERATION_NAME_HISTORY
        case 6:
            variables.operation_type = (
                constants.Operation_Type.OPERATION_NAME_STATISTICS
            )
        case _:
            variables.operation_type = constants.Operation_Type.OPERATION_MENU_DEFAULT


def perform_user_operation() -> None:
    # If menu gets updated, update this also
    match variables.operation_type:
        case constants.Operation_Type.OPERATION_NAME_CIRCLE:
            geometry.operation_circle()
        case constants.Operation_Type.OPERATION_NAME_RECTANGLE:
            geometry.operation_rectangle()
        case constants.Operation_Type.OPERATION_NAME_TRIANGLE:
            geometry.operation_triangle()
        case constants.Operation_Type.OPERATION_NAME_DISTANCE:
            geometry.operation_distance()
        case constants.Operation_Type.OPERATION_NAME_HISTORY:
            data_processing.display_history()
        case constants.Operation_Type.OPERATION_NAME_STATISTICS:
            data_processing.display_statistics()
        case _:
            print("ERROR: Invalid operation.")


def print_result() -> None:
    results: dict[str, float] = variables.history[-1][4]

    results_keys = results.keys()

    print("\n")
    for key in results_keys:
        print(f"{key}: {results[key]}")


def main() -> None:
    while not variables.exit_program:
        input_loop_validation()
        variables.exit_program = is_input_exit()

        if not variables.exit_program:
            determine_user_operation()
            perform_user_operation()

            if util.is_operation_with_result():
                print_result()

            blank: str = input("\nPress Enter to continue...")
            del blank

    print("Thank you. Goodbye.")


main()
