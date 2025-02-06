class BankAccount:
    def __init__(self, number, last_name, first_name, balance, overdraft=False):
        self.__number = number
        self.__last_name = last_name
        self.__first_name = first_name
        self.__balance = balance
        self.__overdraft = overdraft
    
    def display(self):
        print(f"Account No.{self.__number} - Holder: {self.__first_name} {self.__last_name} - Balance: {self.__balance}€")
    
    def displayBalance(self):
        print(f"Current balance: {self.__balance}€")
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposit of {amount}€ made. New balance: {self.__balance}€")
    
    def withdrawal(self, amount):
        if self.__balance - amount < 0 and not self.__overdraft:
            print("Insufficient funds to make this withdrawal.")
        else:
            self.__balance -= amount
            print(f"Withdrawal of {amount}€ made. New balance: {self.__balance}€")
    
    def overdraftFees(self):
        if self.__balance < 0:
            self.__balance *= 1.05  
            print(f"Overdraft fees applied. New balance: {self.__balance}€")
    
    def transfer(self, recipient_account, amount):
        if self.__balance - amount < 0 and not self.__overdraft:
            print("Transfer refused: insufficient funds.")
        else:
            self.withdrawal(amount)
            recipient_account.deposit(amount)
            print(f"Transfer of {amount}€ made to {recipient_account.__last_name} {recipient_account.__first_name}")

account1 = BankAccount("123456", "Dupont", "Jean", 1000)
account2 = BankAccount("789012", "Martin", "Sophie", -200, overdraft=True)

account1.display()
account2.display()

account1.deposit(500)
account1.withdrawal(200)
account2.overdraftFees()

account1.transfer(account2, 300)

account1.displayBalance()
account2.displayBalance()
