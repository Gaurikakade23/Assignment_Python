def Factor(num):
    
    for i in range(1,num+1):
        if num%i ==0:
            print(i,end= " ")
def main():
    No= int(input("Enter Number: "))
    Factor(No)
if __name__ == "__main__":
    main()    