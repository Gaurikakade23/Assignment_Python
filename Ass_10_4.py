def FindEven(No):
    result =[]
    for i in range(2,No+1,2):
        result.append(i)
    return result
def main():
    a = int(input("Enter Number: "))
    res= FindEven(a)
    print("Even Numbers: ",res)
if __name__ =="__main__" :
    main()    