def reverse(no):
    rev =0
    while no != 0:
        digit = no%10
        rev = rev*10 +digit
        no //=10
    return rev    
def main():
    no1= int(input("Enter Number: "))
    res = reverse(no1) 
    print("Reverse: ",res)
if __name__ == "__main__":
    main()    