def _n(x: int) -> str:
    if x < 10:
        return f"0{x}"
    else:
        return str(x)


def le(x: int) -> str:
    with open(f"inputs/{_n(x)}e.txt", "r") as f:
        return f.read()


def li(x: int) -> str:
    with open(f"inputs/{_n(x)}i.txt", "r") as f:
        return f.read()


def eight_adj(y: int, x: int):
    return [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1), (y + 1, x + 1), (y + 1, x - 1), (y - 1, x + 1), (y - 1, x - 1)]
