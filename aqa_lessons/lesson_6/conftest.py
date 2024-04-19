import pytest


@pytest.fixture(scope="function")
def test_data():
    print("\n->func start")
    data = "func"
    yield data
    print("\nfunc finish<-")
