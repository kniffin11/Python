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

class user: 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # this initializes the connection between the two classes and sets the "account" object to the link
        self.account = BankAccount(int_rate = 2, balance = 0)

    def another_acc(self, first_name, last_name, new_acc_name):
        self.first_name = first_name
        self.last_name = last_name
        self.new_acc_name = new_acc_name
        self.new_acc_name = BankAccount(int_rate = 2, balance = 0)

    def withdrawal(self, amount):
        # self(user). account(BankAccount object link). withdraw(BankAccount method)
        self.account.withdraw(amount)
        return self

    def deposit(self, amount):
        # self(user class).account(BankAccount object).deposit(BankAccount class)
        self.account.deposit(amount)
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)

    def display_account_info(self):
        self.account.display_account_info()

bob = user('Bob', 'Connahay')
tim = user('Tim', 'Mathew')
max = user('Max', 'fedrizzi')

bob.deposit(300).deposit(200).deposit(400).withdrawal(100).display_account_info()
tim.deposit(2100).deposit(300).withdrawal(500).withdrawal(50).display_account_info()
