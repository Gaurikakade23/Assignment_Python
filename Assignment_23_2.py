class BankAccount:
    ROI=10.5

    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount

    def Display(self):
        print("Account Holder Name: ",self.Name)
        print("Account Balance: ",self.Amount)
    def Deposit(self):
        amt=float(input("Enter amount to deposit: "))
        self.Amount+=amt
        print("Amount deposited Successfully.")    
    def Withdraw(self):
        amt=float(input("Enter amount to withdraw: "))
        if amt <= self.Amount:
            self.Amount-=amt
            print("Withdrawn succesful.")
        else:
            print("Insuffcient Balance!")    
    def CalculateInterest(self):
        interest=(self.Amount* BankAccount.ROI)/100
        return interest

Obj1= BankAccount("Ram",4000)

Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest: ",Obj1.CalculateInterest())
Obj1.Display()