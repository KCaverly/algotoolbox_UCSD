# Uses python3
import sys
import random


def partition(a, left, right):

    x, j, t = a[left], left, right

    i = j

    while i <= t:

        if a[i] < x:
            a[j], a[i] = a[i], a[j]
            j += 1

        elif a[i] > x:
            a[t], a[i] = a[i], a[t]
            t -= 1
            i -= 1

        i += 1

    return j, t

def randomized_quick_sort(a, left, right):

    if left >= right:
        return

    k = random.randint(left, right)

    a[left], a[k] = a[k], a[left]

    m1, m2 = partition(a, left, right)

    randomized_quick_sort(a, left, m1-1)
    randomized_quick_sort(a, m2+1, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n-1)
    for x in a:
        print(x, end=' ')
