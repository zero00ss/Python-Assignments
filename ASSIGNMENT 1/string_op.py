str= " Hello world "
r=str.capitalize() #same as upper() but only for the first alphabet 
s=str.center(20)
print(r)
print(s)
r=str.casefold() #same as lower() but only for the first alphabet
print(r)
print(str.find("o")) #Index(first one incase of multiple) at which the element is present in the string, -1 if element not present
print(str.isidentifier()) #wether the string can act as a variable name(identifier)
k= str.encode("ascii")
print(k)
f= str.endswith("ld") #Check if the string ends with mentioned element(s)
print(f)
l=str.join("***") #inserts the string between each element(of a single) or string given 
print(l)
o= str.count('o') #counts the number of times the element is present in the string given
print(o)
w= str.strip() #removes the starting and trailing white spaces
print(w)