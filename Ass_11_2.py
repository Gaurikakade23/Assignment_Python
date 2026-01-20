def countno(num):
    count=0
    while num !=0:
        count +=1
        num//=10
    print("Count of digits: ",count)    
def main():
    a= int(input("enter a number: "))
    countno(a)
if __name__ == "__main__":
    main()    