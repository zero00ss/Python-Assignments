
# Sort a list of numbers and strings without using built-in functions
user_input = input("Enter list elements separated by space: ")
lst = user_input.split()
lst_num = []
lst_str = []

for i in lst:
    if i.isdigit():
        lst_num.append(int(i)) 
    else:
        lst_str.append(i)

for i in range(len(lst_num)-1):
    for j in range(len(lst_num)-1):
        if lst_num[j] > lst_num[j +1 ]:
            lst_num[j], lst_num[j + 1] = lst_num[j+ 1], lst_num[j]

   
for i in range(len(lst_str)-1):
    for j in range(len(lst_str)-1):
        if lst_str[j].lower() > lst_str[j + 1].lower():
            lst_str[j], lst_str[j + 1] = lst_str[j + 1], lst_str[j]
 
lst= lst_num + lst_str
print("Sorted list:", lst)