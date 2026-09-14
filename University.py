import Professor


class University:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.professors: list[Professor.Professor] = []

        print(f"{self.name} University has been formally established.")

    def add_professor(self, professor: Professor.Professor) -> None:
        if professor in self.professors:
            print(f"Professor {professor.name} is already on the list.")
            return

        self.professors.append(professor)
        print(f"Professor {professor.name} added to the University.")

    def remove_professor(self, professor: Professor.Professor) -> None:
        if professor not in self.professors:
            print(f"Professor {professor.name} is not on the list.")
            return

        self.professors.remove(professor)
        print(f"Professor {professor.name} is terminated from the University.")

    def display_professors(self) -> None:
        for professor in self.professors:
            print(professor)

    def display_professors_students(self, professor: Professor.Professor) -> None:
        professor.display_all_students()

    def display_all_university_students(self) -> None:
        for professor in self.professors:
            print(f"Professor {professor.name} students:")
            for student in professor.students:
                print(student)

            print("\n")
