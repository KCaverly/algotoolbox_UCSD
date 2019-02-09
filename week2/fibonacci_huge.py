# Uses python3
import sys

def get_pisano_period(m):

    fib = [0, 1]

    i = 1
    while True:
        i += 1
        fib.append( (fib[i-1] + fib[i-2]) % m)

        if fib[i-1] == 0 and fib[i-2] == 1 and i != 1:
            return len(fib) - 2

def get_fibonacci_huge(n, m):

    remainder = n % get_pisano_period(m)

    fib = [0, 1]

    for i in range(2, remainder + 1):
        fib.append( (fib[i-1] + fib[i-2]) % m)

    return fib[-1]

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

