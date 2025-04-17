if __name__ == "__main__":
    main()
class BankAccount:
 def __init__(self, account_number, balance=0):
            self.account_number = account_number
            self.balance = balance
 def deposit(self, amount):
     if amount > 0:
                    self.balance += amount
                    print("depositing amount")
     else:
                    print("Deposit amounnt")
def withdrawal(self, amount):
    if amount <= self.balance:
                    self.balance -= amount
                    print("Withdrawing amount")
    else:
                    print("Inadequate amount in account")
 def balance(self):
                print("Current balance: (self_balance)")
def main():
            amount = BankAccount("123456789")
    
