def min_of_list(numbers):
    return min(numbers)  # built-in min function
    
n = int(input("Enter how many numbers: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Minimum number is:", min_of_list(numbers))