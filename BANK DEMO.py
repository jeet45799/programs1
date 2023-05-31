class Bank:

    def openaccount(self,cname,acno,balance):
        self.c=cname
        self.a=acno
        self.b=balance
        print("hello",self.c,"your account number",self.a,"is opened with",self.b,"rs.")
    def deposit(self,amount):
        self.b=self.b+amount
    def withdraw(self,amount):
        if amount<=self.b:
            self.b=self.b-amount
        else:
            print("you need another",amount-self.b,"rs.")
    def checkbalance(self):
        print("current balance :",self.b)

b1=Bank()
print("*"*75)
cname=input("enter customer name :")
print("*"*75)
acno=int(input("enter account number :"))
print("*"*75)
balance=int(input("enter initial balance :"))
print("*"*75)
b1.openaccount(cname, acno, balance)
print("*"*75)

while True:
    print("1. deposit")
    print("2. withdraw")
    print("3. checkbalance")
    print("4. exit")
    print("*"*75)

    choice=int(input("enter your choice :"))
    if choice==1:
        amount=int(input("enter deposit amount:"))
        b1.deposit(amount)
        print("*"*75)
    elif choice==2:
        amount=int(input("enter withdraw amount :"))
        b1.withdraw(amount)
        print("*"*75)
    elif choice==3:
        b1.checkbalance()
        print("*"*75)
    else:
        print("thank you for using our services have a good day")
        print("*"*75)
        break


