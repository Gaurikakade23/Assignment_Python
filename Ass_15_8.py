Checkdiv = lambda x:x%3==0 and x%5 ==0
def main():
    Data=[1,5,6,10,15,30]
    Fdata= list(filter(Checkdiv,Data))
    print("CheckDiv",Fdata)
if __name__ == "__main__":
    main()    