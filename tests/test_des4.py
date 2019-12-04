from AoC import des4
import pytest

@pytest.mark.parametrize("test,result", [("111111",True),("223450",False),("123789",False)])
def test_is_password(test,result):
    assert des4.Passwords.is_password(test) == result

@pytest.mark.parametrize("test,result", [(("111111", "111122"),10),(("111222", "111240"),15)])
def test_count(test,result):
    pw = des4.Passwords(*test)
    assert pw.count_passwords() == result

