from Classes import Student
from Enums import Courses


def exercise_1() -> None:
    student_1: Student.Student = Student.Student("Vemi", 19, Courses.Course.BSBA_MAJ_FM)
    student_2: Student.Student = Student.Student(
        "Amoha", 17, Courses.Course.BSBA_MAJ_HRM
    )
    student_3: Student.Student = Student.Student("Jole", 60, Courses.Course.BSBA_MAJ_OM)

    student_1.display_information()
    student_2.display_information()
    student_3.display_information()


def main() -> None:
    exercise_1()


main()
