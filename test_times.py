from times import compute_overlap_time, time_range
from pytest import raises

def test_given_input():
    outer = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    inner = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(outer, inner)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_nooverlap():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    second = time_range("2010-01-12 09:30:00", "2010-01-12 09:45:00")
    result = compute_overlap_time(first, second)
    expected = []
    assert result == expected

def test_multipleintervals():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3, 10)
    second = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(first, second)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:39:53'), ('2010-01-12 10:40:03', '2010-01-12 10:45:00')]
    assert result == expected

def test_border():
    first = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    second = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
    result = compute_overlap_time(first, second)
    expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00')]
    assert result == expected

def test_backwardsrange():
    with raises(ValueError):
        range = time_range("2010-01-12 14:00:00", "2010-01-12 12:00:00")