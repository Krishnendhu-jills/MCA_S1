N=int(input("Enter a number: "))
a=0
b=1
print(b)
for i in range(N):
    c=a+b
    print(c)
    a=b
    b=c
    