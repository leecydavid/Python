class BankAccount():
# class == blueprint
    bank_name = 'Gringotts'

# create a bank account class with attributes: interest rate & balance
# directly relates to BankAccount class --> David = BankAccount(0.1, 500) 
    def __init__(self, int_rate, balance=0):
        # 0.1 = int_rate / 500 = balance (balance can be set to 0 inside argument so when we create a new User class for BankAccount, the balance is automatically set to 0)
        # self = referring to what has been created
        self.balance = balance
        self.int_rate = int_rate

# Add a deposit method to the BankAccount class 
# Deposit(self, amount) - increases the account balance by the given amount
    def deposit (self, amount):
    # amount = the amount of money the user uses(deposit or withdraw)
        self.amount = amount
        self.balance = self.balance + self.amount
        # ^ because self.balance(balance in bank) & self.amount(amount of money user deposits) = final balance in bank after the deposit
        print('Total Deposit Amount : $', self.amount)
        return self

# Add a withdraw method to the BankAccount class / 
# Withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw (self, amount):
    # amount = the amount of money the user uses(deposit or withdraw)
        self.amount = amount
        if self.balance >= amount:
            self.balance = self.balance - amount
            # if self.balance(bank balance) is >= amount(amount of money withdrawn) then -->
            # self.balance(bank balance) = self.balance(bank balance) - amount(amount of money withdrawn)
            # because if self.balance is less than amount, user cannot withdraw money 
            print('Withdraw Amount: $', amount)
        else:
            self.balance = self.balance - 5
            # if the if statemnet is false then self.balance(bank balance) = self.balance(bank balance) - 5 --> overdraft fee
            print('You have insufficient funds.', 'You have been charged a $5 fee.')
        return self

# Add a yield_interest method to the BankAccount class
# Yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def interest_rate (self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            # (self.balance * self.int_rate) = 
            print ('Account balance after yielded interest rate:', self.balance)
            return self

# Add a display_account_info method to the BankAccount class
# display_account_info(self) - print to the console: eg. "Balance: $100"
    def total_balance (self):
        print('Your total balance: $', self.balance)
        # after running through the methods in our class, self.balance(bank balance) should display the result of deposit,withdraw and int_rate combined
        return self

# Create 2 accounts
David = BankAccount(.1)
Jessica = BankAccount(.2)
    # (.1) = int_rate from parent class
    # (balance) = is already created in the parent class / (balance=0)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
David.deposit(400).deposit(250).deposit(400).withdraw(360).interest_rate().total_balance()
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
Jessica.deposit(650).deposit(1000).withdraw(40).withdraw(160).withdraw(100).interest_rate().total_balance()

Luffy = BankAccount(.5)
Luffy.deposit(50).withdraw(100).total_balance()

