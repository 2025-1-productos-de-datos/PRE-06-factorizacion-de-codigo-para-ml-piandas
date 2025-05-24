import os
import pytest

@pytest.fixture(scope='session', autouse=True)
def check_models_directory():
    assert os.path.exists("models"), "models/ directory does not exist"