from um import count

def test_pass1():
    assert count("um?") == 1
def test_pass2():
    assert count("Um, thanks for the album") ==1
def test_pass3():
    assert count("Um, thanks, um...") == 2