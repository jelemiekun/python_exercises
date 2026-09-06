listKo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for digit in listKo:
    divisibles = []
    if digit % 1 == 0:
        divisibles.append(1)
    if digit % 2 == 0:
        divisibles.append(2)
    if digit % 3 == 0:
        divisibles.append(3)
    if digit % 4 == 0:
        divisibles.append(4)
    if digit % 5 == 0:
        divisibles.append(5)
    if digit % 6 == 0:
        divisibles.append(6)
    if digit % 7 == 0:
        divisibles.append(7)
    if digit % 8 == 0:
        divisibles.append(8)
    if digit % 9 == 0:
        divisibles.append(9)
    if digit % 10 == 0:
        divisibles.append(10)

    print(f"Digit {digit} is divisible be {divisibles}")
