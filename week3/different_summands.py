# Uses python3
import sys


def optimal_summands(n):
    summands = []

    i = 0
    while True:

        i += 1

        if n-i <= i:
            summands.append(n)
            return summands

        else:
            summands.append(i)
            n -= i

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
