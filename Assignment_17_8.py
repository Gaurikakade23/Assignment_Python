def Pattern(No):
    for i in range(1, No + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # for move to next line
Num= int(input("Enter Number: "))
Pattern(Num)
