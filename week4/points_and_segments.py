# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    # Generate zip iterators for starts
    starts = zip(starts, ['left'] * len(starts), range(len(starts)))

    # Generate zip iterators for ends
    ends = zip(ends, ['right'] * len(ends), range(len(ends)))

    # Generate zip iterators for points
    points = zip(points, ['point'] * len(points), range(len(points)))

    # Combine zip iterators
    sort_list = sorted(chain(starts, ends, points))

    i = 0
    for val, loc, idx in sort_list:

        if loc == 'left':
            i += 1
        elif loc == 'right':
            i -= 1
        elif loc == 'point':
            cnt[idx] = i

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
