string=input("Enter a word: ")
n=input("Enter a character: ")
i=0
for c in string:
    if(c==n):
        i=i+1
print("Character frequency:",i)