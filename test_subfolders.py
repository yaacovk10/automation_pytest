import pytest
import os
from pytest_lazyfixture import lazy_fixture


import pytest
import os

def pytest_generate_tests(metafunc):
    if 'subfolder' in metafunc.fixturenames:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        subfolders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
        metafunc.parametrize('subfolder', subfolders)

def test_subfolder(subfolder):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    subfolder_path = os.path.join(base_dir, subfolder)
    
    # Perform your test here, for example:
    assert os.path.isdir(subfolder_path)
    # Add more assertions or operations as needed

    # Simulate a test result
    print(f"Test completed for: {subfolder}")
