# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_fast(n):

    fib = [1, 1]

    if n <= 2:
        return 1
    else:
        for i in range(2, n):

            if len(fib) == 2:
                fib.append(fib[0] + fib[1])
            else:
                fib.append((fib[1] + fib[2]) % 10)
                fib = fib[-3:]

    return fib[2]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_fast(n))
