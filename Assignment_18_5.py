import Marvellous_Prime_18

def ListPrime(arr):
    sum=0
    for n in arr:
        if Marvellous_Prime_18.ChkPrime(n):
            sum+=n
    return sum

def main():
    num= int(input("Enter Number of elements: "))
    arr=[]

    print("Enter Elements: ")
    for i in range(num):
        arr.append(int(input()))

        result = ListPrime(arr)
        print("Output: ",result) 

if __name__ == "__main__":
    main()            