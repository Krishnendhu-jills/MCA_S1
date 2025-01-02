a=int(input("Enter the first number :  "))
b=int(input("Enter the second number :  "))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
c=int(input("Enter a choice"))
if(c==1):
    print("Addition is",a+b)
elif(c==2):
    print("Subtraction is",a-b)
elif(c==3):
    print("Multiplication is",a*b)
elif(c==4):
    print("Division is",a/b)
else:
    print("ERROR")