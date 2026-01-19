def Factorial(No):
    result=1
    for i in range(1,No+1):
        result*=i
    return result    
def main():
    a= int(input("Enter Number: "))
    res= Factorial(a)
    print("Factorial is: ",res)
if __name__ == "__main__":
    main()    