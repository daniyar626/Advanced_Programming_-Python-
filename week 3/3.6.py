def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
a = int(input())
b = int(input())
print("GCD is ", gcd(a, b))
print("LCM is ", lcm(a, b))


