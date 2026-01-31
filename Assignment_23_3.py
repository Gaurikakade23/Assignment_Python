class Numbers:
    def __init__(self):
        self.Value=int(input("Enter a Number: "))

    def chkprime(self):
        if self.Value <= 1:
            return False
        for i in range(2,int(self.Value ** 0.5)+1):
            if self.Value%1 == 0:
                return False
        return True
    def Factors(self):
        print("Factors: ",end=" ")
        for i in range(1,self.Value+1):
            if self.Value%i == 0:
                print(i,end=" ")
        print()

    def SumFactors(self):
        s=0
        for i in range(1,self.Value+1):
            if self.Value%i ==0:
                s += i
        return s

    def ChkPerfect(self):
        return self.SumFactors()-self.Value == self.Value

Obj1 =Numbers()
Obj1.chkprime()
Obj1.Factors()
Obj1.SumFactors()
Obj1.ChkPerfect()        

