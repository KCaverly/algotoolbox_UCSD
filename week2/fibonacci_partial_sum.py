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

def fibonacci_partial_sum(from_, to):

    pisano = get_pisano_period(10)
    from_pisano = from_ % pisano
    to_pisano = to % pisano

    sum = 0
    current = 0
    next = 1

    for i in range(to_pisano+1):
        if i >= from_pisano:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))