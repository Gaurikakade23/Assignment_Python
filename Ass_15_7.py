Words = lambda s: len(s)>5
def main():
    Data=["Hello","Sun","Happy","Sad","Prgramming"]
    FData= list(filter(Words,Data))
    print("List: ",FData)
if __name__ == "__main__":
    main()    