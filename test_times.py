import sys 
sys.path.append('wk5_testing/times-tests/')
from times import compute_overlap_time, time_range
import pytest

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result =  compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected


def test_no_overlap():
    t2 = time_range("2011-01-12 10:30:00", "2011-01-12 10:45:00")
    t1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    assert compute_overlap_time(t1, t2) == 0


def test_both_several_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 11:30:00", 2, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00", 2, 60)
    expect = [("2010-01-12 10:00:00", "2010-01-12 10:44:30"), ("2010-01-12 10:45:30", "2010-01-12 11:00:00")]
    assert compute_overlap_time(large, short) == expect


def test_start_stop():
    t1 = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    t2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    assert compute_overlap_time(t1, t2) == 0

def test_negative_interval():
    t2 = time_range("2011-01-12 10:30:00", "2011-01-12 10:45:00")
    t1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    compute_overlap_time(t1, t2) == pytest.raises(ValueError)
