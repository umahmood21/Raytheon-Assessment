from math import sqrt

def isPrime(n):
    if i > 1:
        for x in range(2, int(sqrt(n) + 1)):
            if i % x == 0: return False
        return True
    else:
        return False

for i in range(1, 101):
    if isPrime(i):
        print(i)