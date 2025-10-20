# test_code.py


def test_it(server, port):
    assert server.endswith(".com")
    assert port > 8000
