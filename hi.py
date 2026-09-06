name = input("What is your name? ")

englishAlphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

nameHasSpecialCharac = False
invalid_char = ""

for char in name:
    char_passed = False
    for charEnglishAlphbet in englishAlphabet:
        if char == charEnglishAlphbet:
            char_passed = True

    nameHasSpecialCharac = not char_passed
    invalid_char = char

    if nameHasSpecialCharac:
        break

    print("Character passed: ", char)

print('INVALID: Your name has special character: "', invalid_char, '" ')
