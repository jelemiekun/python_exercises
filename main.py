import numpy as np

employees = np.array(
    [
        [101, 25000, 85, 90],
        [102, 32000, 78, 88],
        [103, 28000, 92, 95],
        [104, 45000, 88, 82],
        [105, 38000, 76, 80],
        [106, 22000, 95, 91],
        [107, 50000, 89, 93],
        [108, 30000, 84, 86],
        [109, 42000, 91, 89],
        [110, 27000, 73, 78],
    ]
)

# Column information:
# [Employee_ID, Salary, Attendance, Performance]

employees
employees.shape
employees.ndim
employees.size
employees.dtype
employees[2, 1]
employees[6, -1]
employees[4, :]
employees[:, 0]
employees[:, [1, -1]]

employees[:5]
employees[-3:]
employees[:, :3]
employees[:5, 1]
employees[2:7]
employees[::2]
employees[:, -1]
employees[[1, -1], :]
employees[:5, 1::2]

employees[:, 1] += 2000
employees = employees.astype(np.float64)
employees[:, 1] *= 0.1
np.sum(employees[:, 1])
np.mean(employees[:, 1])
np.max(employees[:, 1])
np.min(employees[:, 1])
# idk what to do on 7
np.mean(employees[:, 2])
np.max([employees[:, 1]]) - np.min([employees[:, 1]])

# [Employee_ID, Salary, Attendance, Performance]

employees[employees[:, 1] > 30000]
employees[employees[:, 1] < 30000]
employees[employees[:, 2] > 85]
employees[employees[:, -1] >= 90]
employees[(employees[:, 1] > 25000) & (employees[:, 1] < 40000)]
employees[(employees[:, -2] < 80) | (employees[:, -1] < 85)]
employees[(employees[:, 1] > 30000) & (employees[:, -1]) > 90]
employees[employees[:, -1] >= 85][:, 0].size
employees[employees[:, 1] < 30000][:, 0].size
employees[:, -1] = np.where(employees[:, -1] < 80, 80, employees)

np.mean(employees[:, 1])
np.median(employees[:, 1])
np.std(employees[:, 1])
np.var(employees[:, 1])
np.max(employees[:, -1])
np.min(employees[:, -2])
np.argmax(employees[:, -2])
np.argmin(employees[:, -1])
np.mean(employees[employees[:, -2] > 85][:, 1])
np.mean(employees[employees[:, 1] > 30000][:, -1])

np.sort(employees[:, 1])
np.sort(employees[:, 1])[::-1]
np.sort(employees[:, -1])
np.argsort(employees[:, -1])

employees[[np.argsort(employees[:, 1])], :]
employees[[np.argsort(employees[:, -1])[::-1]], :]
employees[::-1]
employees[np.argsort(employees[:, 1])[:-4:-1], :]
employees[np.argsort(employees[:, -1])[:-4:-1], :]
employees[np.argsort(employees[:, -2])[::-1], :]

copy_1 = employees[:, [0, 1]].copy()
copy_2 = employees[:, [2, 3]].copy()

new_employee = np.array([[111, 35000, 87, 92]])

# idk na
copy_1 = np.vstack(new_employee[:, [0, 1]])
print(copy_1)
