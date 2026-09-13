from Enums import Courses


class Student:
    def __init__(self, name: str, age: int, course: Courses.Course) -> None:
        self.name: str = name
        self.age: int = age
        self.course: Courses.Course = course

    def display_information(self) -> None:
        print("=================================")
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.course}")
        print("=================================")

    def is_adult(self) -> bool:
        return self.age >= 18
