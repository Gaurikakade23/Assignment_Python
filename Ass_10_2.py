# Sum of natural number
def NaturalNum(No):
    result=0
    for i in range(1,No+1):
        result+=i
    return result

def main():
    a= int(input("enter number :"))
    res= NaturalNum(a)
    print("Sum is: ",res)
if __name__ == "__main__":
    main()    