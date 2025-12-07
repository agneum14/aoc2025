import utils


def parse(i):
    splits = []
    beams = set()
    start = (0, 0)
    for y, line in enumerate(i.splitlines()):
        splits.append([])
        for x, c in enumerate(line):
            if c == "S":
                start = (y, x)
                beams.add(x)
            elif c == "^":
                splits[-1].append(x)
    return splits[2:], beams, start


def silver(i):
    splits, beams, start = parse(i)
    res = 0
    for r in splits:
        bs = beams.copy()
        for s in r:
            if s in bs:
                beams.remove(s)
                beams.add(s - 1)
                beams.add(s + 1)
                res += 1
    return res


def gold(i):
    splits, beams, start = parse(i)
    max_y = len(splits)
    cache = {}

    def recur(y, x):
        if y == max_y:
            return 1
        ke = (y, x)
        if ke in cache:
            return cache[ke]
        if x in splits[y]:
            res = recur(y + 1, x - 1) + recur(y + 1, x + 1)
        else:
            res = recur(y + 1, x)
        cache[ke] = res
        return res

    return recur(0, beams.pop())


if __name__ == "__main__":
    e = utils.le(7)
    print(silver(e))
    i = utils.li(7)
    print(silver(i))
    print(gold(e))
    print(gold(i))
