def replace(s):
    if(len(s)<2):
        return s
    else:
        return s[-1]+s[1:-1]+s[0]
    s=input("Enter the string: ")
    res=replace(s)
    print(res)
    