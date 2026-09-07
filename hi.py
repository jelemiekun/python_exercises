def miniCalc(number: int, typeOfOperation: int = 0) -> int:
    def innerFunc1AddTen(x: int) -> int:
        return x + 10

    def innerFunc2SubTen(x: int) -> int:
        return x - 10

    match typeOfOperation:
        case 1:
            return innerFunc1AddTen(number)
        case 2:
            return innerFunc2SubTen(number)
        case _:
            print("ERROR: No type of operation defined OR invalid type operation.")
            return number


print(miniCalc(50, 1))
