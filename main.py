import numpy as np

a = np.array([1, 2, 3], "u8")
print(a)


b = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print(b)

c = np.array(
    [
        [[2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18]],
        [[4, 8, 12, 16, 20, 24], [5, 10, 15, 20, 25, 30]],
    ],
    "u1",
)

print(a.ndim, b.ndim)
print(a.shape)

print(c.shape)
print(c.dtype)

c[1, 1, 0:-1:2] = [255, 254, 253]

print(c)
