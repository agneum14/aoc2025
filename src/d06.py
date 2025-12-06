import utils


def parse(i):
    foo = i.splitlines()
    grid = [x.split() for x in foo]
    res = []
    for c in range(len(grid[0])):
        nums = []
        op = ""
        for r in range(len(grid)):
            if r != len(grid) - 1:
                nums.append(int(grid[r][c]))
            else:
                op = grid[r][c]
        res.append((nums, op))
    return res


def silver(i):
    data = parse(i)
    res = 0
    for nums, op in data:
        if op == "+":
            res += sum(nums)
        else:
            prod = 1
            for x in nums:
                prod *= x
            res += prod
    return res


def gold(i):
    grid = []
    foo = i.splitlines()
    for y in foo:
        grid.append([x for x in y])

    res = 0
    x = 0
    while x < len(grid[0]):
        by = len(grid) - 1
        next_x = x + 1
        while next_x < len(grid[0]) and grid[by][next_x] not in ["+", "*"]:
            next_x += 1
        op = grid[by][x]
        nums = []

        r = next_x - 1 if next_x != len(grid[0]) else next_x
        nums = []
        for z in range(x, r):
            s = ""
            for y in range(by):
                s += grid[y][z]
            s = s.strip()
            if s:
                nums.append(int("".join(s)))
        if op == "+":
            res += sum(nums)
        else:
            prod = 1
            for n in nums:
                prod *= n
            res += prod

        x = next_x

    return res


if __name__ == "__main__":
    e = utils.le(6)
    print(silver(e))
    i = utils.li(6)
    print(silver(i))
    print(gold(e))
    print(gold(i))
