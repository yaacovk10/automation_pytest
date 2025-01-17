# Basic test
```
    pytest 
```

# Substring Matching of Test Names
```
    pytest -k <substring> -v
```

example:
```
    pytest -k great -v
```

# Grouping the Tests - markername
decorator before the function
```
    @pytest.mark.<markername>
```

and run tests with this command
```
    pytest -m <markername> -v
```
# Fixture
Add decorator to fixture function
```
@pytest.fixture
def input_value()
```
Fixture function should have a return value

And insert the fixture function name as a parameter of the function. According to example:
```
def test_<>(input_value)
```
Return value of fixture function will be the parameter of test function

## Fixtures can request other fixtures

```
# contents of test_append.py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]
```

## More than one fixture at a time


# Conftest
You can define the fixture function in another file named contest.py
All the configuration is like the fixture


# Parameterizing Tests
Add decorator  , and parameters like following
```
@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output
```
note : not only with 2 params. It works also like this
```
@pytest.mark.parametrize("number",  [36, 18, 16])
def test_division_6(number):
   assert number % 6 == 0
```

## Generating parameters by command line
Let takes example. 
Test is __test_compute.py__
```
def test_compute(param1):
    assert param1 < 4
```
__conftest.py is __
```
def pytest_addoption(parser):
    parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc):
    if "param1" in metafunc.fixturenames:
        if metafunc.config.getoption("all"):
            end = 5
        else:
            end = 2
        metafunc.parametrize("param1", range(end))
```
* pytest_addoption adds a command-line option __--all__
* pytest_generate_tests checks if __param1__ is a fixture in the test function and sets the range of values for param1 
    * if --all option is selected -> __param1 = 5__ and test_compute tests in the range 5 -> 1 failure
    * else -> __param1 = 2__ and test_compute tests in range 2 -> no failure

##  parameter provided by the user
__'pytest_addoption'__ hook allows to add a command-line option that the user can specify
```
import pytest

def pytest_addoption(parser):
    parser.addoption("--user-param", action="store", help="User provided parameter")

@pytest.fixture
def user_param(request):
    return request.config.getoption("--user-param")

# Example test using the command-line option
def test_example(user_param):
    assert user_param == "expected_value"
```

to run the test use
```
pytest test_file.py --user-param="some_value"
```





# Xfail/Skip Tests
To execute the xfailed test, but it will not be considered as part failed or passed tests
```
@pytest.mark.xfail
```

To skip tests
```
@pytest.mark.skip
```
# Stop Test Suite after N Test Failures
to stop the execution of test suite soon after n number of test fails
```
pytest --maxfail = <num>
```

# Run Tests in Parallel
Install pytest-xdist by running the following command −
```
pip install pytest-xdist
```

run tests by using the syntax pytest -n <num>, while num is a multiple workers. For example 
```
pytest -n 3

```
# Test Execution Results in XML Format
```
pytest <test file> -v --junitxml="result.xml"
```


