MinNum= lambda No1,No2 : No1<No2
def main():
    
    n1=int(input("Enter first number: "))
    n2=int(input("Enter first number: "))
    if MinNum(n1,n2):
        print("Minimum number is: ",n1)
    else:
        print("Minimum number is: ",n2)   

if __name__ == "__main__":
    main()    