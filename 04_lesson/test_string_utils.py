import pytest
from string_utils import StringUtils


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("привет", "Привет"),
    (" привет", " Привет"),
    ("ПРИВЕТ", "ПРИВЕТ")
])
def test_capitalize_positive(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("!№;%", "!№%"),
    pytest.param(None, None, marks=pytest.mark.xfail)
])
def test_capitalize_negative(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("skypro  ", "skypro  "),
    (" Hallo friend", "Hallo friend"),
    (" привет ", "привет ")
    ])
def test_trim_positive(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", " skypro"),
    ("skypro  ", "skypro"),
    (" Hallo friend", " Hallofriend")
])
def test_trim_negative(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, search_symbol, expected", [
    ("Skypro", "S", True),
    ("Привет", "П", True),
    ("123", "1", True),
    (" ", " ", True)
    ("Skypro", "Sky", True),
    ("Привет", "Привет", True),
    ("Skypro", "U", False),
    ("Привет", "Ю", False),
    ("123", "0", False),
    ("Skypro", "1", False),
    ("Привет", "Приветик", False)
])
def test_contains_positive(input_str, search_symbol, expected):
    string_utils = StringUtils()
    assert string_utils.contains(input_str, search_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, search_symbol, expected", [
    ("", "a", False),
    ("abc", "", False),
    ("", "", False),
    ("abc", "а", False)
])
def test_contains_edge_cases_negative(input_str, search_symbol, expected):
    string_utils = StringUtils()
    assert string_utils.contains(input_str, search_symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "s", "kypro"),
    ("hello world", "w", "hello orld"),
    ("python", "n", "pytho"),
    ("привет", "ет", "при"),
    ("привет1", "1", "привет"),
    ("хорошо", "о", "хрш")
])
def test_delete_positive(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "s", ""),
    ("  ", "w", "  "),
    ("python", "", "python"),
    ("привет", "e", "привет")
])
def test_delete_negative(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == expected
