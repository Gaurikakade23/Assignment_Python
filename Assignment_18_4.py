def Frequency(arr,search):
    count=0
    for num in arr:
        if num == search:
            count += 1
    return count

def main():
    n= int(input("Enter Numbers: "))
    arr=[]

    print("Enter elements: ")
    for i in range(n):
        arr.append(int(input()))
    search =int(input("Enter element to search: "))

    result= Frequency(arr, search)
    print("Output: ",result)    

if __name__ == "__main__":
    main()                