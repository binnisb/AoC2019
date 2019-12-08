import os
from AoC import des8
import pytest

def test_layers():
    instr = "123456789012345678900221"

    data = [int(c) for c in instr]
    assert 2 == des8.create_layers(data, 3, 2)

def test_decode():
    instr = "0222112222120000"

    data = [int(c) for c in instr]
    res = os.linesep.join(["01","10"])
    assert res == des8.decode_image(data, 2, 2)