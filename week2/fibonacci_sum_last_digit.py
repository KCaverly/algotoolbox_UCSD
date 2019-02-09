# Uses python3
import sys

def fibonacci_sum_last_digit(n):

    # Get Pisano Period Where M = 10
    m = 10
    fib = [0,1]
    sumFib = [0,1]
    i = 1
    while True:
        i += 1
        fib.append(fib[i-1] + fib[i-2])
        sumFib.append(sum(fib) % 10)
        if sumFib[i-1] == 1 and sumFib[i-2] == 0 and i != 2:
            pisano_period = len(sumFib[:-3])
            break

    remainder = n % pisano_period
    return sumFib[remainder]

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

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_last_digit(n))
