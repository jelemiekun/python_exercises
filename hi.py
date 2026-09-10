def printSet(set: set[int]) -> None:
    print(set)


setOne: set[int] = {1, 2, 3, 4, 5}
setTwo: set[int] = {1, 3, 5, 7, 9}

setOne.add(10)

setUnion: set[int] = setOne ^ setTwo
printSet(setUnion)
