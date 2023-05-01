import pytest

from utils import arrs
from utils.arrs import coating_types, divide


def test_get():
    assert arrs.get([1, 2, -3], 1, default='default') == 2
    assert arrs.get([1, 2, 3, 4], -1, default='default') == 'default'


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]



@pytest.mark.parametrize('array, coating_in_array, expcted', [
    ([1, 2, 3], int, 3),
    ([1, '2', '3'], str, 2),
    ([1, '2', '3'], int, 1)

])

def test_coating_tupes(array, coating_in_array, expcted):
    assert coating_types(array, coating_in_array) == expcted


def test_divide():
    assert divide(35, 7) == 5
    assert divide(1_000_000, 2) == 500_000
    assert divide(81, 9) == 9
    assert divide(6.6, 2) == 3.3
    assert divide(25, 5) == 5
    assert divide(18, 3) == 6


def test_divide_division_zro():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)