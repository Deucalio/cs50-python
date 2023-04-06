from bank import value

def test_bank():
    assert value("Ok") == 100
    assert value("Cool") == 100
    assert value("Hammad") == 20
    assert value("Hello") == 0
