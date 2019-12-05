from AoC import des4
import pytest

@pytest.mark.parametrize("test,result", [(("111111", "111122"),10),(("111222", "111240"),15)])
def test_count_large_group(test,result):
    assert des4.count_pw(*test, True) == result

@pytest.mark.parametrize("test,result", [(("111111", "111122"),1),(("111222", "111240"),8)])
def test_count_must_be_2(test,result):
    assert des4.count_pw(*test, False) == result
