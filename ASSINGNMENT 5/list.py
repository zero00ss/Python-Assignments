List1=[1,2,3,4,5,6,7,8,9,10]
List2=[]
for i in range(0,5):
    List2.append(List1[i])
print("The Original numbers :", List1)  
print("The Extracted numbers :", List2)
List2.reverse()
print("The reversed numbers :", List2)
   
