
def pattern(No):
    for i in range(No):
        for j in range(No):
            print("*", end=" ")    
        print()

Num =int(input("Enter Number: "))
pattern(Num)
