import utils
import heapq
import pulp


def parse(i):
    machines = []
    for line in i.splitlines():
        data = line.split(" ")
        target = [x == "#" for x in data[0][1:-1]]
        buttons = []
        for x in data[1:-1]:
            buttons.append([int(y) for y in x[1:-1].split(",")])
        joltages = [int(x) for x in data[-1][1:-1].split(",")]
        machines.append((target, buttons, joltages))
    return machines


def silver(i):
    machines = parse(i)

    def bfs(target, buttons):
        state = [False] * len(target)
        q = [(0, state)]
        visited = set([tuple(state)])

        while q:
            dist, state = heapq.heappop(q)

            if state == target:
                return dist

            for b in buttons:
                new_state = state[:]
                for i in b:
                    new_state[i] = not new_state[i]
                tns = tuple(new_state)
                if tns not in visited:
                    visited.add(tns)
                    heapq.heappush(q, (dist + 1, new_state))
        return -1

    res = 0
    for target, buttons, _ in machines:
        res += bfs(target, buttons)
    return res


def gold(i):
    machines = parse(i)

    def solve(buttons, joltage):
        prob = pulp.LpProblem("X", pulp.LpMinimize)
        vars = [pulp.LpVariable(str(i), lowBound=0, cat=pulp.LpInteger) for i in range(len(buttons))]
        prob += sum(vars)

        for i, t in enumerate(joltage):
            vs = []
            for j, b in enumerate(buttons):
                if i in b:
                    vs.append(vars[j])
            prob += sum(vs) == t

        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        return sum([int(x.varValue) for x in vars])

    res = 0
    for _, buttons, joltage in machines:
        res += solve(buttons, joltage)
    return res


if __name__ == "__main__":
    e = utils.le(10)
    print(silver(e))
    i = utils.li(10)
    print(silver(i))
    print(gold(e))
    print(gold(i))
