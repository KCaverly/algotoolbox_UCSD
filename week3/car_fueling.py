# python3
import sys

def compute_min_refills_2(distance, tank, stops):
    current_position = 0

    i = 0
    while (current_position < end_position):

        i += 1
        current_position += (stops[i] - stop[i-1])
        if stops[i] - stops[i-1] > fullTank:
            return -1
        elif stops[i] - stops[i-1] < tank:
            tank -= stops[i]
        else:
            refills += 1
            tank = fullTank

def compute_min_refills(distance, tank, stops):

    fullTank = tank
    refills = 0
    stops = [0] + stops + [distance]

    for i in range(1, len(stops)):

        if stops[i] - stops[i-1] > fullTank:
            return -1
        elif stops[i] - stops[i-1] <= tank and i != len(stops):
            tank -= stops[i]
        else:
            refills += 1
            tank = fullTank

        i += 1

    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
