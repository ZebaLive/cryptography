def gcd(x, y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd

def modInverse(a, m) :
    a = a % m
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

print("__GCD__")
num1 = input("Input number one: ")
num2 = input("Input number two: ")
print("GCD:", gcd(int(num1), int(num2)))

input("Press anything to continue...")
print(" ")
print("__ModInverse__")

num3 = input("Input number: ")
modulo = input("Input modulo: ")
print("Modulo inverse:", modInverse(int(num3), int(modulo)))

input("Press anything to continue...")