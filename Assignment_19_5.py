from functools import reduce

def Fun1(No):
    if No <= 1:
        return False

    for i in range(2, int(No**0.5) + 1):
        if No % i == 0:
            return False

    return True


def Fun2(No):
    return No*2

def Fun3(A,B):
    return A if A>B else B

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