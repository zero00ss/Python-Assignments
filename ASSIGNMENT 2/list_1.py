a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = int(input("Enter the index to remove (0-9): "))
if k < 0 or k >= len(a):
    print("Index out of range")
    exit()
for i in range(k, len(a) - 1):
    a[i] = a[i + 1]
a[-1] = 0  # Set the last element to 0 (or any placeholder)
print(a)
