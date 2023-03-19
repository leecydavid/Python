# Parent Class
# we do not need to change anything in the Parent Class
class BankAccount():
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate

    def deposit (self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print('Total Deposit Amount : $', self.amount)
        return self

    def withdraw (self, amount):
        self.amount = amount
        if self.balance >= amount:
            self.balance = self.balance - amount
            print('Withdraw Amount: $', amount)
        else:
            self.balance = self.balance - 5
            print('You have insufficient funds.', 'You have been charged a $5 fee.')
        return self

    def interest_rate (self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            print ('Account balance after yielded interest rate:', self.balance)
            return self
    def total_balance (self):
        print('Your total balance: $', self.balance)
        return self
    
# Child Class

# Create a User class with an __init__ method
class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0, balance=0)
        # User's bank account is passed into the child class
        # BankAccount has the same arguments as the parent BankAccount = int_rate & balance
        
        print('User:', self.name, ",", self.email)

# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
        self.account.deposit(amount)
        # connecting from Parent Class Attribute deposit
        # self.account located in the Child User Class is set/linked to the Parent BankAccount Class
        return self

# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        # connecting from Parent Class Attribute withdraw 
        # self.account located in the Child User Class is set/linked to the Parent BankAccount Class
        return self

# Add a display_user_balance method to the User class that displays user's account balance
    def user_balance(self):
        print('Total balance:', self.account.balance)
        # after running through the methods in our class, self.balance(bank balance) should display the result of deposit,withdraw and int_rate combined


David = User('David', 'david@gmail.com')
David.make_deposit(100).make_withdrawal(50).user_balance()
Jessica = User('Jessica', 'jessica@gmail.com')
Jessica.make_deposit(50).make_withdrawal(100).user_balance()






