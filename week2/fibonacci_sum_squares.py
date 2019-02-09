# Uses python3
import sys

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def get_pisano_period(m):

    fib = [0,1]

    i = 1
    while True:
        i += 1
        fib.append( ((fib[i-1] + fib[i-2]) ** 2) % m)

        if i == 50:
            print(fib)
            exit()

        if fib[i-1] == 1 and fib[i-2] == 0 and i != 2:
            return len(fib[:-3])

def fibonacci_sum_squares(n):

    pisano = get_pisano_period(10)
    remainder = n % pisano

    fib = [0,1]

    i = 1
    while True:
        i += 1
        fib.append( ((fib[i-1] + fib[i-2]) ** 2) % m)



    print(pisano, remainder)

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(fibonacci_sum_squares(n))

