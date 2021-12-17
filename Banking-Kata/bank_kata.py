class Account(object):

    def __init__(self,balance):
        self.balance = balance

    def deposit(self,deposit):
        self.balance += deposit
        return "deposit + %d || balance is %d" %(deposit,self.balance)

    def withdraw(self,draw):
        if self.balance - draw <= 0:
            raise ValueError()
        else:
            self.balance -= draw
            return "draw - %d || balance is %d" %(draw,self.balance)


client1 = Account(0)

print(client1.deposit(500))
print(client1.withdraw(100))
print(client1.deposit(300))
print(client1.deposit(100))
print(client1.withdraw(300))