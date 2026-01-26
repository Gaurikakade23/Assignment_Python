import math
import threading

def calculate_even_factors_sum(number):

    even_factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
           
            if i % 2 == 0:
                even_factors.append(i)
            if (number // i) % 2 == 0 and i != (number // i):
                even_factors.append(number // i)
  
    even_factors.sort() 
    total_sum = sum(even_factors)
    print(f"\nThread EvenFactor (Number: {number}):")
    print(f"  Even Factors: {even_factors}")
    print(f"  Sum of Even Factors: {total_sum}")

def calculate_odd_factors_sum(number):
    """Identifies odd factors and calculates their sum."""
    odd_factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            
            if i % 2 != 0:
                odd_factors.append(i)
            if (number // i) % 2 != 0 and i != (number // i):
                odd_factors.append(number // i)

    odd_factors.sort()
    total_sum = sum(odd_factors)
    print(f"\nThread OddFactor (Number: {number}):")
    print(f"  Odd Factors: {odd_factors}")
    print(f"  Sum of Odd Factors: {total_sum}")

target_number = 60 

even_factor_thread = threading.Thread(
    target=calculate_even_factors_sum, 
    args=(target_number,), 
    name="EvenFactor"
)

odd_factor_thread = threading.Thread(
    target=calculate_odd_factors_sum, 
    args=(target_number,), 
    name="OddFactor"
)

print(f"Main thread started. Analyzing number: {target_number}")

even_factor_thread.start()
odd_factor_thread.start()

even_factor_thread.join()
odd_factor_thread.join()

print("\nExit from main")



