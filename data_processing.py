import variables


def display_history() -> None:
    for record in variables.history:
        print(f"""
            {record[0]} | {record[2].value} | {record[3]} | {record[4]} | {record[1]}
        """)


def display_statistics() -> None:
    pass
