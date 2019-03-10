#Uses python3
import sys
import math

def getDistance(points):
    x1 = points[0][0]
    x2 = points[1][0]

    y1 = points[0][1]
    y2 = points[1][1]

    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

def minimum_distance(points):

    # Split list of points into two points
    mid = len(points)//2

    left = points[:mid]
    right = points[mid:]

    # Recursively split tree
    if len(left) > 2:
        left_min = minimum_distance(left)
    else:
        left_min = left

    if len(right) > 2:
        right_min = minimum_distance(right)
    else:
        right_min = right

    # Calculate differences among sub trees
    if len(left_min) > 1:
        left_dist = getDistance(left_min)
    else:
        left_dist = float('inf')

    if len(right_min) > 1:
        right_dist = getDistance(right_min)
    else:
        right_dist = float('inf')

    # Return minimum distance calculation
    d = min(left_dist, right_dist)

    # Generate Split Mid
    split = []
    for i in left:
        if mid-i[0] <= d:
            for j in right:
                if abs(i[0] - j[0]) <= d and abs(i[1]-j[1]) <= d:
                    if getDistance((i, j)) <= d:
                        split.append([i, j])

    if len(split) != 0:
        l = []

        # Calculate distances and pick lowest
        for i in split:
            l.append({getDistance(i): i})
        l.sort(key=lambda x: x.keys())

        return list(l[0].values())[0]
    elif left_dist > right_dist:
        return right_min
    else:
        return left_min


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    # Convert to sorted list of points
    points = []
    for i in range(0,len(x)):
        points.append([x[i], y[i]])

    points = sorted(points)

    print(minimum_distance(points))
    print(getDistance(minimum_distance(points)))
    #print("{0:.9f}".format(minimum_distance(points)))
