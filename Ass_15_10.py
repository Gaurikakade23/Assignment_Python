CountEven = lambda x:x%2==0
def main():
    Data=[1,6,4,5,6,7,9,3,2]
    Fdata=len(list(filter(CountEven,Data))) 
    print("Count of Even Number: ",Fdata)
if __name__ == "__main__":
    main()    