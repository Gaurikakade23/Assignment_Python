import os
def main():
    FileName=input("Enter name of file: ")

    Ret = os.path.exists(FileName)

    if(Ret==True):
        print(FileName +" exists in current directory")
    else:
        print("File doesn't exists in current directory")   

if __name__=="__main__":
    main()