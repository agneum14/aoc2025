import utils
from functional import seq


def parse_ranges(i: str) -> [int, int]:
    foo = []
    for x in i.split(','):
        y = [int(z) for z in x.split('-')]
        foo.append(y)
    return foo


def invalid_ids(rng: [int, int]) -> [int]:
    l, r = rng
    res = []

    id = l
    while id <= r:
        s = str(id)
        n = len(s)
        h = n // 2
        if n % 2 == 0 and s[0:h] == s[h:n]:
            res.append(id)
        id += 1
    return res


def silver(i) -> int:
    rngs = parse_ranges(i)
    return seq(rngs).flat_map(invalid_ids).sum()


def gold_ids(rng: [int, int]) -> [int]:
    res = []
    left, right = rng

    def check_id(digits: [int], p: int) -> bool:
        if len(digits) % p != 0:
            return False
        i = 0
        j = i + p
        while j <= len(digits) - p:
            if digits[i:j] != digits[j:j + p]:
                return False
            i += p
            j += p
        return True

    id = left
    while id <= right:
        digits = []
        x = id
        while x > 0:
            digits.insert(0, x % 10)
            x //= 10
        if any(check_id(digits, p) for p in range(1, len(digits) // 2 + 1)):
            res.append(id)
        id += 1

    return res


def gold(i) -> int:
    rngs = parse_ranges(i)
    return seq(rngs).flat_map(gold_ids).sum()


if __name__ == "__main__":
    e = utils.le(2)
    print(silver(e))
    i = utils.li(2)
    print(silver(i))
    print(gold(e))
    print(gold(i))
