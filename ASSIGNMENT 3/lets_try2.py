n = int(input("How many numbers? "))
a = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
e = []
k = []
for i in a:
    if i // 15 == 1:
        print("fizzbuzz")
    elif i % 2 == 0:
        e.append(i ** 2)
    elif i % 2 != 0:
        k.append(i * 2)

print(e)
print(k)