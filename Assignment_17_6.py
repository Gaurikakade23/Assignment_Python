
def pattern(No):
    for i in range(No,0,-1):
        for j in range(i):
            print("*", end=" ")    
        print()

Num =int(input("Enter Number: "))
pattern(Num)
