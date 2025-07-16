std_dict={'Alice': 80, 'Bob': 90, 'Charlie': 85, 'David': 70, 'Eve': 95}
a=input("Enter student name: ")
a=a.capitalize() 
print(a)
if a in std_dict:
    print("{}'s marks are {}".format(a, std_dict[a]))
else:
    print("Student not found")  
 