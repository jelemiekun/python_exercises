import math

import constants
import util


def operation_circle() -> None:
    radius: int = util.ask_input_integer(
        constants.OPERATION_INPUT_MINIMUM, constants.OPERATION_INPUT_MAXIMUM, "Radius: "
    )

    area: float = math.pi * (pow(radius, 2))
    circumference: float = 2 * math.pi * radius

    util.add_operation_to_list(
        constants.Operation_Type.OPERATION_NAME_CIRCLE,
        [{"radius": radius}],
        [{"area": area}, {"circumference": circumference}],
    )


def operation_rectangle() -> None:
    width: int = util.ask_input_integer(
        constants.OPERATION_INPUT_MINIMUM, constants.OPERATION_INPUT_MAXIMUM, "Width: "
    )
    height: int = util.ask_input_integer(
        constants.OPERATION_INPUT_MINIMUM, constants.OPERATION_INPUT_MAXIMUM, "Height: "
    )

    area: float = width * height
    diagonal: float = math.sqrt(pow(width, 2) + pow(height, 2))

    util.add_operation_to_list(
        constants.Operation_Type.OPERATION_NAME_RECTANGLE,
        [{"width": width}, {"height": height}],
        [{"area": area}, {"diagonal": diagonal}],
    )


def operation_triangle() -> None:
    base: int = util.ask_input_integer(
        constants.OPERATION_INPUT_MINIMUM, constants.OPERATION_INPUT_MAXIMUM, "Base: "
    )
    height: int = util.ask_input_integer(
        constants.OPERATION_INPUT_MINIMUM, constants.OPERATION_INPUT_MAXIMUM, "Height: "
    )

    area: float = (base * height) / 2

    util.add_operation_to_list(
        constants.Operation_Type.OPERATION_NAME_TRIANGLE,
        [{"base": base}, {"height": height}],
        [{"area": area}],
    )


def operation_distance() -> None:
    x_1: int = util.ask_input_integer(
        constants.OPERATION_INPUT_MINIMUM, constants.OPERATION_INPUT_MAXIMUM, "x_1: "
    )
    y_1: int = util.ask_input_integer(
        constants.OPERATION_INPUT_MINIMUM, constants.OPERATION_INPUT_MAXIMUM, "y_1: "
    )
    x_2: int = util.ask_input_integer(
        constants.OPERATION_INPUT_MINIMUM, constants.OPERATION_INPUT_MAXIMUM, "x_2: "
    )
    y_2: int = util.ask_input_integer(
        constants.OPERATION_INPUT_MINIMUM, constants.OPERATION_INPUT_MAXIMUM, "y_2: "
    )

    distance: float = math.sqrt(pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2))

    util.add_operation_to_list(
        constants.Operation_Type.OPERATION_NAME_DISTANCE,
        [{"x_1": x_1}, {"y_1": y_1}, {"x_2": x_2}, {"y_2": y_2}],
        [{"distance": distance}],
    )
