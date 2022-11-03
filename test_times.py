from pytest import raises
import numpy as np
from times import compute_overlap_time
from times import time_range


def test_Overlap_Intervals():

    n_intervals_1, n_intervals_2 = 3, 3
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", n_intervals_1, 45)
    short = time_range("2010-01-12 09:30:00", "2010-01-12 09:45:00", n_intervals_2, 20)
    result = (compute_overlap_time(large, short))
    expected = [] * n_intervals_1 * n_intervals_2
    
    assert result==expected

def test_():

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 09:30:00", "2010-01-12 09:45:00")
    result = (compute_overlap_time(large, short))
    expected = []
    
    assert result==expected


def test_backwards():
    # large = time_range("2010-01-12 14:00:00", "2010-01-12 12:00:00")
    # short = time_range("2010-01-12 09:30:00", "2010-01-12 09:45:00")
    # result = (compute_overlap_time(large, short))

    with raises(ValueError,match=r'Start time needs to be before the end time'):
        range = time_range("2010-01-12 14:00:00", "2010-01-12 12:00:00")

