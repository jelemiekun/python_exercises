import Student


class Professor:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.students: list[Student.Student] = []

    def add_student(self, student: Student.Student) -> None:
        if student in self.students:
            print(f"Student {student.name} is already on the list.")
            return

        self.students.append(student)
        print(f"Student {student.name} is added to the list.")

    def remove_student(self, student: Student.Student) -> None:
        if student not in self.students:
            print(f"Student {student.name} is not on the list.")
            return

        self.students.remove(student)
        print(f"Student {student.name} is removed from the list.")

    def display_all_students(self) -> None:
        for student in self.students:
            print(student)
