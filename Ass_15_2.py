CheckEven = lambda no: no%2==0
def main():
    data =[1,2,3,4,5,6]
    FData = list(filter(CheckEven,data))
    print("Squares: ",FData)

if __name__ == "__main__":
    main()    