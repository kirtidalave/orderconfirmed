import pytest

@pytest.fixture()
def setUp():
    print("Open Amazon app")
    print("User logged in")
    yield
    print("User logged out")
    print("Close Amazon app")

def test_placeOrder(SetUp):
    print("Placing order")

def test_makePayments(setUp):
    print("Do the payments")

def test_orderConfirmation(setUp):
    print("Order confirmed")
