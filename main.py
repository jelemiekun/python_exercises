import numpy as np


def prac_1() -> None:
    arr = np.array(
        [
            [20, 34, 48, 28, 4],
            [34, 43, 45, 22, 34],
            [34, 28, 27, 45, 23],
            [23, 50, 26, 12, 25],
            [42, 23, 43, 47, 37],
        ]
    )

    print(arr)
    print(f"1. {arr[2, 1]}")
    print(f"2. {arr[3, :]}")
    print(f"3. {arr[:, 0]}")  # Supposed column 0 is math
    print(f"4. {arr[1:3, :]}")
    print(f"5. {arr.shape}, {arr.size}, {arr.dtype}")

    print(np.random.randint(100, size=(arr.shape)))


def prac_calls() -> None:
    # prac_1()
    pass


prac_calls()
