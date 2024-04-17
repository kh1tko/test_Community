# Створити фікстури для імітації отримання даних через API з різними скоупами.
# Потрібно створити чотири фікстури під кожний з основних скоупів (function, class, module, session),
# які будуть повертати імітовані дані з АПІ. Напишіть тести, які запускаються тільки для двох скоупів: function і session.

import pytest


@pytest.fixture(scope="function")
def api_data_function():
    print("Getting API data for function scope")
    return {"data": "Function API data"}


@pytest.fixture(scope="class")
def api_data_class():
    print("Getting API data for class scope")
    return {"data": "Class API data"}


@pytest.fixture(scope="module")
def api_data_module():
    print("Getting API data for module scope")
    return {"data": "Module API data"}


@pytest.fixture(scope="session")
def api_data_session():
    print("Getting API data for session scope")
    return {"data": "Session API data"}


class TestAPI:
    def test_function_scope(self, api_data_function):
        assert api_data_function["data"] == "Function API data"

    def test_session_scope(self, api_data_session):
        assert api_data_session["data"] == "Session API data"
