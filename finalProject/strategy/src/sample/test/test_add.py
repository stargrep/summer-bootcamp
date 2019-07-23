from src import sample


def test_my_add():
    assert sample.my_add([9, 0, 2], [0, 1]) == [9, 0, 2, 0, 1]
    assert sample.my_add('beverly ', 'hills') == 'beverly hills'
