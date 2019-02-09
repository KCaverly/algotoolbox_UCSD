# Uses python3
import sys

def get_pisano_period(m):

    fib = [0,1]

    i = 1
    while True:
        i += 1
        fib.append( (fib[i-1] + fib[i-2]) % m)

        if fib[i-1] == 0 and fib[i-2] == 1 and i != 1:
            return len(fib) - 2

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_last_digit(n):

    pisano = get_pisano_period(10)

    if n <= 2:
        return n

    n = n % pisano

    fib = [0,1]

    for i in range(2, n+3):
        fib.append( (fib[i-1] + fib[i-2]) % 10)

    return fib[n + 2] - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
