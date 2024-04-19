import pytest
import time


class TestForTest:
    @pytest.mark.order(6)
    def test_1(self, test_data):
        time.sleep(2)
        assert True

    @pytest.mark.order(10)
    @pytest.mark.smoke
    def test_2(self, test_data):
        time.sleep(2)
        assert True

    @pytest.mark.order(1)
    def test_3(self, test_data):
        time.sleep(2)
        assert True

    @pytest.mark.order(7)
    @pytest.mark.smoke
    @pytest.mark.retest
    def test_4(self, test_data):
        time.sleep(2)
        assert True

    @pytest.mark.order(2)
    def test_5(self, test_data):
        time.sleep(2)
        assert True

    @pytest.mark.order(3)
    @pytest.mark.smoke
    def test_6(self, test_data):
        time.sleep(2)
        assert True

    @pytest.mark.order(8)
    def test_7(self, test_data):
        time.sleep(2)
        assert True

    @pytest.mark.order(4)
    @pytest.mark.regression
    def test_8(self, test_data):
        time.sleep(2)
        assert True

    @pytest.mark.order(5)
    def test_9(self, test_data):
        time.sleep(2)
        assert True

    @pytest.mark.order(9)
    @pytest.mark.smoke
    def test_10(self, test_data):
        time.sleep(2)
        assert True
