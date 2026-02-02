from interfaces.interface import NonWithdrawableAccount, WithdrawableAccount
from typing import List

class Client:
    def __init__(self, non_withdrawable_accounts: List[NonWithdrawableAccount], withdrawable_accounts: List[WithdrawableAccount]) -> None:
        self.non_withdrawable_accounts = non_withdrawable_accounts
        self.withdrawable_accounts = withdrawable_accounts
    
    def print_accounts(self) -> None:
        for account in self.non_withdrawable_accounts:
            account.deposit(20)
        
        for account in self.withdrawable_accounts:
            account.deposit(30)
            account.withdraw(10)

class FDAccount(NonWithdrawableAccount):
    def __init__(self, balance: float) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        print("Deposit to FD account.")

class SavingsAccount(WithdrawableAccount):
    def __init__(self, balance: float) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        print("Deposit to savings account.")

    def withdraw(self, amount: float) -> None:
        print("Withdrawl from savings account.")

class CurrentAccount(WithdrawableAccount):
    def __init__(self, balance: float) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        print("Deposit to current account.")

    def withdraw(self, amount: float) -> None:
        print("Withdrawl from current account.")

if __name__ == "__main__":
    fd_account = FDAccount(1000)
    savings_account = SavingsAccount(2000)
    current_account = CurrentAccount(3000)

    client = Client(
        non_withdrawable_accounts=[fd_account],
        withdrawable_accounts=[savings_account, current_account]
    )
    client.print_accounts()