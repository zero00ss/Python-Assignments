a=int(input("enter a input:"))
b=int (input("enter b input:"))
c=0
for i in range(a ,b+1):
    if i % 2 != 0:
      c=c+i
print("Sum of odd numbers from 1 to", a, "is:", c)  