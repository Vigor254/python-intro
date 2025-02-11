from abc import ABC, abstractmethod
# encapsulation
from abc import ABCMeta, abstractclassmethod


class Account:
    def __init__(self,account_id,holder_name,balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited{amount}.New balance: {self.balance}")
    def withdraw(self,amount):
            print(f"attempting to withdraw{amount}from account with balance{self.balance}")
            if amount<=self.balance:

                self.balance -= amount
            else:
                print("insufficient balance")
    def get_balance(self):
        return self.balance
    def get_holder_name(self):
        return self.holder_name
# inheritance
class Customer(Account):
    def __init__(self,account_id,holder_name,balance,phone_number):
        super().__init__(account_id,holder_name,balance,)
        self.phone_number = phone_number
# polymorphism
class Transaction:
    def __init__(self,amount):
        self.amount = amount
    def execute(self,amount):
        pass
class DepositTransaction(Transaction):
    def execute(self,account):
        account.deposit(self.amount)
class WithdrawTransaction(Transaction):
    def execute(self,account):
     account.withdraw(self.amount)

# Abstraction
class PaymentSystem(ABC):
    @abstractclassmethod
    def process_payment(self,amount):
        pass
class MpesaPaymentSystem(PaymentSystem):
    def process_payment(self,amount):
        print(f"Processing Mpesa Payment of {amount}")
# example usage
mpesa = MpesaPaymentSystem()
account1=Customer(account_id=1,holder_name="John",balance=2000,phone_number=745433334)
deposit1=DepositTransaction(amount=450)
withdraw1=WithdrawTransaction(amount=1780)

deposit1.execute(account1)
withdraw1.execute(account1)
print(f"The balance of {account1.get_holder_name()} is : "
      f"{account1.get_balance()}")
account2=Customer(account_id=2,holder_name="Joy",balance=3000,phone_number=74565564)
deposit2=DepositTransaction(amount=550)
withdraw2=WithdrawTransaction(amount=1780)

deposit2.execute(account2)
withdraw2.execute(account2)

print(f"The balance of {account2.get_holder_name()} is :"
      f"{account2.get_balance()}")
