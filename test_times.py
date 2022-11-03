import pytest

from times import time_range, compute_overlap_time
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))
    result = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    expect = compute_overlap_time(large, short)
    assert result == expect

def test_not_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 9:30:00", "2010-01-12 9:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expect = []
    assert result == expect

def test_negative_test():
    with pytest.raises(ValueError):
        t = time_range("2010-01-12 10:00:00", "2010-01-12 9:00:00")



