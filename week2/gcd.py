# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):

    a1 = max(a, b)
    b1 = min(a, b)

    if b1 == 0:
        return a1
    aPrime = a1 % b1
    return gcd(b1, aPrime)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
