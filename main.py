class Car:
    what_type: str = "Car"

    def __init__(self, brand: str, num_of_wheels: int, production_year: int) -> None:
        self.brand: str = brand
        self.num_of_wheels: int = num_of_wheels
        self.PRODUCTION_YEAR: int = production_year

        print("Car instance created.")

    def print_properties(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Number of wheels: {self.num_of_wheels}")
        print(f"Production year: {self.PRODUCTION_YEAR}")


bmw: Car = Car("BMW", 4, 2024)

bmw.print_properties()

ahamay: Car = Car("Yamaha", 16, 2019)

ahamay.print_properties()
