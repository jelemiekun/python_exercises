from typing import override

from Enums import Courses


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

        print("Person instance created!")

    def display_information(self) -> None:
        print("=================================")
        print(f"{self.name}")
        print(f"{self.age}")
        print("=================================")

    def _do_something(self) -> None:
        print("Top secret!")


class Student(Person):
    def __init__(self, name: str, age: int, course: Courses.Course) -> None:
        self.name: str = f"S_{name}"
        self.age: int = age
        self.course: Courses.Course = course

        print("Student instance created!")

    @override
    def display_information(self) -> None:
        print("POLYMORPHISM!!!!")

    def is_adult(self) -> bool:
        Person._do_something(self)
        return self.age >= 18
