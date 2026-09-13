import constants
import variables


def is_history_empty() -> bool:
    if variables.history_count == 0:
        print("INFO: History is empty.")
        return True

    return False


def display_history() -> None:
    if is_history_empty():
        return

    for record in variables.history:
        print(f"""
            {record[0]} | {record[2].value} | {record[3]} | {record[4]} | {record[1]}
        """)


def calculate_number_of_occurence() -> list[int]:
    circle_count: int = 0
    rectangle_count: int = 0
    triangle_count: int = 0
    distance_count: int = 0

    for record in variables.history:
        match record[2]:
            case constants.Operation_Type.OPERATION_NAME_CIRCLE:
                circle_count += 1
            case constants.Operation_Type.OPERATION_NAME_RECTANGLE:
                rectangle_count += 1
            case constants.Operation_Type.OPERATION_NAME_TRIANGLE:
                triangle_count += 1
            case constants.Operation_Type.OPERATION_NAME_DISTANCE:
                distance_count += 1
            case _:
                print("ERROR: Invalid operation encountered.")

    return [circle_count, rectangle_count, triangle_count, distance_count]


def calculate_percentage_of_occurence(number_of_occurences: list[int]) -> list[float]:
    percentages: list[float] = []

    for occurences in number_of_occurences:
        percentage: float = (occurences / variables.history_count) * 100
        percentages.append(percentage)

    return percentages


def calculate_statistics() -> list[dict[int, float]]:
    number_of_occurences: list[int] = calculate_number_of_occurence()
    occurences_percentage: list[float] = calculate_percentage_of_occurence(
        number_of_occurences
    )

    overall_stat: list[dict[int, float]] = []

    for index in range(len(number_of_occurences)):
        overall_stat.append({number_of_occurences[index]: occurences_percentage[index]})

    return overall_stat


def find_largest_calculated_value() -> float:
    largest_value: float = 0

    for record in variables.history:
        for output in record[4].values():
            if output > largest_value:
                largest_value = output

    return largest_value


def find_smallest_calculated_value() -> float:
    smallest_value: float = constants.OPERATION_INPUT_MAXIMUM

    for record in variables.history:
        for output in record[4].values():
            if output < smallest_value:
                smallest_value = output

    return smallest_value


def display_statistics() -> None:
    if is_history_empty():
        return

    occurence_percent: list[dict[int, float]] = calculate_statistics()
    largest_calculated_value = find_largest_calculated_value()
    smallest_calculated_value = find_smallest_calculated_value()

    print(f"""

    === Statistics ===

    Total number of calculations: {variables.history_count} 
    
    Number of usage | Percentage
    Circle:     {occurence_percent[0]}
    Rectangle:  {occurence_percent[1]}
    Triangle:   {occurence_percent[2]}
    Distance:   {occurence_percent[3]}

    Largest Calculated Value:   {largest_calculated_value}
    Smallest Calculated Value:  {smallest_calculated_value}
    
    """)
