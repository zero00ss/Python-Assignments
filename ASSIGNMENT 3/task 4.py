import math
number = int(input("Enter a number: "))

def square_root(number):

    if number < 0:
        print("Cannot compute square root of a negative number.")
    else:
        return math.sqrt(number)

def logarithm(number, base=math.e):
    if number <= 0:
        print("Cannot compute logarithm of a non-positive number.")
    else:   
        return math.log(number, base)

def sine(number):
    return math.sin(number)

result_sqrt = square_root(number)
result_log = logarithm(number)  
result_sin = sine(number)
print("Square root of", number, "is", result_sqrt)  
print("Logarithm of", number, "is", result_log)
print("Sine of", number, "is", result_sin)  