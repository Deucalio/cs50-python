from um import count


def test_um_comma():
    assert count("um, hello, um, world") == 2
    assert count("um, hello, um") == 2
    assert count("um....") == 1
    assert count("um, hello, um, um, um") == 4
    assert count("um,2,21,x,cat,um") == 2


def test_um_question_marks():
    assert count("um?") == 1
    assert count("Um, thanks for the album?") == 1
    assert count("Um, thanks, um...? um") == 3


def test_zero_count():
    assert count("yummy") == 0
    assert count("ummy") == 0
    assert count("yum") == 0

