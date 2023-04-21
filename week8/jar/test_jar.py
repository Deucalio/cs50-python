from jar import Jar
import pytest


def test_init():
    jar = Jar(12)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(13)

    
    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar(15)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_withdraw():
    jar = Jar(12)
    jar.withdraw(10)
    assert str(jar) == "🍪🍪"