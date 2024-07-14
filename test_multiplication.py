import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output

@pytest.mark.parametrize("number",  [36, 18, 16])
def test_division_6(number):
   assert number % 6 == 0

