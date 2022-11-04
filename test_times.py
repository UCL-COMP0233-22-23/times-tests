from times import * 
import pytest
from pytest import raises
import yaml

with open("test_fixtures.yaml", "r") as file:
    test_info = yaml.safe_load(file)

parameters=[(eval(test["range1"]), eval(test["range2"]), eval(test["expected"])) for test in test_info.values()]

@pytest.mark.parametrize("range1, range2, expected", parameters)
def test_given_input(range1, range2, expected):
    result = compute_overlap_time(range1,range2)
    assert result == expected

def test_time_range_invalid_input():
    with raises(ValueError):
        range = time_range("2001-01-01 10:00:00", "2000-01-01 10:00:00")
