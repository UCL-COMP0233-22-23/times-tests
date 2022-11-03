from times import time_range
from times import compute_overlap_time
from collections.abc import Iterable


def test_given_input_nooverlap():
    large = time_range("2012-01-12 10:00:00", "2012-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [('2012-01-12 10:00:00', '2010-01-12 10:37:00'), ('2012-01-12 10:00:00', '2010-01-12 10:45:00')]
    result = compute_overlap_time(large, short)
    assert result == expected

def test_given_input_many_interval():
    large = time_range("2012-01-12 10:00:00", "2012-01-12 12:00:00",3, 20)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [('2012-01-12 10:00:00', '2010-01-12 10:37:00'), ('2012-01-12 10:00:00', '2010-01-12 10:45:00'), ('2012-01-12 10:40:06', '2010-01-12 10:37:00'), ('2012-01-12 10:40:06', '2010-01-12 10:45:00'), ('2012-01-12 11:20:13', '2010-01-12 10:37:00'), ('2012-01-12 11:20:13', '2010-01-12 10:45:00')]
    result = compute_overlap_time(large, short)
    assert result == expected

def test_given_input_sameend():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 12:00:00")
    expected = [('2010-01-12 10:30:00', '2010-01-12 12:00:00')]
    result = compute_overlap_time(large, short)
    assert result == expected        


if __name__ == "__main__":
    test_given_input_many_interval()
    test_given_input_sameend()
    test_given_input_nooverlap()

