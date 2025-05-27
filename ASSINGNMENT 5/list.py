List1=[]
n=int(input("enter the number of entries: "))
for i in range(n):
    List1.append(input('enter the number:'))    
print("The Orignal list:", List1)

List2=[]
for i in range(0,5):
    List2.append(List1[i])
print("The Extracted numbers :", List2)
List2.reverse()
print("The reversed numbers :", List2)
   
