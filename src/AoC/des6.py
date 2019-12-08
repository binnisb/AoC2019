import networkx as nx

def parse_orbit(orb, g, curr_len=0):
    if g.out_degree() == 0:
        return curr_len
    return curr_len + sum(parse_orbit(s, g, curr_len+1) for s in g.successors(orb))

def checksum(orbits):
    return parse_orbit("COM", nx.DiGraph(orbits))

def solve61(path: str = 'assets/des6.1.txt') -> int:
    with open(path) as fh:
        return checksum(map(lambda x: x.strip().split(")"), fh.readlines()))

def solve62(path: str = 'assets/des6.1.txt') -> int:
    with open(path) as fh:
        data = map(lambda x: x.strip().split(")"), fh.readlines())
    return nx.shortest_path_length(nx.Graph(data), "YOU","SAN") - 2

def solve622():
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
    print(data)
    return nx.shortest_path_length(nx.Graph(data), "YOU","SAN") - 2

if __name__ == "__main__":
    print(f"solve 6.1: {solve61()}")
    print(f"solve 6.2: {solve62()}")
    print(f"solve 6.22: {solve622()}")
