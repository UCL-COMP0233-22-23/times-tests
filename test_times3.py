from times import time_range
from times import compute_overlap_time
import pytest
import yaml

with open('fixture.yml') as ymlfile:
    yml = yaml.safe_load(ymlfile)
    fixture = []
    for i in yml:
        time_range_1 = eval(i['time_range_1'])
        time_range_2 = eval(i['time_range_2'])
        expected = [eval(j) for j in i['expected']]
        fixture.append((time_range_1,time_range_2,expected))

@pytest.mark.parametrize("time_range_1, time_range_2, expected", fixture)
def test_compute_overlap_time(time_range_1, time_range_2, expected):
    result = compute_overlap_time(time_range_1, time_range_2)
    assert result == expected