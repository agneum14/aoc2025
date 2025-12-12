import utils
from functools import cache


def parse(i):
    adj = {}
    for line in i.splitlines():
        foo = line.split()
        adj[foo[0][:-1]] = foo[1:]
    return adj


def silver(i):
    adj = parse(i)

    @cache
    def dfs(u):
        if u == "out":
            return 1
        return sum(dfs(v) for v in adj[u])

    return dfs("you")


def gold(i):
    adj = parse(i)

    @cache
    def dfs(u, dac, fft):
        if u == "out":
            if dac and fft:
                return 1
            return 0
        elif u == "dac":
            dac = True
        elif u == "fft":
            fft = True
        return sum(dfs(v, dac, fft) for v in adj[u])

    return dfs("svr", False, False)


if __name__ == "__main__":
    e = utils.le(11)
    print(silver(e))
    i = utils.li(11)
    print(silver(i))
    e = utils.lei(11, 2)
    print(gold(e))
    print(gold(i))
