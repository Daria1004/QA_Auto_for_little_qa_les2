from bank.homework_2 import BankAccount, SavingsAccount
import pytest

def test_SavingsAccount():
    my_account = SavingsAccount("Daria")
    my_account.deposit(500)
    my_account.withdraw(100)
    my_account.apply_interest()
    assert my_account.get_balance() > 0

