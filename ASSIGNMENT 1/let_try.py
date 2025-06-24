a = int(input("enter a input: "))
for i in range(1, a + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbizz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("bizz")
    else:
        print(i)
