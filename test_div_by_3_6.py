import pytest

# @pytest.fixture
# def input_value():
#    input = 39
#    return input


@pytest.fixture
def input_value_2():
   input  = 18
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0

def test_divisible_by_9(input_value_2):
   assert input_value_2 % 9 ==0