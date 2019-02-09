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


def fibonacci_sum_squares(n):

    # Generate Fib And Pisano Period
    m = 10
    fib = [0,1]
    squareFib = [0,1]
    sumFib = [0,1]

    i = 1
    while True:
        i += 1
        fib.append( (fib[i-1] + fib[i-2]))
        squareFib.append( ( fib[i]**2))
        sumFib.append( sum(squareFib) % 10)
        if sumFib[i-1] == 1 and sumFib[i-2] == 0 and i!=2:
            pisano_period = len(sumFib[:-3])
            break

    remainder = n % pisano_period
    return sumFib[remainder]

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(fibonacci_sum_squares(n))

