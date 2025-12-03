from functional import seq
import utils


def parse_bats(i: str) -> [[int]]:
    return seq(i.splitlines()).map(lambda x: [int(y) for y in x]).list()


def joltage(bat: [int]) -> int:
    mi = 0
    mv = 0
    for i, x in enumerate(bat[:-1]):
        if x > mv:
            mv = x
            mi = i
    return mv * 10 + max(bat[mi + 1:])


def silver(i: str) -> int:
    bats = parse_bats(i)
    return sum([joltage(x) for x in bats])


def gold_joltage(bat: [int]) -> int:
    res = []
    prev_i = -1
    width = 12
    while width > 0:
        i = prev_i + 1
        mv = 0
        mi = 0
        while i <= len(bat) - width:
            if bat[i] > mv:
                mv = bat[i]
                mi = i
            i += 1
        res.append(mv)
        width -= 1
        prev_i = mi
    return int("".join(map(str, res)))


def gold(i: str) -> int:
    bats = parse_bats(i)
    return sum([gold_joltage(x) for x in bats])


if __name__ == "__main__":
    e = utils.le(3)
    print(silver(e))
    i = utils.li(3)
    print(silver(i))
    print(gold(e))
    print(gold(i))
