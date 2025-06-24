a = int(input("enter a input: "))
digits = []
temp = a

# Extract digits
while temp != 0:
    digits.append(temp % 10)
    temp //= 10

digits = digits[::-1]  # Now digits[0] is the leftmost digit

# Collect even digits and reverse them
even_digits = [d for d in digits if d % 2 == 0][::-1]
even_idx = 0

# Build result with reversed even digits
result = []
for d in digits:
    if d % 2 == 0:
        result.append(str(even_digits[even_idx]))
        even_idx += 1
    else:
        result.append(str(d))

print("".join(result))


