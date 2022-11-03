import times 
from pytest import raises

def test_given_input():

    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_several_intervals_empty_intersection():

    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2011-01-12 10:30:00", "2011-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_several_intervals_nonempty_intersections():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 12, 15)
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:03', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:39:50'), ('2010-01-12 10:40:05', '2010-01-12 10:45:00')]
    assert result == expected

def test_several_intervals_one_second_intersections():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00", 12, 15)
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:30:00')]
    assert result == expected

def test_invalid_date_order_raise_error():
    with raises(ValueError):
        times.time_range("2010-01-12 10:30:00", "2010-01-12 10:00:00", 12, 15)
    
