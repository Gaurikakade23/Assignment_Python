def CheckChar(Ch):
    
    if Ch in('a','e','i','o','u'):
        return Ch
    else:
        return None    
def main():
    a= input("Enter a character: ").lower()
    res= CheckChar(a)

    if res != None:
        print("Vowel")
    else:
        print("Constant")
if __name__ == "__main__":
    main()    