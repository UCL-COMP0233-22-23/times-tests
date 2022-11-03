import times
from times import time_range
from times import compute_overlap_time
#large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#print(compute_overlap_time(large, short))

def test_given_input():
    intervals1 =  time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    intervals2 =  time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(intervals1, intervals2)
    print('Result: ', result)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),\
                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    print('Expected: ', expected)
    assert result == expected


def test_no_overlap():

    intervals1 =  time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    intervals2 =  time_range("2010-01-12 16:00:00", "2010-01-12 19:00:00", 2, 60*60)

    result = compute_overlap_time(intervals1, intervals2)
    print('Result: ', result)
    expected = []
    print('Expected: ', expected)
    assert result == expected

def test_multiple_ranges():

    intervals1 =  time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 2, 3600)
    intervals2 =  time_range("2010-01-12 11:00:00", "2010-01-12 14:00:00", 2, 60*60)

    result = compute_overlap_time(intervals1, intervals2)
    print('Result: ', result)
    expected = [('2010-01-12 11:00:00', '2010-01-12 11:00:00'), \
                ('2010-01-12 12:00:00', '2010-01-12 12:00:00')]
    print('Expected: ', expected)
    assert result == expected

def test_same_time():
    
    intervals1 =  time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    intervals2 =  time_range("2010-01-12 09:00:00", "2010-01-12 12:00:00", 2, 60*60)

    result = compute_overlap_time(intervals1, intervals2)
    print('Result: ', result)
    expected = [("2010-01-12 10:00:00", "2010-01-12 10:00:00"),\
                ("2010-01-12 11:00:00", "2010-01-12 12:00:00")]
    print('Expected: ', expected)
    assert result == expected