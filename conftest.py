import pytest

# @pytest.fixture
# def input_value():
#    input = 39
#    return input


def pytest_addoption(parser):
   parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc):
   if "param1" in metafunc.fixturenames:
      if metafunc.config.getoption("all"):
         end = 6
      else:
         end = 2
      metafunc.parametrize("param1", range(end))


import pytest
import os

@pytest.fixture(scope="session")
def subfolders():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]