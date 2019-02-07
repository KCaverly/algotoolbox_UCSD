# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):

    fib = [0,1]

    if n <= 1:
        return n
    else:
        fib[0] = 1
        fib[1] = 1

        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])

        return max(fib)


n = int(input())
print(calc_fib_fast(n))
