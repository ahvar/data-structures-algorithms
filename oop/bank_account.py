import math
from abc import ABC, abstractmethod
from datetime import datetime, time


class BankAccount(ABC):
    pass

    def __init__(self) -> None:
        super().__init__()
        self._balance = 0
        self._deposits = {}
        self._withdrawals = {}

    @abstractmethod
    def deposit(self) -> float:
        pass

    @abstractmethod
    def withdraw(self) -> float:
        pass

    @abstractmethod
    def check_balance(self, amt_needed: int) -> float:
        pass

    @property
    def balance(self):
        return self._balance


class SavingsAccount(BankAccount):

    def __init__(self) -> None:
        super().__init__()
        self._max_withdraw_percent = 0.50

    def deposit(self, amount: float) -> None:
        if not isinstance(amount, float) and not isinstance(amount, int):
            raise ValueError(f"Expected float or int but got {amount.__class__}")
        self._balance = self._balance + amount

    def withdraw(self, amount: float) -> float:
        if amount < self._max_withdraw_percent * self._balance:
            self._balance = self._balance - amount
            self._withdrawals[datetime.today().hour] = amount
        else:
            raise ValueError(
                f"Withdrawal amount is greater than max: {self._max_withdraw_percent * 100} of savings account balance"
            )

    def check_balance(self):
        pass


class CheckingAccount(BankAccount):
    def __init__(self) -> None:
        super().__init__()
