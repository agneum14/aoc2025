import utils

def parse_dist(i: str):

    def foo(x: str):
        dist = int(x[1:])
        if x[0] == "L":
            dist *= -1
        return dist

    return [foo(x) for x in i.splitlines()]

def silver(i: str):
    cur = 50
    res = 0
    for dist in parse_dist(i):
        cur += dist
        if cur < 0:
            cur += 100
        cur %= 100
        if cur == 0:
            res += 1
    return res

def gold(i: str):
    cur = 50
    prev = cur
    res = 0
    for dist in parse_dist(i):
        cur += dist
        if cur < 0:
            res += cur // -100
            cur %= -100
            if prev > 0:
                res += 1
        elif cur > 0:
            res += cur // 100
            cur %= 100
            if prev < 0:
                res += 1
        else:
            res += 1
        prev = cur
    return res


if __name__ == "__main__":
    e = utils.le(1)
    print(silver(e))
    i = utils.li(1)
    print(silver(i))
    print(gold(e))
    print(gold(i))
