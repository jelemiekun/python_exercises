import numpy as np

list_a = np.ones(shape=(3, 3), dtype=int)

print(list_a)

list_a[0, :] = 0
print(list_a)
