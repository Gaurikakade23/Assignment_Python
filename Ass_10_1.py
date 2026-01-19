#Print table 
def Table(g):
    result=[]
    for i in range(1,11):
        result.append(g*i)       
    return result    
def main():
    no= int(input("Enter Number: "))
    Res=Table(no)
    print("Table is ",Res)
if __name__ =="__main__":
    main()