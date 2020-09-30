#Created by Shelley Ophir
#Coding Dojo Sep. 30, 2020
#Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# For this assignment, we'll add some functionality to the User class

#create class User
class User:
    #define attritbutes
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    #define methods
    def make_deposits(self, amount):
        self.account_balance += amount
    
    # make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawl(self, amount):
        self.account_balance -= amount

    # display_user_balance(self) - have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        print("User:", self.name, "\nBalance:", self.account_balance)

    # BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposits(amount)

# Create 3 instances of the User class
birder1 = User("Brad", "email1@cardinal.com")
birder2 = User("Stu", "stu@priessler.com")
birder3 = User("Kenny", "722@bostick.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
birder1.make_deposits(722)
birder1.make_deposits(10)
birder1.make_deposits(5)
birder1.make_withdrawl(15)
birder1.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
birder2.make_deposits(100)
birder2.make_deposits(500)
birder2.make_withdrawl(10)
birder2.make_withdrawl(20)
birder2.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
birder3.make_deposits(815)
birder3.make_withdrawl(10)
birder3.make_withdrawl(20)
birder3.make_withdrawl(30)
birder3.display_user_balance()

# BONUS: have the first user transfer money to the third user and then print both users' balances
birder1.transfer_money(birder3, 100)
birder1.display_user_balance()
birder3.display_user_balance()