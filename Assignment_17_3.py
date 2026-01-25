def Factorial(No):
    fact = 1
    for i in range(1, No + 1):
        fact = fact * i
    return fact

Num = int(input("Enter Number: "))
print(Factorial(Num))
