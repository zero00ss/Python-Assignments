a= int(input("enter a number: "))
if a==1:
    print("not prime")
    exit()  

i=2
while i*i < a:
    if a % i == 0:
        break
    i += 1
if i*i == a:
    print("prime")
else:
    print("not prime")
