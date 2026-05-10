import pytest
from BankAccount import BankAccount      # import the BankAccount class
def test_init():
    acc1 = BankAccount("John", 500)
    assert acc1.owner == "John"
    assert acc1.balance == 500

def test_deposit():
    acc1 = BankAccount("John", 150)
    acc1.deposit(150)
    assert acc1.balance == 300
    with pytest.raises(ValueError):
        acc1.deposit(-100)

def test_withdraw():
    acc1 = BankAccount("John", 300)
    acc1.withdraw(150)
    assert acc1.balance == 150
    with pytest.raises(ValueError):
        acc1.withdraw(200)

def test_transfer():
    acc1 = BankAccount("John", 300)
    acc2 = BankAccount("Jane", 300)
    acc1.transfer(100, acc2)
    assert acc1.balance == 200
    assert acc2.balance == 400