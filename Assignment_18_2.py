def max_of_list(numbers):
    return max(numbers)  # built-in max function
    
n = int(input("Enter how many numbers: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Maximum number is:", max_of_list(numbers))
