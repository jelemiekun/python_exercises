import sys

tupleKo = ("C++", "Javascript", "Java", "Python", "Assembly")

print(tupleKo[0])
print(tupleKo[-1])
print(tupleKo[:3])
print(tupleKo[:-3])


tuple2 = (10, 25, 30, 45, 50)

userInput1 = input("Input a number: ")

validDigits = "0123456789"

for char in userInput1:
    if char not in validDigits:
        print(f"ERROR: You have entered an invalid character: {char}")
        print("Exiting program.")
        sys.exit()

userInput1 = int(userInput1)


if userInput1 in tuple2:
    print(f"{userInput1} exists in the tuple")
else:
    print(f"{userInput1} does not exist in the tuple.")

del userInput1
del validDigits

tuple3 = ("one", "two", "three")

(fi, se, th) = tuple3

print(f"fi: {type(fi)}, {fi}")

del tuple3, fi, se, th

tuple3 = 1, 3, 5, 7

(fi, *si) = tuple3

print(si)

tupleMeow = (12, 5, 8, 21, 30, 7, 16)

for num in tupleMeow:
    if num % 2 == 0:
        print(num)

print("===================================================")

for index in range(len(tupleMeow)):
    print(index)

print("===================================================")

combined_tuple = tupleKo + tupleMeow
print(len(combined_tuple))

print("===================================================")

print(combined_tuple)
