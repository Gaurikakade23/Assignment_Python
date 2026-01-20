def Area(r):    #area of circle
    pi=3.14
    area=pi*(r**2)
    return area
def main():
    a=int(input("enter radius: "))
    res = Area(a)
    print("Area of circle is: ",res)

if __name__ == "__main__":
    main()    