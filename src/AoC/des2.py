from typing import Union, List, Any
import attr
from itertools import product

@attr.s
class Intcodes(object):
    intcodes: List[int] = attr.ib()
    opcode_pos: int = attr.ib(default=0, init=False)
    opcode_pos_shift: int = attr.ib(default=4, init=False)

    def process_program(self):
        tmp_intcodes = self.intcodes.copy()
        self.opcode_pos = 0
        op = self.get_opcdoe(tmp_intcodes)
        while op != 99:
            ind_first, ind_last, ind_out, tmp_intcodes = self.get_program_values(tmp_intcodes)
            tmp_intcodes = self.update_intcodes(tmp_intcodes, op, ind_first,ind_last,ind_out)
            op = self.get_opcdoe(tmp_intcodes)

        return tmp_intcodes
    
    def update_intcodes(self, intcodes, op, f,l,o):
        f_v = intcodes[f]
        l_v = intcodes[l]
        if op == 1:
            res = f_v + l_v
        elif op == 2:
            res = f_v*l_v
        intcodes[o] = res
        return intcodes

    def get_program_values(self, intcodes):
        ind_first, ind_last , ind_out = intcodes[self.opcode_pos+1:self.opcode_pos+self.opcode_pos_shift]
        self.opcode_pos += 4
        return ind_first, ind_last, ind_out, intcodes

    def get_opcdoe(self, intcodes):
        opcode = intcodes[self.opcode_pos]
        if opcode not in {1,2,99}:
            raise ValueError(f"Not valid OpCode: {op}, from pos: {self.opcode_pos} in: {self.intcodes}")    
        return opcode

def solve21(path: str = 'assets/des2.1.txt') -> int:
    with open(path) as fh:
        ic = Intcodes([int(c.strip()) for c in fh.readline().strip().split(",")])
        ic.intcodes[1] = 12
        ic.intcodes[2] = 2
        
    return ic.process_program()[0]

def solve22(path: str = 'assets/des2.1.txt') -> int:
    with open(path) as fh:
        ic = Intcodes([int(c.strip()) for c in fh.readline().strip().split(",")])

    for i,j in product(range(100),range(100)):
        ic.intcodes[1] = i
        ic.intcodes[2] = j
        if ic.process_program()[0] == 19690720:
            break
        

    return 100*i + j
