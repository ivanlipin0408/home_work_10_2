import pytest


@pytest.fixture
def numbers():
    return "1250 89** **** 5255"


@pytest.fixture
def account():
    return "**2255"


@pytest.fixture
def date():
    return "11.03.2024"