def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter a number: "))
result=factorial(n)
print("The factorial of", n, "from recursion is", result)

for i in range(1,n+1):
    result=1
    for j in range(1,i+1):
        result=result*j

print("The factorial of", i, "from loops is", result)

