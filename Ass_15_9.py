from functools import reduce
Product= lambda a,b: a*b
def main():
    Data=[2,3,8,5,4]
    Rdata = reduce(Product,Data)
    print("Product is: ",Rdata)

if __name__ == "__main__":
    main()    