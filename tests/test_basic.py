import pytest

import myeditdistance as ed


def test_package_has_version():
    assert ed.__version__ is not None


def test_package_importable():
    pass


@pytest.mark.skip(reason="This decorator should be removed when test passes.")
def test_wrong_edit_distance():
    assert 1 == 0  # This test is designed to fail.


# @pytest.mark.skip(reason="This decorator should be removed when test passes.")
@pytest.mark.parametrize(
    "output, expected",
    [
        # Test identical strings
        (ed.edit_distance(string1="kitten", string2="kitten"), 0),
        # Test insertion
        (ed.edit_distance(string1="kitten", string2="kittens"), 1),
        # Test deletion
        (ed.edit_distance(string1="hello", string2="hllo"), 1),
        # Test substition
        (ed.edit_distance(string1="hello", string2="hallo"), 1),
        # Test one string empty
        (ed.edit_distance(string1="", string2="kitten"), 6),
        (ed.edit_distance(string1="kitten", string2=""), 6),
        # Test both strings empty
        (ed.edit_distance(string1="", string2=""), 0),
        # Test any input
        (ed.edit_distance(string1="kitten", string2="sitting"), 3),
    ],
)
def test_edit_distance(output, expected):
    assert output == expected


def test_invalid_input():
    with pytest.raises(TypeError):
        ed.edit_distance(123, "kitten")
