import pytest


@pytest.fixture()
def setUp():
    print("Open Amazon app")
    print("User logged in")
    yield
    print("User logged out")
    print("Close Amazon app")

def test_AddItemtoCart(SetUp):
    print("Added successfully")

def test_RemoveItemfromCart(setUp):
    print("removed successfully")


