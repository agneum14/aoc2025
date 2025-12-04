import utils


def parse(i: str):
    forklifts = set()
    for y, line in enumerate(i.splitlines()):
        for x, c in enumerate(line):
            if c == "@":
                forklifts.add((y, x))
    return forklifts


def valid_forklift(forklifts, p):
    y, x = p
    adj = utils.eight_adj(y, x)
    return len([z for z in adj if z in forklifts]) < 4


def silver(i: str) -> int:
    forklifts = parse(i)
    return len([x for x in forklifts if valid_forklift(forklifts, x)])


def gold(i: str) -> int:
    forklifts = parse(i)
    change = True
    res = 0
    while change:
        change = False
        slated = set([x for x in forklifts if valid_forklift(forklifts, x)])
        if slated:
            forklifts = forklifts - slated
            res += len(slated)
            change = True
    return res


if __name__ == "__main__":
    e = utils.le(4)
    print(silver(e))
    i = utils.li(4)
    print(silver(i))
    print(gold(e))
    print(gold(i))
