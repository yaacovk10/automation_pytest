import pytest
import os

def pytest_addoption(parser):
    parser.addoption("--path", action="store", help="User provided parameter")

@pytest.fixture
def user_param(request):
    return request.config.getoption("--path")


def test_folder_list(user_param):
    directory = user_param
    l = os.listdir(directory)
    assert len(l) != 0
