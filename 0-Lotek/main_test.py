from main import Application


def test_get_six():
    # given
    random_numbers = Application()

    # when
    result = random_numbers.get_six()

    # then
    assert len(result) == 6
