fruits = ("apple", "banana", "apple", "orange", "apple", "grape")

print(f'Number of "Apples" appeared: {fruits.count("apple")}')
print(f'Index of "orange": {fruits.index("orange")}')

del fruits
print("\n")

#
#
#
#
#


students = (("Alice", 98), ("Bob", 92), ("Charlie", 78), ("David", 95))

for name, grade in students:
    print(f"{name}: {grade}")

print("\n")

highest_grade: int = 0
highest_grade_index = 0

index = 0
for info in students:
    if info[1] > highest_grade:
        highest_grade = info[1]
        highest_grade_index = index
    index += 1

del highest_grade
del index

print(f"Highest Grade: {students[highest_grade_index][0]}")
print(f"Grade: {students[highest_grade_index][1]}")

del students, highest_grade_index

#
#
#
#
#


def calculate(inputs: tuple[int, int]) -> tuple[int, int, int]:
    return (
        int(inputs[0] + inputs[1]),
        int(inputs[0] - inputs[1]),
        int(inputs[0] * inputs[1]),
    )


def printResult(inputs: tuple[int, int], results: tuple[int, int, int]) -> None:
    (sum, difference, product) = results
    (FN, SN) = inputs
    print(f"{FN} + {SN}: {sum}")
    print(f"{FN} - {SN}: {difference}")
    print(f"{FN} * {SN}: {product}")


inputs = (1, 3)
results = calculate(inputs)

printResult(inputs, results)

del inputs, results
print("\n")

#
#
#
#
#

print("================ NEW ===============\n")

students = (("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95), ("Eve", 88))


def printRecord(record: tuple[str, int]) -> None:
    (name, grade) = record
    print(f"{name}: {grade}")


def printEverything(records) -> None:
    for record in records:
        printRecord(record)


def calculateAverageGrade(records) -> float:
    index = 0
    total_grade: int = 0

    while index < len(records):
        total_grade += records[index][1]
        index += 1

    return float(total_grade / index)


def findHighestGradeIndex(records) -> int:
    highest_grade: int = 0
    highest_grade_index: int = 0

    index = 0
    while index < len(records):
        if records[index][1] > highest_grade:
            highest_grade = records[index][1]
            highest_grade_index = index
        index += 1

    return highest_grade_index


def findLowestGradeIndex(records) -> int:
    lowest_grade = records[0][1]
    lowest_grade_index = 0

    index = 0
    for record in records:
        if records[index][1] < lowest_grade:
            lowest_grade = records[index][1]
            lowest_grade_index = index
        index += 1

    return lowest_grade_index


def countNumberOfStudentsPassed(records, passingGrade) -> int:
    count = 0

    for record in records:
        if record[1] >= passingGrade:
            count += 1

    return count


def findStudentRecord(records) -> None:
    def inputStudentName() -> str:
        return input("Student's Name: ")

    studentName = inputStudentName()

    isStudentRecordExist = False

    index = 0
    for record in records:
        if studentName in record:
            isStudentRecordExist = True
            break

        index += 1

    if isStudentRecordExist:
        printRecord(records[index])
    else:
        print(f"Record not found with student name: {studentName}")
