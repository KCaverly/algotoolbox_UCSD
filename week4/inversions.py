# Uses python3
import sys
from operator import itemgetter

def inversions(arr):

    if len(arr) == 1:
        return arr, 0

    else:

        mid = len(arr) // 2
        a = arr[:mid]
        b = arr[mid:]

        a, a_inv = inversions(a)
        b, b_inv = inversions(b)

        merged = []

        i = 0
        j = 0
        inv = 0 + a_inv + b_inv

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
                inv += (len(a)-i)

        merged += a[i:]
        merged += b[j:]

    return merged, inv


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    result, inv = inversions(a)
    print(inv)
