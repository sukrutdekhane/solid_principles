from abc import ABC, abstractmethod

class NonWithdrawableAccount(ABC):
    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

class WithdrawableAccount(NonWithdrawableAccount):
    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass