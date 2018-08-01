class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print(f'Added {dep_amt} to your account')

    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('withdrawal accepted')
        else:
            print('your balance is not enough')

    def __str__(self):
        return f'Owner: {self.owner} \nBalance: {self.balance}'


a = Account('amir', 5000)

print(a.owner)

a.deposit(343)
print(a)
