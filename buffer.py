def greeting(name: str) -> None:
    print(f"Hello, {name}")


def createRange(start: int = 0, stop: int = 1, step: int = 1) -> list[int]:
    my_list: list[int] = []
    while start < stop:
        my_list.append(start)

        start += step

    return my_list
