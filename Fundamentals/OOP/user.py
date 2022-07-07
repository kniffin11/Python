class user: 
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

# this wasnt a method we were told to add, just was asked to make a deposit
    def deposit(self, amount):
        self.balance += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.first_name} {self.last_name}, Balance: {self.balance}")

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount

bob = user('Bob', 'Connahay', 300)
tim = user('Tim', 'Mathew', 400)
max = user('Max', 'fedrizzi', 4000 )

bob.deposit(300).deposit(200).deposit(400).make_withdrawal(100).display_user_balance()

tim.deposit(2100).deposit(300).make_withdrawal(500).make_withdrawal(50).display_user_balance()

max.deposit(500).make_withdrawal(500).make_withdrawal(200).make_withdrawal(130).display_user_balance()

bob.transfer_money(max, 100)
bob.display_user_balance()
max.display_user_balance()





