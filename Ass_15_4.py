
from functools import reduce
total= lambda a,b: a+b

def main():
    Data=[1,2,3,4,5,6]
    Rdata= reduce(total,Data)
    print("Total is: ",Rdata)
if __name__ == "__main__":
    main()    