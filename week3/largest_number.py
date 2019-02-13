#Uses python3

import sys

def largest_number(a):

    result = ''

    number = sorted([int(q) for q in a], reverse=True)
    number = [str(q) for q in number]

    #print(number)

    i = 0
    while len(number) != 0:

        #print('-'*10)
        #print('Number:    {}'.format(number))
        #print('i:         {}'.format(i))

        if len(number) == i:
            i = 0

        digit = number[i]

        if digit[0] >= max([x[0] for x in number]):

            A = result + digit
            B = digit + result

            if A > B:
                result = A
            else:
                result = B

            del number[i]

            #print('-'*10)
            #print('A:    {}'.format(A))
            #print('B:    {}'.format(B))
            #print(result)

        elif i+1 == len(number):
            i = 0
        else:
            i += 1

    return int(result)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
