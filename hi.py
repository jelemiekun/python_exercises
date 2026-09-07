def func() -> None:
    global meow
    meow = 10

    def funccc() -> None:
        meow = 30

    funccc()

    print(meow)


def printKo() -> None:
    print(meow)


func()
printKo()
