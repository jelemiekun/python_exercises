name = input("What is your name? ")

englishAlphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
digits = "0123456789"

nameHasSpecialCharac = False
invalid_char = ""

for char in name:
    char_passed = False
    for charEnglishAlphbet in englishAlphabet:
        if char == charEnglishAlphbet:
            char_passed = True
            break

    nameHasSpecialCharac = not char_passed
    invalid_char = char

    if nameHasSpecialCharac:
        break

    print("Character passed: ", char)

if nameHasSpecialCharac:
    print(f"INVALID: Your name has special character: {invalid_char}")
else:
    print(name[1:3])
    print(name.upper())
    print(name.replace("e", "3"))
    print(name.strip())
    name = name.strip()
    names = name.split()

    print(len(names))

    age = input("What is your age? ")

    ageHasInvalidDigit = False

    for digit in age:
        digit_passed = False
        for validDigit in digits:
            if digit == validDigit:
                digit_passed = True

        if not digit_passed:
            ageHasInvalidDigit = not digit_passed
            print(f"INVALID: Your name has invalid digit: {digit}")

    if not ageHasInvalidDigit:
        print(f"Hello, {name}, you are fucking {age} years old.")
