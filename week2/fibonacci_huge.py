# Uses python3
import sys

def get_fibonacci_huge(n, m):

    # Get Pisano Period and Fibonacci to Search
    fib = [0, 1]

    i = 1
    while True:
        i += 1
        fib.append( (fib[i-1] + fib[i-2]) % m)
        if fib[i-2] == 0 and fib[i-1] == 1 and i != 2:
            pisano_period = len(fib[:-3])
            break

    # Return only value needed
    remainder = n % pisano_period

    return fib[remainder]

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))

