import utils
from ortools.sat.python import cp_model
import collections


def parse(i):
    data = i.split("\n\n")
    shapes = []
    regions = []

    for shape_data in data[:-1]:
        points = []
        for y, line in enumerate(shape_data.splitlines()[1:]):
            for x, c in enumerate(line):
                if c == "#":
                    points.append((y, x))
        shapes.append(points)

    for region_data in data[-1].splitlines():
        xs = region_data.split()
        foo = xs[0][:-1]
        y_len, x_len = [int(x) for x in foo.split("x")]
        shape_counts = [int(x) for x in xs[1:]]
        regions.append((y_len, x_len, shape_counts))

    return (shapes, regions)


def rotate(ps):
    return [(y, -x) for (x, y) in ps]


def flip(ps):
    return [(y, -x) for (y, x) in ps]


def normalize(ps):
    y_min = min(y for (y, _) in ps)
    x_min = min(x for (_, x) in ps)
    return [(y - y_min, x - x_min) for (y, x) in ps]


def calc_variants(ps):
    variants = set()
    cur = ps

    for _ in range(4):
        cur = tuple(sorted(normalize(rotate(cur))))
        flipped = tuple(sorted(normalize(flip(cur))))
        variants.add(cur)
        variants.add(flipped)

    return [list(x) for x in variants]


def calc_placements(y_len, x_len, variants):
    placements = []
    for v in variants:
        y_max = max(y for (y, _) in v)
        x_max = max(x for (_, x) in v)
        for yd in range(y_len - y_max):
            for xd in range(x_len - x_max):
                placements.append([(y + yd, x + xd) for (y, x) in v])
    return placements


def silver(i):
    shapes, regions = parse(i)
    variants = [calc_variants(x) for x in shapes]

    def solvable(region):
        y_len, x_len, shape_counts = region
        placements = [calc_placements(y_len, x_len, v) for v in variants]
        model = cp_model.CpModel()

        # create boolean variables for each placement
        placement_vars = []
        for i, ps in enumerate(placements):
            shape_placement_vars = []
            for j, p in enumerate(ps):
                v = model.NewBoolVar(f"{i}-{j}")
                shape_placement_vars.append(v)
            placement_vars.append(shape_placement_vars)

        # shape count constraint
        for pvs, count in zip(placement_vars, shape_counts):
            model.Add(sum(pvs) == count)

        # no overlap constraint
        point_vars = collections.defaultdict(list)
        for i, shape_placements in enumerate(placements):
            for j, p in enumerate(shape_placements):
                for y, x in p:
                    point_vars[(y, x)].append(placement_vars[i][j])
        for x in point_vars.values():
            model.Add(sum(x) <= 1)

        solver = cp_model.CpSolver()
        status = solver.solve(model)
        return status in [cp_model.FEASIBLE, cp_model.OPTIMAL]

    res = 0
    for i, r in enumerate(regions):
        x = solvable(r)
        print(i, x)
        res += x
    return res


def silver_dumbly(i):
    shapes, regions = parse(i)
    shape_areas = [len(x) for x in shapes]

    def solvable(region):
        y_len, x_len, shape_counts = region
        area = y_len * x_len
        shape_area = sum([sa * c for (sa, c) in zip(shape_areas, shape_counts)])
        return shape_area <= area

    return sum([solvable(x) for x in regions])


if __name__ == "__main__":
    e = utils.le(12)
    print(silver(e))
    i = utils.li(12)
    # print(silver(e))
    print(silver_dumbly(i))
