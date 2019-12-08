from AoC import des6
import pytest

def test_orbit_paths():
    data = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""
    data = list(map(lambda x: x.strip().split(")"), data.split()))
    return des6.shortest_paths(data)
