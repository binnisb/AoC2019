from typing import Union, List, Any
import attr

@attr.s(frozen=True)
class Mass(object):
    mass: float = attr.ib(converter=float)
    fuel_from_mass: int = attr.ib(init=False)
    fuel_from_fuel: int = attr.ib(init=False)
    fuel_total: int = attr.ib(init=False)

    @staticmethod
    def _counter_upper(mass: float) -> int:
        return max(int(mass/3.0) - 2, 0)

    @fuel_from_mass.default
    def _calc_fuel_from_mass(self):
        return self._counter_upper(self.mass)

    @fuel_from_fuel.default
    def _calc_fuel_from_fuel(self):
        extra = 0
        fuel = self.fuel_from_mass
        while fuel > 0:
            extra_cu = self._counter_upper(fuel)
            if extra_cu <= 0:
                break
            extra += extra_cu
            fuel = extra_cu
        return extra

    @fuel_total.default
    def _calc_total_fuel(self):
        return self.fuel_from_mass + self.fuel_from_fuel


def _convert_to_masses(in_val: Union[List[Mass], List[Any], Any]) -> List[Mass]:
    if type(in_val) is list:
        return [v if type(v) is Mass else Mass(v) for v in in_val]
    else:
        return [in_val if type(in_val) is Mass else Mass(in_val)]

@attr.s(frozen=True)
class FuelCalculator(object):
    masses: List[Mass] = attr.ib(converter=_convert_to_masses)

    def mass_fuel(self):
        return sum([m.fuel_from_mass for m in self.masses])

    def total_fuel(self):
        return sum([m.fuel_total for m in self.masses])

    @classmethod
    def input_to_masses(cls, path: str) -> List[float]:
        with open(path) as fh:
            return cls(masses=[mass.strip() for mass in fh])


def solve11(path: str = 'assets/des1.1.txt') -> int:
    fc = FuelCalculator.input_to_masses(path)
    return fc.mass_fuel()

def solve12(path: str = 'assets/des1.1.txt') -> int:
    fc = FuelCalculator.input_to_masses(path)
    return fc.total_fuel()

if __name__ == "__main__":
    print(f"solve 1.1: {solve11()}")
    print(f"solve 1.2: {solve12()}")