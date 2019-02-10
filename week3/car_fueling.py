# python3
import sys


def compute_min_refills(distance, tank, stops):

    fullTank = tank
    refills = 0
    stops = [0] + stops + [distance]

    for i in range(1, len(stops)-1):

        tank -= (stops[i] - stops[i-1])

        if stops[i+1] - stops[i] > fullTank:
            return -1
        elif stops[i+1] - stops[i] > tank:
            refills += 1
            tank = fullTank
        else:
            next

        #print('-'*10)
        #print('Stop                  {}'.format(i))
        #print('Distance:             {}'.format(stops[i]))
        #print('Refills:              {}'.format(refills))
        #print('Tank:                 {}'.format(tank))
        #print('Distance to Travel:   {}'.format(stops[i+1] - stops[i]))

    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
