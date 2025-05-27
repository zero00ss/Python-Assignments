std_dict={'Alice': 80, 'Bob': 90, 'Charlie': 85, 'David': 70, 'Eve': 95}
a=input("Enter student name(case sensitive): ") 
if a in std_dict:
    print("{}'s marks are {}".format(a, std_dict[a]))
else:
    print("Student not found")  
