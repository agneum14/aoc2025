import utils
import math
import heapq
import collections


def parse(i):
    boxes = []
    for line in i.splitlines():
        x = line.split(',')
        box = [int(y) for y in x]
        boxes.append(box)
    return boxes


def find(forest, u):
    if forest[u] == u:
        return u
    forest[u] = find(forest, forest[u])
    return forest[u]


def union(forest, u, v):
    pu = find(forest, u)
    pv = find(forest, v)
    if pu != pv:
        forest[pu] = pv
        return True
    return False


def dist(b1, b2):
    return math.sqrt((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 + (b1[2] - b2[2]) ** 2)


def silver(i, k):
    boxes = parse(i)
    q = []
    forest = [x for x in range(len(boxes))]

    for i in range(len(boxes) - 1):
        b1 = boxes[i]
        for j in range(i + 1, len(boxes)):
            b2 = boxes[j]
            d = dist(b1, b2)
            heapq.heappush(q, (d, i, j))

    while q and k:
        _, u, v = heapq.heappop(q)
        union(forest, u, v)
        k -= 1

    counter = collections.Counter([find(forest, x) for x in range(len(boxes))])
    top = sorted(counter.values(), reverse=True)[:3]
    prod = 1
    for x in top:
        prod *= x
    return prod


def gold(i):
    boxes = parse(i)
    q = []
    forest = [x for x in range(len(boxes))]

    for i in range(len(boxes) - 1):
        b1 = boxes[i]
        for j in range(i + 1, len(boxes)):
            b2 = boxes[j]
            d = dist(b1, b2)
            heapq.heappush(q, (d, i, j))

    cons = 0
    while True:
        _, u, v = heapq.heappop(q)
        if union(forest, u, v):
            cons += 1

        if cons == len(boxes) - 1:
            return boxes[u][0] * boxes[v][0]
    return -1


if __name__ == "__main__":
    e = utils.le(8)
    print(silver(e, 10))
    i = utils.li(8)
    print(silver(i, 1000))
    print(gold(e))
    print(gold(i))
