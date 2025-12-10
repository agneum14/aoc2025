import utils
import matplotlib.pyplot as plt
import heapq
from functional import seq


def parse(i):
    points = []
    for x in i.splitlines():
        y = [int(z) for z in x.split(",")]
        points.append(y)
    return points


def area(u, v):
    return (abs(u[0] - v[0]) + 1) * (abs(u[1] - v[1]) + 1)


def silver(i):
    points = parse(i)
    ma = 0
    for i in range(len(points) - 1):
        for j in range(i, len(points)):
            ma = max(ma, area(points[i], points[j]))
    return ma


def visual(i):
    points = parse(i)
    points.append(points[0])
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]])

    plt.plot([6165, 100000], [68497, 68497])

    plt.axis('equal')
    plt.show()


def gold(i):
    points = parse(i)

    # find two big horizontal lines
    q = []
    for i in range(len(points) - 1):
        u = points[i]
        v = points[i + 1]
        d = abs(u[0] - v[0]) + 1
        heapq.heappush(q, (d, u, v))
        if len(q) > 2:
            heapq.heappop(q)
    ps = seq(q).flat_map(lambda x: [x[1], x[2]]).sorted().list()[2:]
    ps.sort(key=lambda x: -x[1])

    # find largest valid rect with top
    top = ps[0]
    pairs = seq(range(len(points) - 1)).map(lambda x: [points[x], points[x + 1]]).list()
    foo = seq(points).filter(lambda p: p[1] > top[1] and p[0] < top[0]).sorted(key=lambda x: -(abs(top[0] - x[0]) + abs(top[1] - x[1]))).list()
    verts = seq(pairs).filter(lambda p: p[0][0] == p[1][0] and min(p[0][1], p[1][1]) > top[1]).list()
    horz = seq(pairs).filter(lambda p: p[0][1] == p[1][1] and p[0][1] > top[1]).list()
    for p in foo:
        vs = seq(verts).filter(lambda u: min(u[0][1], u[1][1]) <= p[1] and max(u[0][1], u[1][1]) >= p[1] and u[0][0] > p[0] and u[0][0] < top[0]).list()
        if vs:
            continue
        h1 = seq(horz).filter(lambda u: min(u[0][0], u[1][0]) <= p[0] and max(u[0][0], u[1][0]) > p[0] and u[0][1] < p[1]).list()
        if h1:
            continue
        tr = [top[0], p[1]]
        h2 = seq(horz).filter(lambda u: min(u[0][0], u[1][0]) < tr[0] and max(u[0][0], u[1][0]) >= tr[0] and u[0][1] < tr[1]).list()
        if h2:
            continue
        return area(p, top)

    return -1


if __name__ == "__main__":
    e = utils.le(9)
    print(silver(e))
    i = utils.li(9)
    print(silver(i))
    # visual(i)
    print(gold(i))
