from times import compute_overlap_time, time_range
import pytest
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlaps():
    large = time_range("2010-01-12 11:50:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_several_intervals_each():
    large = time_range("2010-01-12 10:40:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [("2010-01-12 10:40:00", "2010-01-12 10:45:00")]
    assert result == expected

def test_same_ending_time():
    large = time_range("2010-01-12 10:40:00", "2010-01-12 10:45:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    result = compute_overlap_time(large, short)
    expected = [("2010-01-12 10:40:00", "2010-01-12 10:45:00")]
    assert result == expected

def test_start_time_bigger_than_end_time():
    with pytest.raises(ValueError):
        wrong = time_range("2010-01-12 10:45:00", "2010-01-12 10:40:00")

