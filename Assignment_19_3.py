from functools import reduce

def Fun1(No):
    return (No>70 and No<=90)

def Fun2(No):
    return No+10

def Fun3(A,B):
    return A*B

def main():
    Data=list(map(int, input("Enter number: ").split()))
    print ("Actual data is :",Data)

    FData=list(filter(Fun1, Data))   
    print("Data after filter is: ",FData)

    Mdata= list(map(Fun2, FData))
    print("Data after map is: ",Mdata)

    RData= reduce(Fun3, Mdata)
    print("Data after reduce is: ",RData)

if __name__ == "__main__":
    main()    