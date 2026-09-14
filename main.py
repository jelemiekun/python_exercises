import random


class BankAccount:
    @staticmethod
    def __generate_account_number() -> int:
        return random.randint(100000000, 999999999)

    def __init__(self, owner: str, initial_balance: float = 0) -> None:
        self.account_number: int = self.__generate_account_number()
        self.owner: str = owner
        self.balance: float = initial_balance

    def deposit(self, amount: float) -> None:
        if not self.__is_amount_greater_than_zero(amount):
            return

        self.balance += amount

    def withdraw(self, amount: float) -> float:
        if not self.__is_amount_greater_than_zero(amount):
            return 0

        if amount > self.balance:
            print(
                "ERROR: You are trying to withdraw an amount greater than your balance."
            )
            return 0

        print(f"Withdrawing {amount}")

        self.balance -= amount

        return amount

    def get_balance(self) -> float:
        return self.balance

    def display_account(self) -> None:
        print(f"""
            Account Number: {self.account_number}
            Owner: {self.owner}
            Balance: {self.balance}
        """)

    def __is_amount_greater_than_zero(self, amount: float) -> bool:
        if amount <= 0:
            print("ERROR: Amount can not be less than zero.")
            return False

        return True


account_1: BankAccount = BankAccount("John", 100)

account_1.display_account()

account_1.deposit(34829)

account_1.display_account()

account_1.withdraw(9999999)

account_1.withdraw(34929)

account_1.display_account()
