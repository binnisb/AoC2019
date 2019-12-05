try:
    import cytoolz as toolz
except:
    import pytoolz as toolz
from toolz.curried import pipe, map, reduce, filter, frequencies, count
from operator import add

def count_pw(low,high, handle_large_groups):
    return pipe(
        range(int(low), int(high)+1),
        map(str),
        filter(is_sorted),
        map(frequencies),
        map(lambda x: handle_large_groups(x.values())),
        reduce(add)
    )

def is_sorted(x):
    first = x[0]
    for c in x[1:]:
        if first > c:
            return False
        first = c
    return True

def allow_large_groups(x):
    return max(x) >= 2

def not_allow_large_groups(x):
    return 2 in x

def solve41() -> int:
    return count_pw(136760, 595730, handle_large_groups=allow_large_groups)
def solve42() -> int:
    return count_pw(136760, 595730, handle_large_groups=not_allow_large_groups)


if __name__ == "__main__":
    print(f"solve 4.1: {solve41()}")
    print(f"solve 4.2: {solve42()}")
