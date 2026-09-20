import numpy as np


def prac_1() -> None:
    inventory = np.array(
        [
            12,
            8,
            15,
            20,
            7,
            11,
            14,
            9,
            18,
            6,
            13,
            21,
            10,
            16,
            5,
            19,
            8,
            12,
            17,
            4,
            14,
            22,
            9,
            15,
        ]
    )

    inv_reshaped = inventory.reshape(4, 6)

    inv_bin_count = np.zeros(inv_reshaped.shape[1])

    index: int = 0
    for element in np.nditer(inv_reshaped):
        inv_bin_count[index] += element

        index += 1

        if index >= inv_reshaped.shape[1]:
            index = 0

    print(f"Each bin's inventory: {inv_bin_count}")
    del index

    inv_aisle_count = np.zeros(inv_reshaped.shape[0])
    index: int = 0

    for element in np.nditer(inv_reshaped):
        inv_aisle_count[index] += element

        index += 1

        if index >= inv_reshaped.shape[0]:
            index = 0

    print(f"Each aisle's inventory: {inv_aisle_count}")


def prac_2() -> None:
    pass


def prac_3() -> None:
    for index in range(1, 6):
        print(index)
