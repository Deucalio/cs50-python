from numb3rs import validate


def test_valid_ip():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True


def test_invalid_ip():
      assert validate("cat") == False
      assert validate("x.x.x.x") == False
      assert validate("275.1.1.1") == False
      assert validate("285.563.325.59") == False
      assert validate("255.x.x.cat") == False
      assert validate("1.290.290.309") == False



