
n=[['','']]*10 # This creates a list of 10 references to the same list ['','']
print(n)
n[0][0] = 'a'
print(n)

k=[] 
for i in range(10): # creats an empty list k with 10 references to the same list ['','']
    k.append(['', ''])
print(k)
k[0][0] = 'a'
print(k)
