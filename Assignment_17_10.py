def sum_of_digits(no):
    total = 0
    while no > 0:
        total += no % 10  # add last digit
        no //= 10          # remove last digit
    return total

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
