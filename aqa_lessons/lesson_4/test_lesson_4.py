class TestA:
    def setup_method(self):
        print("-->Connection<--")
        self.value = 42

    def teardown_method(self):
        print("--> End of Connection<--")

    def test_1(self):
        print('test_1 run')
        assert self.value == 42

    def test_2(self):
        print('test_2 run')
        assert self.value < 43


def test_3(client):
    print(' test_3 run')
    assert client == 42
