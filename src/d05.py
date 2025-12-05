import utils


def parse(i):
    foo = i.split("\n\n")

    def _rng(l):
        x = l.split('-')
        return [int(x[0]), int(x[1])]

    rngs = [_rng(x) for x in foo[0].splitlines()]
    ings = [int(x) for x in foo[1].splitlines()]
    rngs.sort(key=lambda x: x[0])
    rngs = merge_overlapping(rngs)
    return (rngs, ings)


def merge_overlapping(rngs):
    res = [[float('-inf'), float('-inf')]]
    for l, r in rngs:
        if l <= res[-1][1]:
            res[-1][1] = max(res[-1][1], r)
        else:
            res.append([l, r])
    return res[1:]


def is_fresh(rngs, ing):
    l = 0
    r = len(rngs) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if rngs[mid][0] <= ing and rngs[mid][1] >= ing:
            return True
        elif rngs[mid][1] < ing:
            l = mid + 1
        else:
            r = mid - 1
    return False


def silver(i):
    rngs, ings = parse(i)
    return len([x for x in ings if is_fresh(rngs, x)])


def gold(i):
    rngs, _ = parse(i)
    res = 0
    for l, r in rngs:
        res += 1 + (r - l)
    return res


if __name__ == "__main__":
    e = utils.le(5)
    print(silver(e))
    i = utils.li(5)
    print(silver(i))
    print(gold(e))
    print(gold(i))
