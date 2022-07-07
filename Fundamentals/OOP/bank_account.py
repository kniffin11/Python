class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self 

    def display_account_info(self):
        print(f"Balance: {self.balance}, Interest Rate: {self.int_rate}")

    def yield_interest(self): 
        # rounds to keep balance within 2 deciaml places
        self.balance = round(self.balance * (1 + (self.int_rate * .01)), 2)
        return self

    @classmethod
    def all_instances(cls):
        for i in cls.all_accounts:
            # for some reason it returns none after every itteration 
            print(i.display_account_info())


account1 = BankAccount(9, 3000)
account2 = BankAccount(6, 8000)

account1.deposit(500).deposit(400).deposit(800).withdraw(1000).yield_interest() #.display_account_info()
account2.deposit(800).deposit(300).withdraw(100).withdraw(600).withdraw(200).withdraw(100).yield_interest() #.display_account_info()

BankAccount.all_instances()

