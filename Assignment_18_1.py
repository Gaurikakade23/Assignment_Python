def sum_of_list(numbers):
    return sum(numbers) 
n = int(input("Enter how many numbers: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Sum of all elements:", sum_of_list(numbers))
