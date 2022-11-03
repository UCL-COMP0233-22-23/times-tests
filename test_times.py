from times import time_range, compute_overlap_time
import pytest

def test_given_input():

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected


def test_given_input_2():

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00")

    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_given_input_3():

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",3,120)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    expected =[('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:38:40'), ('2010-01-12 10:40:40', '2010-01-12 10:45:00')]
    assert result == expected


def test_given_input_4():

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 14:00:00")

    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected



def test_negative():
    with pytest.raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

