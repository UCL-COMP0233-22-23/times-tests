from times import * 
from pytest import raises

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large,short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_given_input_2():
    range1 = time_range("2000-01-01 10:00:00", "2001-01-01 10:00:00")
    range2 = time_range("2100-01-01 10:00:00", "2101-01-01 10:00:00")
    result = compute_overlap_time(range1,range2)
    expected = []
    assert result == expected

def test_given_input_3():
    range1 = time_range("2000-01-01 10:00:00", "2001-01-01 10:00:00", 2, 60)
    range2 = time_range("2000-06-01 10:00:00", "2001-06-01 10:00:00", 2, 120)
    result = compute_overlap_time(range1,range2)
    assert len(result) == 3

def test_given_input_4():
    range1 = time_range("2000-01-01 10:00:00", "2001-01-01 10:00:00") 
    range2 = time_range("2001-01-01 10:00:00", "2002-01-01 10:00:00")
    result = compute_overlap_time(range1,range2)
    assert result == [("2001-01-01 10:00:00", "2001-01-01 10:00:00")]

def test_time_range_invalid_input():
    with raises(ValueError):
        range = time_range("2001-01-01 10:00:00", "2000-01-01 10:00:00")
