Square = lambda x: x**2
def main():
    data =[1,2,3,4,5]
    MData = list(map(Square,data))
    print("Squares: ",MData)
if __name__ == "__main__":
    main()    