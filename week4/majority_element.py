# Uses python3
import sys

def get_majority_element(a):

    if len(a) == 0:
        return -1
    if len(a) == 1:
        return a[0]

    mid = int(len(a) / 2)
    left = get_majority_element(a[0:mid])
    right = get_majority_element(a[mid:])

    if left == right:
        return left
    elif a.count(left) > mid:
        return left
    elif a.count(right) > mid:
        return right

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
