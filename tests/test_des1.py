from AoC import des1
import pytest

@pytest.mark.parametrize("test,result", [(12,2),(14,2),(1969,654),(100756,33583)])
def test_mass(test,result):
    fc = des1.FuelCalculator(masses=test)
    assert fc.mass_fuel() == result

@pytest.mark.parametrize("test,result",[(14,2),(1969,966),(100756,50346)])
def test_marginal_fuel(test,result):
    fc = des1.FuelCalculator(masses=test)
    assert fc.total_fuel() == result
