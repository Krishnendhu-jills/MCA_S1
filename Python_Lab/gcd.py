a=int(input("Enter the value of the first number =  "))
b=int(input("Enter the value of the second number=  "))
gcd=0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
        print("The G.C.D of a and b is ",gcd)