from plates import is_valid

def test_only_letters():
    assert is_valid("HAMMAD") == True
    assert is_valid("Outlas") == True
    assert is_valid("hello world") == False
    assert is_valid("a") == False


def test_only_numbers():
    assert is_valid("7.866") == False
    assert is_valid("3.14") == False
    assert is_valid("3") == False
    assert is_valid("23") == False
    assert is_valid("123456") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False


def test_both():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("cs01") == False
    assert is_valid("c6") == False
    assert is_valid("cs") == True
    assert is_valid("abc10") == True
    assert is_valid("000") == False
    assert is_valid("cs50asdaa") == False
    assert is_valid("cs50p") == False

    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("1a") == False
    assert is_valid("c2") == False
    assert is_valid("1z") == False
    assert is_valid("2A") == False
    assert is_valid("3x") == False
    assert is_valid("zu#kk") == False



def comma():
    assert is_valid("Ham,s") == False
    assert is_valid("J:d,s") == False
    assert is_valid(",.,a") == False
    assert is_valid(" ") == False
    assert is_valid("      ") == False
    assert is_valid("What's up, eh?") == False
    assert is_valid("vs,20?") == False

