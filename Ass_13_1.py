def Area(l,w):
    area=l*w
    return area
def main():
    a=int(input("enter length: "))
    b=int(input("enter width: "))
    res = Area(a,b)
    print("Area of rectangle is: ",res)

if __name__ == "__main__":
    main()    