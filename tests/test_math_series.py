from math_series import __version__
from math_series.series import fibonacci as fb
from math_series.series import lucas as lu
from math_series.series import sum_series
def test_version():
    assert __version__ == '0.1.0'

# Fibonacci

def test_fibonacci_10():
    expected =55
    actual = fb(10)
    assert expected == actual

def test_fibonacci_1():
    expected =1
    actual = fb(1)
    assert expected == actual

def test_fibonacci_0():
    expected =0
    actual = fb(0)
    assert expected == actual
# ----------------------------------------------------------------

# Lucas

def test_lucas_10():
    expected =123
    actual =lu(10)
    assert expected == actual

def test_lucas_0():
    expected =2
    actual =lu(0)
    assert expected == actual

def test_lucas_1():
    expected =1
    actual = lu(1)
    assert expected == actual

# ----------------------------------------------------------------

# Sum series

def test_sum_10():
    expected =55
    actual = sum_series(10)
    assert expected == actual

def test_sum_7():
    expected =29
    actual = sum_series(7,2,1)
    assert expected == actual

def test_sum_9():
    expected =76
    actual = sum_series(9,2,1)
    assert expected == actual
