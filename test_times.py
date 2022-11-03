from pytest import raises
import numpy as np
from times import compute_overlap_time
from times import time_range


def test_given_input():

    large_2 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",3,45)
    short_2 = time_range("2010-01-12 09:30:00", "2010-01-12 09:45:00",2,20)
    result_2 = (compute_overlap_time(large_2, short_2))
    expected_2 = np.array([0,0,0,0,0,0])


    
    assert np.all(result_2==expected_2)

