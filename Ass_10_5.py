def FindOdd(No):
    result =[]
    for i in range (1,No+1):
        if i%2 !=0:
            result.append(i)
    return result
def main():
    a = int(input("Enter Number: "))
    res= FindOdd(a)
    print("Odd Numbers: ",res)
if __name__ =="__main__" :
    main()    