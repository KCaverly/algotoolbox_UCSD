# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=attrgetter('end','start'))

    i = 0
    while i < len(segments):

        if segments[i].end not in points:
            points.append(segments[i].end)

        j = i + 1
        while j < len(segments):

            if segments[j].start <= segments[i].end <= segments[j].end:
                del segments[j]
                next

            else:
                break

        i += 1

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
