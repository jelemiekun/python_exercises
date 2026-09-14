from Classes import Student
from Enums import Courses


def exercise_1() -> None:
    person_1: Student.Person = Student.Person("John", 22)

    student_1: Student.Student = Student.Student("Vemi", 19, Courses.Course.BSBA_MAJ_FM)
    student_2: Student.Student = Student.Student(
        "Amoha", 17, Courses.Course.BSBA_MAJ_HRM
    )
    student_3: Student.Student = Student.Student("Jole", 60, Courses.Course.BSBA_MAJ_OM)

    person_1.display_information()
    student_1.display_information()
    student_2.display_information()
    student_3.display_information()

    print(student_1.is_adult())


def main() -> None:
    exercise_1()


main()
