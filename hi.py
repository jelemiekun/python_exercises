number = input("Input a number from 1 to 10: ")

validCharacters = "0123456789"
validInput = True
invalidCharacters = []

for char in number:
    if char not in validCharacters:
        validInput = False
        invalidCharacters.append(char)

if validInput:
    number = int(number)

    match number:
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case 4:
            print("Four")
        case 5:
            print("Five")
        case 6:
            print("Six")
        case 7:
            print("Seven")
        case 8:
            print("Eight")
        case 9:
            print("Nine")
        case 10:
            print("Ten")
        case _:
            print("What fucking number did you put in? I said 1-10")
else:
    print(f"You have entered an invalid character(s): {invalidCharacters}")
