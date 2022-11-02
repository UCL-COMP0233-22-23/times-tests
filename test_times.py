import times
from times import time_range
from times import compute_overlap_time
#large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#print(compute_overlap_time(large, short))


def test_given_input():
    
    intervals1 =  time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    intervals2 =  time_range("2010-01-12 09:00:00", "2010-01-12 12:00:00", 2, 60*60)

    result = compute_overlap_time(intervals1, intervals2)
    print('Result: ', result)
    expected = [("2010-01-12 10:00:00", "2010-01-12 10:00:00"),\
                ("2010-01-12 11:00:00", "2010-01-12 12:00:00")]
    print('Expected: ', expected)
    assert result == expected