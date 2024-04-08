import pytest

class BankAccount:
    owner: str
    __balance: float

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        # добавляет сумму к балансу, если сумма положительная, иначе выбрасывает ValueError
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение прошло успешно на {amount} рублей. Текущий баланс {self.__balance} рублей")
        else:
            raise ValueError("Сумма пополнения отрицательная или равна 0")

    def withdraw(self, amount):
        # снимает сумму с баланса, если на счету достаточно средств, иначе выбрасывает ValueError
        if amount > self.__balance:
            raise ValueError("На счету недостаточно средств")
        else:
            self.__balance -= amount
            print(f"Снятие средств прошло успешно. Текущий баланс {self.__balance} рублей")

    def get_balance(self):
        # возвращает текущий баланс
        return self.__balance


class SavingsAccount(BankAccount):
    interest_rate: float

    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.deposit(self.get_balance() * self.interest_rate)


class CheckingAccount(BankAccount):

    def withdraw(self, amount):
        self.__balance -= amount
        print("Снятие средств прошло успешно")


