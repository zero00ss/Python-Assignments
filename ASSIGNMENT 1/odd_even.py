
a=int(input("Enter a number: "))
if a>9 and a<100 and a % 2 == 0:
        print("The number is even double digit.")
   
elif a > 99 and a < 1000 and a % 2 == 1:
            print("The number is odd three digit.")

elif a in [1, 2, 3, 5, 7]:
    print("The number is a single digit prime number")
else:
    print("category not found")


b=input("Enter a number 2: ")

if len(b)==2 and int(b) % 2 == 0:
            print("The number is even double digit.")

elif len(b) == 3 and int(b) % 2 == 1:
            print("The number is odd three digit.")
elif len(b) == 1 and int(b) in [1, 2, 3, 5, 7]:
    print("The number is a single digit prime number")  
else:
    print("category not found")



