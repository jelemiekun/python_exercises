import sys
from enum import Enum

MENU_MESSAGE: str = """

    === Geometry Analyzer ===

    1. Circle
    2. Rectangle
    3. Triangle
    4. Distance between points
    5. Show History
    6. Show Statistics
    7. Exit
    
"""

MENU_INPUT_START: int = 1

# If menu gets updated, update this also
MENU_INPUT_END: int = 7

MENU_INPUT_MESSAGE: str = "Choose an option: "

OPERATION_INPUT_MINIMUM: int = 0

OPERATION_INPUT_MAXIMUM: int = 2**15 - 1

VALID_INPUT_INTEGERS = "0123456789"


# If menu gets updated, update this also
class Operation_Type(Enum):
    OPERATION_NAME_CIRCLE = "Circle      "
    OPERATION_NAME_RECTANGLE = "Rectangle   "
    OPERATION_NAME_TRIANGLE = "Triangle    "
    OPERATION_NAME_DISTANCE = "Distance    "
    OPERATION_NAME_HISTORY = "History     "
    OPERATION_NAME_STATISTICS = "Statistics  "
    OPERATION_MENU_DEFAULT = "Default"
