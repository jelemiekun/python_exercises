python_students = (
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
)

database_students = (
    "Bob",
    "David",
    "Frank",
    "Grace",
    "Alice",
)


def tupleToSet(data) -> set[str]:
    return set(data)


def findStudentTakingBothCourses(firstSet: set[str], secondSet: set[str]) -> set[str]:
    return firstSet.intersection(secondSet)


def findStudentTakingOnlyPython(firstSet: set[str], secondSet: set[str]) -> set[str]:
    return firstSet.difference(secondSet)


def findStudentTakingAtLeastOneCourse(
    firstSet: set[str], secondSet: set[str]
) -> set[str]:
    return firstSet.union(secondSet)


def checkIfStudentIsEnrolled(*students: tuple[str, ...]) -> None:
    def inputName() -> str:
        return input("Enter student name: ")

    def convertTupleArgsToSet() -> set[str]:
        unified_set: set[str] = set()
        for record in students:
            unified_set.update(record)

        return unified_set

    def isStudentNameInOverAllRecord(name: str, record: set[str]) -> bool:
        return name in record

    name: str = inputName()
    overall_student: set[str] = convertTupleArgsToSet()
    is_in_record: bool = isStudentNameInOverAllRecord(name, overall_student)

    print(f"{name} is enrolled.") if is_in_record else print(f"{name} is not enrolled.")


print(
    findStudentTakingBothCourses(
        tupleToSet(python_students), tupleToSet(database_students)
    )
)

print(
    findStudentTakingOnlyPython(
        tupleToSet(python_students), tupleToSet(database_students)
    )
)

print(
    findStudentTakingAtLeastOneCourse(
        tupleToSet(python_students), tupleToSet(database_students)
    )
)

checkIfStudentIsEnrolled(python_students, database_students)
