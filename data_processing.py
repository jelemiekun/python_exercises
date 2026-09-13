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


def display_statistics() -> None:
    if is_history_empty():
        return
