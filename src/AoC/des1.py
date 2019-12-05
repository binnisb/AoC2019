try:
    import cytoolz as toolz
except:
    import pytoolz as toolz
from toolz.curried import pipe, map, reduce, curry
from operator import add

@curry
def calc(mass, sub_mass=False):
    if mass <= 0:
        return 0
    else:
        fuel = max((int(mass/3) -2, 0))
        if sub_mass:
            return fuel + calc(fuel, sub_mass)
        else:
            return fuel

def calc_fuel(masses, sub_mass=False):
    def mass_to_int(m):
        if type(m) is int:
            return m
        elif type(m) is str:
            return m.strip()
        else:
            raise ValueError("mass should be int or string")
            
    return pipe(masses,
                map(mass_to_int),
                map(int),
                map(calc(sub_mass=sub_mass)),
                reduce(add))   

def solve11(path: str = 'assets/des1.1.txt') -> int:
    with open(path) as fh:
        return calc_fuel(fh)

def solve12(path: str = 'assets/des1.1.txt') -> int:
    with open(path) as fh:
        return calc_fuel(fh,sub_mass=True)
        

if __name__ == "__main__":
    print(f"solve 1.1: {solve11()}")
    print(f"solve 1.2: {solve12()}")
