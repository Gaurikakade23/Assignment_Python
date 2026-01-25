def sum_factors(no):
    total = 0
    for i in range(1, no):
        if no % i == 0:
            total += i
    return total

num = int(input("Enter number: "))
print(sum_factors(num))
