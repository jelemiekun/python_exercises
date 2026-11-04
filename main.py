import numpy as np

np.set_printoptions(precision=2)

students = np.array(
    [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Frank",
        "Grace",
        "Henry",
        "Ivy",
        "Jack",
    ]
)

math = np.array([85, 72, 91, 64, 88, 76, 95, 69, 82, 78])
science = np.array([90, 75, 88, 70, 92, 80, 94, 73, 85, 81])
english = np.array([78, 82, 85, 68, 91, 77, 89, 72, 84, 80])

attendance = np.array([95, 80, 98, 65, 92, 85, 99, 70, 88, 82])

print(np.array([students, math, science, english, attendance]))

# 1
math_avrg_score = np.mean(math)

# 2
sci_avrg_score = np.mean(science)

# 3
english_highest = np.max(english)
english_lowest = np.min(english)

# 4
stud_total_score_per_subj = np.sum(np.array([math, science, english]), axis=0)

# 5
stud_avrg_score_per_subj = np.mean(np.array[math, science, english], axis=0)

# 6
math_score_asc_order = np.sort(math)
print(math_score_asc_order)

# 7

# 8
math_median = np.median(math)

# 9
sd_per_subj = np.std(np.array([math, science, english]), axis=1)

# 10
stud_passed_attendance = (attendance[attendance > 90]).size
print(stud_passed_attendance)

# 11
math_greater_90 = math[math > 90]
print(math_greater_90)

# 12
names_math_greater_80 = students[math > 80]

# 13
names_sci_below_75 = students[science < 75]

# 14
names_attendance_below_80 = students[attendance < 80]

# 15
names_above_85_all_subj = students[(math > 85) & (science > 85) & (english > 85)]
print(names_above_85_all_subj)

# 16
names_90_any_subj = students[(math >= 90) | (science >= 90) | (english >= 90)]
print(names_90_any_subj)

# 17
names_math_score_70_to_90 = students[(math >= 70) & (math <= 90)]
print(names_math_score_70_to_90)

# 18
math_replaced = np.where(math < 75, 75, math)
print(math_replaced)

# 19
passed_student_count = (students[(math > 75) & (science > 75) & (english > 75)]).size
print(passed_student_count)

# 20
names_passed_math_failed_science = students[(math > 75) & (science < 75)]
print(names_passed_math_failed_science)

# 21
variance_each_subj = np.var(np.array([math, science, english]), axis=1)
print(variance_each_subj)

# 22
ranges = np.array(
    [
        np.max(np.array([math, science, english]), axis=1)
        - np.min(np.array([math, science, english]), axis=1)
    ]
)
print(ranges)

# 23
subjects_23 = np.array(["math", "science", "english"])
average_scores = np.mean(np.array([math, science, english]), axis=1)
highest_average_score = np.max(average_scores)
subject_highest_avrg_score = subjects_23[(average_scores == highest_average_score)]
print(subject_highest_avrg_score)

# 24
subjects_24 = np.array(["math", "science", "english"])
standard_deviations = np.std(np.array([math, science, english]), axis=1)
highest_std = np.max(standard_deviations)
subject_highest_std = subjects_24[(standard_deviations == highest_std)]
print(subject_highest_std)

# 25
overall_avrg_score = np.mean(np.array([math, science, english]))
print(overall_avrg_score)

# 26
number_student_passed_each_subj = (
    students[(science > 75) & (math > 75) & (english > 75)]
).size
percentage_passed = (number_student_passed_each_subj / students.size) * 100
print(percentage_passed)

# 27
normalized = (math - np.min(math)) / (np.max(math) - np.min(math))
print(normalized)
