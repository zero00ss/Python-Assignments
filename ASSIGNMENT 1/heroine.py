a,b,c=input('enter the three sides of triangle: ').split()
a=float(a)
b=float(b)      
c=float(c)  
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5 
print("Area of triangle is: ", area)
print(s)

