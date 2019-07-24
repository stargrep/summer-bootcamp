from finalProject.strategy.src import sample


def test_shout_and_repeat():
    result = sample.shout_and_repeat('hello goodbye-')
    assert result == 'HELLO GOODBYE-HELLO GOODBYE-'


# def test_shout():
#     assert sample._shout('have a nice day') == 'HAVE A NICE DAY'

