import math
import cmath
a=int(input("Enter the value of a =  "))
b=int(input("Enter the value of b =  "))
c=int(input("Enter the value of c =  "))
d=b*b-4*a*c
if(d<0):
    r1=(-b-cmath.sqrt(d))/2*a
    r2=(-b+cmath.sqrt(d))/2*a
    print("The roots are",r1,r2)
elif(d>0):
    r1=(-b-math.sqrt(d))/2*a
    r2=(-b+math.sqrt(d))/2*a
    print("The roots are",r1,r2)
else:
    r=-b/2*a
    print("The Roots of the Quadratic equation =",r)






