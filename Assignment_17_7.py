def number_pattern(No):
    for i in range(No):
        for j in range(1, No + 1):
            print(j, end=" ")
        print()

n1= int(input("Enter Number: "))
number_pattern(n1)