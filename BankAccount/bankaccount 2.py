class BankAccount():
    bank_name = 'Gringotts'

    def __init__(self, int_rate, balance=0):

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
    
David = BankAccount(.1)
Jessica = BankAccount(.2)
David.deposit(400).deposit(250).deposit(400).withdraw(360).interest_rate().total_balance()
Jessica.deposit(650).deposit(1000).withdraw(40).withdraw(160).withdraw(100).interest_rate().total_balance()

Luffy = BankAccount(.5)
Luffy.deposit(50).withdraw(100).total_balance()

