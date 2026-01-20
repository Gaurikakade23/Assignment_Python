def SumofDigit(num):
    sum =0
    while num!=0:
        digit = num%10
        sum += digit
        num//=10
    return sum    
def main():
    no= int(input("Enter Number: "))
    res = SumofDigit(no) 
    print("Sum of digit: ",res)
if __name__ == "__main__":
    main()    