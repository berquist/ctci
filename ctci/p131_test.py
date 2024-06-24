from p131 import impls

_F20 = 6765
_F50 = 12586269025
_F100 = 354224848179261915075
_F200 = 280571172992510140037611932413038677189525
_F500 = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125


def test_p131():
    for impl in impls:
        assert impl(20) == _F20
