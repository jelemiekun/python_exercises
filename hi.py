details = [str(""), int(), float(), int()]

details[0] = input("What is your name? ")

validCharactersForName = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ "
nameHasSpecialDigit = False

for char in details[0]:
    if char not in validCharactersForName:
        print(f"Invalid Character: {char}")

details[1] = input("What is your age? ")

validDigits = "0123456789"

for digit in details[1]:
    if digit not in validDigits:
        print(f"Invalid Character: {details[1]}")

details[2] = input("What is your height (meters)? ")

details[3] = input("What is your favorite number (whole number only)? ")

for digit in details[3]:
    if digit not in validDigits:
        print(f"Invalid Character: {details[3]}")

print(
    f"Your name is {details[0]}, {details[1]} years old. You are {details[2]} tall. Your favorite number is {details[3]}"
)
