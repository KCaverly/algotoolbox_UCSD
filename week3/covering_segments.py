# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points_fast(segments):

    points = []

    segments = sorted(segments, key=attrgetter('end', 'start'))
    max = segments[len(segments)-1].end

    i = 0
    while i < len(segments):

        #print('-'*10)
        #print(segments)
        #print('Iteration (i):     {}'.format(i))

        j = i+1
        #print('Iteration (j):     {}'.format(j))

        if len(segments) == 1:
            return points

        if segments[i].end == max:

            if segments[i].end not in points:
                points.append(segments[i].end)

            return points

        else:



            while j < len(segments):
                #print('i:                        {}'.format(i))
                #print('j:                        {}'.format(j))
                #print(len(segments))


                #print('Segment 1:                {}'.format(segments[i].end))
                #print('Segment 2 (Start):        {}'.format(segments[j].start))
                #print('Segment 2 (End):          {}'.format(segments[j].end))

                if segments[j].start <= segments[i].end <= segments[j].end:
                    #print(j)
                    if segments[i].end not in points:
                        points.append(segments[i].end)

                    del segments[j]
                else:
                    if segments[i].end not in points:
                        points.append(segments[i].end)
                    i += 1

                break

        #print(points)
        #print(segments)


    return points

def optimal_points(segments):
    points = []
    #write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points_fast(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
