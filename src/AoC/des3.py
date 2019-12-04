from typing import Union, List, Any, Tuple
import attr
import numpy as np
from enum import Enum
from collections import defaultdict

class Direction(Enum):
    U = "U"
    D = "D"
    R = "R"
    L = "L"

@attr.s
class Point(object):
    direction: Direction = attr.ib()
    length: int = attr.ib()

    @classmethod
    def from_str(cls, s):
        d = s[0].upper()
        l = int(s[1:])

        return cls(Direction(d), l)

    def shift_point(self,x,y,step):
        if self.direction is Direction.R:
            return x + step, y
        elif self.direction is Direction.L:
            return x - step, y
        elif self.direction is Direction.U:
            return x, y + step
        elif self.direction is Direction.D:
            return x, y - step
        else:
            raise ValueError("Strange")

def _wire_converter(wire: Union[List[str], List[Point], str]) -> List[Point]:
    if type(wire) in (list, tuple):
        return [w if type(w) is Point else Point.from_str(w.strip()) for w in wire]
    elif type(wire) is str:
        return _wire_converter(wire.split(","))

@attr.s
class Grid(object):
    wire1: List[Point] = attr.ib(converter=_wire_converter)
    wire2: List[Point] = attr.ib(converter=_wire_converter)
    grid: tuple = attr.ib(init=False)
    
    @grid.default
    def _grid_default(self):
        wire_paths = {}
        for wire, name in zip((self.wire1, self.wire2), ("wire1","wire2")):
            wire_path = dict()
            current_x = 0
            current_y = 0
            steps = 0
            for point in wire:
                for i in range(1, point.length + 1):
                    key = point.shift_point(current_x, current_y, i)
                    steps += 1
                    if key not in wire_path:                    
                        wire_path[key] = steps
                current_x, current_y = key
            wire_paths[name] = wire_path
        return wire_paths

    def manhattan(self):
        wire1 = self.grid["wire1"]
        wire2 = self.grid["wire2"]
        intersection = wire1.keys() & wire2.keys()
        
        return min([abs(x) + abs(y) for (x,y) in intersection])

    def shortest_path(self):
        wire1 = self.grid["wire1"]
        wire2 = self.grid["wire2"]
        intersection = wire1.keys() & wire2.keys()
        
        return min([wire1[key] + wire2[key] for key in intersection])


def solve31(path: str = 'assets/des3.1.txt') -> int:
    with open(path) as fh:
        g = Grid(*list(map(str.strip,fh.readlines())))
    return g.manhattan()

def solve32(path: str = 'assets/des3.1.txt') -> int:
    with open(path) as fh:
        g = Grid(*list(map(str.strip,fh.readlines())))
    return g.shortest_path()


if __name__ == "__main__":
    print(f"solve 3.1: {solve31()}")
    print(f"solve 3.2: {solve32()}")