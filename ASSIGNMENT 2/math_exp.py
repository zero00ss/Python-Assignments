import math

class MathExp:
    def exp1(self, x, y):
        # (x^2 + y^2) / (x - y)
        return (x**2 + y**2) / (x - y)
    
    def exp2(self, a, b, c):
        # Quadratic formula: (-b + sqrt(b^2 - 4ac)) / (2a)
        return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    
    def exp3(self, x):
        # sin(x) + cos(x) + tan(x)
        return math.sin(x) + math.cos(x) + math.tan(x)
    
    def exp4(self, x):
        # ln(x^2 + 1)
        return math.log(x**2 + 1)
    
    def exp5(self, x, y):
        # e^(x*y) + log10(x + y)
        return math.exp(x*y) + math.log10(x + y)
    
    def exp6(self, x):
        # |x| + sqrt(|x - 5|)
        return abs(x) + math.sqrt(abs(x - 5))
    
    def exp7(self, x, y):
        # (x^3 - y^3) / (x*y)
        return (x**3 - y**3) / (x*y)
    
    def exp8(self, x):
        # sinh(x) + cosh(x) //hyperbolic sine and cosine
        return math.sinh(x) + math.cosh(x)
    
    def exp9(self, x, y):
        # arctan(x/y) + arccos(x/(y+1)) // angle in radians
        return math.atan(x/y) + math.acos(x/(y+1))
    
    def exp10(self, x, n):
        # x^n / n!
        return x**n / math.factorial(n)

# Example usage:
if __name__ == "__main__":
    m = MathExp()
    print("exp1:", m.exp1(5, 2))
    print("exp2:", m.exp2(1, -3, 2))
    print("exp3:", m.exp3(math.pi/4))
    print("exp4:", m.exp4(3))
    print("exp5:", m.exp5(2, 3))
    print("exp6:", m.exp6(-7))
    print("exp7:", m.exp7(4, 2))
    print("exp8:", m.exp8(1))
    print("exp9:", m.exp9(1, 2))
    print("exp10:", m.exp10(2, 4))