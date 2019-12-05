from cytoolz.curried import pipe, map, reduce, filter, frequencies, count
from operator import add

def count_pw(low,high, handle_large_groups):
    return pipe(
        range(int(low), int(high)+1),
        map(str),
        filter(lambda x: "".join(sorted(x)) == x),
        map(frequencies),
        map(lambda x: handle_large_groups(x.values())),
        reduce(add)
    )

def solve41() -> int:
    return count_pw(136760, 595730, handle_large_groups=lambda x: max(x) >= 2)
def solve42() -> int:
    return count_pw(136760, 595730, handle_large_groups=lambda x: 2 in x)


if __name__ == "__main__":
    print(f"solve 4.1: {solve41()}")
    print(f"solve 4.2: {solve42()}")