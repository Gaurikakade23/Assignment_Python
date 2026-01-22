def reverserange(b):
    for i in range(b,0,-1):
        print(i,end="")
def main():
    num= int(input("Enter number: "))
    reverserange(num)
if __name__ == "__main__":
    main()    