from twttr import shorten

def test_twittr():
    assert shorten("Hammad") == "Hmmd"
    assert shorten("Ali Sethi") == "l Sth"
    assert shorten("Jedi") == "Jd"
    assert shorten("Star Wars") == "Str Wrs"
    assert shorten("CS50") == "CS50"
    assert shorten("No, however!") == "N, hwvr!"