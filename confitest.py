import pytest

@pytest.fixture(scope="session",autouse=True)
def setUp():
    print("open Amazon app")
    print("User logged in")
    yield
    print("User logout ")
    print("close Amazon app")
