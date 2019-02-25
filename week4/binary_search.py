# Uses python3
import sys

def binary_search(a, x, left, right):

    mid = int(left + ((right-left) / 2))

    if left == right and x != a[right]:
        return -1
    elif a[left] > x or a[right] < x:
        return -1
    elif x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search(a, x, 0, mid-1)
    elif x > a[mid]:
        return binary_search(a, x, mid+1, len(a) - 1)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, len(a)-1), end = ' ')
