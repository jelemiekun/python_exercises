import numpy as np

arr = np.zeros((2, 5))

ones = np.ones((3, 3), "u1")

full = np.full((999, 999), 255, "u1")

random_a = np.random.randint(100, size=(3, 3))

identity = np.identity(50)

challenge = np.ones((5, 5))

challenge[1:-1, 1:-1] = 0
challenge[2, 2] = 9


print(arr)
print(ones)
print(full)
print(random_a)
print(identity)

print(challenge)
