from functools import reduce
findMax = lambda a,b: a if a>b else b
def main():
    Data=[4,6,2,7,9,8]
    Rdata= reduce(findMax,Data)
    print("Maximum number is :",Rdata)
if __name__ == "__main__":
    main()    