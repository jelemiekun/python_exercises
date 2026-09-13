import datetime

import constants

user_input: int = -1

exit_program: bool = False

history_count: int = 0
history: list[
    tuple[
        int,
        datetime.datetime,
        constants.Operation_Type,
        dict[str, int],
        dict[str, float],
    ]
] = []
# Operation_ID,
# Operation_Timestamp,
# Operation_Name,
# Operation_Inputs,
# *Operation_Outputs

operation_type: str
