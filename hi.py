x = "variable"


def myfunc():
    global x
    global y
    y = 15
    print(x)
    x = "changed"


def secFunc():
    global y
    y = 20
    print(y)


myfunc()

print(x)

print(y)

secFunc()

print(y)
