from times import compute_overlap_time, time_range
from pytest import raises

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00",2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 13:30:00", "2010-01-12 13:45:00",2, 60)
    result = compute_overlap_time(range1,range2)
    expected = [('0000-00-00 00:00:00', '0000-00-00 00:00:00')]
    assert result == expected

def test_more_intervals():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",4)
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00",2, 60)
    result = compute_overlap_time(range1, range2)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_end_start():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:45:00",2, 60)
    result = compute_overlap_time(range1, range2)
    expected = [('0000-00-00 00:00:00', '0000-00-00 00:00:00')]
    assert result == expected

def test_fails_inverted_interval():
    with raises(ValueError):
        range1 = time_range("2010-01-12 11:00:00", "2010-01-12 10:00:00")
        range2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:45:00",2, 60)
        compute_overlap_time(range1, range2)
